import json

def parse_sarif(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    alerts = []
    for run in data['runs']:
        for result in run['results']:
            alert = {}
            alert['ruleId'] = result['ruleId']
            alert['message'] = result['message']['text']
            #alert['level'] = result['level']
            if 'locations' in result:
                alert['locations'] = []
                for location in result['locations']:
                    loc = {}
                    loc['uri'] = location['physicalLocation']['artifactLocation']['uri']
                    if 'region' in location['physicalLocation']:
                        loc['startLine'] = location['physicalLocation']['region']['startLine']
                        #loc['startColumn'] = location['physicalLocation']['region']['startColumn']
                    alert['locations'].append(loc)
            alerts.append(alert)
    return alerts

alerts = parse_sarif('../2024-06-12/python.sarif')
for alert in alerts:
    print(alert)
