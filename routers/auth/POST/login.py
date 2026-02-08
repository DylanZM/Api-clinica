from fastapi import APIRouter, HTTPException
from schemas.auth import LoginRequest, LoginResponse
from core.supabase import supabase

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest):
    user_resp = (
        supabase
        .table("users")
        .select("id, email, role")
        .eq("username", data.username)
        .single()
        .execute()
    )

    if not user_resp or not getattr(user_resp, "data", None):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    user_data = user_resp.data
    user_id = user_data.get("id")
    email = user_data.get("email")
    role = user_data.get("role")

    if not user_id or not email:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    session = supabase.auth.sign_in_with_password({
        "email": email,
        "password": data.password
    })

    if not session or not getattr(session, "session", None):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Guardar el refresh token en la tabla user_tokens (si existe)
    refresh_token = getattr(session.session, "refresh_token", None)
    if refresh_token:
        try:
            supabase.table("user_tokens").insert({
                "user_id": user_id,
                "token": refresh_token
            }).execute()
        except Exception as e:
            # No bloquea el login si falla el guardado del token
            print(f"Error guardando refresh token: {e}")

    return LoginResponse(
        access_token=session.session.access_token,

                user={ 
            "id":user_id,
            "email": email,
            "role": role
        }
    )
    