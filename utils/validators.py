def ensure_list(value):

    if isinstance(value, list):

        return value

    return []


def ensure_string(value):

    if isinstance(value, str):

        return value

    return ""