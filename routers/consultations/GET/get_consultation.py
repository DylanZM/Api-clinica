from fastapi import APIRouter, HTTPException
from core.supabase import supabase

router = APIRouter(prefix="/consultations", tags=["Consultations"])
@router.get("/{consultation_id}")
def get_consultation(consultation_id: str):
    try:
        result = supabase.table("medical_consultations").select("*").eq("id", consultation_id).execute()
        if not result.data:
            raise HTTPException(status_code=404, detail="Consultation not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving consultation: {str(e)}")
    return {"consultation": result.data[0]}