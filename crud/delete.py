


class Delete:

	def  __init__(self, instance_name):
		self.instance_name = instance_name

	def  __str__(self):
		return self.instance_name


	def delete_from_workspace(self):
		query = "DELETE FROM workspace;"
		return query

	def delete_workspace(self, workspace_id):
		query = f"DELETE FROM workspace WHERE workspace_id = '{workspace_id}';"
		return query


	def delete_from_role(self):
		query = "DELETE FROM role;"
		return query

	def delete_role(self, role_id):
		query = f"DELETE FROM role WHERE role_id = '{role_id}';"
		return query

	def delete_from_privilege(self):
		query = "DELETE FROM privilege;"
		return query

	def delete_privilege(self, privilege_id):
		query = f"DELETE FROM privilege WHERE privilege_id = '{privilege_id}';"
		return query

	def delete_from_user(self):
		query = "DELETE FROM user;"
		return query

	def delete_user(self, user_id):
		query = f"DELETE FROM user WHERE user_id = '{user_id}';"
		return query

	def delete_user_by_workspace_id(self, workspace_id):
		query = f"DELETE FROM user WHERE workspace_id = '{workspace_id}';"
		return query


	def delete_from_workflow(self):
		query = "DELETE FROM workflow;"
		return query

	def delete_workflow(self, workflow_id):
		query = f"DELETE FROM workflow WHERE workflow_id = '{workflow_id}';"
		return query

	def delete_workflow_by_workspace_id(self, workspace_id):
		query = f"DELETE FROM workflow WHERE workspace_id = '{workspace_id}';"
		return query

	def delete_from_step(self):
		query = "DELETE FROM step;"
		return query

	def delete_step(self, step_id):
		query = f"DELETE FROM step WHERE step_id = '{step_id}';"
		return query

	def delete_step_by_workflow_id(self, workflow_id):
		query = f"DELETE FROM step WHERE workflow_id = '{workflow_id}';"
		return query

	def delete_from_time(self):
		query = "DELETE FROM time;"
		return query

	def delete_time(self, time_id):
		query = f"DELETE FROM time WHERE time_id = '{time_id}';"
		return query

	def delete_time_by_step_id(self, step_id):
		query = f"DELETE FROM time WHERE step_id = '{step_id}';"
		return query

	def delete_from_workflow_case(self):
		query = "DELETE FROM workflow_case;"
		return query

	def delete_workflow_case(self, workflow_case_id):
		query = f"DELETE FROM workflow_case WHERE workflow_case_id = '{workflow_case_id}';"
		return query

	def delete_from_report(self):
		query = "DELETE FROM report;"
		return query

	def delete_report(self, report_id):
		query = f"DELETE FROM report WHERE report_id = '{report_id}';"
		return query

	def delete_report_by_step_user_and_workflow_case(self, step_id, user_id, workflow_case_id):
		query = f"DELETE FROM report WHERE step_id = '{step_id}' AND user_id = '{user_id}' AND workflow_case_id = '{workflow_case_id}';"
		return query

	def delete_report_by_user_id(self, user_id):
		query = f"DELETE FROM report WHERE user_id = '{user_id}';"
		return query

	def delete_report_by_workflow_case_id(self, workflow_case_id):
		query = f"DELETE FROM report WHERE workflow_case_id = '{workflow_case_id}';"
		return query

	def delete_from_workspacerolemap(self):
		query = "DELETE FROM workspacerolemap;"
		return query

	def delete_workspacerolemap(self, workspace_id, role_id):
		query = f"DELETE FROM workspacerolemap WHERE workspace_id = '{workspace_id}' AND role_id = '{role_id}';"
		return query

	def delete_workspacerolemap_by_workspace_id(self, workspace_id):
		query = f"DELETE FROM workspacerolemap WHERE workspace_id = '{workspace_id}';"
		return query

	def delete_workspacerolemap_by_role_id(self, role_id):
		query = f"DELETE FROM workspacerolemap WHERE role_id = '{role_id}';"
		return query

	def delete_from_workflowworkflow_casemap(self):
		query = "DELETE FROM workflowworkflow_casemap;"
		return query

	def delete_workflowworkflow_casemap(self, workflow_id, workflow_case_id):
		query = f"DELETE FROM workflowworkflow_casemap WHERE workflow_id = '{workflow_id}' AND workflow_case_id = '{workflow_case_id}';"
		return query

	def delete_workflowworkflow_casemap_by_workflow_id(self, workflow_id):
		query = f"DELETE FROM workflowworkflow_casemap WHERE workflow_id = '{workflow_id}';"
		return query

	def delete_workflowworkflow_casemap_by_workflow_case_id(self, workflow_case_id):
		query = f"DELETE FROM workflowworkflow_casemap WHERE workflow_case_id = '{workflow_case_id}';"
		return query

	def delete_from_steprolemap(self):
		query = "DELETE FROM steprolemap;"
		return query

	def delete_steprolemap(self, step_id, role_id):
		query = f"DELETE FROM steprolemap WHERE step_id = '{step_id}' AND role_id = '{role_id}';"
		return query

	def delete_steprolemap_by_step_id(self, step_id):
		query = f"DELETE FROM steprolemap WHERE step_id = '{step_id}';"
		return query

	def delete_steprolemap_by_role_id(self, role_id):
		query = f"DELETE FROM steprolemap WHERE role_id = '{role_id}';"
		return query

	def delete_from_stepworkflow_casemap(self):
		query = "DELETE FROM stepworkflow_casemap;"
		return query

	def delete_stepworkflow_casemap(self, step_id, workflow_case_id):
		query = f"DELETE FROM stepworkflow_casemap WHERE step_id = '{step_id}' AND workflow_case_id = '{workflow_case_id}';"
		return query

	def delete_stepworkflow_casemap_by_step_id(self, step_id):
		query = f"DELETE FROM stepworkflow_casemap WHERE step_id = '{step_id}';"
		return query

	def delete_stepworkflow_casemap_by_workflow_case_id(self, workflow_case_id):
		query = f"DELETE FROM stepworkflow_casemap WHERE workflow_case_id = '{workflow_case_id}';"
		return query

	def delete_from_roleprivilegemap(self):
		query = "DELETE FROM roleprivilegemap;"
		return query

	def delete_roleprivilegemap(self, role_id, privilege_id):
		query = f"DELETE FROM roleprivilegemap WHERE role_id = '{role_id}' AND privilege_id = '{privilege_id}';"
		return query

	def delete_roleprivilegemap_by_role_id(self, role_id):
		query = f"DELETE FROM roleprivilegemap WHERE role_id = '{role_id}';"
		return query

	def delete_roleprivilegemap_by_privilege_id(self, privilege_id):
		query = f"DELETE FROM roleprivilegemap WHERE privilege_id = '{privilege_id}';"
		return query

	def delete_from_userrolemap(self):
		query = "DELETE FROM userrolemap;"
		return query

	def delete_userrolemap(self, user_id, role_id):
		query = f"DELETE FROM userrolemap WHERE user_id = '{user_id}' AND role_id = '{role_id}';"
		return query

	def delete_userrolemap_by_user_id(self, user_id):
		query = f"DELETE FROM userrolemap WHERE user_id = '{user_id}';"
		return query

	def delete_userrolemap_by_role_id(self, role_id):
		query = f"DELETE FROM userrolemap WHERE role_id = '{role_id}';"
		return query

	def delete_from_userstepmap(self):
		query = "DELETE FROM userstepmap;"
		return query

	def delete_userstepmap(self, user_id, step_id):
		query = f"DELETE FROM userstepmap WHERE user_id = '{user_id}' AND step_id = '{step_id}';"
		return query

	def delete_userstepmap_by_user_id(self, user_id):
		query = f"DELETE FROM userstepmap WHERE user_id = '{user_id}';"
		return query

	def delete_userstepmap_by_step_id(self, step_id):
		query = f"DELETE FROM userstepmap WHERE step_id = '{step_id}';"
		return query
