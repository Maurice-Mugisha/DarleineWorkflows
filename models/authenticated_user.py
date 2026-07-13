from dataclasses import dataclass, asdict
from models.role import RoleModel

@dataclass
class AuthenticatedUserModel:
    id: str
    workspace_id: str
    first_name: str
    last_name: str
    email: str
    password: str
    job_title: str
    roles: list[RoleModel] | None = None
