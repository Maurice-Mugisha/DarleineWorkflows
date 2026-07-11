
def insert_workflow_case(database_connection_object, query_executor, selection_object, insertion_object, workflow_case_id, legacy_id, name, description):

	query_executor.execute(selection_object.select_workflow_case(workflow_case_id))
	workflow_case_check_query_result = query_executor.fetchall()
	result_list_length = len(workflow_case_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_workflow_case(workflow_case_id))
		database_connection_object.commit()

	if len(str(legacy_id).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_workflow_case_legacy_id(workflow_case_id, legacy_id))
		database_connection_object.commit()


	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_workflow_case_name(workflow_case_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_workflow_case_description(workflow_case_id, description))
		database_connection_object.commit()
