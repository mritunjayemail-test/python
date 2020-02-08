import json

json_string = """
{
    "persons": {
        "name": "Kumar",
        "working": false,
        "email": null,
        "address": [
            {
                "street": "Leerdamof",
                "country": "Netherlands"
            }
        ]
    }
}
"""
data_python = json.loads(json_string)
print(data_python)
print(type(data_python))
print("******************************")
data_json_new = json.dumps(data_python, indent=2, sort_keys=True)
print(data_json_new)



