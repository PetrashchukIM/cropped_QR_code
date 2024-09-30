import io
import os
import numpy as np
from PIL import Image


BACKGROUND_PATH_LAYER1 = os.path.join('template_background', 'layer1.png')
BACKGROUND_PATH_TMP_LAYER1 = os.path.join('temp', 'tmp_layer1.png')

def crop_circle(image_path, out_path):
    image = Image.open(image_path)
    image_array = np.array(image)

    height, width = image_array.shape[:2]
    radius = min(height, width) // 2

    Y, X = np.ogrid[:height, :width]
    center = (height // 2, width // 2)
    mask = (X - center[1])**2 + (Y - center[0])**2 <= radius**2

    result_array = np.zeros_like(image_array)
    result_array[mask] = image_array[mask]

    result_image = Image.fromarray(result_array)
    result_image.save(out_path)

crop_circle(BACKGROUND_PATH_LAYER1, BACKGROUND_PATH_TMP_LAYER1)