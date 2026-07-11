
def insert_workspace(database_connection_object, query_executor, selection_object, insertion_object, workspace_id, name, description, email, country, language, organization_type):

	query_executor.execute(selection_object.select_workspace(workspace_id))
	workspace_check_query_result = query_executor.fetchall()
	result_list_length = len(workspace_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_workspace(workspace_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_workspace_name(workspace_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_workspace_description(workspace_id, description))
		database_connection_object.commit()


	if len(str(email).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_workspace_email(workspace_id, email))
		database_connection_object.commit()


	if len(str(country).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_workspace_country(workspace_id, country))
		database_connection_object.commit()


	if len(str(language).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_workspace_language(workspace_id, language))
		database_connection_object.commit()


	if len(str(organization_type).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_workspace_organization_type(workspace_id, organization_type))
		database_connection_object.commit()
