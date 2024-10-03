from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Colored Squares as Layers", new_x='LMARGIN', new_y='NEXT', align='C')

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", new_x='LMARGIN', new_y='TOP', align='C')

    def draw_square(self, x, y, size, color, label):
        # Заливка кольором
        self.set_fill_color(*color)
        self.rect(x, y, size, size, 'F')  # 'F' означає заливку
        # Додавання назви
        self.set_xy(x, y + size + 2)  # Переміщуємо позицію для тексту
        self.set_font("Arial", "B", 12)
        self.cell(size, 10, label, align='C')

# Створення PDF
pdf = PDF()
pdf.add_page()

# Параметри квадратів
squares = [
    {"position": (10, 20), "size": 40, "color": (255, 0, 0), "label": "Red Square"},
    {"position": (60, 20), "size": 40, "color": (0, 255, 0), "label": "Green Square"},
    {"position": (110, 20), "size": 40, "color": (0, 0, 255), "label": "Blue Square"},
    {"position": (10, 70), "size": 40, "color": (255, 255, 0), "label": "Yellow Square"},
    {"position": (60, 70), "size": 40, "color": (255, 165, 0), "label": "Orange Square"},
    {"position": (110, 70), "size": 40, "color": (128, 0, 128), "label": "Purple Square"},
]

# Додавання квадратів у PDF
for square in squares:
    pdf.draw_square(square["position"][0], square["position"][1], square["size"], square["color"], square["label"])

# Зберегти PDF
pdf.output("colored_squares.pdf")

print("PDF with colored squares created successfully!")
