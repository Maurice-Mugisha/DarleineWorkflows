
def insert_role(database_connection_object, query_executor, selection_object, insertion_object, role_id, name, description):

	query_executor.execute(selection_object.select_role(role_id))
	role_check_query_result = query_executor.fetchall()
	result_list_length = len(role_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_role(role_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_role_name(role_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_role_description(role_id, description))
		database_connection_object.commit()
