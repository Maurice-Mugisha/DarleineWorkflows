
def insert_steprolemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, step_id, role_id):

	query_executor.execute(selection_object.select_steprolemap(key_column, step_id, role_id))
	steprolemap_check_query_result = query_executor.fetchall()
	result_list_length = len(steprolemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_steprolemap(key_column, step_id, role_id))
		database_connection_object.commit()