from fastapi import APIRouter, HTTPException
from core.supabase import supabase

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/{user_id}")
def get_user(user_id: str):
    try:
        result = supabase.table("users").select("*").eq("id", user_id).single().execute()
        if not result.data:
            raise HTTPException(status_code=404, detail="User not found")
        user = result.data
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching user: {str(e)}")
    return {"user": user}