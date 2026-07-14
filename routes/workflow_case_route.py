import os
from fastapi import APIRouter

from models.workflow_case import WorkflowCaseModel
from includes.utility_functions import *
from includes.idgenerator import IDGenerator
from includes.business_logic_functions import *
from models.step import StepModel


router = APIRouter(prefix="/workflow_case", tags=["workflow case"])


@router.post("/register_a_workflow_case")
async def register_a_workflow_case(workflowCaseModel: WorkflowCaseModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    idgenerator_obj = IDGenerator("Africa", "Kigali")
    workflow_case_id = idgenerator_obj.generate_workflow_case_id()
    workflow_case_query = insertion_object.insert_workflow_case(workflow_case_id, workflowCaseModel.legacy_id, workflowCaseModel.name, workflowCaseModel.description)
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
            step_workflow_case_map_query = insertion_object.insert_stepworkflow_casemap(step_id, workflow_case_id)
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
    workflow_case_query = update_object.update_workflow_case(workflowCaseModel.id, workflowCaseModel.legacy_id, workflowCaseModel.name, workflowCaseModel.description)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(workflow_case_query)
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
        workflow_case_model.step_list = step_model_list

        query_executor, _, selection_object, _, _ = get_database_utility_tuple()
        workflow_id_list = get_workflow_case_workflow_id_list(query_executor, selection_object, workflow_case_id)
        workflow_case_model.workflow_id_list = workflow_id_list

        query_executor, _, selection_object, _, _ = get_database_utility_tuple()
        report_list = get_specific_workflow_case_reports(query_executor, selection_object, workflow_case_id)
        report_model_list = []
        if report_list and len(report_list) > 0:
            report_model_list = [StepModel(**report_dictionary) for report_dictionary in report_list]
        workflow_case_model.report_list = report_model_list

        return workflow_case_model

    return None
