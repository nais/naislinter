def check_keys(target, reference, errors, trail):
    for key in target.keys():
        trail.append(key)
        trail_string = ".".join(trail)
        if "additionalProperties" in reference.keys():
            trail.pop()
            continue
        if key not in reference["properties"].keys():
            errors.append(trail_string)
        if isinstance(target[key], dict):
            if key in reference["properties"]:
                errors = check_keys(
                    target[key], reference["properties"][key], errors, trail
                )
            else:
                errors = check_keys(target[key], reference, errors, trail)
        trail.pop()
    return errors
