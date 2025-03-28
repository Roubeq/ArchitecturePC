import json

result_json = [{"target": "region1.host1.metric_name1", "datapoints": [[123.2323232, 1634083200]]}]

result_data = {"timestamp": [], "host": [], "request_type": [], "value": []}

for entry in result_json:
    _, host, request_type = entry["target"].split('.')
    for value, timestamp in entry["datapoints"]:
        result_data["timestamp"].append(timestamp)
        result_data["host"].append(host)
        result_data["request_type"].append(request_type)
        result_data["value"].append(f"{value:.3f}")

print(json.dumps(result_data, indent=4))
