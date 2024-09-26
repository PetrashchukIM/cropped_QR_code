from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas

# Функція для створення PDF
def create_pdf(image_paths, output_pdf_path):
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    width, height = letter  # Розміри сторінки

    # Визначте розміри картинок
    img_width = 200
    img_height = 200
    x_offset = 50
    y_offset = height - img_height - 50  # Відстань зверху

    for i, image_path in enumerate(image_paths):
        if i > 0 and i % 5 == 0:  # Якщо 5 картинок, переходьте на нову сторінку
            c.showPage()
            y_offset = height - img_height - 50  # Скидання відстані зверху

        c.drawImage(image_path, x_offset, y_offset, width=img_width, height=img_height)
        x_offset += img_width + 10  # Збільшуємо відстань між картинками

        if x_offset + img_width > width:  # Якщо не вміщаються в ряд, переходьте на новий ряд
            x_offset = 50
            y_offset -= img_height + 10  # Збільшуємо відстань між рядами

    c.save()

# Шляхи до картинок
image_paths = [
    "image1.jpg",
    "image2.jpg",
    "image3.jpg",
    "image4.jpg",
    "image5.jpg"
]

# Вихідний PDF файл
output_pdf_path = "output.pdf"

# Викликаємо функцію для створення PDF
create_pdf(image_paths, output_pdf_path)
