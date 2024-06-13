import requests
import json

history = [{
            "role": "user",
            "content": "Write me some vulnerable code in c"
        },
        {
            "role": "assistant",
            "content": {
                "response_text": "Sure, here is an example of a vulnerable C code. This code is vulnerable to a buffer overflow attack.\n\n```c\n#include <stdio.h>\n#include <string.h>\n\nvoid unsafe_function(char *input) {\n    char buffer[10];\n    strcpy(buffer, input);\n}\n\nint main(int argc, char *argv[]) {\n    if (argc < 2) {\n        printf(\"Usage: %s <input>\\n\", argv[0]);\n        return 1;\n    }\n\n    unsafe_function(argv[1]);\n\n    return 0;\n}\n```\n\nIn this code, the `unsafe_function` copies the input string into a buffer without checking the size of the input. If the input string is longer than the buffer, it will overflow the buffer and overwrite adjacent memory. This can lead to unpredictable behavior, including program crashes, incorrect operation, and security vulnerabilities.",
                "relevant_links": [
                    "Not Applicable"
                ]
            }
        },]

cookie = "_gcl_au=1.1.1539318608.1715104059; _mkto_trk=id:885-ZYT-361&token:_mch-amd.com-1715104060210-93879; _rdt_uuid=1715104060675.a6cb767b-41f9-454f-8037-327403ea9303; _ga=GA1.1.1693354044.1715104061; fpestid=qoOA7tNa967bayvKOG1K08g3nWscrnrVLs6yLxoHXYl2r1fzl8-ZRUfHSewCBApXD2n5kw; __de_uid=4-fy2guzab-lvwoobpj; _cc_id=327abf114b19cdcb60872fac07ba71b3; _clck=c2sl8o%7C2%7Cflr%7C0%7C1588; _fbp=fb.1.1715714009240.85196269; OptanonAlertBoxClosed=2024-05-14T19:14:14.239Z; OptanonConsent=isGpcEnabled=0&datestamp=Tue+May+14+2024+15%3A14%3A16+GMT-0400+(Eastern+Daylight+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=32154369-f426-4ede-8cca-53b02c69f9b4&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0002%3A1%2CC0004%3A1%2CC0003%3A1%2CC0001%3A1&geolocation=CA%3BON&AwaitingReconsent=false; _ga_5KTY6V8M8J=GS1.1.1715714006.2.1.1715714079.49.0.0; _nabu=CfDJ8Hcc9kptfwtPgvHwYxAuH6fsC5E9h1M2rypUIoi7oPHsDhIGSndqGXTsnmO%2FzsXZ88dovlRDKBXnNhGrWubKTDEBqWZUIBpLwtxqQoWrSvglnjR%2BZHW5piEGwcf44Vb%2FQjb%2FnDcSqIkWzM6GsOUSQVCSIJImSToPCiY3pgR2clcX"
payload = {
    "history": [
        
       
    ],
    "user_prompt": "Tell me something I don't know",
    "plugins": [],
    "index_names": [],
    "is_doc_summary": False,
    "doc_assist_file_name": "null",
    "file_name": "",
    "jira_oauth2": "null"
}
auth = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIzZmQzZGNlNS1hZjExLTRiMDEtYTUxNS01YjA1ZmVjMmY5Y2MiLCJzdWIiOiJ5b2VsbWF5cyIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWUiOiJ5b2VsbWF5cyIsImV4cCI6MTcyMDg5MzY2NCwiaXNzIjoiaHR0cHM6Ly9uYWJ1LmFtZC5jb20vIiwiYXVkIjoiaHR0cHM6Ly9uYWJ1LmFtZC5jb20vIn0.LbVIM3slgdP679BVHVP4O8V4MpKZLKbK7p0iOXwRdzHBW2GjNc6I2m81BoTGvO4_2Zj8PbTEVXFxIIChtNohGMIkRduKmZUgJ-_VdOXWkYPvza132ixEZqMAajOSVQO4cF332bxBUisISkr0FXkTKymfcS6o9ITE7wPQdE-Adil9RI_F3aRnWomZ4jSdPv2RP0mOCiZdvdFbbVUFiJ_ztPcG95pIzEgzcANHyebskavKGsUgttEf0RZyKt5B4Xvo81m_m_lw7p_PuxfWCL-zAukWXB11ZiXPGZUHEPb8v8v7ox5hU-Y595IZy7l4Isf04JXeYVwAhq3QYBhOp4zuWw"

print(json.dumps(payload))
res =requests.post("https://nabu.amd.com/KB/ask_kb?&kb=AMD%20Private%20ChatGPT&model_name=gpt-4-32k", headers={
    "Authorization": auth,
    "Content-Type": "application/json"
}, data=json.dumps(payload))

print(res.text)