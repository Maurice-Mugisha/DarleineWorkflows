
def insert_workflowworkflow_casemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, workflow_id, workflow_case_id):

	query_executor.execute(selection_object.select_workflowworkflow_casemap(key_column, workflow_id, workflow_case_id))
	workflowworkflow_casemap_check_query_result = query_executor.fetchall()
	result_list_length = len(workflowworkflow_casemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_workflowworkflow_casemap(key_column, workflow_id, workflow_case_id))
		database_connection_object.commit()