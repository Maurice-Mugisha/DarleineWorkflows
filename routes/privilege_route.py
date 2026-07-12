import os
from fastapi import APIRouter

from models.privilege import PrivilegeModel
from includes.utility_functions import *
from includes.idgenerator import IDGenerator
from includes.business_logic_functions import *


router = APIRouter(prefix="/privilege", tags=["privilege"])


@router.post("/register_a_privilege")
async def register_a_privilege(privilegeModel: PrivilegeModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    idgenerator_obj = IDGenerator("Africa", "Kigali")
    privilege_id = idgenerator_obj.generate_privilege_id()
    privilege_query = insertion_object.insert_privilege(privilege_id, privilegeModel.name, privilegeModel.description)

    connection_cursor = query_executor.cursor()
    connection_cursor.execute(privilege_query)
    query_executor.commit()
    query_executor.close()

    return "Successuflly registered a privilege"


@router.get("/retrieve_all_privileges", response_model = list[PrivilegeModel])
async def retrieve_all_privileges():
    query_executor, insertion_object, selection_object, _, _ = get_database_utility_tuple()
    privilege_list = get_privileges(selection_object, query_executor)
    return privilege_list

@router.get("/retrieve_a_privilege/{privilege_id}", response_model = PrivilegeModel)
async def retrieve_a_privilege(privilege_id):
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    privilege_dictionary = get_specific_privilege(selection_object, query_executor, privilege_id)
    return privilege_dictionary

@router.post("/update_a_privilege", response_model = str)
async def update_a_privilege(privilegeModel: PrivilegeModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    privilege_query = update_object.update_privilege(privilege_id, privilegeModel.name, privilegeModel.description)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(privilege_query)
    query_executor.commit()
    query_executor.close()

    return "successfully updated a privilege"

@router.delete("/delete_a_privilege", response_model = str)
async def delete_a_privilege(privilege_id: str):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    privilege_query = deletion_object.delete_privilege(privilege_id)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(privilege_query)
    query_executor.commit()
    query_executor.close()

    return "successfully deleted a privilege"
