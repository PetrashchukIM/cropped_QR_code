def create_pdf_with_layers_low_level(filename):
    # Визначаємо параметри PDF
    width = 595.0  # Ширина сторінки (A4)
    height = 842.0  # Висота сторінки (A4)
    square_size = 100
    spacing = 5
    squares_per_row = 3

    colors = [
        (1, 0, 0),   # Червоний
        (0, 0, 1)    # Синій
    ]

    # Відкриваємо файл для запису
    with open(filename, 'wb') as f:
        # Стандартний заголовок PDF
        f.write(b"%PDF-1.4\n")
        f.write(b"1 0 obj\n")
        f.write(b"<< /Type /Catalog /Pages 2 0 R >>\n")
        f.write(b"endobj\n")

        # Створюємо сторінку
        f.write(b"2 0 obj\n")
        f.write(b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>\n")
        f.write(b"endobj\n")

        # Опис сторінки
        f.write(b"3 0 obj\n")
        f.write(b"<< /Type /Page /MediaBox [0 0 595 842] /Contents 4 0 R >>\n")
        f.write(b"endobj\n")

        # Створюємо вміст сторінки (старт потокового блоку)
        f.write(b"4 0 obj\n")
        f.write(b"<< /Length 5 0 R >>\n")
        f.write(b"stream\n")

        # Перший контур для червоних квадратів
        f.write(b"q\n")  # Збереження стану
        f.write(b"/OC /Layer1 BDC\n")  # Початок першого контуру
        f.write(b"1 0 0 rg\n")  # Червоний колір

        start_x = (width - (squares_per_row * square_size + (squares_per_row - 1) * spacing)) / 2
        start_y = height - 150

        for row in range(1):  # Перший рядок
            for col in range(squares_per_row):
                x = start_x + col * (square_size + spacing)
                y = start_y - row * (square_size + spacing)
                f.write(f"{x} {y} {square_size} {square_size} re\n".encode())
                f.write(b"f\n")  # Заповнення кольором

        f.write(b"EMC\n")  # Закінчення контуру
        f.write(b"Q\n")  # Відновлення стану

        # Другий контур для синіх квадратів
        f.write(b"q\n")  # Збереження стану
        f.write(b"/OC /Layer2 BDC\n")  # Початок другого контуру
        f.write(b"0 0 1 rg\n")  # Синій колір

        for row in range(1, 2):  # Другий рядок
            for col in range(squares_per_row):
                x = start_x + col * (square_size + spacing)
                y = start_y - row * (square_size + spacing)
                f.write(f"{x} {y} {square_size} {square_size} re\n".encode())
                f.write(b"f\n")  # Заповнення кольором

        f.write(b"EMC\n")  # Закінчення контуру
        f.write(b"Q\n")  # Відновлення стану

        # Завершення потокового блоку
        f.write(b"endstream\n")
        f.write(b"endobj\n")

        # Створення таблиці перекладу
        f.write(b"xref\n")
        f.write(b"0 5\n")
        f.write(b"0000000000 65535 f \n")
        f.write(b"0000000010 00000 n \n")
        f.write(b"0000000060 00000 n \n")
        f.write(b"0000000110 00000 n \n")
        f.write(b"0000000200 00000 n \n")

        # Завершення PDF
        f.write(b"trailer\n")
        f.write(b"<< /Size 5 /Root 1 0 R >>\n")
        f.write(b"%%EOF\n")

# Виклик функції для створення PDF
create_pdf_with_layers_low_level("grouped_squares_layers.pdf")
