from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from core.supabase import supabase

router = APIRouter(prefix="/users", tags=["Users"])

class CreateUserRequest(BaseModel):
    username: str
    email: str
    password: str
    role: str

# Simulación: en producción, extrae el rol real del usuario autenticado
def get_current_user_role():
    return "admin"  # Cambia a "assistant" para probar

@router.post("")
def create_user(data: CreateUserRequest, current_role: str = Depends(get_current_user_role)):
    if current_role == "admin":
        allowed_roles = ["admin", "doctor", "assistant", "patient"]
    elif current_role == "assistant":
        allowed_roles = ["patient"]
    else:
        raise HTTPException(status_code=403, detail="Not authorized to create users")

    if data.role not in allowed_roles:
        raise HTTPException(status_code=400, detail="Role not allowed for this user")

    try:
        auth_user = supabase.auth.sign_up({
            "email": data.email,
            "password": data.password
        })
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error in Supabase Auth: {str(e)}")
    try:
        user_insert = supabase.table("users").insert({
            "username": data.username,
            "role": data.role,
            "email": data.email,
            "auth_id": auth_user.user.id  
        }).execute()
    except Exception as e:
        supabase.auth.admin.delete_user(auth_user.user.id)
        raise HTTPException(status_code=400, detail=f"Error in users table: {str(e)}")
    return {"status": "User created", "user_id": auth_user.user.id}