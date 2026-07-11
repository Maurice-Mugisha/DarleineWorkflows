
def insert_report(database_connection_object, query_executor, selection_object, insertion_object, report_id, report_text, optional_document_url, step_id, user_id, workflow_case_id):

	query_executor.execute(selection_object.select_report(report_id))
	report_check_query_result = query_executor.fetchall()
	result_list_length = len(report_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_report(step_id, user_id, workflow_case_id, report_id))
		database_connection_object.commit()

	if len(str(report_text).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_report_report_text(step_id, user_id, workflow_case_id, report_id, report_text))
		database_connection_object.commit()


	if len(str(optional_document_url).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_report_optional_document_url(step_id, user_id, workflow_case_id, report_id, optional_document_url))
		database_connection_object.commit()
