import os
from fastapi import APIRouter, HTTPException

from dataclasses import asdict

from models.step import StepModel
from models.time import TimeModel
from includes.utility_functions import *
from includes.idgenerator import IDGenerator
from includes.business_logic_functions import *


router = APIRouter(prefix="/step", tags=["step"])


@router.post("/register_a_step")
async def register_a_step(stepModel: StepModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    idgenerator_obj = IDGenerator("Africa", "Kigali")
    step_id = idgenerator_obj.generate_step_id()
    role_id_list = stepModel.role_id_list
    time_list = stepModel.time_list

    step_query = insertion_object.insert_step(step_id, stepModel.name, stepModel.description, stepModel.code, stepModel.step_number, stepModel.percentage, stepModel.status, stepModel.warning_threshold, stepModel.workflow_id)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(step_query)

    if time_list and len(time_list) > 0:
        for timeModel in time_list:
            time_id = idgenerator_obj.generate_time_id()
            time_query = insertion_object.insert_time(time_id, timeModel.time_unit, timeModel.time_unit_category, timeModel.time_unit_value, step_id)
            connection_cursor.execute(time_query)

    if role_id_list and len(role_id_list) > 0:
        for role_id in role_id_list:
            step_role_map_query = insertion_object.insert_steprolemap(step_id, role_id)
            connection_cursor.execute(step_role_map_query)
    else:
        raise HTTPException(status_code=401, detail="You must provide the roles associated with executing this step.")

    query_executor.commit()
    connection_cursor.close()
    query_executor.close()

    return "Successuflly registered a step"


@router.get("/retrieve_all_steps", response_model = list[StepModel])
async def retrieve_all_steps():
    query_executor, insertion_object, selection_object, _, _ = get_database_utility_tuple()
    step_list = get_steps(selection_object, query_executor)
    step_model_list = []

    if step_list and len(step_list) > 0:
        for step_dictionary in step_list:
            stepModel = get_step_information(step_dictionary)
            step_model_list.append(stepModel)

    return step_model_list


@router.get("/retrieve_a_step/{step_id}", response_model = StepModel)
async def retrieve_a_step(step_id):
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    step_dictionary = get_specific_step(query_executor, selection_object, step_id)
    if step_dictionary:
        stepModel = get_step_information(step_dictionary)
        return stepModel

    return {}


@router.get("/retrieve_workflow_steps/{workflow_id}", response_model = list[StepModel])
async def retrieve_workflow_steps(workflow_id):
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    step_list = get_workflow_steps(selection_object, query_executor, workflow_id)
    step_model_list = []

    if step_list and len(step_list) > 0:
        for step_dictionary in step_list:
            stepModel = get_step_information(step_dictionary)
            step_model_list.append(stepModel)

    return step_model_list


@router.post("/update_a_step", response_model = str)
async def update_a_step(stepModel: StepModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    step_query = update_object.update_step(stepModel.id, stepModel.name, stepModel.description, stepModel.code, stepModel.step_number, stepModel.percentage, stepModel.status, stepModel.warning_threshold)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(step_query)
    query_executor.commit()
    query_executor.close()

    return "successfully updated a step"

@router.delete("/delete_a_step", response_model = str)
async def delete_a_step(step_id: str):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    step_query = deletion_object.delete_step(step_id)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(step_query)
    query_executor.commit()
    query_executor.close()

    return "successfully deleted a step"

def get_step_information(step_dictionary):

    step_id = step_dictionary["id"]
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    step_dictionary = get_specific_step(query_executor, selection_object, step_id)

    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    time_list = get_step_times(query_executor, selection_object, step_id)
    time_model_list = []
    if time_list and len(time_list) > 0:
        time_model_list = [TimeModel(**time_dictionary) for time_dictionary in time_list]
    stepModel = StepModel(**step_dictionary)
    stepModel.time_list = time_model_list

    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    role_list = get_step_roles(query_executor, selection_object, step_id)
    role_id_list = []
    if role_list and len(role_list):
        role_id_list = [role_dictionary["id"] for role_dictionary in role_list]
    stepModel.role_id_list = role_id_list
    return stepModel
