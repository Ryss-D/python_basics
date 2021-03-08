#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, Paragrapho):

    styles = getSampleStyleSheet()    
    report = SimpleDocTemplate(attachment)
    report_tittle = Paragraph(title, styles["h1"])
    report_body = Paragraph(Paragrapho.replace('\n', '<br />\n'), styles["p"]) 
    report.build([report_tittle, report_body])
