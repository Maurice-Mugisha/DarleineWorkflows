


class Select:

	def  __init__(self, instance_name):
		self.instance_name = instance_name

	def  __str__(self):
		return self.instance_name


	def select_from_workspace(self):
		query = "SELECT * FROM workspace;"
		return query

	def select_workspace(self, workspace_id):
		query = f"SELECT * FROM workspace WHERE workspace_id = '{workspace_id}';"
		return query

	def select_count_from_workspace(self):
		query = "SELECT COUNT(*) AS count FROM workspace;"
		return query

	def select_from_role(self):
		query = "SELECT * FROM role;"
		return query

	def select_role(self, role_id):
		query = f"SELECT * FROM role WHERE role_id = '{role_id}';"
		return query

	def select_count_from_role(self):
		query = "SELECT COUNT(*) AS count FROM role;"
		return query

	def select_from_privilege(self):
		query = "SELECT * FROM privilege;"
		return query

	def select_privilege(self, privilege_id):
		query = f"SELECT * FROM privilege WHERE privilege_id = '{privilege_id}';"
		return query

	def select_count_from_privilege(self):
		query = "SELECT COUNT(*) AS count FROM privilege;"
		return query

	def select_from_user(self):
		query = "SELECT * FROM user;"
		return query

	def select_user(self, user_id):
		query = f"SELECT * FROM user WHERE user_id = '{user_id}';"
		return query

	def select_count_from_user(self):
		query = "SELECT COUNT(*) AS count FROM user;"
		return query

	def select_user_by_workspace_id(self, workspace_id):
		query = f"SELECT * FROM user WHERE workspace_id = '{workspace_id}';"
		return query

	def select_from_workflow(self):
		query = "SELECT * FROM workflow;"
		return query

	def select_workflow(self, workflow_id):
		query = f"SELECT * FROM workflow WHERE workflow_id = '{workflow_id}';"
		return query

	def select_count_from_workflow(self):
		query = "SELECT COUNT(*) AS count FROM workflow;"
		return query

	def select_workflow_by_workspace_id(self, workspace_id):
		query = f"SELECT * FROM workflow WHERE workspace_id = '{workspace_id}';"
		return query

	def select_from_step(self):
		query = "SELECT * FROM step;"
		return query

	def select_step(self, step_id):
		query = f"SELECT * FROM step WHERE step_id = '{step_id}';"
		return query

	def select_count_from_step(self):
		query = "SELECT COUNT(*) AS count FROM step;"
		return query

	def select_step_by_workflow_id(self, workflow_id):
		query = f"SELECT * FROM step WHERE workflow_id = '{workflow_id}';"
		return query

	def select_from_time(self):
		query = "SELECT * FROM time;"
		return query

	def select_time(self, time_id):
		query = f"SELECT * FROM time WHERE time_id = '{time_id}';"
		return query

	def select_count_from_time(self):
		query = "SELECT COUNT(*) AS count FROM time;"
		return query

	def select_time_by_step_id(self, step_id):
		query = f"SELECT * FROM time WHERE step_id = '{step_id}';"
		return query

	def select_from_workflow_case(self):
		query = "SELECT * FROM workflow_case;"
		return query

	def select_workflow_case(self, workflow_case_id):
		query = f"SELECT * FROM workflow_case WHERE workflow_case_id = '{workflow_case_id}';"
		return query

	def select_count_from_workflow_case(self):
		query = "SELECT COUNT(*) AS count FROM workflow_case;"
		return query

	def select_from_report(self):
		query = "SELECT * FROM report;"
		return query

	def select_report(self, report_id):
		query = f"SELECT * FROM report WHERE report_id = '{report_id}';"
		return query

	def select_count_from_report(self):
		query = "SELECT COUNT(*) AS count FROM report;"
		return query

	def select_report_by_step_id(self, step_id):
		query = f"SELECT * FROM report WHERE step_id = '{step_id}';"
		return query

	def select_report_by_workflow_case_id(self, workflow_case_id):
		query = f"SELECT * FROM report WHERE step_id = '{workflow_case_id}';"
		return query

	def select_report_by_user_id(self, user_id, workflow_case_id):
		query = f"SELECT * FROM report WHERE step_id = '{user_id}';"
		return query

	def select_report_by_workflow_case_step_and_user(self, step_id, user_id, workflow_case_id):
		query = f"SELECT * FROM report WHERE step_id = '{step_id}' AND user_id = '{user_id}' AND workflow_case_id = '{workflow_case_id}';"
		return query

	def select_from_workspacerolemap(self):
		query = "SELECT * FROM workspacerolemap;"
		return query

	def select_workspacerolemap(self, workspace_id, role_id):
		query = f"SELECT * FROM workspacerolemap WHERE workspace_id = '{workspace_id}' AND role_id = '{role_id}';"
		return query

	def select_count_from_workspacerolemap(self):
		query = "SELECT COUNT(*) AS count FROM workspacerolemap;"
		return query

	def select_workspacerolemap_by_workspace(self, workspace_id):
		query = f"SELECT * FROM workspacerolemap WHERE workspace_id = '{workspace_id}';"
		return query

	def select_workspacerolemap_by_role(self, role_id):
		query = "SELECT * FROM workspacerolemap WHERE role_id = '{role_id}';"
		return query

	def select_from_workflowworkflow_casemap(self):
		query = "SELECT * FROM workflowworkflow_casemap;"
		return query

	def select_workflowworkflow_casemap(self, workflow_id, workflow_case_id):
		query = f"SELECT * FROM workflowworkflow_casemap WHERE workflow_id = '{workflow_id}' AND workflow_case_id = '{workflow_case_id}';"
		return query

	def select_count_from_workflowworkflow_casemap(self):
		query = "SELECT COUNT(*) AS count FROM workflowworkflow_casemap;"
		return query

	def select_workflowworkflow_casemap_by_workflow(self, workflow_id):
		query = f"SELECT * FROM workflowworkflow_casemap WHERE workflow_id = '{workflow_id}';"
		return query

	def select_workflowworkflow_casemap_by_workflow_case(self, workflow_case_id):
		query = f"SELECT * FROM workflowworkflow_casemap WHERE workflow_case_id = '{workflow_case_id}';"
		return query

	def select_from_steprolemap(self):
		query = "SELECT * FROM steprolemap;"
		return query

	def select_steprolemap(self, step_id, role_id):
		query = f"SELECT * FROM steprolemap WHERE step_id = '{step_id}' AND role_id = '{role_id}';"
		return query

	def select_count_from_steprolemap(self):
		query = "SELECT COUNT(*) AS count FROM steprolemap;"
		return query

	def select_steprolemap_by_step(self, step_id):
		query = f"SELECT * FROM steprolemap WHERE step_id = '{step_id}';"
		return query

	def select_steprolemap_by_role(self, role_id):
		query = f"SELECT * FROM steprolemap WHERE role_id = '{role_id}';"
		return query

	def select_from_stepworkflow_casemap(self):
		query = "SELECT * FROM stepworkflow_casemap;"
		return query

	def select_stepworkflow_casemap(self, step_id, workflow_case_id):
		query = f"SELECT * FROM stepworkflow_casemap WHERE step_id = '{step_id}' AND workflow_case_id = '{workflow_case_id}';"
		return query

	def select_count_from_stepworkflow_casemap(self):
		query = "SELECT COUNT(*) AS count FROM stepworkflow_casemap;"
		return query

	def select_stepworkflow_casemap_by_step(self, step_id):
		query = f"SELECT * FROM stepworkflow_casemap WHERE step_id = '{step_id}';"
		return query

	def select_stepworkflow_casemap_by_workflow_case(self, workflow_case_id):
		query = f"SELECT * FROM stepworkflow_casemap WHERE workflow_case_id = '{workflow_case_id}';"
		return query

	def select_from_roleprivilegemap(self):
		query = "SELECT * FROM roleprivilegemap;"
		return query

	def select_roleprivilegemap(self, role_id, privilege_id):
		query = f"SELECT * FROM roleprivilegemap WHERE role_id = '{role_id}' AND privilege_id = '{privilege_id}';"
		return query

	def select_count_from_roleprivilegemap(self):
		query = "SELECT COUNT(*) AS count FROM roleprivilegemap;"
		return query

	def select_roleprivilegemap_by_privilege(self, privilege_id):
		query = f"SELECT * FROM roleprivilegemap WHERE privilege_id = '{privilege_id}';"
		return query

	def select_roleprivilegemap_by_role(self, role_id):
		query = f"SELECT * FROM roleprivilegemap WHERE role_id = '{role_id}';"
		return query

	def select_from_userrolemap(self):
		query = "SELECT * FROM userrolemap;"
		return query

	def select_userrolemap(self, user_id, role_id):
		query = f"SELECT * FROM userrolemap WHERE user_id = '{user_id}' AND role_id = '{role_id}';"
		return query

	def select_count_from_userrolemap(self):
		query = "SELECT COUNT(*) AS count FROM userrolemap;"
		return query

	def select_userrolemap_by_user(self, user_id):
		query = f"SELECT * FROM userrolemap WHERE user_id = '{user_id}';"
		return query

	def select_userrolemap_by_role(self, role_id):
		query = f"SELECT * FROM userrolemap WHERE role_id = '{role_id}';"
		return query

	def select_from_userstepmap(self):
		query = "SELECT * FROM userstepmap;"
		return query

	def select_userstepmap(self, user_id, step_id):
		query = f"SELECT * FROM userstepmap WHERE user_id = '{user_id}' AND step_id = '{step_id}';"
		return query

	def select_count_from_userstepmap(self):
		query = "SELECT COUNT(*) AS count FROM userstepmap;"
		return query

	def select_userstepmap_by_step(self, step_id):
		query = f"SELECT * FROM userstepmap WHERE step_id = '{step_id}';"
		return query

	def select_userstepmap_by_user(self, user_id):
		query = f"SELECT * FROM userstepmap WHERE user_id = '{user_id}';"
		return query
