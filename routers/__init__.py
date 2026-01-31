from routers.auth import login, register

all_routers = [
    login.router,
    register.router,
]
