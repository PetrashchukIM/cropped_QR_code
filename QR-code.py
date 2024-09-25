import cv2
from PIL import Image
import os
import shutil


OUTPUT_RESULT="output_QR"
OUTPUT_PATH = 'output_QR_code'
TMP_PATH = 'temp'
TMP_FILE_ONE = 'one_part.png'
TMP_FILE_SECOND = 'second_part.png'
COUNT_PART = 5

def split_image(image_path):
    print(f'Start spliting {image_path}')
    image = cv2.imread(image_path)

    if image is None:
        print("Failed to load image.")
        return
    
    height, width, _ = image.shape
    part_width = width // COUNT_PART
    left_half = image[:, :part_width]
    right_half = image[:, (COUNT_PART-1) * part_width:]

    save_img (left_half,TMP_FILE_ONE)
    save_img (right_half,TMP_FILE_SECOND)

    extract_and_safe_qr_code (TMP_FILE_ONE,"one_qr.png")
    extract_and_safe_qr_code (TMP_FILE_SECOND,"second_qr.png")

def save_img(half, name_file):
    half_rgb = cv2.cvtColor(half, cv2.COLOR_BGR2RGB)
    half_pil = Image.fromarray(half_rgb)
    half_pil.save(os.path.join(TMP_PATH, name_file))
    print(f"File {name_file} saved")

def extract_and_safe_qr_code (name_file, otput_name_file):
    
    input_img = os.path.join(TMP_PATH, name_file)
    print(f'Start extracting {input_img}')

    image = cv2.imread(input_img)

    if image is None:
        print("Failed to load image.")
        return
    qr_detector = cv2.QRCodeDetector()

    data, points, _ = qr_detector.detectAndDecode(image)
    if points is not None and len(points) > 0:
        points = points[0]
        x_min = int(min(points[:, 0]))
        y_min = int(min(points[:, 1]))
        x_max = int(max(points[:, 0]))
        y_max = int(max(points[:, 1]))

        cropped_image = image[y_min:y_max, x_min:x_max]
        cropped_image_pi = Image.fromarray(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
        output_full_path_img = os.path.join(OUTPUT_PATH, otput_name_file)
        cropped_image_pi.save(output_full_path_img)

        print(f"Extracted QR code and saved as {output_full_path_img}")
    else:
        print(F"QR code not found in {input_img}")


def check_and_remove_directory(directory_path):
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        shutil.rmtree(directory_path)
        print(f"The folder '{directory_path}' was delete.")
    else:
        print(f"The fiolder '{directory_path}' not found.")

def create_directory(directory_path):
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(f"The folder '{directory_path}' created.")
    except Exception as e:
        print(f"Error create a folder: {e}")

check_and_remove_directory(OUTPUT_PATH)
create_directory(OUTPUT_PATH)

check_and_remove_directory(TMP_PATH)
create_directory(TMP_PATH)

split_image("1453.png")




