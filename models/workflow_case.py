from dataclasses import dataclass, asdict

@dataclass 
class WorkflowCaseModel:
    id: str
    legacy_id: str
    name: str
    description: str
