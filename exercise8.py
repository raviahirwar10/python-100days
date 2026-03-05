import os
from pypdf import PdfWriter

folder = "exer8pdf"   # jaha tumhare PDFs rakhe hain
files = os.listdir("exer8pdf")

# Step 1: Rename PDFs
pdf_list = []
for i, file in enumerate(files, start=1):
    if file.endswith(".pdf"):
        old_path = os.path.join(folder, file)
        new_name = f"document_{i}.pdf"
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)
        pdf_list.append(new_path)
        print(f"Renamed {file} → {new_name}")

# Step 2: Merge PDFs
merger = PdfWriter()
for pdf in pdf_list:
    merger.append(pdf)

merger.write("finalmerged.pdf")
merger.close()

