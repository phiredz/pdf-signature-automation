import fitz  # PyMuPDF
import os

input_pdf = "C:/Users/faiqah.redzuan/Desktop/PDF_Sign/input/GHQPV202509000004_Rental.pdf"
output_pdf = "C:/Users/faiqah.redzuan/Desktop/PDF_Sign/output/grid_preview.pdf"

pdf = fitz.open(input_pdf)
page = pdf[0]  # first page

page_width = page.rect.width
page_height = page.rect.height

step = 100  # grid spacing (change to 50 for finer grid)

for x in range(0, int(page_width), step):
    for y in range(0, int(page_height), step):
        page.insert_text(
            (x, y),
            f"{x},{y}",
            fontsize=7,
            color=(1, 0, 0)  # red text
        )

pdf.save(output_pdf)
pdf.close()

print("✅ Grid overlay created. Open the output PDF to see coordinates.")
