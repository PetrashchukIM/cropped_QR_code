import cv2
from PIL import Image
import os
import shutil

OUTPUT_PATH='output_QR_code'

def extract_qr_codes(image_path, output_path1, output_path2):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    if image is None:
        print("Failed to load image.")
        return

    # Create a QR code detector
    qr_detector = cv2.QRCodeDetector()

    height, width, _ = image.shape
    left_half = image[:, :width // 2]
    right_half = image[:, width // 2:]
    
    # Detect and decode the QR codes
    data1, points1, _ = qr_detector.detectAndDecode(image)
    if points1 is not None and len(points1) > 0:
        points1 = points1[0]
        x_min1 = int(min(points1[:, 0]))
        y_min1 = int(min(points1[:, 1]))
        x_max1 = int(max(points1[:, 0]))
        y_max1 = int(max(points1[:, 1]))

        # Crop the first QR code
        cropped_image1 = image[y_min1:y_max1, x_min1:x_max1]
        cropped_image1_pil = Image.fromarray(cv2.cvtColor(cropped_image1, cv2.COLOR_BGR2RGB))
        cropped_image1_pil.save(output_path1)
        print(f"First QR code saved as {output_path1}")
        print("Extracted data:", data1)
    else:
        print("First QR code not found.")

    # Detect and decode the second QR code
    data2, points2, _ = qr_detector.detectAndDecode(image)
    if points2 is not None and len(points2) > 0:
        points2 = points2[0]
        x_min2 = int(min(points2[:, 0]))
        y_min2 = int(min(points2[:, 1]))
        x_max2 = int(max(points2[:, 0]))
        y_max2 = int(max(points2[:, 1]))

        # Crop the second QR code
        cropped_image2 = image[y_min2:y_max2, x_min2:x_max2]
        cropped_image2_pil = Image.fromarray(cv2.cvtColor(cropped_image2, cv2.COLOR_BGR2RGB))
        cropped_image2_pil.save(output_path2)
        print(f"Second QR code saved as {output_path2}")
        print("Extracted data:", data2)
    else:
        print("Second QR code not found.")



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

output_path1 = os.path.join(OUTPUT_PATH, "output_qr1.png")
output_path2 = os.path.join(OUTPUT_PATH, "output_qr2.png")

extract_qr_codes("145311.png", output_path1, output_path2)
