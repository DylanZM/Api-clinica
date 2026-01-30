from fastapi import FastAPI

app = FastAPI(
    title="API Clínica",
    
)

@app.get("/")
def root():
    return {"status": "API Clínica funcionando "}
