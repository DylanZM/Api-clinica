from fastapi import APIRouter, HTTPException
from core.supabase import supabase

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/list")
def list_users():
    try:
        result = supabase.table("users").select("*").execute()
        users = result.data if result.data else []
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching users: {str(e)}")
    return {"users": users}
