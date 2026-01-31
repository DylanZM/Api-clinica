from pydantic import BaseModel
from core.supabase import supabase
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/users", tags=["Users"])

class UpdateUserRequest(BaseModel):
    username: str = None
    email: str = None
    role: str = None
    active: bool = None

@router.put("/{user_id}")
def update_user(user_id: str, data: UpdateUserRequest):
    update_data = {k: v for k, v in data.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No data provided for update")
    try:
        result = supabase.table("users").update(update_data).eq("id", user_id).execute()
        if not result.data:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating user: {str(e)}")
    return {"status": "User updated", "user_id": user_id}
