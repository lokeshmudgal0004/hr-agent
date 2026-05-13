# this endpoint does no longer provide its services


import requests

API_KEY = "d6eb49aa07mshb1aff0f568a298fp13509bjsnc9bab9910e38"


def fetch_linkedin_profile(linkedin_url):

    url = "https://linkedin-data-api.p.rapidapi.com/get-profile-data-by-url"

    querystring = {
        "url": linkedin_url
    }

    headers = {
        "content-type": "application/json",
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com"
    }

    response = requests.get(
        url,
        headers=headers,
        params=querystring
    )

    return response.json()

def normalize_linkedin_data(data):

    profile = {
        "name": data.get("full_name"),
        "skills": data.get("skills", []),
        "current_role": data.get("headline"),
        "experiences": data.get("experiences", []),
        "education": data.get("education", [])
    }

    return profile