import os
from fastapi import APIRouter

from models.report import ReportModel
from includes.utility_functions import *
from includes.idgenerator import IDGenerator
from includes.business_logic_functions import *


router = APIRouter(prefix="/report", tags=["report"])


@router.post("/register_a_report")
async def register_a_report(reportModel: ReportModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    idgenerator_obj = IDGenerator("Africa", "Kigali")
    report_id = idgenerator_obj.generate_report_id()
    step_id = reportModel.step_id
    report_query = insertion_object.insert_report(report_id, reportModel.report_text, reportModel.optional_document_url, reportModel.workflow_case_id, reportModel.step_id, reportModel.user_id)

    connection_cursor = query_executor.cursor()
    connection_cursor.execute(report_query)
    query_executor.commit()
    query_executor.close()

    return "Successuflly registered a report"


@router.get("/retrieve_all_reports", response_model = list[ReportModel])
async def retrieve_all_reports():
    query_executor, insertion_object, selection_object, _, _ = get_database_utility_tuple()
    report_list = get_reports(selection_object, query_executor)
    return report_list

@router.get("/retrieve_a_report/{report_id}", response_model = ReportModel)
async def retrieve_a_report(report_id):
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    report_dictionary = get_specific_report(selection_object, query_executor, report_id)
    return report_dictionary

@router.get("/retrieve_workflow_case_reports/{workflow_case_id}", response_model = list[ReportModel])
async def retrieve_step_reports(workflow_case_id):
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    report_list = get_specific_workflow_case_reports(selection_obj, query_executor, workflow_case_id)
    report_model_list = []
    if report_list and len(report_list) > 0:
        report_model_list = [ReportModel(**report_dictionary) for report_dictionary in report_list]
    return report_model_list

@router.post("/update_a_report", response_model = str)
async def update_a_report(reportModel: ReportModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    report_query = update_object.update_report(reportModel.id, reportModel.report_text, reportModel.optional_document_url)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(report_query)
    query_executor.commit()
    query_executor.close()

    return "successfully updated a report"

@router.delete("/delete_a_report", response_model = str)
async def delete_a_report(report_id: str):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    report_query = deletion_object.delete_report(report_id)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(report_query)
    query_executor.commit()
    query_executor.close()

    return "successfully deleted a report"
