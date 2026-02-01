from fastapi import APIRouter, HTTPException, Depends
from core.supabase import supabase
from datetime import datetime

router = APIRouter(prefix="/stats", tags=["Stats"])

@router.get("/admin")
async def get_admin_stats():
	try:
		all_appointments = supabase.table("appointments").select("id").execute().data
		total_appointments = len(all_appointments) if all_appointments else 0

		patients = supabase.table("patients").select("id").execute().data
		total_patients = len(patients) if patients else 0

		now = datetime.utcnow()
		first_day_month = now.replace(day=1).date().isoformat()
		consultations_month = supabase.table("medical_consultations").select("*").gte("consultation_date", first_day_month).execute().data
		total_consultations_month = len(consultations_month) if consultations_month else 0

		users = supabase.table("users").select("id").execute().data
		total_users = len(users) if users else 0

		return {
			"total_appointments": total_appointments,
			"total_patients": total_patients,
			"consultations_month": total_consultations_month,
			"total_users": total_users
		}
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))
