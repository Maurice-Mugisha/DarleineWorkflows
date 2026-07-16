from dataclasses import dataclass

@dataclass
class ProgressReportModel:
    step_id: str
    status: str # pending, on-time, overdue
    delay_time: float
