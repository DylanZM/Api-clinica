from fastapi import APIRouter, HTTPException
from core.supabase import supabase


router = APIRouter(prefix="/patients", tags=["Patients"])


@router.get("/{patient_id}")
def get_patient(patient_id: str):
    try:
        response = supabase.table("patients").select("*").eq("id", patient_id).single().execute()
        patient = response.data
        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching patient: {str(e)}")
    return {"patient": patient}
