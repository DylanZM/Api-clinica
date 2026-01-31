from routers.auth.POST import login, register
from core.supabase import supabase


all_routers = [
    login.router,
    register.router,
]
