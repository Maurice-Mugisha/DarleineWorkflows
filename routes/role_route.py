import os
from fastapi import APIRouter, Depends

from models.role import RoleModel
from models.login import LoginModel
from includes.utility_functions import *
from includes.idgenerator import IDGenerator
from includes.business_logic_functions import *


router = APIRouter(prefix="/role", tags=["role"])


@router.post("/register_a_role")
async def register_a_role(roleModel: RoleModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    idgenerator_obj = IDGenerator("Africa", "Kigali")
    role_id = idgenerator_obj.generate_role_id()
    role_query = insertion_object.insert_role(
        role_id,
        escape_postgres_string(roleModel.name),
        escape_postgres_string(roleModel.description)
    )

    connection_cursor = query_executor.cursor()
    connection_cursor.execute(role_query)
    query_executor.commit()
    query_executor.close()

    return "Successuflly registered a role"


@router.get("/retrieve_all_roles/{workspace_id}", response_model = list[RoleModel])
async def retrieve_all_roles(workspace_id):
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    role_list = get_specific_workspace_roles(query_executor, selection_object, workspace_id)
    role_model_list = []

    if role_list and len(role_list) > 0:
        for role_dictionary in role_list:
            roleModel = UserModel(**role_dictionary)
            role_model_list.append(roleModel)

    return role_model_list


@router.get("/retrieve_a_role/{role_id}", response_model = RoleModel)
async def retrieve_a_role(role_id):
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    role_dictionary = get_specific_role(selection_object, query_executor, role_id)
    return role_dictionary


@router.post("/update_a_role", response_model = str)
async def update_a_role(roleModel: RoleModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    role_query = update_object.update_role(
        role_id,
        escape_postgres_string(roleModel.name),
        escape_postgres_string(roleModel.description)
    )
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(role_query)
    query_executor.commit()
    query_executor.close()

    return "successfully updated a role"

@router.delete("/delete_a_role", response_model = str)
async def delete_a_role(role_id: str):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    role_query = deletion_object.delete_role(role_id)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(role_query)
    query_executor.commit()
    query_executor.close()

    return "successfully deleted a role"
