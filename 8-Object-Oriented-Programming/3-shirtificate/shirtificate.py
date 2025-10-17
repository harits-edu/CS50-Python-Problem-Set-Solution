from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.image("shirtificate.png", x=10, y=95, w=self.w - 20)


def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Times", "B", 50)
    pdf.cell(0, 70, "CS50 Shirtificate", align="C")
    pdf.set_text_color(255, 255, 255)
    pdf.ln()
    pdf.set_font("Courier", "B", 24)
    pdf.cell(0, 150, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
