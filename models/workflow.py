from dataclasses import dataclass, asdict

@dataclass
class WorkflowModel:
    id: str
    workspace_id: str 
    name: str
    description: str
    is_mandatory: str
    number_of_steps: int
    status: str
