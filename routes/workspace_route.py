import os
from fastapi import APIRouter

from models.workspace import WorkspaceModel
from includes.utility_functions import *
from includes.idgenerator import IDGenerator
from includes.business_logic_functions import *


router = APIRouter(prefix="/workspace", tags=["workspace"])


@router.post("/register_a_workspace")
async def register_a_workspace(workspaceModel: WorkspaceModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    idgenerator_obj = IDGenerator("Africa", "Kigali")
    workspace_id = idgenerator_obj.generate_workspace_id()
    workspace_query = insertion_object.insert_workspace(workspace_id, workspaceModel.name, workspaceModel.description, workspaceModel.language, workspaceModel.organization_type, workspaceModel.email, workspaceModel.country)
    admin = workspaceModel.admin
    user_id = idgenerator_obj.generate_user_id()
    user_query = insertion_object.insert_user(user_id, admin.first_name, admin.last_name, admin.job_title, admin.email, admin.password, workspace_id)

    connection_cursor = query_executor.cursor()
    connection_cursor.execute(workspace_query)
    connection_cursor.execute(user_query)
    query_executor.commit()
    query_executor.close()

    return "Successuflly registered a workspace"


@router.get("/retrieve_all_workspaces", response_model = list[WorkspaceModel])
async def retrieve_all_workspaces():
    query_executor, insertion_object, selection_object, _, _ = get_database_utility_tuple()
    workspace_list = get_workspaces(selection_object, query_executor)
    return workspace_list

@router.get("/retrieve_a_workspace/{workspace_id}", response_model = WorkspaceModel)
async def retrieve_a_workspace(workspace_id):
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    workspace_dictionary = get_specific_workspace(selection_object, query_executor, workspace_id)
    return workspace_dictionary

@router.post("/update_a_workspace", response_model = str)
async def update_a_workspace(workspaceModel: WorkspaceModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    workspace_query = update_object.update_workspace(workspace_id, workspaceModel.name, workspaceModel.description, workspaceModel.language, workspaceModel.organization_type, workspaceModel.email, workspaceModel.country)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(workspace_query)
    query_executor.commit()
    query_executor.close()

    return "successfully updated a workspace"

@router.delete("/delete_a_workspace", response_model = str)
async def delete_a_workspace(workspace_id: str):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    workspace_query = deletion_object.delete_workspace(workspace_id)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(workspace_query)
    query_executor.commit()
    query_executor.close()

    return "successfully deleted a workspace"
