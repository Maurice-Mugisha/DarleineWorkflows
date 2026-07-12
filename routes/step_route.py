import os
from fastapi import APIRouter

from models.step import StepModel
from includes.utility_functions import *
from includes.idgenerator import IDGenerator
from includes.business_logic_functions import *


router = APIRouter(prefix="/step", tags=["step"])


@router.post("/register_a_step")
async def register_a_step(stepModel: StepModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    idgenerator_obj = IDGenerator("Africa", "Kigali")
    step_id = idgenerator_obj.generate_step_id()
    step_query = insertion_object.insert_step(step_id, stepModel.name, stepModel.description, stepModel.code, stepModel.step_number, stepModel.percentage, stepModel.status, stepModel.warning_threshold, stepModel.workflow_id)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(step_query)
    query_executor.commit()
    query_executor.close()

    return "Successuflly registered a step"


@router.get("/retrieve_all_steps", response_model = list[StepModel])
async def retrieve_all_steps():
    query_executor, insertion_object, selection_object, _, _ = get_database_utility_tuple()
    step_list = get_steps(selection_object, query_executor)
    return step_list

@router.get("/retrieve_a_step/{step_id}", response_model = StepModel)
async def retrieve_a_step(step_id):
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    step_dictionary = get_specific_step(selection_object, query_executor, step_id)
    return step_dictionary

@router.get("/retrieve_workflow_steps/{workflow_id}", response_model = list[StepModel])
async def retrieve_workflow_steps(workflow_id):
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    step_list = get_workflow_steps(selection_object, query_executor, workflow_id)
    return step_list

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
