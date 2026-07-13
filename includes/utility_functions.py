import os

from fastapi import Request, HTTPException
import json

from crud.insert import Insert
from crud.selection import Select
from crud.update import Update
from crud.delete import Delete
from includes.database_connection import DatabaseConnection
from includes.idgenerator import IDGenerator
from includes.business_logic_functions import *
from models.authenticated_user import AuthenticatedUserModel
from models.role import RoleModel


def get_database_utility_tuple():
    query_executor = get_query_executor()
    selection_object = get_selection_object()
    insertion_object = get_insertion_object()
    update_object = get_update_object()
    deletion_object = get_deletion_object()
    database_utility_tuple = (query_executor, insertion_object, selection_object, update_object, deletion_object)
    return database_utility_tuple

def get_query_executor():
    auth_credentials_file_name = get_authentication_file_name()
    database_connection_facility = DatabaseConnection(auth_credentials_file_name)
    database_connection_object = database_connection_facility.get_database_connection_object()
    query_executor = database_connection_object
    return query_executor

def get_insertion_object():
    insertion_object = Insert("workflows system insertion object")
    return insertion_object

def get_selection_object():
    selection_object = Select("Workflows system selection object")
    return selection_object

def get_update_object():
    update_object = Update("Workflows system update object")
    return update_object

def get_deletion_object():
    deletion_object = Delete("Workflows system deletion object")
    return deletion_object

def get_authentication_file_name():
    authentication_directory = "auth"
    authentication_file = "auth.txt"
    auth_credentials_file_name = authentication_directory + os.sep + authentication_file
    return auth_credentials_file_name

def initialize_roles():
    user_dictionary = {}
    query_executor, insertion_object, selection_object, _, _ = get_database_utility_tuple()
    role_model_list = []
    with open("data/roles.json") as file:
        role_data = json.load(file)
        role_model_list = [RoleModel(**role_dictionary) for role_dictionary in role_data]
    saved_role_list = get_roles(selection_object, query_executor)

    if not saved_role_list or len(saved_role_list) == 0:
        idgenerator_obj = IDGenerator("Africa", "Kigali")
        query_executor, insertion_object, selection_object, _, _ = get_database_utility_tuple() # connection initially closed already, open it up again
        connection_cursor = query_executor.cursor()
        for roleModel in role_model_list:
            role_id = idgenerator_obj.generate_role_id()
            role_query = insertion_object.insert_role(role_id, roleModel.name, roleModel.description)
            connection_cursor.execute(role_query)
        query_executor.commit()
        query_executor.close()


def get_specific_authenticated_user_by_email(email):
    user_dictionary = {}
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    user_dictionary = get_specific_user_by_email(selection_object, query_executor, email)
    authenticated_user = AuthenticatedUserModel(**user_dictionary)
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    role_list = get_specific_user_roles(selection_object, query_executor, user_dictionary["id"])
    if len(role_list) > 0:
        authenticated_user.roles = role_list
    else:
        authenticated_user.roles = []

    return (authenticated_user, role_list)


# Helper function to enforce authentication across routes
def get_currently_logged_user_info(request: Request):
    user = request.session.get("user")
    if not user:
        raise HTTPException(status_code=401, detail="You must be authenticated to access this information")
    authenticatedUserModel = AuthenticatedUserModel(**user)
    return authenticatedUserModel
