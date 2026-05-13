from jinja2 import Environment
from jinja2 import FileSystemLoader

import os


TEMPLATE_DIR = os.path.join(
    os.path.dirname(__file__),
    "templates"
)


def generate_html_report(data):

    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR)
    )

    template = env.get_template(
        "report_template.html"
    )

    html_content = template.render(data)

    return html_content