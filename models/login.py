from dataclasses import dataclass, asdict

@dataclass
class LoginModel:
    email: str
    password: str
