from fpdf import FPDF
import pandas as pd


pdf = FPDF()
pdf.set_auto_page_break(auto=False, margin=0)

# uploaded the title file from csv into a data frame
df = pd.read_csv("topics (1).csv")

# Created the multiple first page
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=18, txt=row["Topic"], align="L", ln=1)
    for n in range(22, 292, 10):
        pdf.line(x1=10, y1=n, x2=200, y2=n)

    # Added a footer
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

# Added multiple pages
    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.ln(278)
        pdf.set_font(family="Times", style="B", size=10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)
        for n in range(12, 292, 10):
            pdf.line(x1=10, y1=n, x2=200, y2=n)

# created document for viewing
pdf.output("raw1.pdf")
