from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string",
            "minLength": 20
        },
        "content": {
            "type": "string",
            "minLength": 200
        },
        "category": {
            "type": "string",
            "minLength": 3
        },
        "status": {
            "type": "string",
            "enum": [
                "publish",
                "draft",
                "thrash"
            ]
        }
    },
    "required": [
        "title",
        "content",
        "category",
        "status"
    ]
}

data = {
    "title": "This is a short title",
    "content": "This is a short content",
    "category": "abc",
    "status": "draft"
}

try:
    validate(instance=data, schema=schema)
    print("Data is valid")
except Exception as e:
    print(f"Data is invalid: {e.message}")
