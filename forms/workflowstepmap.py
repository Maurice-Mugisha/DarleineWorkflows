
def insert_workflowstepmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, workflow_id, step_id):

	query_executor.execute(selection_object.select_workflowstepmap(key_column, workflow_id, step_id))
	workflowstepmap_check_query_result = query_executor.fetchall()
	result_list_length = len(workflowstepmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_workflowstepmap(key_column, workflow_id, step_id))
		database_connection_object.commit()