
def insert_step(database_connection_object, query_executor, selection_object, insertion_object, step_id, name, description, step_number, percentage, status, warning_threshold, workflow_id):

	query_executor.execute(selection_object.select_step(step_id))
	step_check_query_result = query_executor.fetchall()
	result_list_length = len(step_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_step(workflow_id, step_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_step_name(workflow_id, step_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_step_description(workflow_id, step_id, description))
		database_connection_object.commit()


	if len(str(step_number).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_step_step_number(workflow_id, step_id, step_number))
		database_connection_object.commit()


	if len(str(percentage).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_step_percentage(workflow_id, step_id, percentage))
		database_connection_object.commit()


	if len(str(status).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_step_status(workflow_id, step_id, status))
		database_connection_object.commit()


	if len(str(warning_threshold).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_step_warning_threshold(workflow_id, step_id, warning_threshold))
		database_connection_object.commit()
