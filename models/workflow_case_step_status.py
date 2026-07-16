from dataclasses import dataclass, asdict

@dataclass
class WorkflowCaseStepStatusModel:
    workflow_case_id: str
    step_id: str
    status: str
