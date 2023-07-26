def get_value(obj, key):
    """Gets the value of a nested object given the key."""
    if key not in obj:
        return None

    path = key.split("/")
    value = obj
    for p in path:
        if isinstance(value, dict):
            value = value.get(p)
        elif isinstance(value, list):
            if p in value:
                value = value[p]
            else:
                return None

    return value

def main():
    """Prints the value of a nested object given the key."""
    obj = {
        "a": {
            "b": {
                "c": "d"
            }
        },
        "x": {
            "y": {
                "z": "a"
            }
        }
    }

    value = get_value(obj, "a/b/c")
    print(value)
    value = get_value(obj, "x/y/z")
    print(value)

if __name__ == "__main__":
    main()

