"""
This file is just for test/demo purpose
"""

from fastapi import FastAPI
import uvicorn
# uvicorn to implement Async server gateway interface

# pip install fastapi uvicorn

app = FastAPI()


@app.get('/')
def index():
    return 'Hello'


@app.get("/welcome")
def get_name(name: str):
    return {"Welcome to FastAPI": f"{name}"}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# 'uvicorn app:app --reload' to run it from command line
# library filename:appname --reload