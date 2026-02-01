from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.supabase import supabase
from schemas.appointments import Status

router = APIRouter(prefix="/appointments", tags=["Appointments"])

class CreateAppointmentRequest(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: str
    status: Status


@router.post("")
async def create_appointment(appointment: CreateAppointmentRequest):
    data = {
        "patient_id": appointment.patient_id,
        "doctor_id": appointment.doctor_id,
        "appointment_date": appointment.appointment_date,
        "status": appointment.status,
    }
    try:
        result = supabase.table("appointments").insert(data).execute()
        if hasattr(result, 'status_code') and result.status_code >= 400:
            raise HTTPException(status_code=result.status_code, detail="Error al insertar la cita médica")
        if not result.data:
            raise HTTPException(status_code=400, detail="No se pudo crear la cita médica")
        return {"message": "Cita médica creada exitosamente", "appointment": result.data[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))