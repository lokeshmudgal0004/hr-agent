from flask import Blueprint

from app.api.controllers import (
    upload_job,
    upload_resumes,
    upload_linkedin_profiles,
    run_shortlisting,
    apply_hr_override
)

api = Blueprint("api", __name__)


api.route(
    "/upload-jd",
    methods=["POST"]
)(upload_job)

api.route(
    "/upload-resumes",
    methods=["POST"]
)(upload_resumes)

api.route(
    "/upload-linkedin",
    methods=["POST"]
)(upload_linkedin_profiles)

api.route(
    "/run-shortlisting",
    methods=["POST"]
)(run_shortlisting)

api.route(
    "/override-score",
    methods=["POST"]
)(apply_hr_override)