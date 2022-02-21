from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_item(q, p):
    try:
        return float(int(q)/int(p))
    
    except ValueError:
        return "Values entered are not numbers."
        
