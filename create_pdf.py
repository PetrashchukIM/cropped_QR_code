from reportlab.lib.pagesizes import letter,portrait
from reportlab.lib import colors
from reportlab.pdfgen import canvas

IMG_WIDTH = 100
IMG_HEIGHT = 100
X_OFFSETS = 35
Y_OFFSETS = 35
IMGS_BTW_WIDTH = 10
IMGS_BTW_HEIGHT = 10

def create_pdf(image_paths, output_pdf_path):
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    width, height = portrait(letter)

    x_offset = X_OFFSETS
    y_offset = height - IMG_HEIGHT - IMGS_BTW_HEIGHT

    for image_path in enumerate(image_paths):

        c.drawImage(image_path, x_offset, y_offset, width=IMG_WIDTH, height=IMG_HEIGHT)
        x_offset += IMG_WIDTH + IMGS_BTW_WIDTH  

        if x_offset + IMG_WIDTH > width:  
            x_offset = X_OFFSETS
            y_offset -= IMG_HEIGHT + Y_OFFSETS 

        if y_offset < IMG_HEIGHT:
            c.showPage()  
            x_offset = X_OFFSETS 
            y_offset = height - IMG_HEIGHT - Y_OFFSETS  

    c.save()

image_paths = [
    "output_QR_code\\one_qr_1453.png",
    "output_QR_code\\one_qr_1454.png",
    "output_QR_code\\one_qr_1455.png",
    "output_QR_code\\one_qr_1456.png",
    "output_QR_code\\one_qr_1457.png",
    "output_QR_code\\second_qr_1453.png",
    "output_QR_code\\second_qr_1454.png",
    "output_QR_code\\second_qr_1455.png",
    "output_QR_code\\second_qr_1456.png",
    "output_QR_code\\second_qr_1457.png"
]

output_pdf_path = "output_QR\output.pdf"

create_pdf(image_paths, output_pdf_path)
