import requests
from time import sleep


class Challenge:

    def __init__(self, prompt, data, additional_data=None):
        self.prompt = prompt
        self.q = prompt
        self.question = prompt
        self.data = data
        self.additional_data = additional_data

    def __str__(self):
        return f"{self.q} DATA: {self.data}"


class Server:

    def __init__(self, url, key, username, output=True):
        self.url = url
        self.api_key = key
        self.aws_header = {'X-API-KEY': self.api_key}
        self.chatty = output
        self.user = username
        self.clint_version = 1.1

    def output(self, *args, **kwargs):
        if self.chatty:
            print(*args, **kwargs)

    def get(self, q):
        data = {
            "type": "get",
            "q": q,
            "user": self.user
        }
        r = requests.post(self.url, headers=self.aws_header, json=data)
        if r.json().get('q') is None and r.json().get('data') is None:
            challenge = Challenge("Sorry, something went wrong getting "
                                  "a question from the server", r.json().get('data'))
        else:
            challenge = Challenge(r.json().get('q'), r.json().get('data'), additional_data=r.json().get('additional_data'))
        self.output(f"\n{challenge}")
        return challenge

    def submit(self, q, answer):
        data = {
            "type": "submit",
            "q": q,
            "user": self.user,
            "data": answer
        }
        self.output(f"Q{q}: Submitting: {answer}")
        r = requests.post(self.url, headers=self.aws_header, json=data)
        if r.json() is True or r.json() is False:
            self.output(f'Q{q}: {"Correct!" if r.json() else "Incorrect"} {answer}')
        else:
            self.output(r.json())

        return r.json()























