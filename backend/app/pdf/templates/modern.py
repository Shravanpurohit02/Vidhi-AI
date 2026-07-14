from io import BytesIO

from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

from app.pdf.base_template import BaseInvoiceTemplate


class ModernTemplate(BaseInvoiceTemplate):

    def render(self, invoice):
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)

        pdf.setFillColor(HexColor("#1F4E79"))
        pdf.rect(0, 760, 595, 82, fill=1, stroke=0)

        pdf.setFillColor(HexColor("#FFFFFF"))
        pdf.setFont("Helvetica-Bold", 22)
        pdf.drawString(40, 790, "VIDHI AI")

        pdf.setFont("Helvetica", 11)
        pdf.drawString(40, 770, "Professional Legal Invoice")

        pdf.setFillColor(HexColor("#000000"))

        y = 720

        rows = [
            ("Invoice", invoice.invoice_number),
            ("Issue Date", invoice.issue_date.date()),
            ("Due Date", invoice.due_date.date()),
            ("Status", invoice.status),
            ("Total", f"₹ {invoice.total_amount}"),
            ("Paid", f"₹ {invoice.amount_paid}"),
            ("Balance", f"₹ {invoice.balance_due}"),
        ]

        pdf.setFont("Helvetica", 12)

        for key, value in rows:
            pdf.setFont("Helvetica-Bold", 12)
            pdf.drawString(40, y, key)

            pdf.setFont("Helvetica", 12)
            pdf.drawString(170, y, str(value))

            y -= 24

        if invoice.notes:
            y -= 15
            pdf.setFont("Helvetica-Bold", 12)
            pdf.drawString(40, y, "Notes")

            y -= 20
            pdf.setFont("Helvetica", 11)
            pdf.drawString(40, y, invoice.notes)

        pdf.showPage()
        pdf.save()

        buffer.seek(0)
        return buffer
