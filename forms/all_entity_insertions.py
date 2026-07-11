
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



def insert_role(database_connection_object, query_executor, selection_object, insertion_object, role_id, name, description):

	query_executor.execute(selection_object.select_role(role_id))
	role_check_query_result = query_executor.fetchall()
	result_list_length = len(role_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_role(role_id))
		database_connection_object.commit()

	if len(str(name).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_role_name(role_id, name))
		database_connection_object.commit()


	if len(str(description).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_role_description(role_id, description))
		database_connection_object.commit()



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



def insert_time(database_connection_object, query_executor, selection_object, insertion_object, time_id, time_unit, time_unit_category, time_unit_value, step_id):

	query_executor.execute(selection_object.select_time(time_id))
	time_check_query_result = query_executor.fetchall()
	result_list_length = len(time_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_time(step_id, time_id))
		database_connection_object.commit()

	if len(str(time_unit).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_time_time_unit(step_id, time_id, time_unit))
		database_connection_object.commit()


	if len(str(time_unit_category).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_time_time_unit_category(step_id, time_id, time_unit_category))
		database_connection_object.commit()


	if len(str(time_unit_value).strip()) > 0 and result_list_length == 0:
		query_executor.execute(insertion_object.insert_time_time_unit_value(step_id, time_id, time_unit_value))
		database_connection_object.commit()



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



def insert_workspacerolemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, workspace_id, role_id):

	query_executor.execute(selection_object.select_workspacerolemap(key_column, workspace_id, role_id))
	workspacerolemap_check_query_result = query_executor.fetchall()
	result_list_length = len(workspacerolemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_workspacerolemap(key_column, workspace_id, role_id))
		database_connection_object.commit()


def insert_workflowworkflow_casemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, workflow_id, workflow_case_id):

	query_executor.execute(selection_object.select_workflowworkflow_casemap(key_column, workflow_id, workflow_case_id))
	workflowworkflow_casemap_check_query_result = query_executor.fetchall()
	result_list_length = len(workflowworkflow_casemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_workflowworkflow_casemap(key_column, workflow_id, workflow_case_id))
		database_connection_object.commit()


def insert_steprolemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, step_id, role_id):

	query_executor.execute(selection_object.select_steprolemap(key_column, step_id, role_id))
	steprolemap_check_query_result = query_executor.fetchall()
	result_list_length = len(steprolemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_steprolemap(key_column, step_id, role_id))
		database_connection_object.commit()


def insert_roleprivilegemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, role_id, privilege_id):

	query_executor.execute(selection_object.select_roleprivilegemap(key_column, role_id, privilege_id))
	roleprivilegemap_check_query_result = query_executor.fetchall()
	result_list_length = len(roleprivilegemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_roleprivilegemap(key_column, role_id, privilege_id))
		database_connection_object.commit()


def insert_userrolemap(database_connection_object, query_executor, selection_object, insertion_object, key_column, user_id, role_id):

	query_executor.execute(selection_object.select_userrolemap(key_column, user_id, role_id))
	userrolemap_check_query_result = query_executor.fetchall()
	result_list_length = len(userrolemap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_userrolemap(key_column, user_id, role_id))
		database_connection_object.commit()


def insert_userstepmap(database_connection_object, query_executor, selection_object, insertion_object, key_column, user_id, step_id):

	query_executor.execute(selection_object.select_userstepmap(key_column, user_id, step_id))
	userstepmap_check_query_result = query_executor.fetchall()
	result_list_length = len(userstepmap_check_query_result)

	if result_list_length == 0:
		query_executor.execute(insertion_object.insert_userstepmap(key_column, user_id, step_id))
		database_connection_object.commit()

