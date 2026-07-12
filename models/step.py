from dataclasses import dataclass, asdict

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
