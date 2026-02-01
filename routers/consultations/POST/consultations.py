from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.supabase import supabase

router = APIRouter(prefix="/consultations", tags=["Consultations"])


class CreateConsultationRequest(BaseModel):
	medical_record_id: int
	doctor_id: int
	reason: str
	diagnosis: str = None
	treatment: str = None
	observations: str = None



@router.post("")
async def create_consultation(consultation: CreateConsultationRequest):
	data = {
		"medical_record_id": consultation.medical_record_id,
		"doctor_id": consultation.doctor_id,
		"reason": consultation.reason,
		"diagnosis": consultation.diagnosis,
		"treatment": consultation.treatment,
		"observations": consultation.observations,
	}
	try:
		result = supabase.table("medical_consultations").insert(data).execute()
		if hasattr(result, 'status_code') and result.status_code >= 400:
			raise HTTPException(status_code=result.status_code, detail="Error al insertar la consulta médica")
		if not result.data:
			raise HTTPException(status_code=400, detail="No se pudo crear la consulta médica")
		return {"message": "Consulta médica creada exitosamente", "consultation": result.data[0]}
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))
    
