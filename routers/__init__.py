from routers.auth.POST import login, register
from routers.users.POST import create_user
from routers.users.PUT import update_user
from routers.users.DELETE import delete_user
from routers.users.GET import list_users,get_user
from routers.patients.GET import list_patients,get_patient
from routers.patients.POST import patients
from routers.patients.PUT import update_patient
from routers.medical_records.GET import record
from routers.consultations.GET import consultations as consultations_get
from routers.consultations.GET import get_consultation
from routers.consultations.POST import consultations as consultations_post
from routers.appointments.GET import appointment as appointment_get
from routers.appointments.GET import appointments as appointments_all
from routers.appointments.POST import appointments as appointments_create
from routers.appointments.PUT import update_appointment
from routers.appointments.DELETE import delete_appointment
from routers.stats.GET import stats

all_routers = [
    login.router,
    register.router,
    create_user.router,
    update_user.router,
    delete_user.router,
    list_users.router,
    get_user.router,
    list_patients.router,
    get_patient.router,
    patients.router,
    update_patient.router,
    record.router,
    consultations_get.router,
    consultations_post.router,
    get_consultation.router,
    appointment_get.router,
    appointments_all.router,
    appointments_create.router,
    update_appointment.router,
    delete_appointment.router,
    stats.router
]
