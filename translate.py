#LUCIANO CARBONERA

import requests, json

def translate():
    texto = input("Digite seu texto em qualquer idioma para receber em Frances: ")
    key = '################################'
    endpoint = "https://api.cognitive.microsofttranslator.com"
    location = "global"

    path= '/MicrosoftTranslator'
    url= endpoint + path

    params = {
        'api-version': '3.0',
        'to': ['de', 'fr']
        #'to': ['de', 'it']
        }
    url = endpoint + path

    headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json'
        }

    # You can pass more than one object in body.
    body = [{
            'text': texto
        }]

    request = requests.post(url, params=params, headers=headers, json=body)
    response = request.json()

    print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

translate()