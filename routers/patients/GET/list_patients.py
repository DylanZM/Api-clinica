from fastapi import APIRouter, HTTPException
from core.supabase import supabase

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.get("/")
def list_patients():
    try:
        response = supabase.table("patients").select("*").execute()
        patients = response.data
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching patients: {str(e)}")
    return {"patients": patients}