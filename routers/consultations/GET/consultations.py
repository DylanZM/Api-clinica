from fastapi import APIRouter, HTTPException
from core.supabase import supabase

router = APIRouter(prefix="/consultations", tags=["Consultations"])
@router.get("/")
def get_consultations():
    try:
        result = supabase.table("medical_consultations").select("*").execute()
        if not result.data:
            raise HTTPException(status_code=404, detail="No consultations found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving consultations: {str(e)}")
    return {"consultations": result.data}