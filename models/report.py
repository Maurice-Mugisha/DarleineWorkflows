from dataclasses import dataclass, asdict

@dataclass
class ReportModel:
    id: str
    step_id: str
    user_id: str
    workflow_case_id: str
    report_text: str
    submission_time_stamp: str | None = None
    optional_document_url: str | None = None
