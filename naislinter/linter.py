def check_keys(target, reference, error=False, trail=[]):
    for key in target.keys():
        trail.append(key)
        trail_string = ".".join(trail)
        if "additionalProperties" in reference.keys():
            trail.pop()
            continue
        if key not in reference["properties"].keys():
            print(f"Field outside of spec: {trail_string}")
            error = True
        if isinstance(target[key], dict):
            check_keys(target[key], reference["properties"][key], error, trail)
        trail.pop()
    return error
