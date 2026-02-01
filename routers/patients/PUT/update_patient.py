from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.supabase import supabase
from schemas.patients import GenderEnum

router = APIRouter(prefix="/patients", tags=["Patients"])

class UpdatePatientRequest(BaseModel):
    first_name: str = None
    last_name: str = None
    brith_date: str = None
    gender : GenderEnum = None
    phone : str = None

@router.put("/{patient_id}")
def update_patient(patient_id: str, data: UpdatePatientRequest):
    update_data = {k: v for k, v in data.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No data provided for update")
    try:
        result = supabase.table("patients").update(update_data).eq("id", patient_id).execute()
        if not result.data:
            raise HTTPException(status_code=404, detail="Patient not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating patient: {str(e)}")
    return {"status": "Patient updated", "patient_id": patient_id}

