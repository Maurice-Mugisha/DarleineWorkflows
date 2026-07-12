from dataclasses import dataclass, asdict

@dataclass
class TimeModel:
    id: str
    step_id: str
    time_unit: str
    time_unit_category: str
    time_unit_value: float
