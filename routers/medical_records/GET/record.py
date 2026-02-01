from fastapi import APIRouter, HTTPException
from core.supabase import supabase

router = APIRouter(prefix="/medical_records", tags=["Medical Records"])

@router.get("/record/{record_id}")
def get_medical_record(record_id: str):
    try:
        result = supabase.table("medical_records").select("*").eq("id", record_id).execute()
        if not result.data:
            raise HTTPException(status_code=404, detail="Medical record not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving medical record: {str(e)}")
    return {"medical_record": result.data[0]}