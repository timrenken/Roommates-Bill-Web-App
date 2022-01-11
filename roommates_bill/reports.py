from fpdf import FPDF
import webbrowser
import os


class PdfReport:
    """
    Creates a PDF file that contains data about
    the roommates such as their names, their due amount,
    for which service, and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    # TODO: a list of roommates if more than 2
    def generate(self, roommate1, roommate2, bill):

        roommate1_pay = round(roommate1.pays(bill, roommate2), 2)
        roommate2_pay = round(roommate2.pays(bill, roommate1), 2)

        pdf = FPDF(orientation="P", unit="pt", format="Letter")
        pdf.add_page()

        # Add icon
        pdf.image(name="files/home.png", w=30, h=30)

        # Insert title
        pdf.set_font(family="Arial", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Roommates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Arial", size=14, style="B")
        pdf.cell(w=165, h=30, txt="Period:", border=0)
        pdf.cell(w=150, h=30, txt=bill.period, border=0, ln=1)

        # Insert service label and value
        pdf.cell(w=200, h=30, txt=f"for: {bill.service}", border=0, ln=1)

        # Insert name and due amount of the first roommate
        pdf.set_font(family="Arial", size=12)
        pdf.cell(w=50, h=20, txt=roommate1.name, border=0)
        pdf.cell(w=150, h=20, txt=f"${roommate1_pay}", border=0, ln=1)

        # Insert name and due amount of the second roommate
        pdf.cell(w=50, h=20, txt=roommate2.name, border=0)
        pdf.cell(w=150, h=20, txt=f"${roommate2_pay}", border=0, ln=1)

        # If the reports directory doesn't already exist, create it.
        if os.path.exists("reports"):
            pass
        else:
            os.mkdir("reports")

        # Change directory to reports, and open PDF
        os.chdir("reports")
        pdf.output(self.filename)
        webbrowser.open(self.filename)