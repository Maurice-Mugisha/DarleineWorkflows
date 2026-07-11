


class Insert:

	def  __init__(self, instance_name):
		self.instance_name = instance_name

	def  __str__(self):
		return self.instance_name


	def insert_workspace(self, id, name, description, language, organization_type, email, country):
		query = f"INSERT INTO workspace VALUES('{id}', '{name}', '{description}', '{language}', '{organization_type}', '{email}', '{country}');"
		return query

	def insert_workflow(self, id, name, description, is_mandatory, number_of_steps, status, workspace_id):
		query = f"INSERT INTO workflow VALUES('{id}', '{name}', '{description}', '{is_mandatory}', {number_of_steps}, '{status}', '{workspace_id}');"
		return query

	def insert_user(self, id, first_name, last_name, job_title, email, password, workspace_id):
		query = f"INSERT INTO user VALUES('{id}', '{first_name}', '{last_name}', '{job_title}', '{email}', '{password}', '{workflow_id}');"
		return query

	def insert_role(self, id, name, description):
		query = f"INSERT INTO role VALUES('{id}', '{name}', '{description}');"
		return query

	def insert_privilege(self, id, name, description):
		query = f"INSERT INTO privilege VALUES('{id}', '{name}', '{description}');"
		return query

	def insert_step(self, id, name, description, code, step_number, percentage, status, warning_threshold, workflow_id):
		query = f"INSERT INTO step VALUES('{id}', '{name}', '{description}', '{code}', {step_number}, {percentage}, '{status}', {warning_threshold}, '{workflow_id}');"
		return query

	def insert_time(self, id, time_unit, time_unit_category, time_unit_value, step_id):
		query = f"INSERT INTO time VALUES('{id}', '{time_unit}', '{time_unit_category}', {time_unit_value}, {step_id});"
		return query

	def insert_workflow_case(self, id, legacy_id, name, description):
		query = f"INSERT INTO workflow_case VALUES('{id}', '{legacy_id}', '{name}', '{description}');"
		return query

	def insert_report(self, id, report_text, optional_document_url, workflow_case_id, step_id, user_id):
		query = f"INSERT INTO report VALUES('{id}', '{report_text}', '{optional_document_url}', '{workflow_case_id}', '{step_id}', '{user_id}');"
		return query



	def insert_workspacerolemap(self, workspace_id, role_id):
		query = f"INSERT INTO workspacerolemap VALUES('{workspace_id}', '{role_id}');"
		return query

	def insert_workflowworkflow_casemap(self, workflow_id, workflow_case_id):
		query = f"INSERT INTO workflowworkflow_casemap VALUES('{workflow_id}', '{workflow_case_id}');"
		return query

	def insert_steprolemap(self, step_id, role_id):
		query = f"INSERT INTO steprolemap VALUES('{step_id}', '{role_id}');"
		return query

	def insert_stepworkflow_casemap(self, step_id, workflow_case_id):
		query = f"INSERT INTO stepworkflow_casemap VALUES('{step_id}', '{workflow_case_id}');"
		return query

	def insert_roleprivilegemap(self, role_id, privilege_id):
		query = f"INSERT INTO roleprivilegemap VALUES('{role_id}', '{privilege_id}');"
		return query

	def insert_userrolemap(self, user_id, role_id):
		query = f"INSERT INTO userrolemap VALUES('{user_id}', '{role_id}');"
		return query

	def insert_userstepmap(self, user_id, step_id):
		query = f"INSERT INTO userstepmap VALUES('{user_id}', '{step_id}');"
		return query
