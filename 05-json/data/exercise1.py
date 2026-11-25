import json 


sample = {
    "name": "Asha",
    "age": 30,
    "married": False,
    "scores": (90, 85),
    "nickname": None,
    "height": 1.68,
}


compact_json=json.dumps(sample)
print(f"compact: {compact_json}")


indented_json =json.dumps(sample,indent=2,sort_keys=True)
print("indented: ")
print(indented_json)


def roundtrip(obj):
    json_str = json.dumps(obj)
    return json.loads(json_str)

restored = roundtrip(sample)

before_type = type(sample["scores"]).__name__
after_type = type(restored["scores"]).__name__

print(f"scores type before: {before_type} | after: {after_type}")
print(f"married after: {restored['married']} | nickname after: {restored['nickname']}")
print(f"equal after round trip: {sample == restored}")

int_key_result = roundtrip({1: "a", 2: "b"})
print(f"int keys: {int_key_result}")

try:
    json.dumps({"items": {1, 2, 3}})
except TypeError as err:
    print(f"TypeError: {err}")