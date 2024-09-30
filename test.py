import os
import numpy as np
from PIL import Image

BACKGROUND_PATH_LAYER1 = os.path.join('template_background', 'layer1.png')
BACKGROUND_PATH_TMP_LAYER1 = os.path.join('temp', 'tmp_layer1.png')

def crop_circle(image_path, out_path, bg_color=(255, 255, 255, 255)):
    image = Image.open(image_path).convert("RGBA")  # Перетворення на RGBA
    image_array = np.array(image)

    height, width = image_array.shape[:2]
    radius = min(height, width) // 2

    # Створення маски для кола
    Y, X = np.ogrid[:height, :width]
    center = (height // 2, width // 2)
    mask = (X - center[1])**2 + (Y - center[0])**2 <= radius**2

    # Створення нового зображення з фоном заданого кольору
    result_array = np.zeros((height, width, 4), dtype=np.uint8)
    result_array[:, :] = bg_color  # Заповнюємо все білим (або іншим кольором)

    # Накладання маски для круглої частини
    result_array[mask] = image_array[mask]

    # Створення нового зображення з масиву
    result_image = Image.fromarray(result_array)
    result_image.save(out_path)

# Виклик функції з білим фоном
crop_circle(BACKGROUND_PATH_LAYER1, BACKGROUND_PATH_TMP_LAYER1, bg_color=(255, 255, 255, 255))  # Білий фон
