from fastapi import APIRouter, HTTPException
from schemas.auth import LoginRequest, LoginResponse
from core.supabase import supabase

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest):
    user_resp = (
        supabase
        .table("users")
        .select("id, email")
        .eq("username", data.username)
        .single()
        .execute()
    )

    if not user_resp or not getattr(user_resp, "data", None):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    user_data = user_resp.data
    user_id = user_data.get("id")
    email = user_data.get("email")

    if not user_id or not email:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    session = supabase.auth.sign_in_with_password({
        "email": email,
        "password": data.password
    })

    if not session or not getattr(session, "session", None):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return LoginResponse(
        access_token=session.session.access_token
    )