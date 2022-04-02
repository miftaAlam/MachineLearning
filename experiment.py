import tflite_runtime.interpreter as tflite
import numpy as np
from PIL import Image
import time

models = [("MobileNet V1 224","models/mobilenet_v1_1.0_224_quant/mobilenet_v1_1.0_224_quant.tflite"),
          ("MobileNet V1 128","models/mobilenet_v1_0.25_128_quant/mobilenet_v1_0.25_128_quant.tflite")
         ]

print("Which model would you like to run?")
for i, mod in enumerate(models):
  print(f"({i}) {mod[0]}")
index = int(input())

interpreter = tflite.Interpreter(model_path=models[index][1])
interpreter.allocate_tensors()

inputs = interpreter.get_input_details();
outputs = interpreter.get_output_details();
width  = inputs[0]["shape"][2]
height = inputs[0]["shape"][1]
dtype = inputs[0]["dtype"]

print("# inputs")
print(f"  * height = {width}")
print(f"  * width  = {height}")
print(f"  * type   = {dtype}")

lables=[]
with open("models/mobilenet_labels.txt", "r") as f:
    labels = [line.strip() for line in f.readlines()]

for img_path in ["images/224x224/mug.jpg", "images/224x224/paper_cup.jpg", "images/224x224/can.jpg", "images/room.jpg", "images/239x215/cat.jpg", "images/128x128/example.jpg", "images/128x128/mug.jpg"]:
  print(f"=== {img_path} ===")
  img = Image.open(f"{img_path}").convert('RGB').resize((width, height))

  # we need another dimension
  input_data = np.expand_dims(img, axis=0)

  # lets get to it
  print("# Interpreter:")
  print("  * starting")
  interpreter.set_tensor(inputs[0]["index"], input_data)
#   interpreter.set_tensor(inputs[0]["index"], input_data.astype(np.float32))

  start_time = time.time()
  interpreter.invoke()
  print(f"  * Interpreter done after {time.time() - start_time}")

  output_data = interpreter.get_tensor(outputs[0]["index"]).squeeze()

  ordered_indexes = np.flip(output_data.argsort())
  print("  * predictions")
  for i in ordered_indexes[:5]:
      print(f"    * %0.3f prediction of {labels[i]}" % output_data[i])

