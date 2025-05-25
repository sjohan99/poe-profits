def sort_json_lists(obj):
    if isinstance(obj, dict):
        return {k: sort_json_lists(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        if all(isinstance(item, dict) and "name" in item for item in obj):
            return sorted([sort_json_lists(item) for item in obj], key=lambda x: x["name"])
        else:
            return sorted([sort_json_lists(item) for item in obj])
    else:
        return obj


def round_json_floats(obj):
    if isinstance(obj, dict):
        return {k: round_json_floats(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [round_json_floats(item) for item in obj]
    elif isinstance(obj, float):
        return round(obj, 4)
    else:
        return obj


def sort_and_round_json(obj):
    return round_json_floats(sort_json_lists(obj))
