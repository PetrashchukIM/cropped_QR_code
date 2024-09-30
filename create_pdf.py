import os
from reportlab.lib.pagesizes import letter, portrait
from reportlab.pdfgen import canvas

IMG_WIDTH = 40
IMG_HEIGHT = 40
X_OFFSETS = 35
Y_OFFSETS = 35

IMGS_BTW_WIDTH = 10
IMGS_BTW_HEIGHT = 15
IMGS_PER_ROW = 5

BACKGROUND_WIDTH = 75
BACKGROUND_HEIGHT = 75
BACKGROUND_WIDTH_LAYER1 = 0.5
BACKGROUND_WIDTH_LAYER2 = 12

BACKGROUND_PATH_ONE = os.path.join('template_background', 'tml_background_one.png')
BACKGROUND_PATH_SECOND = os.path.join('template_background', 'tml_background_second.png')
BACKGROUND_PATH_LAYER1 = os.path.join('template_background', 'layer1.png')
BACKGROUND_PATH_LAYER2 = os.path.join('template_background', 'layer2.png')
BACKGROUND_PATH_LAYER3 = os.path.join('template_background', 'layer3.png')


def create_pdf(image_paths, output_pdf_path):
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    width, height = letter

    x_offset = X_OFFSETS
    y_offset = height - BACKGROUND_HEIGHT - Y_OFFSETS

    image_pairs = {}

    for path in image_paths:
        base_name = os.path.basename(path)
        identifier = base_name.split('_')[2]
        
        if 'one' in base_name:
            image_pairs[identifier] = [path, None]
        elif 'second' in base_name:
            if identifier in image_pairs:
                image_pairs[identifier][1] = path

    for identifier, pair in image_pairs.items():
        one_image = pair[0]
        second_image = pair[1]
        
        c.drawImage(BACKGROUND_PATH_LAYER1, x_offset, y_offset, width=BACKGROUND_WIDTH, height=BACKGROUND_HEIGHT)
        
        c.drawImage(BACKGROUND_PATH_LAYER2, 
                    x_offset + BACKGROUND_WIDTH_LAYER1, 
                    y_offset + BACKGROUND_WIDTH_LAYER1, 
                    width=BACKGROUND_WIDTH - 2 * BACKGROUND_WIDTH_LAYER1, 
                    height=BACKGROUND_HEIGHT - 2 * BACKGROUND_WIDTH_LAYER1)
        
        c.drawImage(BACKGROUND_PATH_LAYER3, 
                    x_offset + BACKGROUND_WIDTH_LAYER2, 
                    y_offset + BACKGROUND_WIDTH_LAYER2, 
                    width=BACKGROUND_WIDTH - 2 * BACKGROUND_WIDTH_LAYER2, 
                    height=BACKGROUND_HEIGHT - 2 * BACKGROUND_WIDTH_LAYER2)
        
        # c.drawImage(BACKGROUND_PATH_ONE, x_offset, y_offset, width=BACKGROUND_WIDTH, height=BACKGROUND_HEIGHT)
        if one_image:
            c.drawImage(one_image, x_offset + (BACKGROUND_WIDTH - IMG_WIDTH) / 2, 
                         y_offset + (BACKGROUND_HEIGHT - IMG_HEIGHT) / 2, 
                         width=IMG_WIDTH, height=IMG_HEIGHT)
        x_offset += BACKGROUND_WIDTH + IMGS_BTW_WIDTH

        c.drawImage(BACKGROUND_PATH_SECOND, x_offset, y_offset, width=BACKGROUND_WIDTH, height=BACKGROUND_HEIGHT)
        if second_image:
            c.drawImage(second_image, x_offset + (BACKGROUND_WIDTH - IMG_WIDTH) / 2, 
                         y_offset + (BACKGROUND_HEIGHT - IMG_HEIGHT) / 2, 
                         width=IMG_WIDTH, height=IMG_HEIGHT)
        x_offset += BACKGROUND_WIDTH + IMGS_BTW_WIDTH

        if x_offset + BACKGROUND_WIDTH > width:
            x_offset = X_OFFSETS
            y_offset -= BACKGROUND_HEIGHT + IMGS_BTW_HEIGHT

    c.save()



def draw_circle_image(c, x, y, image_path):
    radius = IMG_WIDTH / 2
    c.saveState()  
    c.translate(x + radius, y + radius)  
    c.circle(0, 0, radius)  
    c.clipPath()  
    c.drawImage(image_path, x, y, width=IMG_WIDTH, height=IMG_HEIGHT)  
    c.restoreState()  

def get_image_paths(directory):
    image_paths = []
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            image_paths.append(os.path.join(directory, filename))
    return sorted(image_paths)

def generate_output_pdf_path(base_path):
    output_pdf_path = base_path
    counter = 1
    while os.path.exists(output_pdf_path):
        output_pdf_path = f"{base_path.rsplit('.', 1)[0]}_{counter}.pdf"
        counter += 1
    return output_pdf_path

image_directory = "output_QR_code"
image_paths = get_image_paths(image_directory)
output_pdf_path = generate_output_pdf_path("output_QR/output.pdf")

create_pdf(image_paths, output_pdf_path)
