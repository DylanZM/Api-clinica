from fastapi import FastAPI
from supabase import create_client, Client
from dotenv import load_dotenv
import os
from routers import all_routers

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI(
    title="API clinic",
)

for router in all_routers:
    app.include_router(router)


@app.get("/")
def root():
    return {"status": "API clinic activated"}


@app.get("/health")
def health_check():
    try:
        supabase.auth.get_user()
        return {"status": "Conected to supabase"}
    except Exception as e:
        return {"status": "Connection error", "error": str(e)}
