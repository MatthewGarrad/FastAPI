from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_item(q, p):
    try:
        return float(int(q)/int(p))
    
    except ValueError:
        webbrowser.open("file:///C:/Users/Matthew/Documents/GitHubPages/index.html", new=0)
        return "Values entered are not numbers."
        
