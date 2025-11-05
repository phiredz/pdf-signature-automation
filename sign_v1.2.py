from datetime import datetime
import fitz  # PyMuPDF
from reportlab.pdfgen import canvas
import os

input_folder = "C:/Users/faiqah.redzuan/Desktop/PDF_Sign/input"
output_folder = "C:/Users/faiqah.redzuan/Desktop/PDF_Sign/output"
signature_img = "C:/Users/faiqah.redzuan/Desktop/PDF_Sign/signature.png"

signature_width = 110
signature_height = 44

# Create PDF stamp from image
def create_stamp(img_path, stamp_path, width, height):
    c = canvas.Canvas(stamp_path, pagesize=(width, height))
    c.drawImage(img_path, 0, 0, width=width, height=height, mask='auto')
    c.save()

stamp_pdf = "signature_stamp.pdf"
create_stamp(signature_img, stamp_pdf, signature_width, signature_height)

# Coordinates for signature placement
x = 462
y = 719

# Coordinates for date placement
date_x = 495
date_y = 815

# Process PDFs
for file in os.listdir(input_folder):
    if file.lower().endswith(".pdf"):
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, file)

        pdf = fitz.open(input_path)
        stamp = fitz.open(stamp_pdf)

        page = pdf[0]  # first page

        # Draw signature
        bbox = fitz.Rect(
            x,
            y,
            x + signature_width,
            y + signature_height
        )
        page.show_pdf_page(bbox, stamp, 0)

        # ✅ Draw current date
        today = datetime.today().strftime("%d %b %Y")  # example: 31 Oct 2025

        page.insert_text(
            (date_x, date_y),
            today,
            fontname="helv",
            fontsize=12,
            color=(0, 0, 0)
        )

        pdf.save(output_path)
        pdf.close()
        stamp.close()

print("✅ Signature + date applied successfully.")
