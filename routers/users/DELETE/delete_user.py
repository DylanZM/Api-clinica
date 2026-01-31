from core.supabase import supabase
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/users", tags=["Users"])


@router.delete("/{user_id}")
def delete_user(user_id: str):
    try:
        result = supabase.table("users").delete().eq("id", user_id).execute()
        if not result.data:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting user: {str(e)}")
    return {"status": "User deleted", "user_id": user_id}