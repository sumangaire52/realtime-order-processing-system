from pydantic import BaseModel

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    first_name: str
    last_name: str

class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    first_name: str
    last_name: str
    is_active: bool
    is_verified: bool
    created_at: datetime

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int

class RefreshTokenRequest(BaseModel):
    refresh_token: str

class PasswordChange(BaseModel):
    current_password: str
    new_password: str