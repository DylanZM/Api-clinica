from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.supabase import supabase
from typing import Optional
from schemas.patients import GenderEnum

router = APIRouter(prefix="/patients", tags=["Patients"])



class CreatePatientRequest(BaseModel):
    first_name: str
    last_name: str
    birth_date: Optional[str] = None
    gender: GenderEnum
    phone : str


@router.post("")
def create_patient(data: CreatePatientRequest):
    try:
        patient_insert = supabase.table("patients").insert({
            "first_name": data.first_name,
            "last_name": data.last_name,
            "birth_date": data.birth_date,
            "gender": data.gender,
            "phone": data.phone
        }).execute()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating patient: {str(e)}")
    return {"status": "Patient created", "patient_id": patient_insert.data[0]["id"]}
