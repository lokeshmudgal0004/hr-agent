from weasyprint import HTML


def generate_pdf_report(
    html_content,
    output_path
):

    HTML(
        string=html_content
    ).write_pdf(output_path)

    print(
        f"PDF report saved at: {output_path}"
    )