from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.supabase import supabase

router = APIRouter(prefix="/auth", tags=["Auth"])

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str
    role: str 

@router.post("/register")
def register(data: RegisterRequest):
 
    try:
        auth_user = supabase.auth.sign_up({
            "email": data.email,
            "password": data.password
        })
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error en Supabase Auth: {str(e)}")


    try:
        user_insert = supabase.table("users").insert({
            "username": data.username,
            "role": data.role,
            "email": data.email,
            "auth_id": auth_user.user.id
        }).execute()
    except Exception as e:
     
        supabase.auth.admin.delete_user(auth_user.user.id)
        raise HTTPException(status_code=400, detail=f"Error en tabla users: {str(e)}")

    return {"status": "Usuario registrado", "user_id": auth_user.user.id}
