from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.supabase import supabase
from schemas.appointments import Status
from typing import Optional


router = APIRouter(prefix="/appointments", tags=["Appointments"])

class UpdateAppointmentRequest(BaseModel):
    appointment_date: Optional[str] = None
    status: Optional[Status] = None

@router.put("/{appointment_id}")
async def update_appointment(appointment_id: int, appointment: UpdateAppointmentRequest):
    data = {}
    if appointment.appointment_date is not None:
        data["appointment_date"] = appointment.appointment_date
    if appointment.status is not None:
        data["status"] = appointment.status
    if not data:
        raise HTTPException(status_code=400, detail="No se proporcionaron campos para actualizar")
    try:
        result = supabase.table("appointments").update(data).eq("id", appointment_id).execute()
        if hasattr(result, 'status_code') and result.status_code >= 400:
            raise HTTPException(status_code=result.status_code, detail="Error updating the appointment")
        if not result.data:
            raise HTTPException(status_code=400, detail="Could not update the appointment")
        return {"message": "Appointment updated successfully", "appointment": result.data[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))