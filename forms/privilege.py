
def insert_privilege(database_connection_object, query_executor, selection_object, insertion_object, privilege_id, name, description):

	query_executor.execute(selection_object.select_privilege(privilege_id))
	privilege_check_query_result = query_executor.fetchall()
	result_list_length = len(privilege_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_privilege(privilege_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_privilege_name(privilege_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_privilege_description(privilege_id, description))
		database_connection_object.commit()
