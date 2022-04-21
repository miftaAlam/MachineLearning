import argparse
import subprocess
import tflite_runtime.interpreter as tflite
import numpy as np
from PIL import Image
import time
import glob
import picamera

cam = picamera.PiCamera()
cam.resolution = (224,224)
cam.rotation = 180

def feed(lst_globs):
  if lst_globs == "":
    while True:
      cam.capture("images/camera-feed.jpg")
      yield "images/camera-feed.jpg"
  else:
    for img_glob in sources[src_i][1]:
      for img_path in glob.glob(img_glob):
        yield img_path

argparser = argparse.ArgumentParser(description="Run a Model on a set of images or a camera feed and generate predictions.")
argparser.add_argument("--model", metavar="M", type=int, help="the index of the model to use.")
argparser.add_argument("--source", metavar="S", type=int, help="the index of the source to use.")
args = argparser.parse_args()

models = [("MobileNet V1 224","models/mobilenet_v1_1.0_224_quant"),
          ("MobileNet V1 128","models/mobilenet_v1_0.25_128_quant"),
          ("Inception V4", "models/inception_v4_quant"),
          ("Custom: Is the camera covered?", "models/covered_quant")
         ]

sources = [("Example Images",["images/224x224/*",
                              "images/room.jpg", 
                              "images/239x215/*", 
                              "images/128x128/*",
                              "images/imagenet_examples/*"
                              ]),
           ("Camera","")
          ]

if args.model is None:
  print("Which model would you like to run?")
  for i, mod in enumerate(models):
    print(f"({i}) {mod[0]}")
  model_i = int(input())
else:
  model_i = args.model

if args.source is None:
  print("Which source would you like predict from?")
  for i, src in enumerate(sources):
    print(f"({i}) {src[0]}")
  src_i = int(input())
else:
  src_i = args.source

interpreter = tflite.Interpreter(models[model_i][1]+"/model.tflite")
interpreter.allocate_tensors()

inputs = interpreter.get_input_details()[0];
outputs = interpreter.get_output_details()[0];
width  = inputs["shape"][2]
height = inputs["shape"][1]
dtype = inputs["dtype"]
scale, zero = outputs['quantization']
print(f"Predicting with model:  {models[model_i][0]}\n  * size: ({width}x{height})\n  * type: {dtype}\n  * scale: ({scale},{zero})")

lables=[]
with open(models[model_i][1]+"/labels.txt", "r") as f:
    labels = [line.strip() for line in f.readlines()]

print(f"Predicting from source: {sources[src_i][0]}")

for img_path in feed(sources[src_i][1]):
  img = Image.open(img_path).convert('RGB').resize((width, height))

  # we need another dimension
  input_data = np.expand_dims(img, axis=0)

  # lets get to it
  interpreter.set_tensor(inputs["index"], input_data)

  interpreter.invoke()

  output_data = interpreter.get_tensor(outputs["index"]).squeeze()
  
  output_data = (scale*100) * (output_data - zero)

  ordered_indexes = np.flip(output_data.argsort())
  best_index = ordered_indexes[0]
  print(f"  * {img_path} = {labels[best_index]} %0.0f%%" % output_data[best_index])
