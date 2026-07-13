from dataclasses import dataclass, asdict
from models.time import TimeModel

@dataclass
class StepModel:
    id: str
    workflow_id: str
    name: str
    description: str
    step_number: int
    status: str
    percentage: float
    warning_threshold: float
    code: str
    role_id_list: list[str] | None = None
    time_list: list[TimeModel] | None = None
