from dataclasses import dataclass


@dataclass
class UserLoginCredentials:
    email: str
    password: str


@dataclass
class UserData:
    email: str
    usernameL: str
    bio: str
    image: str
    token: str


@dataclass
class LoginResponse:
    user: UserData
