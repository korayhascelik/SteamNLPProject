from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import mm

def md_to_flowables(md_text):
    styles = getSampleStyleSheet()
    h1 = ParagraphStyle('Heading1', parent=styles['Heading1'], fontSize=16, leading=20)
    h2 = ParagraphStyle('Heading2', parent=styles['Heading2'], fontSize=14, leading=18)
    normal = styles['Normal']

    flow = []
    for line in md_text.splitlines():
        line = line.rstrip()
        if line.startswith('# '):
            flow.append(Paragraph(line[2:].strip(), h1))
            flow.append(Spacer(1, 6))
        elif line.startswith('## '):
            flow.append(Paragraph(line[3:].strip(), h2))
            flow.append(Spacer(1, 4))
        elif line.startswith('### '):
            flow.append(Paragraph(line[4:].strip(), normal))
            flow.append(Spacer(1, 3))
        elif line == '---':
            flow.append(Spacer(1, 6))
        elif line.strip() == '':
            flow.append(Spacer(1, 4))
        else:
            flow.append(Paragraph(line, normal))
    return flow


def main():
    with open('REPORT.md', 'r', encoding='utf-8') as f:
        md = f.read()

    doc = SimpleDocTemplate('report.pdf', pagesize=A4,
                            rightMargin=20*mm, leftMargin=20*mm,
                            topMargin=20*mm, bottomMargin=20*mm)
    flow = md_to_flowables(md)
    doc.build(flow)
    print('report.pdf oluşturuldu.')

if __name__ == '__main__':
    main()
