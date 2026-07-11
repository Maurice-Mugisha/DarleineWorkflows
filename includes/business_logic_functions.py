


def get_workspaces(selection_obj, query_executor):

	workspace_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_from_workspace())
	for row in cursor:
		workspace_id = row['id']
		workspace_dictionary[workspace_id] = get_specific_workspace(selection_obj, query_executor, workspace_id)
	return workspace_dictionary


def get_roles(selection_obj, query_executor):

	role_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_from_role())
	for row in cursor:
		role_id = row['id']
		role_dictionary[role_id] = get_specific_role(selection_obj, query_executor, role_id)
	return role_dictionary


def get_privileges(selection_obj, query_executor):

	privilege_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_from_privilege())
	for row in cursor:
		privilege_id = row['id']
		privilege_dictionary[privilege_id] = get_specific_privilege(selection_obj, query_executor, privilege_id)
	return privilege_dictionary


def get_users(selection_obj, query_executor):

	user_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_from_user())
	for row in cursor:
		user_id = row['id']
		workspace_id = row['workspace_id']
		key = user_id + "__" + workspace_id
		user_dictionary[key] = get_specific_user(selection_obj, query_executor, user_id, workspace_id)
	return user_dictionary


def get_workflows(selection_obj, query_executor):

	workflow_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_from_workflow())
	for row in cursor:
		workflow_id = row['id']
		workspace_id = row['workspace_id']
		key = workflow_id + "__" + workspace_id
		workflow_dictionary[key] = get_specific_workflow(selection_obj, query_executor, workflow_id, workspace_id)
	return workflow_dictionary


def get_steps(selection_obj, query_executor):

	step_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_from_step())
	for row in cursor:
		step_id = row['id']
		workflow_id = row['workflow_id']
		key = step_id + "__" + workflow_id
		step_dictionary[key] = get_specific_step(selection_obj, query_executor, step_id, workflow_id)
	return step_dictionary


def get_times(selection_obj, query_executor):

	time_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_from_time())
	for row in cursor:
		time_id = row['id']
		step_id = row['step_id']
		key = time_id + "__" + step_id
		time_dictionary[key] = get_specific_time(selection_obj, query_executor, time_id, step_id)
	return time_dictionary


def get_workflow_cases(selection_obj, query_executor):

	workflow_case_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_from_workflow_case())
	for row in cursor:
		workflow_case_id = row['id']
		workflow_case_dictionary[workflow_case_id] = get_specific_workflow_case(selection_obj, query_executor, workflow_case_id)
	return workflow_case_dictionary


def get_reports(selection_obj, query_executor):

	report_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_from_report())
	for row in cursor:
		report_id = row['id']
		step_id = row['step_id']
		user_id = row['user_id']
		workflow_case_id = row['workflow_case_id']
		key = report_id + "__" + step_id + "__" + user_id + "__" + workflow_case_id
		report_dictionary[key] = get_specific_report(selection_obj, query_executor, report_id, step_id, user_id, workflow_case_id)
	return report_dictionary


def get_workspacerolemaps(selection_obj, query_executor):

	workspacerolemap_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_from_workspacerolemap())
	for row in cursor:
		workspace_id = row['workspace_id']
		role_id = row['role_id']
		key = workspace_id + "__" + role_id
		workspacerolemap_dictionary[key] = get_specific_workspacerolemap(selection_obj, query_executor, key_column, workspace_id, role_id)
	return workspacerolemap_dictionary


def get_workflowworkflow_casemaps(selection_obj, query_executor):

	workflowworkflow_casemap_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_from_workflowworkflow_casemap())
	for row in cursor:
		workflow_id = row['workflow_id']
		workflow_case_id = row['workflow_case_id']
		key = workflow_id + "__" + workflow_case_id
		workflowworkflow_casemap_dictionary[key] = get_specific_workflowworkflow_casemap(selection_obj, query_executor, key_column, workflow_id, workflow_case_id)
	return workflowworkflow_casemap_dictionary


def get_steprolemaps(selection_obj, query_executor):

	steprolemap_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_from_steprolemap())
	for row in cursor:
		step_id = row['step_id']
		role_id = row['role_id']
		key = step_id + "__" + role_id
		steprolemap_dictionary[key] = get_specific_steprolemap(selection_obj, query_executor, key_column, step_id, role_id)
	return steprolemap_dictionary


def get_stepworkflow_casemaps(selection_obj, query_executor):

	stepworkflow_casemap_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_from_stepworkflow_casemap())
	for row in cursor:
		step_id = row['step_id']
		workflow_case_id = row['workflow_case_id']
		key = step_id + "__" + workflow_case_id
		stepworkflow_casemap_dictionary[key] = get_specific_stepworkflow_casemap(selection_obj, query_executor, key_column, step_id, workflow_case_id)
	return stepworkflow_casemap_dictionary


def get_roleprivilegemaps(selection_obj, query_executor):

	roleprivilegemap_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_from_roleprivilegemap())
	for row in cursor:
		role_id = row['role_id']
		privilege_id = row['privilege_id']
		key = role_id + "__" + privilege_id
		roleprivilegemap_dictionary[key] = get_specific_roleprivilegemap(selection_obj, query_executor, key_column, role_id, privilege_id)
	return roleprivilegemap_dictionary


def get_userrolemaps(selection_obj, query_executor):

	userrolemap_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_from_userrolemap())
	for row in cursor:
		user_id = row['user_id']
		role_id = row['role_id']
		key = key_column + "__" + user_id + "__" + role_id
		userrolemap_dictionary[key] = get_specific_userrolemap(selection_obj, query_executor, key_column, user_id, role_id)
	return userrolemap_dictionary


def get_userstepmaps(selection_obj, query_executor):

	userstepmap_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_from_userstepmap())
	for row in cursor:
		user_id = row['user_id']
		step_id = row['step_id']
		key = user_id + "__" + step_id
		userstepmap_dictionary[key] = get_specific_userstepmap(selection_obj, query_executor, key_column, user_id, step_id)
	return userstepmap_dictionary




def get_specific_workspace(selection_obj, query_executor, workspace_id):

	workspace_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor = query_executor.execute(selection_obj.select_workspace(workspace_id))
	workspace_dictionary = cursor.fetchone()
	return workspace_dictionary



def get_specific_role(selection_obj, query_executor, role_id):

	role_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor = query_executor.execute(selection_obj.select_role(role_id))
	role_dictionary = cursor.fetchone()

	return role_dictionary



def get_specific_privilege(selection_obj, query_executor, privilege_id):

	privilege_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor = query_executor.execute(selection_obj.select_privilege(privilege_id))
	privilege_dictionary = cursor.fetchone()

	return privilege_dictionary



def get_specific_user(selection_obj, query_executor, user_id, workspace_id): #todo: perhaps remove the workspace ID, since the user is already unique by nature

	user_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor = query_executor.execute(selection_obj.select_user(user_id))
	user_dictionary = cursor.fetchone()

	return user_dictionary



def get_specific_workflow(selection_obj, query_executor, workflow_id, workspace_id):

	workflow_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor = query_executor.execute(selection_obj.select_workflow_name(workflow_id))
	workflow_dictionary = cursor.fetchone()

	return workflow_dictionary



def get_specific_step(selection_obj, query_executor, step_id, workflow_id):

	step_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor = query_executor.execute(selection_obj.select_step_name(step_id))
	step_dictionary = cursor.fetchone()

	return step_dictionary



def get_specific_time(selection_obj, query_executor, time_id, step_id):

	time_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor = query_executor.execute(selection_obj.select_time_time_unit(time_id))
	time_dictionary = cursor.fetchone()

	return time_dictionary



def get_specific_workflow_case(selection_obj, query_executor, workflow_case_id):

	workflow_case_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor = query_executor.execute(selection_obj.select_workflow_case_legacy_id(workflow_case_id))
	workflow_case_dictionary = cursor.fetchone()

	return workflow_case_dictionary



def get_specific_report(selection_obj, query_executor, report_id, step_id, user_id, workflow_case_id):

	report_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor = query_executor.execute(selection_obj.select_report_report_text(report_id))
	report_dictionary = cursor.fetchone()

	return report_dictionary



def get_specific_workspacerolemap(selection_obj, query_executor, key_column, workspace_id, role_id):

	workspacerolemap_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor = query_executor.execute(selection_obj.select_workspacerolemap(key_column, workspace_id, role_id))
	workspacerolemap_dictionary = cursor.fetchone()

	return workspacerolemap_dictionary



def get_specific_workflowworkflow_casemap(selection_obj, query_executor, key_column, workflow_id, workflow_case_id):

	workflowworkflow_casemap_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor = query_executor.execute(selection_obj.select_workflowworkflow_casemap(key_column, workflow_id, workflow_case_id))
	workflowworkflow_casemap = cursor.fetchone()

	return workflowworkflow_casemap_dictionary



def get_specific_steprolemap(selection_obj, query_executor, key_column, step_id, role_id):

	steprolemap_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor = query_executor.execute(selection_obj.select_steprolemap(key_column, step_id, role_id))
	steprolemap_dictionary = cursor.fetchone()

	return steprolemap_dictionary



def get_specific_stepworkflow_casemap(selection_obj, query_executor, key_column, step_id, workflow_case_id):

	stepworkflow_casemap_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor = query_executor.execute(selection_obj.select_stepworkflow_casemap(key_column, step_id, workflow_case_id))
	stepworkflow_casemap_dictionary = cursor.fetchone()

	return stepworkflow_casemap_dictionary



def get_specific_roleprivilegemap(selection_obj, query_executor, key_column, role_id, privilege_id):

	roleprivilegemap_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor = query_executor.execute(selection_obj.select_roleprivilegemap(key_column, role_id, privilege_id))
	roleprivilegemap_dictionary = cursor.fetchone()

	return roleprivilegemap_dictionary



def get_specific_userrolemap(selection_obj, query_executor, key_column, user_id, role_id):

	userrolemap_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor = query_executor.execute(selection_obj.select_userrolemap(key_column, user_id, role_id))
	userrolemap_dictionary = cursor.fetchone()

	return userrolemap_dictionary



def get_specific_userstepmap(selection_obj, query_executor, key_column, user_id, step_id):

	userstepmap_dictionary = {}
	cursor = query_executor.cursor(dictionary=True)
	cursor = query_executor.execute(selection_obj.select_userstepmap(key_column, user_id, step_id))
	userstepmap_dictionary = cursor.fetchone()

	return userstepmap_dictionary


def get_specific_workspace_roles(selection_obj, query_executor, workspace_id):

	role_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_workspacerolemap_by_workspace(workspace_id))
	for row in cursor:
		role_id = row['role_id']
		role_dictionary[role_id] = get_specific_role(selection_obj, query_executor, role_id)

	return role_dictionary



def get_specific_role_workspaces(selection_obj, query_executor, role_id):

	workspace_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_workspacerolemap_by_role(role_id))
	for row in cursor:
		workspace_id = row['workspace_id']
		workspace_dictionary[workspace_id] = get_specific_workspace(selection_obj, query_executor, workspace_id)

	return workspace_dictionary


def get_specific_role_steps(selection_obj, query_executor, role_id):

	step_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_steprolemap_by_role(role_id))
	for row in cursor:
		step_id = row['step_id']
		workflow_id = row['workflow_id']
		step_dictionary[step_id, workflow_id] = get_specific_step(selection_obj, query_executor, step_id, workflow_id)

	return step_dictionary


def get_specific_role_privileges(selection_obj, query_executor, role_id):

	privilege_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_roleprivilegemap_by_role(role_id))
	for row in cursor:
		privilege_id = row['privilege_id']
		privilege_dictionary[privilege_id] = get_specific_privilege(selection_obj, query_executor, privilege_id)

	return privilege_dictionary


def get_specific_role_users(selection_obj, query_executor, role_id):

	user_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_userrolemap_by_role(role_id))
	for row in cursor:
		user_id = row['user_id']
		workspace_id = row['workspace_id']
		user_dictionary[user_id, workspace_id] = get_specific_user(selection_obj, query_executor, user_id, workspace_id)

	return user_dictionary



def get_specific_privilege_roles(selection_obj, query_executor, privilege_id):

	role_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_roleprivilegemap_by_privilege(privilege_id))
	for row in cursor:
		role_id = row['role_id']
		role_dictionary[role_id] = get_specific_role(selection_obj, query_executor, role_id)

	return role_dictionary



def get_specific_user_roles(selection_obj, query_executor, user_id, workspace_id):

	role_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_userrolemap_by_user(user_id))
	for row in cursor:
		role_id = row['role_id']
		role_dictionary[role_id] = get_specific_role(selection_obj, query_executor, role_id)

	return role_dictionary


def get_specific_user_steps(selection_obj, query_executor, user_id, workspace_id):

	step_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_userstepmap_by_user(user_id))
	for row in cursor:
		step_id = row['step_id']
		workflow_id = row['workflow_id']
		step_dictionary[step_id, workflow_id] = get_specific_step(selection_obj, query_executor, step_id, workflow_id)

	return step_dictionary



def get_specific_workflow_workflow_cases(selection_obj, query_executor, workflow_id, workspace_id):

	workflow_case_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_workflowworkflow_casemap_by_workflow(workflow_id))
	for row in cursor:
		workflow_case_id = row['workflow_case_id']
		workflow_case_dictionary[workflow_case_id] = get_specific_workflow_case(selection_obj, query_executor, workflow_case_id)

	return workflow_case_dictionary



def get_specific_step_roles(selection_obj, query_executor, step_id, workflow_id):

	role_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_steprolemap_by_step(step_id))
	for row in cursor:
		role_id = row['role_id']
		role_dictionary[role_id] = get_specific_role(selection_obj, query_executor, role_id)

	return role_dictionary


def get_specific_step_workflow_cases(selection_obj, query_executor, step_id, workflow_id):

	workflow_case_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_stepworkflow_casemap_by_step(step_id))
	for row in cursor:
		workflow_case_id = row['workflow_case_id']
		workflow_case_dictionary[workflow_case_id] = get_specific_workflow_case(selection_obj, query_executor, workflow_case_id)

	return workflow_case_dictionary


def get_specific_step_users(selection_obj, query_executor, step_id, workflow_id):

	user_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_userstepmap_by_step(step_id))
	for row in cursor:
		user_id = row['user_id']
		workspace_id = row['workspace_id']
		user_dictionary[user_id, workspace_id] = get_specific_user(selection_obj, query_executor, user_id, workspace_id)

	return user_dictionary




def get_specific_workflow_case_workflows(selection_obj, query_executor, workflow_case_id):

	workflow_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_workflowworkflow_casemap_by_workflow_case(workflow_case_id))
	for row in cursor:
		workflow_id = row['workflow_id']
		workspace_id = row['workspace_id']
		workflow_dictionary[workflow_id, workspace_id] = get_specific_workflow(selection_obj, query_executor, workflow_id, workspace_id)

	return workflow_dictionary


def get_specific_workflow_case_steps(selection_obj, query_executor, workflow_case_id):

	step_dictionary = {}

	cursor = query_executor.cursor(dictionary=True)
	cursor.execute(selection_obj.select_stepworkflow_casemap_by_workflow_case(workflow_case_id))
	for row in cursor:
		step_id = row['step_id']
		workflow_id = row['workflow_id']
		step_dictionary[step_id, workflow_id] = get_specific_step(selection_obj, query_executor, step_id, workflow_id)

	return step_dictionary



def get_workspace_roles_map(query_executor, selection_obj, workspace_dictionary):

	workspacerolemap_dictionary = ()

	for workspace in workspace_dictionary:
		workspace_id = workspace_dictionary[workspace]
		role_dictionary = get_specific_workspace_roles(selection_obj, query_executor, workspace_id)
		workspacerolemap_dictionary[workspace] = role_dictionary

	return workspacerolemap_dictionary



def get_role_workspaces_map(query_executor, selection_obj, role_dictionary):

	roleworkspacemap_dictionary = ()

	for role in role_dictionary:
		role_id = role_dictionary[role]
		workspace_dictionary = get_specific_role_workspaces(selection_obj, query_executor, role_id)
		roleworkspacemap_dictionary[role] = workspace_dictionary

	return roleworkspacemap_dictionary



def get_role_steps_map(query_executor, selection_obj, role_dictionary):

	rolestepmap_dictionary = ()

	for role in role_dictionary:
		role_id = role_dictionary[role]
		step_dictionary = get_specific_role_steps(selection_obj, query_executor, role_id)
		rolestepmap_dictionary[role] = step_dictionary

	return rolestepmap_dictionary



def get_role_privileges_map(query_executor, selection_obj, role_dictionary):

	roleprivilegemap_dictionary = ()

	for role in role_dictionary:
		role_id = role_dictionary[role]
		privilege_dictionary = get_specific_role_privileges(selection_obj, query_executor, role_id)
		roleprivilegemap_dictionary[role] = privilege_dictionary

	return roleprivilegemap_dictionary



def get_role_users_map(query_executor, selection_obj, role_dictionary):

	roleusermap_dictionary = ()

	for role in role_dictionary:
		role_id = role_dictionary[role]
		user_dictionary = get_specific_role_users(selection_obj, query_executor, role_id)
		roleusermap_dictionary[role] = user_dictionary

	return roleusermap_dictionary



def get_privilege_roles_map(query_executor, selection_obj, privilege_dictionary):

	privilegerolemap_dictionary = ()

	for privilege in privilege_dictionary:
		privilege_id = privilege_dictionary[privilege]
		role_dictionary = get_specific_privilege_roles(selection_obj, query_executor, privilege_id)
		privilegerolemap_dictionary[privilege] = role_dictionary

	return privilegerolemap_dictionary



def get_user_roles_map(query_executor, selection_obj, user_dictionary):

	userrolemap_dictionary = ()

	for user in user_dictionary:
		user_id = user_dictionary[user]
		workspace_id = user_dictionary[user]
		role_dictionary = get_specific_user_roles(selection_obj, query_executor, user_id, workspace_id)
		userrolemap_dictionary[user] = role_dictionary

	return userrolemap_dictionary



def get_user_steps_map(query_executor, selection_obj, user_dictionary):

	userstepmap_dictionary = ()

	for user in user_dictionary:
		user_id = user_dictionary[user]
		workspace_id = user_dictionary[user]
		step_dictionary = get_specific_user_steps(selection_obj, query_executor, user_id, workspace_id)
		userstepmap_dictionary[user] = step_dictionary

	return userstepmap_dictionary



def get_workflow_workflow_cases_map(query_executor, selection_obj, workflow_dictionary):

	workflowworkflow_casemap_dictionary = ()

	for workflow in workflow_dictionary:
		workflow_id = workflow_dictionary[workflow]
		workspace_id = workflow_dictionary[workflow]
		workflow_case_dictionary = get_specific_workflow_workflow_cases(selection_obj, query_executor, workflow_id, workspace_id)
		workflowworkflow_casemap_dictionary[workflow] = workflow_case_dictionary

	return workflowworkflow_casemap_dictionary



def get_step_roles_map(query_executor, selection_obj, step_dictionary):

	steprolemap_dictionary = ()

	for step in step_dictionary:
		step_id = step_dictionary[step]
		workflow_id = step_dictionary[step]
		role_dictionary = get_specific_step_roles(selection_obj, query_executor, step_id, workflow_id)
		steprolemap_dictionary[step] = role_dictionary

	return steprolemap_dictionary



def get_step_workflow_cases_map(query_executor, selection_obj, step_dictionary):

	stepworkflow_casemap_dictionary = ()

	for step in step_dictionary:
		step_id = step_dictionary[step]
		workflow_id = step_dictionary[step]
		workflow_case_dictionary = get_specific_step_workflow_cases(selection_obj, query_executor, step_id, workflow_id)
		stepworkflow_casemap_dictionary[step] = workflow_case_dictionary

	return stepworkflow_casemap_dictionary



def get_step_users_map(query_executor, selection_obj, step_dictionary):

	stepusermap_dictionary = ()

	for step in step_dictionary:
		step_id = step_dictionary[step]
		workflow_id = step_dictionary[step]
		user_dictionary = get_specific_step_users(selection_obj, query_executor, step_id, workflow_id)
		stepusermap_dictionary[step] = user_dictionary

	return stepusermap_dictionary



def get_workflow_case_workflows_map(query_executor, selection_obj, workflow_case_dictionary):

	workflow_caseworkflowmap_dictionary = ()

	for workflow_case in workflow_case_dictionary:
		workflow_case_id = workflow_case_dictionary[workflow_case]
		workflow_dictionary = get_specific_workflow_case_workflows(selection_obj, query_executor, workflow_case_id)
		workflow_caseworkflowmap_dictionary[workflow_case] = workflow_dictionary

	return workflow_caseworkflowmap_dictionary



def get_workflow_case_steps_map(query_executor, selection_obj, workflow_case_dictionary):

	workflow_casestepmap_dictionary = ()

	for workflow_case in workflow_case_dictionary:
		workflow_case_id = workflow_case_dictionary[workflow_case]
		step_dictionary = get_specific_workflow_case_steps(selection_obj, query_executor, workflow_case_id)
		workflow_casestepmap_dictionary[workflow_case] = step_dictionary

	return workflow_casestepmap_dictionary
