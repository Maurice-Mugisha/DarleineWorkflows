from dataclasses import dataclass, asdict

@dataclass
class UserModel:
    id: str
    workspace_id: str
    first_name: str
    last_name: str
    email: str
    password: str
    job_title: str
