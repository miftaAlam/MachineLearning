import argparse

argparser = argparse.ArgumentParser(description="Run a Model on a set of images or a camera feed and generate predictions.")
argparser.add_argument("--model", metavar="M", type=int, help="the index of the model to use.")
argparser.add_argument("--source", metavar="S", type=int, help="the index of the source to use.")
args = argparser.parse_args()

models = [("MobileNet V1 224","models/mobilenet_v1_1.0_224_quant/mobilenet_v1_1.0_224_quant.tflite"),
          ("MobileNet V1 128","models/mobilenet_v1_0.25_128_quant/mobilenet_v1_0.25_128_quant.tflite")
         ]

sources = ["Example Images",
           "Camera"
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
    print(f"({i}) {src}")
  src_i = int(input())
else:
  src_i = args.source

print(f"Predicting with model:  {models[model_i][0]}")
print(f"Predicting from source: {sources[src_i]}")
