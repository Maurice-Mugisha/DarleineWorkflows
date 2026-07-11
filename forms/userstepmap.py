
def insert_userstepmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, user_id, step_id):

	query_executor.execute(selection_object.select_userstepmap(key_column, user_id, step_id))
	userstepmap_check_query_result = query_executor.fetchall()
	result_list_length = len(userstepmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_userstepmap(key_column, user_id, step_id))
		database_connection_object.commit()