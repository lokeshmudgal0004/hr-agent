import json

from reports.report_builder import (
    build_report
)

from reports.html_generator import (
    generate_html_report
)

from reports.pdf_generator import (
    generate_pdf_report
)

from reports.skill_gap import (
    find_missing_skills
)

from reports.summary_generator import (
    generate_summary
)


def generate_full_report(
    jd,
    ranked_candidates
):

    enriched_candidates = []

    for candidate in ranked_candidates:

        candidate["missing_skills"] = (
            find_missing_skills(
                jd["required_skills"],
                candidate["candidate_skills"]
            )
        )

        summary = generate_summary(
            jd,
            candidate
        )

        candidate["strengths"] = (
            summary["strengths"]
        )

        candidate["weaknesses"] = (
            summary["weaknesses"]
        )

        enriched_candidates.append(
            candidate
        )

    report_data = build_report(
        jd["role"],
        enriched_candidates
    )

    html_content = generate_html_report(
        report_data
    )

    with open(
        "output/report.html",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html_content)

    generate_pdf_report(
        html_content,
        "output/report.pdf"
    )

    with open(
        "output/report.json",
        "w"
    ) as file:

        json.dump(
            report_data,
            file,
            indent=4
        )

    return report_data