from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Image, Paragraph,PageBreak
from reportlab.lib.styles import ParagraphStyle

def download(data, data1, data2, data3, p_data, data4, p_data1, p_data2, p_data3, p_data4, ci1, ci2, ai, img):
    # Create a PDF document
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="apprisal.pdf"'

    # Load the logo image
    logo = Image(f"data:image/png;base64,{img}", width=100, height=50)

    # Define styles
    centered_style = ParagraphStyle(name='Centered', alignment=1)
    bold_style = ParagraphStyle(name='Bold', alignment=1, fontSize=12, fontName='Helvetica-Bold')
    acknowledgement_style = ParagraphStyle(name='Acknowledgement', alignment=0, fontSize=8, fontName='Helvetica')

    # Create Paragraphs
    heading0 = Paragraph("<b>SRM GROUP OF INSTITUTIONS</b>", centered_style)
    heading1 = Paragraph("RAMAPURAM CAMPUS", centered_style)
    heading2 = Paragraph("<b>PROPOSED FACULTY MONTHLY PERFORMANCE SCORE</b>", centered_style)
    heading4 = Paragraph("<b>(A) ACADEMIC / ADMINISTRATIVE CONTRIBUTIONS</b>", bold_style)
    heading5 = Paragraph("<b>(B) RESEARCH PUBLICATIONS</b>", bold_style)
    heading6 = Paragraph("<b>(C) RESEARCH GUIDANCE / PROJECTS / CONSULTANCY</b>", bold_style)
    heading7 = Paragraph("<b>(D) CREATION OF ICT BASED TEACHING LEARNING PEDAGOGY AND CONTENT</b>", bold_style)
    heading8 = Paragraph("<b>Proposed Faculty Monthly Performance Review - 2022 ( Asst. / Asso. / Prof. )</b>", bold_style)

    acknowledgement = Paragraph("*Commitment / Undertaking:", acknowledgement_style)
    acknowledgement1 = Paragraph(f"1. I will- {ci1}", acknowledgement_style)
    acknowledgement2 = Paragraph(f"2. I will- {ci2}", acknowledgement_style)
    acknowledgement3 = Paragraph("<b>Additional Information / Explanation if any:</b>", acknowledgement_style)
    acknowledgement4 = Paragraph("Furnish information regarding Last Month Commitment Progress / Action Taken", acknowledgement_style)
    acknowledgement9 = Paragraph(ai, acknowledgement_style)
    acknowledgement5 = Paragraph("<b>I hereby submit the form for my commitment to accomplish the same. I Understand that, I will be considered as underperformer if I am not able to produce the required outcome which may lead to termination of my service.</b>", acknowledgement_style)
    acknowledgement6 = Paragraph("<b>Remarks given by HoD with Verified Score: ( Faculty progress in criteria - wise to be presented here )</b>", acknowledgement_style)
    acknowledgement7 = Paragraph("<b>Remarks given by HoI: ( Specific comments to be given here )</b>", acknowledgement_style)
    acknowledgement8 = Paragraph("<b>I shall complete the work as per the above commitment given by me. I have read and understood the instructions given by the HOD and HOI. I shall follow their instructions and execute them as per and within the given time period. I understand that, if I do not produce the required outcome, I will be considered as an underperformer which may lead to termination of my service.</b>", acknowledgement_style)

    # Create a table and set its style
    table = Table(data)
    table1 = Table(data1)
    table2 = Table(data2)
    table3 = Table(data3)
    p_table = Table(p_data)
    table4 = Table(data4)
    p_data1 = Table(p_data1)
    p_data1.setStyle(([('FONTSIZE', (0, 0), (-1, -1), 8),]))
    p_data2 = Table(p_data2)
    p_data2.setStyle(([('FONTSIZE', (0, 0), (-1, -1), 8),]))
    p_data3 = Table(p_data3)
    p_data3.setStyle(([('FONTSIZE', (0, 0), (-1, -1), 8),]))
    p_data4 = Table(p_data4)
    p_data4.setStyle(([('FONTSIZE', (0, 0), (-1, -1), 8),]))

    Yale_Blue = "#0B4D92"
    for t in [table, table1, table2, table3, table4]:
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(Yale_Blue)),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

    # Add elements to the Story
    story = []
    story.append(logo)
    story.append(heading0)
    story.append(heading1)
    story.append(heading2)
    story.append(Spacer(1, 20))
    story.append(p_table)
    story.append(Spacer(1, 20))

    # Add table sections
    story.append(heading4)
    story.append(Spacer(1, 10))
    story.append(table)
    story.append(Spacer(1, 20))

    story.append(heading5)
    story.append(Spacer(1, 10))
    story.append(table1)
    story.append(Spacer(1, 20))

    # Add a page break before the table
    story.append(PageBreak())

    story.append(heading6)
    story.append(Spacer(1, 10))
    story.append(table2)
    story.append(Spacer(1, 20))

    story.append(heading7)
    story.append(Spacer(1, 10))
    story.append(table3)    
    story.append(Spacer(1, 10))
    story.append(Spacer(1, 10))

    story.append(Spacer(1, 5, 500))

    story.append(acknowledgement)
    story.append(Spacer(1, 10))
    story.append(acknowledgement1)
    story.append(Spacer(1, 10))
    story.append(acknowledgement2)
    story.append(Spacer(1, 10))
    story.append(Spacer(1, 10))
    story.append(acknowledgement3)
    story.append(Spacer(1, 10))
    story.append(acknowledgement4)
    story.append(acknowledgement9)
    story.append(Spacer(1, 10))
    story.append(Spacer(1, 10))
    story.append(acknowledgement5)

    story.append(Spacer(1, 10))
    story.append(p_data1)

    story.append(Spacer(1, 10))
    story.append(acknowledgement6)

    story.append(Spacer(1, 10))
    story.append(p_data2)

    story.append(PageBreak())
    story.append(Spacer(1, 10))
    story.append(acknowledgement7)

    story.append(Spacer(1, 10))
    story.append(p_data3)

    story.append(acknowledgement8)

    story.append(Spacer(1, 10))
    story.append(p_data4)

    
    story.append(Spacer(1, 10))
    story.append(Spacer(1, 10))
    story.append(heading8)
    story.append(Spacer(1, 10))    
    story.append(table4)
    # Build the PDF document
    doc = SimpleDocTemplate(response, pagesize=letter)
    doc.build(story)

    return response
