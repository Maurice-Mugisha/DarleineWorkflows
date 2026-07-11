
def insert_workspacerolemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, workspace_id, role_id):

	query_executor.execute(selection_object.select_workspacerolemap(key_column, workspace_id, role_id))
	workspacerolemap_check_query_result = query_executor.fetchall()
	result_list_length = len(workspacerolemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_workspacerolemap(key_column, workspace_id, role_id))
		database_connection_object.commit()