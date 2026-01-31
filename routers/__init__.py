from routers.auth.POST import login, register
from routers.users.POST import create_user
from routers.users.PUT import update_user
from routers.users.DELETE import delete_user
from routers.users.GET import list_users

all_routers = [
    login.router,
    register.router,
    create_user.router,
    update_user.router,
    delete_user.router,
    list_users.router,
]
