from dataclasses import dataclass, asdict
from models.user import UserModel

@dataclass
class WorkspaceModel:
    id: str
    name: str
    description: str
    language: str | None = None
    organization_type: str | None = None
    email: str | None = None
    country: str | None = None
    admin: UserModel | None = None
