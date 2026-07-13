from dataclasses import dataclass, asdict
from models.step import StepModel

@dataclass
class WorkflowCaseModel:
    id: str
    legacy_id: str
    name: str
    description: str
    workflow_id_list: list[str] | None = None
    step_list: list[StepModel] | None = None
