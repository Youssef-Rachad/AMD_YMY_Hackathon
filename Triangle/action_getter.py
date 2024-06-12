import json


def read_sarif_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

sarif_data = read_sarif_file('../SARIF_DEPOT/.sarif')

alerts = []
for run in sarif_data["runs"]:
    for result in run["results"]:
        alerts.append(result["message"]["text"])

print(alerts)
