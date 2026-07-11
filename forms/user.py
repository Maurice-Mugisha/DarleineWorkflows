
def insert_user(database_connection_object, query_executor, selection_object, insertion_object, user_id, first_name, last_name, email, password, job_title, workspace_id):

	query_executor.execute(selection_object.select_user(user_id))
	user_check_query_result = query_executor.fetchall()
	result_list_length = len(user_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_user(workspace_id, user_id))
		database_connection_object.commit()

	if len(str(first_name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_first_name(workspace_id, user_id, first_name))
		database_connection_object.commit()


	if len(str(last_name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_last_name(workspace_id, user_id, last_name))
		database_connection_object.commit()


	if len(str(email).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_email(workspace_id, user_id, email))
		database_connection_object.commit()


	if len(str(password).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_password(workspace_id, user_id, password))
		database_connection_object.commit()


	if len(str(job_title).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_user_job_title(workspace_id, user_id, job_title))
		database_connection_object.commit()
