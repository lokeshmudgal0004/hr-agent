import os

from flask import request, jsonify
from app.services.shortlisting_service import (run_pipeline)
from app.scoring.override_manager import (apply_override)

UPLOAD_FOLDER = "uploads/jd"



def upload_job():

    file = request.files["file"]

    path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(path)

    return jsonify({
        "message": "JD uploaded successfully",
        "path": path
    })

RESUME_FOLDER = "uploads/resumes"



def upload_resumes():

    files = request.files.getlist("files")

    uploaded = []

    for file in files:

        path = os.path.join(
            RESUME_FOLDER,
            file.filename
        )

        file.save(path)

        uploaded.append(file.filename)

    return jsonify({
        "uploaded": uploaded
    })

def run_shortlisting():

    ranked_candidates = run_pipeline()

    return jsonify({
        "rankings": ranked_candidates
    })

def apply_hr_override():

    data = request.json

    return jsonify({
        "message": "Override applied",
        "data": data
    })