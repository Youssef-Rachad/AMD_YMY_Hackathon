import json
import os
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import requests
import datetime

global_results = []
date = datetime.datetime.now()
dir_path = os.path.join(os.getcwd(), '../SARIF_DEPOT')

def writer():
    
    with open(os.path.join(os.getcwd(), "../website", "_posts", f"{str(date)[:10]}__results.md"), "w") as f:
        f.write(str(global_results))



def generate_code_snippet(prompt):
    auth = os.getenv("AUTH_TOKEN")
    payload = {
        "history": [],
        "user_prompt": prompt,
        "plugins": [],
        "index_names": [],
        "is_doc_summary": False,
        "doc_assist_file_name": "null",
        "file_name": "",
        "jira_oauth2": "null"
    }
    res = requests.post("https://nabu.amd.com/KB/ask_kb?&kb=AMD%20Private%20ChatGPT&model_name=gpt-4-32k", headers={
        "Authorization": auth,
        "Content-Type": "application/json"
    }, data=json.dumps(payload)) 
    return res.text

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

def generate_fix(prompt):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    # Set the padding token if it's not already set
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    inputs = tokenizer.encode_plus(prompt, return_tensors='pt', padding='longest', truncation=True)
    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']

    outputs = model.generate(input_ids, attention_mask=attention_mask, max_length= 500, num_return_sequences=1, temperature=0.7, top_k=50, top_p=0.95)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def get_most_recent_file(dir_path):
    files = os.listdir(dir_path)
    paths = [os.path.join(dir_path, basename) for basename in files]
    return max(paths, key=os.path.getctime)

def get_code_snippet(file_path, start_line):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_string = ""
        for element in lines:
            line_string = line_string + element
    return line_string + f".    Error at line {start_line}"


most_recent_file = get_most_recent_file(dir_path)
alerts = parse_sarif(most_recent_file)
for alert in alerts:
    print(alert)
    for location in alert['locations']:
        file_path = os.path.join(os.getcwd(), '..', location['uri'])
        code_snippet = get_code_snippet(file_path, location['startLine'])
        # print(f"Code snippet: {code_snippet}")


        language, issue_type = alert['ruleId'].split("/")

        prompt = f"""
                Hey, I have a "{issue_type}" vulnerability in this python script:

                ```
                {code_snippet}
                ```

                Here's a description of the issue: "{alert['message']}"


                Pleas provided 3 solutions to fix this code delimited by "##########".
                """

        # print(prompt)
        prompt = f"Generate a fix for the code issue: {alert['message']}\nCode: {code_snippet}"
        fix = generate_code_snippet(prompt)

        global_results.append({code_snippet, fix})
        print(f"Generated fix: {fix}")


writer()