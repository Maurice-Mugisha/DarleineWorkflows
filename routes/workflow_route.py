import os
from fastapi import APIRouter, Depends

from models.workflow import WorkflowModel
from models.login import LoginModel
from includes.utility_functions import *
from includes.idgenerator import IDGenerator
from includes.business_logic_functions import *
from includes.utility_functions import *



router = APIRouter(prefix="/workflow", tags=["workflow"])


@router.post("/register_a_workflow")
async def register_a_workflow(workflowModel: WorkflowModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    idgenerator_obj = IDGenerator("Africa", "Kigali")
    workflow_id = idgenerator_obj.generate_workflow_id()
    workspace_id = workflowModel.workspace_id
    workflow_data_tuple = (
        workflow_id,
        workflowModel.name,
        workflowModel.description,
        workflowModel.is_mandatory,
        workflowModel.number_of_steps,
        workflowModel.status,
        workspace_id,
    )
    workflow_query = insertion_object.insert_workflow()

    connection_cursor = query_executor.cursor()
    connection_cursor.execute(workflow_query, workflow_data_tuple)
    query_executor.commit()
    query_executor.close()

    return "Successuflly registered a workflow"


@router.get("/retrieve_all_workflows/{workspace_id}", response_model = list[WorkflowModel])
async def retrieve_all_workflows(workspace_id):
    query_executor, insertion_object, selection_object, _, _ = get_database_utility_tuple()
    workflow_list = get_specific_workspace_workflows(query_executor, selection_object, workspace_id)
    workflow_model_list = []
    if workflow_list and len(workflow_list) > 0:
        workflow_model_list = [WorkflowModel(**workflow_dictionary) for workflow_dictionary in workflow_list if workflow_list and len(workflow_list) > 0]
    return workflow_model_list

@router.get("/retrieve_a_workflow/{workflow_id}", response_model = WorkflowModel)
async def retrieve_a_workflow(workflow_id):
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    workflow_dictionary = get_specific_workflow(selection_object, query_executor, workflow_id)
    if workflow_dictionary is not None:
        workflow_model = WorkflowModel(**workflow_dictionary)
        return workflow_model
    return {}

@router.get("/retrieve_workspace_workflows/{workspace_id}", response_model = list[WorkflowModel])
async def retrieve_a_workflow(workspace_id):
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    workflow_list = get_specific_workspace_workflows(query_executor, selection_object, workspace_id)
    return workflow_list

@router.post("/update_a_workflow", response_model = str)
async def update_a_workflow(workflowModel: WorkflowModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    workflow_data_tuple = (
        workflowModel.name,
        workflowModel.description,
        workflowModel.is_mandatory,
        workflowModel.number_of_steps,
        workflowModel.status,
        workflowModel.id,
    )
    workflow_query = update_object.update_workflow()
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(workflow_query, workflow_data_tuple)
    query_executor.commit()
    query_executor.close()

    return "successfully updated a workflow"

@router.delete("/delete_a_workflow", response_model = str)
async def delete_a_workflow(workflow_id: str):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    workflow_query = deletion_object.delete_workflow(workflow_id)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(workflow_query)
    query_executor.commit()
    query_executor.close()

    return "successfully deleted a workflow"
