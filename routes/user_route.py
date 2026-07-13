import os
from fastapi import APIRouter
from dataclasses import asdict

from models.user import UserModel
from includes.utility_functions import *
from includes.idgenerator import IDGenerator
from includes.business_logic_functions import *


router = APIRouter(prefix="/user", tags=["user"])


@router.post("/register_a_user")
async def register_a_user(userModel: UserModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    idgenerator_obj = IDGenerator("Africa", "Kigali")
    user_id = idgenerator_obj.generate_user_id()
    workspace_id = userModel.workspace_id

    select_all_users_query = selection_object.select_from_user()
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(select_all_users_query)
    user_list = connection_cursor.fetchall()

    user_role_map_query = ""
    role_id = userModel.role_id

    if (not user_list or len(user_list) == 0) and (not role_id or len(role_id) == 0):
        role_query = selection_object.select_role_by_name("Super admin")
        connection_cursor = query_executor.cursor()
        connection_cursor.execute(role_query)
        role_dictionary = connection_cursor.fetchone()
        role_model = RoleModel(**role_dictionary)
        role_id = role_model.id

    role_query = selection_object.select_role(role_id)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(role_query)
    role_dictionary = connection_cursor.fetchone()
    if not role_dictionary:
        return "No such role has been found"

    user_query = insertion_object.insert_user(user_id, userModel.first_name, userModel.last_name, userModel.job_title, userModel.email, userModel.password, workspace_id)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(user_query)
    connection_cursor.execute(user_role_map_query)
    query_executor.commit()
    query_executor.close()

    return "Successuflly registered a user"


@router.get("/retrieve_all_users", response_model = list[UserModel])
async def retrieve_all_users():
    query_executor, insertion_object, selection_object, _, _ = get_database_utility_tuple()
    user_list = get_users(selection_object, query_executor)
    return user_list

@router.get("/retrieve_a_user/{user_id}", response_model = UserModel)
async def retrieve_a_user(user_id):
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    user_dictionary = get_specific_user(selection_object, query_executor, user_id)
    if not user_dictionary:
        return {}
    userModel = UserModel(**user_dictionary)

    # connection already closed
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    role_list = get_specific_user_roles(selection_object, query_executor, user_id)
    if role_list or len(role_list) > 0:
        userModel.role_id = role_list[0]["id"]
    return asdict(userModel)

@router.get("/retrieve_workspace_users/{workspace_id}", response_model = list[UserModel])
async def retrieve_a_user(workspace_id):
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    user_list = get_specific_workspace_users(selection_object, query_executor, workspace_id)
    new_user_list = []

    for user_dictionary in user_list:
        userModel = UserModel(**user_dictionary)
        query_executor, _, selection_object, _, _ = get_database_utility_tuple()
        role_list = get_specific_user_roles(selection_object, query_executor, user_dictionary["id"])
        if role_list or len(role_list) > 0:
            userModel.role_id = role_list[0]["id"]
        new_user_list.append(asdict(userModel))

    return new_user_list

@router.post("/update_a_user", response_model = str)
async def update_a_user(userModel: UserModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    user_query = update_object.update_user(userModel.id, userModel.first_name, userModel.last_name, userModel.job_title, userModel.email, userModel.password)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(user_query)
    query_executor.commit()
    query_executor.close()

    return "successfully updated a user"

@router.delete("/delete_a_user", response_model = str)
async def delete_a_user(user_id: str):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    user_query = deletion_object.delete_user(user_id)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(user_query)
    query_executor.commit()
    query_executor.close()

    return "successfully deleted a user"
