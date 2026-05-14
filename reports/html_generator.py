from jinja2 import (
    Environment,
    FileSystemLoader,
    select_autoescape
)

import os


TEMPLATE_DIR = os.path.join(
    os.path.dirname(__file__),
    "templates"
)


def generate_html_report(data):

    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),

        autoescape=select_autoescape(
            ["html", "xml"]
        ),

        trim_blocks=True,

        lstrip_blocks=True
    )

    template = env.get_template(
        "report_template.html"
    )

    html_content = template.render(
        report=data
    )

    return html_content