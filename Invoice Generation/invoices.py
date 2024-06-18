import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:

    pdf = FPDF()
    pdf.add_page()

    # getting the document title and date
    invoice_nr = Path(filepath).stem
    filename, date = invoice_nr.split("-")
    date_n = date.replace(".", "/")

    pdf.set_font(family="Times", size=16, style="UB")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{filename}",ln=1)

    pdf.set_font(family="Times", size=12, style="IB")
    pdf.cell(w=50, h=6, txt=f"Date:{date_n}", ln=2)
    # Add a header
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    columns_a = df.columns
    col =[item.replace('_', ' ').title() for item in columns_a]

    pdf.set_font(family="Times", size=10, style="IB")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=6, txt=col[0], border=1, align="C")
    pdf.cell(w=50, h=6, txt=col[1], border=1, align="C")
    pdf.cell(w=30, h=6, txt=col[2], border=1, align="C")
    pdf.cell(w=30, h=6, txt=col[3], border=1, align="C")
    pdf.cell(w=30, h=6, txt=col[4], border=1, align="C",ln=1)

    # Add the rows
    for index,row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=6, txt=str(row["product_id"]), border=1, align="C")
        pdf.cell(w=50, h=6, txt=str(row["product_name"]), border=1, align="C")
        pdf.cell(w=30, h=6, txt=str(row["amount_purchased"]), border=1, align="C")
        pdf.cell(w=30, h=6, txt=str(row["price_per_unit"]), border=1, align="C")
        pdf.cell(w=30, h=6, txt=str(row["total_price"]), border=1, align="C",ln=1)

    # Added the total sum
    total_sum = df["total_price"].sum()

    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=6, txt='', border=1, align="C")
    pdf.cell(w=50, h=6, txt='', border=1, align="C")
    pdf.cell(w=30, h=6, txt='', border=1, align="C")
    pdf.cell(w=30, h=6, txt='', border=1, align="C")
    pdf.cell(w=30, h=6, txt=str(total_sum), border=1, align="C", ln=1)

    # Added a description line
    pdf.set_font(family="Times", size=10, style="IB")
    pdf.cell(w=30, h=6, txt=f'The total sum is {total_sum}', ln=1)

    # Adding my logo
    pdf.set_font(family="Times", size=14, style="B")
    pdf.cell(w=28, h=6, txt=f'SenatorP.03')
    pdf.image("invoices/my_logo.jpg", w=10)

    pdf.output( f"PDFs/{invoice_nr}.pdf")
