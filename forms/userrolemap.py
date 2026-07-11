
def insert_userrolemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, user_id, role_id):

	query_executor.execute(selection_object.select_userrolemap(key_column, user_id, role_id))
	userrolemap_check_query_result = query_executor.fetchall()
	result_list_length = len(userrolemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_userrolemap(key_column, user_id, role_id))
		database_connection_object.commit()