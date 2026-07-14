from io import BytesIO

from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

from app.models.branding import Branding


class PDFService:

    @staticmethod
    def generate_invoice(db, invoice):
        branding = db.query(Branding).first()

        pdf_buffer = BytesIO()
        pdf = canvas.Canvas(pdf_buffer)

        primary = HexColor(branding.primary_color if branding else "#1F4E79")

        pdf.setFillColor(primary)
        pdf.setFont("Helvetica-Bold", 22)

        pdf.drawString(40, 800, branding.firm_name if branding else "VIDHI AI")

        pdf.setFillColorRGB(0, 0, 0)

        y = 775

        if branding and branding.advocate_name:
            pdf.drawString(40, y, branding.advocate_name)
            y -= 18

        if branding and branding.address:
            pdf.drawString(40, y, branding.address)
            y -= 18

        if branding and branding.phone:
            pdf.drawString(40, y, "Phone : " + branding.phone)
            y -= 18

        if branding and branding.email:
            pdf.drawString(40, y, branding.email)
            y -= 30

        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(40, y, "INVOICE")

        y -= 35

        pdf.setFont("Helvetica", 12)

        pdf.drawString(40, y, f"Invoice No : {invoice.invoice_number}")
        y -= 20

        pdf.drawString(40, y, f"Issue Date : {invoice.issue_date}")
        y -= 20

        pdf.drawString(40, y, f"Due Date : {invoice.due_date}")
        y -= 20

        pdf.drawString(40, y, f"Status : {invoice.status}")
        y -= 30

        pdf.drawString(40, y, f"Total : ₹ {invoice.total_amount}")
        y -= 20

        pdf.drawString(40, y, f"Paid : ₹ {invoice.amount_paid}")
        y -= 20

        pdf.drawString(40, y, f"Balance : ₹ {invoice.balance_due}")

        pdf.showPage()
        pdf.save()

        pdf_buffer.seek(0)

        return pdf_buffer
