from dataclasses import dataclass, asdict
from models.step import StepModel
from models.report import ReportModel
from models.progress_report import ProgressReportModel

@dataclass
class WorkflowCaseModel:
    id: str
    legacy_id: str
    name: str
    description: str
    workflow_id_list: list[str] | None = None
    step_list: list[StepModel] | None = None
    report_list: list[ReportModel] | None = None
    progress_report_list: list[ProgressReportModel] | None = None
