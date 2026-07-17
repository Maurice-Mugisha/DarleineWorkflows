


class Insert:

	def  __init__(self, instance_name):
		self.instance_name = instance_name

	def  __str__(self):
		return self.instance_name


	def insert_workspace(self):
		query = """INSERT INTO workspace (id, name, description, language, organization_type, email, country) VALUES(%s, %s, %s, %s, %s, %s, %s);"""
		return query

	def insert_workflow(self):
		query = """
	        INSERT INTO workflow
	        (id, name, description, is_mandatory, number_of_steps, status, workspace_id)
	        VALUES (%s, %s, %s, %s, %s, %s, %s);
	    """
		return query

	def insert_user(self):
		query = """INSERT INTO workspace_user (id, first_name, last_name, job_title, email, password, workspace_id) VALUES(%s, %s, %s, %s, %s, %s, %s);"""
		return query

	def insert_role(self, id, name, description):
		query = f"INSERT INTO role VALUES('{id}', '{name}', '{description}');"
		return query

	def insert_privilege(self, id, name, description):
		query = f"INSERT INTO privilege VALUES('{id}', '{name}', '{description}');"
		return query

	def insert_step(self):
		query = """
	        INSERT INTO step
	        (id, name, description, code, step_number, percentage, status, warning_threshold, workflow_id)
	        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
	    """
		return query

	def insert_time(self, id, time_unit, time_unit_category, time_unit_value, step_id):
		query = f"INSERT INTO time VALUES('{id}', '{time_unit}', '{time_unit_category}', {time_unit_value}, '{step_id}');"
		return query

	def insert_workflow_case(self, id, legacy_id, name, description):
		query = f"INSERT INTO workflow_case VALUES('{id}', '{legacy_id}', '{name}', '{description}');"
		return query

	def insert_workflow_case(self):
		query = """
	        INSERT INTO workflow_case
	        (id, legacy_id, name, description)
	        VALUES (%s, %s, %s, %s);
	    """
		return query

	def insert_report(self):
		query = """
	        INSERT INTO report
	        (id, report_text, optional_document_url, submission_time_stamp, workflow_case_id, step_id, user_id)
	        VALUES (%s, %s, %s, %s, %s, %s, %s);
	    """
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

	def insert_stepworkflow_casemap(self, step_id, workflow_case_id, status):
		query = f"INSERT INTO stepworkflow_casemap VALUES('{step_id}', '{workflow_case_id}', '{status}');"
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
