from reportlab.lib.pagesizes import letter, portrait
from reportlab.pdfgen import canvas

# Константи
IMG_WIDTH = 75          # Розміри основного зображення
IMG_HEIGHT = 75
BACKGROUND_WIDTH = 100    # Розміри фонової картинки
BACKGROUND_HEIGHT = 100
X_OFFSETS = 35
Y_OFFSETS = 35
IMGS_BTW_WIDTH = 10
IMGS_BTW_HEIGHT = 15  # Встановіть відстань між рядами
IMGS_PER_ROW = 5
BACKGROUND_PATH_ONE = 'template_background/tml_background_one.png'   # Шлях до першого фону
BACKGROUND_PATH_SECOND = 'template_background/tml_background_second.png'  # Шлях до другого фону

def create_pdf(image_paths, output_pdf_path):
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    width, height = portrait(letter)

    x_offset = X_OFFSETS
    y_offset = height - BACKGROUND_HEIGHT - Y_OFFSETS  # Змінено на висоту фону

    # Задаємо, скільки QR-кодів ми будемо малювати в підрядах
    half_per_row = IMGS_PER_ROW // 2  # Кількість QR-кодів в одному підряді

    for index in range(half_per_row):
        # Перевірка, чи є зображення для верхнього підряду
        if index < len(image_paths) // 2:
            top_image_path = image_paths[index]
        else:
            break
        
        # Додати перший фоновий малюнок
        c.drawImage(BACKGROUND_PATH_ONE, x_offset, y_offset, width=BACKGROUND_WIDTH, height=BACKGROUND_HEIGHT)
        c.drawImage(top_image_path, x_offset + (BACKGROUND_WIDTH - IMG_WIDTH) / 2, 
                     y_offset + (BACKGROUND_HEIGHT - IMG_HEIGHT) / 2, 
                     width=IMG_WIDTH, height=IMG_HEIGHT)
        
        # Переходити до наступного зображення
        x_offset += BACKGROUND_WIDTH + IMGS_BTW_WIDTH
        
    # Скинути x_offset для другого ряду
    x_offset = X_OFFSETS
    y_offset -= BACKGROUND_HEIGHT + IMGS_BTW_HEIGHT  # Перехід на новий ряд для другого підряду

    for index in range(half_per_row):
        # Перевірка, чи є зображення для нижнього підряду
        if index + half_per_row < len(image_paths):
            bottom_image_path = image_paths[index + half_per_row]
        else:
            break
        
        # Додати другий фоновий малюнок
        c.drawImage(BACKGROUND_PATH_SECOND, x_offset, y_offset, width=BACKGROUND_WIDTH, height=BACKGROUND_HEIGHT)
        c.drawImage(bottom_image_path, x_offset + (BACKGROUND_WIDTH - IMG_WIDTH) / 2, 
                     y_offset + (BACKGROUND_HEIGHT - IMG_HEIGHT) / 2, 
                     width=IMG_WIDTH, height=IMG_HEIGHT)
        
        # Переходити до наступного зображення
        x_offset += BACKGROUND_WIDTH + IMGS_BTW_WIDTH
        
    c.save()

# Список шляхів до картинок
image_paths = [
    "output_QR_code/one_qr_1453.png",
    "output_QR_code/one_qr_1454.png",
    "output_QR_code/one_qr_1455.png",
    "output_QR_code/one_qr_1456.png",
    "output_QR_code/one_qr_1457.png",
    "output_QR_code/second_qr_1453.png",
    "output_QR_code/second_qr_1454.png",
    "output_QR_code/second_qr_1455.png",
    "output_QR_code/second_qr_1456.png",
    "output_QR_code/second_qr_1457.png"
]

output_pdf_path = "output_QR/output.pdf"

create_pdf(image_paths, output_pdf_path)
