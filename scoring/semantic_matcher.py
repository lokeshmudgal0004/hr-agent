from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(embedding1, embedding2):

    similarity = cosine_similarity(
        [embedding1],
        [embedding2]
    )[0][0]

    return float(similarity)


def similarity_to_score(similarity):

    if similarity >= 0.85:
        return 10

    elif similarity >= 0.75:
        return 8

    elif similarity >= 0.60:
        return 6

    elif similarity >= 0.45:
        return 4

    return 2