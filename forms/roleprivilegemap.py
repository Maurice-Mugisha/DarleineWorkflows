
def insert_roleprivilegemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, role_id, privilege_id):

	query_executor.execute(selection_object.select_roleprivilegemap(key_column, role_id, privilege_id))
	roleprivilegemap_check_query_result = query_executor.fetchall()
	result_list_length = len(roleprivilegemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_roleprivilegemap(key_column, role_id, privilege_id))
		database_connection_object.commit()