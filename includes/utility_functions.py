import os
from crud.insert import Insert
from crud.selection import Select
from crud.update import Update
from crud.delete import Delete
from includes.database_connection import DatabaseConnection


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
