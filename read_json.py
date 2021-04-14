import json
from fpdf import FPDF
from tqdm import tqdm

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
print(data)

print(data['name'])

image_list = ['./img/screenshot1.png',
              './img/screenshot2.png', './img/screenshot3.png']

pdf = FPDF()
for img in tqdm(image_list):
    pdf.add_page()
    pdf.image(img, 0, 0, 210, 150)
pdf.output('result.pdf', 'F')
