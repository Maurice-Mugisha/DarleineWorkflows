import os
from fastapi import APIRouter

import json

from models.time import TimeModel
from includes.utility_functions import *
from includes.idgenerator import IDGenerator
from includes.business_logic_functions import *
from models.time_unit import TimeUnitModel


router = APIRouter(prefix="/time", tags=["time"])


@router.post("/register_a_time")
async def register_a_time(timeModel: TimeModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    idgenerator_obj = IDGenerator("Africa", "Kigali")
    time_id = idgenerator_obj.generate_time_id()
    time_query = insertion_object.insert_time(time_id, timeModel.time_unit, timeModel.time_unit_category, timeModel.time_unit_value, timeModel.step_id)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(time_query)
    query_executor.commit()
    query_executor.close()

    return "Successuflly registered a time"

@router.get("/retrieve_all_time_units", response_model = list[str])
async def retrieve_all_time_units():
    time_unit_name_list = []
    with open("data/time_unit.json") as file:
        time_unit_list = json.load(file)
        for time_unit in time_unit_list:
            time_unit_name_list.append(time_unit["name"])

    return time_unit_name_list


@router.get("/retrieve_all_times", response_model = list[TimeModel])
async def retrieve_all_times():
    query_executor, insertion_object, selection_object, _, _ = get_database_utility_tuple()
    time_list = get_times(selection_object, query_executor)
    return time_list

@router.get("/retrieve_a_time/{time_id}", response_model = TimeModel)
async def retrieve_a_time(time_id):
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    time_dictionary = get_specific_time(selection_object, query_executor, time_id)
    return time_dictionary

@router.get("/retrieve_step_times/{step_id}", response_model = list[TimeModel])
async def retrieve_step_times(step_id):
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    time_list = get_step_times(selection_object, query_executor, step_id)
    return time_list

@router.post("/update_a_time", response_model = str)
async def update_a_time(timeModel: TimeModel):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    time_query = update_object.update_time(timeModel.id, timeModel.time_unit, timeModel.time_unit_category, timeModel.time_unit_value)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(time_query)
    query_executor.commit()
    query_executor.close()

    return "successfully updated a time"

@router.delete("/delete_a_time", response_model = str)
async def delete_a_time(time_id: str):
    query_executor, insertion_object, selection_object, update_object, deletion_object = get_database_utility_tuple()
    time_query = deletion_object.delete_time(time_id)
    connection_cursor = query_executor.cursor()
    connection_cursor.execute(time_query)
    query_executor.commit()
    query_executor.close()

    return "successfully deleted a time"
