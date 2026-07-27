def calculate_score(profile):

    financial = profile["financial_score"]
    lifestyle = profile["lifestyle_score"]
    travel = profile["travel_score"]


    overall = (
        financial * 0.5
        + lifestyle * 0.3
        + travel * 0.2
    )


    return {

        "Financial": financial,
        "Lifestyle": lifestyle,
        "Travel": travel,
        "Overall": round(overall,1)

    }
