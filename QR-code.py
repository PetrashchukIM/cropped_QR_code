import cv2
from PIL import Image

def extract_qr_code(image_path, output_path):
    # Завантаження зображення за допомогою OpenCV
    image = cv2.imread(image_path)
    
    # Створюємо QR-код детектор
    qr_detector = cv2.QRCodeDetector()

    # Визначаємо QR-код на зображенні
    data, points, _ = qr_detector.detectAndDecode(image)

    if points is not None:
        # Якщо QR-код знайдено, витягуємо координати його кутів
        points = points[0]

        # Отримуємо координати (якщо QR-код перекошений, їх буде 4)
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        x4, y4 = points[3]

        # Обрізаємо зображення, вирізаючи QR-код за допомогою координат
        x_min = min(int(x1), int(x2), int(x3), int(x4))
        y_min = min(int(y1), int(y2), int(y3), int(y4))
        x_max = max(int(x1), int(x2), int(x3), int(x4))
        y_max = max(int(y1), int(y2), int(y3), int(y4))

        # Обрізаємо зображення і зберігаємо результат
        cropped_image = image[y_min:y_max, x_min:x_max]
        cropped_image_pil = Image.fromarray(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
        cropped_image_pil.save(output_path)
        print(f"QR-код збережено як {output_path}")
    else:
        print("QR-код не знайдено на зображенні.")

# Виклик функції
extract_qr_code("input.png", "output_qr.png")
