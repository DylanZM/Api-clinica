from routers.auth.POST import login, register
from routers.users.POST import create_user
from routers.users.PUT import update_user
from routers.users.DELETE import delete_user
from routers.users.GET import list_users,get_user
from routers.patients.GET import list_patients,get_patient
from routers.patients.POST import patients
from routers.patients.PUT import update_patient

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
    update_patient.router
]
