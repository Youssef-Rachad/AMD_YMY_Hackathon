import requests
import json

# Fetch the SARIF file
url = "https://api.github.com/repos/{owner}/{repo}/code-scanning/alerts"
headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers)
sarif_file = response.json()

# Parse the SARIF file
alerts = []
for run in sarif_file["runs"]:
    for result in run["results"]:
        alerts.append(result["message"]["text"])

print(alerts)
# Send alerts to ChatGPT API
# url = "https://api.openai.com/v1/engines/davinci-codex/completions"
# headers = {"Content-Type": "application/json", "Authorization": "Bearer YOUR_OPENAI_API_KEY"}
# for alert in alerts:
#     data = {"prompt": alert, "max_tokens": 60}
#     response = requests.post(url, headers=headers, data=json.dumps(data))
#     print(response.json())
