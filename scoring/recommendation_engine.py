def generate_recommendation(score):

    if score >= 8:
        return "Strong Hire"

    elif score >= 6:
        return "Consider"

    elif score >= 4:
        return "Weak Match"

    return "Reject"