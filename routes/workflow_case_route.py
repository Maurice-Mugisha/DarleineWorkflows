import os
from fastapi import APIRouter

from models.workflow_case import WorkflowCaseModel
from includes.utility_functions import *
from includes.idgenerator import IDGenerator
from includes.business_logic_functions import *


router = APIRouter(prefix="/workflow_case", tags=["workflow_case"])


@router.post("/register_a_workflow_case")
async def register_a_workflow_case(workflowCaseModel: WorkflowCaseModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    idgenerator_obj = IDGenerator("Africa", "Kigali")
    workflow_case_id = idgenerator_obj.generate_workflow_case_id()
    workflow_case_query = insertion_object.insert_workflow_case(workflow_case_id, workflowCaseModel.legacy_id, workflowCaseModel.name, workflowCaseModel.description)
    
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(workflow_case_query)
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

    return "successfully updated a workflow_case"

@router.delete("/delete_a_workflow_case", response_model = str)
async def delete_a_workflow_case(workflow_case_id: str):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    workflow_case_query = deletion_object.delete_workflow_case(workflow_case_id)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(workflow_case_query)
    query_executor.commit()
    query_executor.close()

    return "successfully deleted a workflow_case"
