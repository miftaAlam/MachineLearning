import numpy as np
from PIL import Image
import time

def run_prediction(model, image)

  for img_path in :
    print(f"=== {img_path} ===")
    img = Image.open(f"{img_path}").convert('RGB').resize((width, height))

    # we need another dimension
    input_data = np.expand_dims(img, axis=0)

    # lets get to it
    print("# Interpreter:")
    print("  * starting")
    interpreter.set_tensor(inputs[0]["index"], input_data)

    start_time = time.time()
    interpreter.invoke()
    print(f"  * Interpreter done after {time.time() - start_time}")

    output_data = interpreter.get_tensor(outputs[0]["index"]).squeeze()

    ordered_indexes = np.flip(output_data.argsort())
    print("  * predictions")
    for i in ordered_indexes[:5]:
        print(f"    * %0.3f prediction of {labels[i]}" % output_data[i])

