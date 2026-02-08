from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    role: str

class LoginResponse(BaseModel):
    access_token: str
    user: UserResponse  