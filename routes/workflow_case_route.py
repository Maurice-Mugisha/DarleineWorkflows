import os
from fastapi import APIRouter

from models.workflow_case import WorkflowCaseModel
from includes.utility_functions import *
from includes.idgenerator import IDGenerator
from includes.business_logic_functions import *


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
    return workflow_case_list

@router.get("/retrieve_a_workflow_case/{workflow_case_id}", response_model = WorkflowCaseModel)
async def retrieve_a_workflow_case(workflow_case_id):
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    workflow_case_dictionary = get_specific_workflow_case(selection_object, query_executor, workflow_case_id)
    return workflow_case_dictionary

@router.post("/update_a_workflow_case", response_model = str)
async def update_a_workflow_case(workflowCaseModel: WorkflowCaseModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    workflow_case_query = update_object.update_workflow_case(workflow_case_id, workflowCaseModel.legacy_id, workflowCaseModel.name, workflowCaseModel.description)
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
