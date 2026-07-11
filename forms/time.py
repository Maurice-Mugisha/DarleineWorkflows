
def insert_time(database_connection_object, query_executor, selection_object, insertion_object, time_id, time_unit, time_unit_category, time_unit_value, step_id):

	query_executor.execute(selection_object.select_time(time_id))
	time_check_query_result = query_executor.fetchall()
	result_list_length = len(time_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_time(step_id, time_id))
		database_connection_object.commit()

	if len(str(time_unit).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_time_time_unit(step_id, time_id, time_unit))
		database_connection_object.commit()


	if len(str(time_unit_category).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_time_time_unit_category(step_id, time_id, time_unit_category))
		database_connection_object.commit()


	if len(str(time_unit_value).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_time_time_unit_value(step_id, time_id, time_unit_value))
		database_connection_object.commit()
