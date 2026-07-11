
def insert_workflow(database_connection_object, query_executor, selection_object, insertion_object, workflow_id, name, description, number_of_steps, status, is_mandatory, workspace_id):

	query_executor.execute(selection_object.select_workflow(workflow_id))
	workflow_check_query_result = query_executor.fetchall()
	result_list_length = len(workflow_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_workflow(workspace_id, workflow_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_workflow_name(workspace_id, workflow_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_workflow_description(workspace_id, workflow_id, description))
		database_connection_object.commit()


	if len(str(number_of_steps).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_workflow_number_of_steps(workspace_id, workflow_id, number_of_steps))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_workflow_status(workspace_id, workflow_id, status))
		database_connection_object.commit()


	if len(str(is_mandatory).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_workflow_is_mandatory(workspace_id, workflow_id, is_mandatory))
		database_connection_object.commit()
