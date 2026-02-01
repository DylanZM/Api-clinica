from fastapi import APIRouter, HTTPException
from core.supabase import supabase

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.get("")
async def get_appointments():
    try:
        result = supabase.table("appointments").select("*").execute()
        if hasattr(result, 'status_code') and result.status_code >= 400:
            raise HTTPException(status_code=result.status_code, detail="Error fetching appointments")
        return {"appointments": result.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))