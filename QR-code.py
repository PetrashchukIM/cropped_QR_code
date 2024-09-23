import cv2
from PIL import Image

def extract_qr_code(image_path, output_path):
    # Завантаження зображення за допомогою OpenCV
    image = cv2.imread(image_path)

    if image is None:
        print("Не вдалося завантажити зображення.")
        return

    # Створюємо QR-код детектор
    qr_detector = cv2.QRCodeDetector()

    # Визначаємо QR-код на зображенні
    data, points, _ = qr_detector.detectAndDecode(image)

    if points is not None and len(points) > 0:
        # Якщо QR-код знайдено, витягуємо координати його кутів
        points = points[0]

        # Отримуємо координати
        x_min = int(min(points[:, 0]))
        y_min = int(min(points[:, 1]))
        x_max = int(max(points[:, 0]))
        y_max = int(max(points[:, 1]))

        # Обрізаємо зображення і зберігаємо результат
        cropped_image = image[y_min:y_max, x_min:x_max]
        cropped_image_pil = Image.fromarray(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
        cropped_image_pil.save(output_path)
        print(f"QR-save here {output_path}")
    else:
        print("QR-not found.")

# Виклик функції
extract_qr_code("1453.png", "output_qr.png")
