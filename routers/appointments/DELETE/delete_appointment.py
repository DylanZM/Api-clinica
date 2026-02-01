from fastapi import APIRouter, HTTPException
from core.supabase import supabase



router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.delete("/{appointment_id}")
async def delete_appointment(appointment_id: int):
    try:
        result = supabase.table("appointments").delete().eq("id", appointment_id).execute()
        if not result.data:
            raise HTTPException(status_code=404, detail="Appointment not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting appointment: {str(e)}")
    return {"status": "Appointment deleted", "appointment_id": appointment_id}