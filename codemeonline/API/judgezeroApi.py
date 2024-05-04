import requests
import json
from dotenv import load_dotenv
import os
import base64
import time

load_dotenv()

class JudgeZeroApi:

    def __init__(self, language_id:int, source_code:str) -> None:

        self.language_id = language_id
        self.source_code = source_code

    def get_token(self):

        url = "https://judge0-ce.p.rapidapi.com/submissions"

        querystring = {"base64_encoded":"false","fields":"*"}

        payload = {
            "language_id": self.language_id,
            "source_code": self.source_code,
            "callback_url": "https://codexme.reflex.run/",
            "expected_output": "null",
            
        }

        headers = {
            "content-type": "application/json",
            "Content-Type": "application/json",
            "X-RapidAPI-Key": os.getenv("RapidAPI_Key"),
            "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com",
        }

        response = requests.post(url, json=payload, headers=headers, params=querystring)
        print (response.json())
        if response.status_code == 201:
            response_data = response.json()
            token = response_data['token']
            print (token)

            def get_results(token):
                time.sleep(2)
                url = f"https://judge0-ce.p.rapidapi.com/submissions/{token}"
                querystring = {"base64_encoded":"false","fields":"*"}
                headers = {
                    "X-RapidAPI-Key": os.getenv("RapidAPI_Key"),
                    "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
                }
                response = requests.get(url, headers=headers, params=querystring)

                data_response= response.json()
                print (data_response)
                return data_response
        
            return get_results(token=token)
        else:
            print(f"Failed to get valid response. Status Code: {response.status_code}")            




