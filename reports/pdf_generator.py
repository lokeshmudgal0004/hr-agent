from weasyprint import HTML
from weasyprint import CSS

import os


def generate_pdf_report(
    html_content,
    output_path
):

    output_dir = os.path.dirname(
        output_path
    )

    if output_dir:

        os.makedirs(
            output_dir,
            exist_ok=True
        )

    pdf_styles = CSS(
        string="""
        @page {
            size: A4;
            margin: 20px;
        }

        body {
            font-family: Arial, sans-serif;
            font-size: 12px;
            color: #222;
        }

        h1, h2, h3 {
            color: #111;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th, td {
            border: 1px solid #ccc;
            padding: 8px;
        }

        .candidate-card {
            page-break-inside: avoid;
            margin-bottom: 20px;
        }
        """
    )

    HTML(
        string=html_content
    ).write_pdf(
        output_path,
        stylesheets=[pdf_styles]
    )

    print(
        f"PDF report saved at: {output_path}"
    )