import psycopg2
import psycopg2.extras


def get_workspaces(selection_obj, query_executor):

	workspace_dictionary = {}
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_from_workspace())
	workspace_dictionary = cursor.fetchall()
	cursor.close()
	query_executor.close()
	return workspace_dictionary


def get_roles(query_executor, selection_obj):

	role_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_from_role())
	role_list = cursor.fetchall()
	cursor.close()
	query_executor.close()
	return role_list


def get_privileges(selection_obj, query_executor):

	privilege_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_from_privilege())
	privilege_list = cursor.fetchall()
	cursor.close()
	query_executor.close()
	return privilege_list


def get_users(selection_obj, query_executor):

	user_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_from_user())
	user_list = cursor.fetchall()
	cursor.close()
	query_executor.close()
	return user_list


def get_workflows(selection_obj, query_executor):

	workflow_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_from_workflow())
	workflow_list = cursor.fetchall()
	cursor.close()
	query_executor.close()
	return workflow_list


def get_steps(selection_obj, query_executor):

	step_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_from_step())
	step_list = cursor.fetchall()
	cursor.close()
	query_executor.close()
	return step_list


def get_times(selection_obj, query_executor):

	time_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_from_time())
	time_list = cursor.fetchall()
	cursor.close()
	query_executor.close()
	return time_list


def get_workflow_cases(selection_obj, query_executor):

	workflow_case_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_from_workflow_case())
	workflow_case_list = cursor.fetchall()
	cursor.close()
	query_executor.close()
	return workflow_case_list


def get_reports(selection_obj, query_executor):

	report_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_from_report())
	report_list = cursor.fetchall()
	cursor.close()
	query_executor.close()
	return report_list


def get_specific_workspace(selection_obj, query_executor, workspace_id):

	workspace_dictionary = {}
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_workspace(workspace_id))
	workspace_dictionary = cursor.fetchone()
	cursor.close()
	query_executor.close()
	return workspace_dictionary



def get_specific_role(selection_obj, query_executor, role_id):

	role_dictionary = {}
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_role(role_id))
	role_dictionary = cursor.fetchone()
	cursor.close()
	query_executor.close()
	return role_dictionary



def get_specific_privilege(selection_obj, query_executor, privilege_id):

	privilege_dictionary = {}
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_privilege(privilege_id))
	privilege_dictionary = cursor.fetchone()
	cursor.close()
	query_executor.close()
	return privilege_dictionary



def get_specific_user(query_executor, selection_obj, user_id):

	user_dictionary = {}
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_user(user_id))
	user_dictionary = cursor.fetchone()
	cursor.close()
	query_executor.close()
	return user_dictionary


def get_specific_workspace_users(query_executor, selection_obj, workspace_id):

	user_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_user_by_workspace_id(workspace_id))
	user_list = cursor.fetchall()
	cursor.close()
	query_executor.close()
	return user_list


def get_specific_user_by_email(selection_obj, query_executor, email):

	user_dictionary = {}
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_user_by_email(email))
	user_dictionary = cursor.fetchone()
	cursor.close()
	query_executor.close()
	return user_dictionary



def get_specific_workflow(selection_obj, query_executor, workflow_id):

	workflow_dictionary = {}
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_workflow(workflow_id))
	workflow_dictionary = cursor.fetchone()
	cursor.close()
	query_executor.close()
	return workflow_dictionary


def get_specific_workspace_workflows(query_executor, selection_obj, workspace_id):

	workflow_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_workflow_by_workspace_id(workspace_id))
	workflow_list = cursor.fetchall()
	cursor.close()
	query_executor.close()
	return workflow_list



def get_specific_step(query_executor, selection_obj, step_id):

	step_dictionary = {}
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_step(step_id))
	step_dictionary = cursor.fetchone()
	cursor.close()
	query_executor.close()
	return step_dictionary

def get_workflow_steps(selection_obj, query_executor, workflow_id):

	step_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_step_by_workflow_id(workflow_id))
	step_list = cursor.fetchall()
	cursor.close()
	query_executor.close()
	return step_list



def get_specific_time(query_executor, selection_obj, time_id):

	time_dictionary = {}
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_time(time_id))
	time_dictionary = cursor.fetchone()
	cursor.close()
	query_executor.close()
	return time_dictionary


def get_step_times(query_executor, selection_obj, step_id):

	time_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_time_by_step_id(step_id))
	time_list = cursor.fetchall()
	cursor.close()
	query_executor.close()
	return time_list


def get_step_roles(query_executor, selection_obj, step_id):

	role_list = []
	steprolemap_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_steprolemap_by_step(step_id))
	steprolemap_list = cursor.fetchall()

	if steprolemap_list and len(steprolemap_list) > 0:
		for steprolemap in steprolemap_list:
			role_id = steprolemap["role_id"]
			cursor.execute(selection_obj.select_role(role_id))
			role_dictionary = cursor.fetchone()
			if role_dictionary:
				role_list.append(role_dictionary)
	cursor.close()
	query_executor.close()
	return role_list



def get_specific_workflow_case(selection_obj, query_executor, workflow_case_id):

	workflow_case_dictionary = {}
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_workflow_case(workflow_case_id))
	workflow_case_dictionary = cursor.fetchone()
	cursor.close()
	query_executor.close()
	return workflow_case_dictionary



def get_specific_report(selection_obj, query_executor, report_id):

	report_dictionary = {}
	cursor = query_executor.cursor()
	cursor = query_executor.execute(selection_obj.select_report_report_text(report_id))
	report_dictionary = cursor.fetchone()
	cursor.close()
	query_executor.close()
	return report_dictionary


def get_workflow_case_workflow_id_list(query_executor, selection_obj, workflow_case_id):

	workflow_id_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_workflowworkflow_casemap_by_workflow_case(workflow_case_id))
	workflowworkflow_casemap_list = cursor.fetchall()
	if workflowworkflow_casemap_list and len(workflowworkflow_casemap_list) > 0:
		workflow_id_list = [workflowworkflow_casemap["workflow_id"] for workflowworkflow_casemap in workflowworkflow_casemap_list]
	cursor.close()
	query_executor.close()
	return workflow_id_list


def get_specific_workspace_roles(query_executor, selection_obj, workspace_id):

	role_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_workspacerolemap_by_workspace(workspace_id))
	workspacerolemap_list = cursor.fetchall()
	for row in workspacerolemap_list:
		role_id = row['role_id']
		role_dictionary = cursor.execute(selection_obj.select_role(role_id))
		role_list.append(role_dictionary)
	cursor.close()
	query_executor.close()
	return role_list


def get_specific_role_privileges(query_executor, selection_obj, role_id):

	privilege_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_roleprivilegemap_by_role(role_id))
	roleprivilegemap_list = cursor.fetchall()
	for row in roleprivilegemap_list:
		privilege_id = row['privilege_id']
		privilege_dictionary = cursor.execute(selection_obj.select_privilege(privilege_id))
		privilege_list.append(privilege_dictionary)
	cursor.close()
	query_executor.close()
	return privilege_list


def get_specific_user_roles(query_executor, selection_obj, user_id):

	user_role_map_list = {}
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_userrolemap_by_user(user_id))
	user_role_map_list = cursor.fetchall()
	role_list = []
	for row in user_role_map_list:
		role_id = row['role_id']
		cursor.execute(selection_obj.select_role(role_id))
		role_dictionary = cursor.fetchone()
		role_list.append(role_dictionary)
	cursor.close()
	query_executor.close()
	return role_list


def get_specific_user_steps(query_executor, selection_obj, user_id):

	step_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_userstepmap_by_user(user_id))
	userstepmap_list = cursor.fetchall()
	for row in userstepmap_list:
		step_id = row['step_id']
		step_dictionary= cursor.execute(selection_obj.select_step(step_id))
		step_list.append(step_dictionary)
	cursor.close()
	query_executor.close()
	return step_list


def get_specific_workflow_workflow_cases(query_executor, selection_obj, workflow_id):

	workflow_case_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_workflowworkflow_casemap_by_workflow(workflow_id))
	workflowworkflow_casemap_list = cursor.fetchall()
	for row in workflowworkflow_casemap_list:
		workflow_case_id = row['workflow_case_id']
		cursor.execute(selection_obj.select_workflow_case(workflow_case_id))
		workflow_case_dictionary = cursor.fetchone()
		workflow_case_list.append(workflow_case_dictionary)
	cursor.close()
	query_executor.close()
	return workflow_case_list


def get_specific_step_roles(query_executor, selection_obj, step_id):

	role_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_steprolemap_by_step(step_id))
	steprolemap_list = cursor.fetchall()
	for row in steprolemap_list:
		role_id = row['role_id']
		role_dictionary = cursor.execute(selection_obj.select_role(role_id))
		role_list.append(role_dictionary)
	cursor.close()
	query_executor.close()
	return role_list


def get_specific_workflow_case_reports(query_executor, selection_obj, workflow_case_id):

	report_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_report_by_workflow_case_id(workflow_case_id))
	report_list = cursor.fetchall()
	cursor.close()
	query_executor.close()
	return report_list


def get_specific_workflow_case_steps(query_executor, selection_obj, workflow_case_id):

	step_list = []
	stepworkflow_casemap_list = []
	cursor = query_executor.cursor()
	cursor.execute(selection_obj.select_stepworkflow_casemap_by_workflow_case(workflow_case_id))
	stepworkflow_casemap_list = cursor.fetchall()
	for row in stepworkflow_casemap_list:
		step_id = row['step_id']
		cursor.execute(selection_obj.select_step(step_id))
		step_dictionary = cursor.fetchone()
		step_list.append(step_dictionary)
	cursor.close()
	query_executor.close()
	return step_list
