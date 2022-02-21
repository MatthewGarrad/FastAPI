from typing import Optional

from fastapi import FastAPI

from pyperclip import *
import webbrowser

app = FastAPI()


@app.get("/")
def read_item(q, p):
    try:
        return float(int(q)/int(p))
    
    except ValueError:
        webbrowser.open("file:///C:/Users/Matthew/Documents/GitHubPages/index.html", new=0)
        return "Values entered are not numbers, the page has been reopened for you to try again."
        
