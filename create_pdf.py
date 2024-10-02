import os
from reportlab.lib.pagesizes import letter, portrait
from reportlab.pdfgen import canvas


IMG_WIDTH = 40
IMG_HEIGHT = 40
X_OFFSETS = 35
Y_OFFSETS = 35

IMGS_BTW_WIDTH = 10
IMGS_BTW_HEIGHT = 15
IMGS_PER_ROW = 6

BACKGROUND_WIDTH = 75
BACKGROUND_HEIGHT = 75
BACKGROUND_WIDTH_LAYER1 = 0.5
BACKGROUND_WIDTH_LAYER2 = 12
BACKGROUND_CIRCLE_WHITE = 15

BACKGROUND_PATH_LAYER1 = os.path.join('template_background', 'layer1.png')
BACKGROUND_PATH_LAYER2 = os.path.join('template_background', 'layer2.png')
BACKGROUND_PATH_LAYER3 = os.path.join('template_background', 'layer3.png')

BACKGROUND_PATH_CIRCLE = os.path.join('template_background', 'shapes.png')


def create_pdf(image_paths, output_pdf_path):
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    width, height = letter

    x_offset_one = X_OFFSETS
    y_offset_one = height - BACKGROUND_HEIGHT - Y_OFFSETS
    x_offset_second = X_OFFSETS
    y_offset_second = height - 2 * BACKGROUND_HEIGHT -  Y_OFFSETS 

    image_pairs = {}

    for path in image_paths:
        base_name = os.path.basename(path)
        identifier = base_name.split('_')[2]
        
        if 'one' in base_name:
            image_pairs[identifier] = [path, None]
        elif 'second' in base_name:
            if identifier in image_pairs:
                image_pairs[identifier][1] = path

    count_in_row = 0 

    for identifier, pair in image_pairs.items():
        one_image = pair[0]
        second_image = pair[1]
        
        if count_in_row <IMGS_PER_ROW - 1 :
            count_in_row += 1
        else:    
            count_in_row = 0

        c.drawImage(BACKGROUND_PATH_LAYER1, x_offset_one, y_offset_one, width=BACKGROUND_WIDTH, height=BACKGROUND_HEIGHT)
        
        c.drawImage(BACKGROUND_PATH_LAYER2, 
                    x_offset_one + BACKGROUND_WIDTH_LAYER1, 
                    y_offset_one + BACKGROUND_WIDTH_LAYER1, 
                    width=BACKGROUND_WIDTH - 2 * BACKGROUND_WIDTH_LAYER1, 
                    height=BACKGROUND_HEIGHT - 2 * BACKGROUND_WIDTH_LAYER1)
        
        c.drawImage(BACKGROUND_PATH_LAYER3, 
                    x_offset_one + BACKGROUND_WIDTH_LAYER2, 
                    y_offset_one + BACKGROUND_WIDTH_LAYER2, 
                    width=BACKGROUND_WIDTH - 2 * BACKGROUND_WIDTH_LAYER2, 
                    height=BACKGROUND_HEIGHT - 2 * BACKGROUND_WIDTH_LAYER2)
        
        if one_image:
            print(f"One_image {one_image}")
            c.drawImage(one_image, x_offset_one + (BACKGROUND_WIDTH - IMG_WIDTH) / 2, 
                         y_offset_one + (BACKGROUND_HEIGHT - IMG_HEIGHT) / 2, 
                         width=IMG_WIDTH, height=IMG_HEIGHT)
    
    
        c.drawImage(BACKGROUND_PATH_CIRCLE, x_offset_second, y_offset_second, width=BACKGROUND_WIDTH, height=BACKGROUND_HEIGHT)

        c.drawImage(BACKGROUND_PATH_LAYER3, 
                    x_offset_second + BACKGROUND_CIRCLE_WHITE, 
                    y_offset_second + BACKGROUND_CIRCLE_WHITE, 
                    width=BACKGROUND_WIDTH - 2 * BACKGROUND_CIRCLE_WHITE, 
                    height=BACKGROUND_HEIGHT - 2 * BACKGROUND_CIRCLE_WHITE)
        
        if second_image:
            print(f"Second_image {second_image}")
            c.drawImage(second_image, x_offset_second + (BACKGROUND_WIDTH - IMG_WIDTH) / 2, 
                        y_offset_second + (BACKGROUND_HEIGHT - IMG_HEIGHT) / 2, 
                        width=IMG_WIDTH, height = IMG_HEIGHT)

        if count_in_row == 0:    
            x_offset_one = X_OFFSETS
            y_offset_one -= BACKGROUND_HEIGHT +  BACKGROUND_HEIGHT
            x_offset_second = X_OFFSETS
            y_offset_second -= BACKGROUND_HEIGHT + BACKGROUND_HEIGHT
            
        if count_in_row != 0:    
            x_offset_one += BACKGROUND_WIDTH + IMGS_BTW_WIDTH
            x_offset_second += BACKGROUND_WIDTH + IMGS_BTW_WIDTH


        if y_offset_one < 0 or y_offset_second < 0:  
            c.showPage()  
            x_offset_one = X_OFFSETS
            y_offset_one = height - BACKGROUND_HEIGHT - Y_OFFSETS
            x_offset_second = X_OFFSETS
            y_offset_second = height - 2 * BACKGROUND_HEIGHT - Y_OFFSETS

    c.save() 

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

