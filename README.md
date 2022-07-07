## Installation
`pip3 install --user . `


## Getting Started
```python
from python_game import Server, Challenge

api_key = 'your_api_key'
api_url = 'url'

server = Server(api_url, api_key, output=True)

def solve_q0():
    challenge = server.get(0)
    answer = challenge.data
    server.submit(0, answer)

def solve_q1():
    challenge = server.get(1)
    
solve_q0()
solve_q1()
```