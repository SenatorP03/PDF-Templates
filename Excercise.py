from fpdf import FPDF
import pandas as pd
import glob
import pathlib

# Got the filepaths from the folder where the txt files are saved
filepaths = glob.glob("Text+files/*txt")

# create a pdf file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# To create a merged pdf from different txt docs
for filepath in filepaths:
    pdf.add_page()
    df = pd.read_csv(filepath)

# Add a header to each page
    Path = pathlib.Path(filepath).stem
    name = Path.title()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(txt=name, align="L", w=50, h=9, ln=1)

# Added the content of the file
    with open(filepath, "r") as file:
        content = file.read()
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=8,txt=content, align="L")

# create an output pdf file
pdf.output("story.pdf")
