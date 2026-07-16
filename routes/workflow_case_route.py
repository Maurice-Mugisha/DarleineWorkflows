import os
from fastapi import APIRouter
from operator import attrgetter

from models.workflow_case import WorkflowCaseModel
from includes.utility_functions import *
from includes.idgenerator import IDGenerator
from includes.business_logic_functions import *
from models.step import StepModel
from models.time import TimeModel
from models.report import ReportModel
from models.progress_report import ProgressReportModel
from models.workflow_case_step_status import WorkflowCaseStepStatusModel


router = APIRouter(prefix="/workflow_case", tags=["workflow case"])


@router.post("/register_a_workflow_case")
async def register_a_workflow_case(workflowCaseModel: WorkflowCaseModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    idgenerator_obj = IDGenerator("Africa", "Kigali")
    workflow_case_id = idgenerator_obj.generate_workflow_case_id()
    workflow_case_query = insertion_object.insert_workflow_case(
        workflow_case_id,
        escape_postgres_string(workflowCaseModel.legacy_id),
        escape_postgres_string(workflowCaseModel.name),
        escape_postgres_string(workflowCaseModel.description)
    )
    workflow_id_list = workflowCaseModel.workflow_id_list

    step_id_list = []
    if workflow_id_list and len(workflow_id_list) > 0:
        for workflow_id in workflow_id_list:
            step_list = get_workflow_steps(selection_object, query_executor, workflow_id)
            if step_list and len(step_list) > 0:
                for step in step_list:
                    step_id_list.append(step["id"])

    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(workflow_case_query)

    if workflow_id_list and len(workflow_id_list) > 0:
        for workflow_id in workflow_id_list:
            worflow_workflow_case_map_query = insertion_object.insert_workflowworkflow_casemap(workflow_id, workflow_case_id)
            connection_cursor.execute(worflow_workflow_case_map_query)

    if step_id_list and len(step_id_list) > 0:
        for step_id in step_id_list:
            step_workflow_case_map_query = insertion_object.insert_stepworkflow_casemap(step_id, workflow_case_id, "Pending")
            connection_cursor.execute(step_workflow_case_map_query)

    query_executor.commit()
    query_executor.close()

    return "Successuflly registered a workflow case"


@router.get("/retrieve_all_workflow_cases", response_model = list[WorkflowCaseModel])
async def retrieve_all_workflow_cases():
    query_executor, insertion_object, selection_object, _, _ = get_database_utility_tuple()
    workflow_case_list = get_workflow_cases(selection_object, query_executor)
    workflow_case_model_list = []
    if workflow_case_list and len(workflow_case_list) > 0:
        for workflow_case_dictionary in workflow_case_list:
            if not workflow_case_dictionary:
                continue
            workflow_case_model = get_workflow_case_information(workflow_case_dictionary)
            workflow_case_model_list.append(workflow_case_model)
    return workflow_case_model_list


@router.get("/retrieve_a_workflow_case/{workflow_case_id}", response_model = WorkflowCaseModel)
async def retrieve_a_workflow_case(workflow_case_id):
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    workflow_case_dictionary = get_specific_workflow_case(selection_object, query_executor, workflow_case_id)
    if workflow_case_dictionary:
        workflow_case_model = get_workflow_case_information(workflow_case_dictionary)
        return workflow_case_model
    return {}


@router.get("/retrieve_workflow_cases_by_workflow/{workflow_id}", response_model = list[WorkflowCaseModel])
async def retrieve_workflow_cases_by_workflow_id(workflow_id):
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    workflow_case_list = get_specific_workflow_workflow_cases(query_executor, selection_object, workflow_id)
    workflow_case_model_list = []
    if workflow_case_list and len(workflow_case_list) > 0:
        for workflow_case_dictionary in workflow_case_list:
            if not workflow_case_dictionary:
                continue
            workflow_case_model = get_workflow_case_information(workflow_case_dictionary)
            workflow_case_model_list.append(workflow_case_model)
    return workflow_case_model_list


@router.post("/update_a_workflow_case", response_model = str)
async def update_a_workflow_case(workflowCaseModel: WorkflowCaseModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    workflow_case_query = update_object.update_workflow_case(
        workflowCaseModel.id,
        escape_postgres_string(workflowCaseModel.legacy_id),
        escape_postgres_string(workflowCaseModel.name),
        escape_postgres_string(workflowCaseModel.description)
    )
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(workflow_case_query)
    query_executor.commit()
    query_executor.close()

    return "successfully updated a workflow case"


@router.post("/update_a_workflow_case_step_status", response_model = str)
async def update_a_workflow_case_step_status(workflowCaseStepStatusModel: WorkflowCaseStepStatusModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    stepworkflow_casemap_query = update_object.update_stepworkflow_casemap(workflowCaseStepStatusModel.workflow_case_id, workflowCaseStepStatusModel.step_id, workflowCaseStepStatusModel.status)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(stepworkflow_casemap_query)
    query_executor.commit()
    query_executor.close()

    return "successfully updated a workflow case"


@router.delete("/delete_a_workflow_case", response_model = str)
async def delete_a_workflow_case(workflow_case_id: str):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    workflow_case_query = deletion_object.delete_workflow_case(workflow_case_id)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(workflow_case_query)
    query_executor.commit()
    query_executor.close()

    return "successfully deleted a workflow case"


def get_workflow_case_information(workflow_case_dictionary):
    workflow_case_id = workflow_case_dictionary["id"]
    if workflow_case_dictionary:

        workflow_case_model = WorkflowCaseModel(**workflow_case_dictionary)

        query_executor, _, selection_object, _, _ = get_database_utility_tuple()
        step_list = get_specific_workflow_case_steps(query_executor, selection_object, workflow_case_id)
        step_model_list = []
        if step_list and len(step_list) > 0:
            step_model_list = [StepModel(**step_dictionary) for step_dictionary in step_list if step_dictionary is not None]
            new_step_model_list = []
            for step_model in step_model_list:
                query_executor, _, selection_object, _, _ = get_database_utility_tuple()
                time_list = get_step_times(query_executor, selection_object, step_model.id)
                time_model_list = [TimeModel(**time_dictionary) for time_dictionary in time_list if time_list and len(time_list) > 0]
                step_model.time_list = time_model_list
                status = retrieve_workflow_case_status(workflow_case_id, step_model.id)
                step_model.workflow_case_step_status = status
                new_step_model_list.append(step_model)
            step_model_list = new_step_model_list
        workflow_case_model.step_list = step_model_list

        query_executor, _, selection_object, _, _ = get_database_utility_tuple()
        workflow_id_list = get_workflow_case_workflow_id_list(query_executor, selection_object, workflow_case_id)
        workflow_case_model.workflow_id_list = workflow_id_list

        query_executor, _, selection_object, _, _ = get_database_utility_tuple()
        report_list = get_specific_workflow_case_reports(query_executor, selection_object, workflow_case_id)
        report_model_list = []
        if report_list and len(report_list) > 0:
            report_model_list = [ReportModel(**report_dictionary) for report_dictionary in report_list]
        workflow_case_model.report_list = report_model_list

        progress_report_model_list = get_progress_reports(report_model_list, step_model_list)
        workflow_case_model.progress_report_list = progress_report_model_list

        return workflow_case_model

    return None


def get_progress_reports(report_model_list, step_model_list):
    progress_report_model_list = []
    if not step_model_list or len(step_model_list) == 0:
        return progress_report_model_list
    step_model_list = sorted(step_model_list, key=attrgetter("step_number"))
    i = 1
    for step_model in step_model_list:
        step_id = step_model.id
        step_number = step_model.step_number
        report_model = get_execution_report(step_id, report_model_list)
        if report_model is not None:
            delay_time = get_step_delay_time(report_model_list, step_number)
            progress_report = ProgressReportModel(step_id=report_model.step_id, status="Complete", delay_time=delay_time)
            progress_report_model_list.append(progress_report)
        else:
            progress_report = ProgressReportModel(step_id=step_id, status="Pending", delay_time=0.00)
            progress_report_model_list.append(progress_report)
    return progress_report_model_list


def get_execution_report(step_id, report_model_list):
    for report_model in report_model_list:
        if report_model.step_id == step_id:
            return report_model
    # Return a pending report to the user
    return None


def get_step_delay_time(report_model_list, step_number):
    # write the logic here
    if step_number == 1:
        return 0.00
    else:
        if step_number <= len(report_model_list):
            report_model = report_model_list[step_number]
            previous_report_model = report_model_list[step_number-1]
            query_executor, _, selection_object, _, _ = get_database_utility_tuple()
            step_id = report_model.step_id
            time_list = get_step_times(query_executor, selection_object, step_id)
            previous_step_id = previous_report_model.step_id
            query_executor, _, selection_object, _, _ = get_database_utility_tuple()
            previous_time_list = get_step_times(query_executor, selection_object, previous_step_id)
            # submission_timestamp1 - submission_timestamp2 in seconds
            submission_time_stamp = report_model.submission_time_stamp
            previous_submission_time_stamp = previous_report_model.submission_time_stamp
            return 0;
    return 0


def retrieve_workflow_case_status(workflow_case_id, step_id):
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    cursor = query_executor.cursor()
    cursor.execute(selection_object.select_stepworkflow_casemap(step_id, workflow_case_id))
    stepworkflow_casemap = cursor.fetchone()
    if stepworkflow_casemap and stepworkflow_casemap["status"] is not None and len(stepworkflow_casemap["status"]) > 0:
        return stepworkflow_casemap["status"]
    return "Pending"
