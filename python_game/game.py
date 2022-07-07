from aws_requests_auth.aws_auth import AWSRequestsAuth
import requests
import json
import urllib.parse
from requests.auth import HTTPBasicAuth
import requests
from time import sleep


# Get question
# get values
# submit question
# {type: get, q: 1, user: cody} -> status, question, data
# {type: submit, q: 1, user: cody, data: result} -> status, result

class Challenge:

    def __init__(self, prompt, data):
        self.prompt = prompt
        self.q = prompt
        self.question = prompt
        self.data = data

    def __str__(self):
        return f"{self.q} {self.data}"


class Server:

    def __init__(self, url, key, output=True):
        self.url = url
        self.api_key = key
        self.aws_header = {'X-API-KEY': self.api_key}
        self.chatty = output

    def output(self, *args, **kwargs):
        if self.chatty:
            print(*args, **kwargs)

    def get(self, q):
        data = {
            "type": "get",
            "q": q,
            "user": "cody"
        }
        r = requests.post(api_url, headers=self.aws_header, json=data)
        challenge = Challenge(r.json().get('q'), r.json().get('data'))
        self.output(f"\n{challenge}")
        return challenge

    def submit(self, q, answer):
        sleep(.25)
        data = {
            "type": "submit",
            "q": q,
            "user": "cody",
            "data": answer
        }
        self.output(f"Submitting: {answer} for Q{q}")
        r = requests.post(api_url, headers=self.aws_header, json=data)
        self.output(f'{answer} is {"Correct!" if r.json() else "Incorrect"} for Q{q}')

        return r.json()























