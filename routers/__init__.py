from routers.auth.POST import login, register
from routers.users.POST import create_user

all_routers = [
    login.router,
    register.router,
    create_user.router
]
