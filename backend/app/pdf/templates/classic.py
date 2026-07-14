from io import BytesIO

from reportlab.pdfgen import canvas

from app.pdf.base_template import BaseInvoiceTemplate


class ClassicTemplate(BaseInvoiceTemplate):

    def render(self, invoice):
        buffer = BytesIO()

        pdf = canvas.Canvas(buffer)

        y = 800

        pdf.setFont("Helvetica-Bold", 18)
        pdf.drawString(40, y, "VIDHI AI")

        y -= 35
        pdf.setFont("Helvetica", 12)

        fields = [
            ("Invoice No", invoice.invoice_number),
            ("Issue Date", invoice.issue_date.date()),
            ("Due Date", invoice.due_date.date()),
            ("Status", invoice.status),
            ("Total Amount", f"₹ {invoice.total_amount}"),
            ("Amount Paid", f"₹ {invoice.amount_paid}"),
            ("Balance Due", f"₹ {invoice.balance_due}"),
        ]

        for label, value in fields:
            pdf.drawString(40, y, f"{label}: {value}")
            y -= 20

        if invoice.notes:
            y -= 10
            pdf.setFont("Helvetica-Bold", 12)
            pdf.drawString(40, y, "Notes")

            y -= 20
            pdf.setFont("Helvetica", 12)
            pdf.drawString(40, y, invoice.notes)

        pdf.showPage()
        pdf.save()

        buffer.seek(0)
        return buffer
