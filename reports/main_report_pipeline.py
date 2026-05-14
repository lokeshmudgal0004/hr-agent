import os
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
                jd.get(
                    "required_skills",
                    []
                ),
                candidate.get(
                    "candidate_skills",
                    []
                )
            )
        )

        try:

            summary = generate_summary(
                jd,
                candidate
            )

            candidate["strengths"] = (
                summary.get(
                    "strengths",
                    []
                )
            )

            candidate["weaknesses"] = (
                summary.get(
                    "weaknesses",
                    []
                )
            )

        except Exception as error:

            print(
                f"Summary generation failed for "
                f"{candidate.get('candidate_name')}: "
                f"{error}"
            )

            candidate["strengths"] = []

            candidate["weaknesses"] = []

        enriched_candidates.append(
            candidate
        )

    report_data = build_report(
        jd.get(
            "role",
            "Unknown Role"
        ),
        enriched_candidates
    )

    html_content = generate_html_report(
        report_data
    )

    os.makedirs(
        "output",
        exist_ok=True
    )

    with open(
        "output/report.html",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            html_content
        )

    generate_pdf_report(
        html_content,
        "output/report.pdf"
    )

    with open(
        "output/report.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report_data,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(
        "Report generation completed successfully."
    )

    return report_data