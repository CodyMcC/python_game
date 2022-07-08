# Python Game
This project depends on an AWS lambda backend. Code is stored in private repo at: https://github.com/CodyMcC/python_game_backend 

## Installation
`git clone https://github.com/CodyMcC/python_game.git`  
`cd python_game`  
`pip3 install --user -e . `  

To update, run:  
`git pull`


## Getting Started
Create a new python file with the following and then get to work!
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