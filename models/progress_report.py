from dataclasses import dataclass

@dataclass
class ProgressReportModel:
    step_id: str
    status: str
    delay_time: float
    
