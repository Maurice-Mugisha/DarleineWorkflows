


class Update:

	def  __init__(self, instance_name):
		self.instance_name = instance_name

	def  __str__(self):
		return self.instance_name


	def update_workspace(self, id, name, description, language, organization_type, email, country):
		query = f"""
		           UPDATE
				       workspace
				   SET
				       name = '{name}',
					   description = '{description}',
					   language = '{language}',
					   organization_type = '{organization_type}',
					   email = '{email}',
					   country = '{country}'
				   WHERE
					   id = '{id}'
				""";
		return query

	def update_role(self, id, name, description):
		query = f"""
		           UPDATE
				       role
				   SET
				       name = '{name}',
					   description = '{description}',
				   WHERE
					   id = '{id}'
				""";
		return query


	def update_privilege(self, id, name, description):
		query = f"""
		           UPDATE
				       privilege
				   SET
				       name = '{name}',
					   description = '{description}',
				   WHERE
					   id = '{id}'
				""";
		return query

	def update_user(self, id, first_name, last_name, job_title, email, password):
		query = f"""
		           UPDATE
				       workspace_user
				   SET
				       first_name = '{first_name}',
					   last_name = '{last_name}',
					   job_title = '{job_title}',
					   email = '{email}',
					   password = '{password}'
				   WHERE
					   id = '{id}'
				""";
		return query

	def update_workflow(self, id, name, description, is_mandatory, number_of_steps, status):
		query = f"""
		           UPDATE
				       workflow
				   SET
				       name = '{name}',
					   description = '{description}',
					   is_mandatory = '{is_mandatory}',
					   number_of_steps = {number_of_steps},
					   status = '{status}'
				   WHERE
					   id = '{id}'
				""";
		return query

	def update_step(self, id, name, description, code, step_number, percentage, status, warning_threshold):
		query = f"""
		           UPDATE
				       step
				   SET
				       name = '{name}',
					   description = '{description}',
					   code = '{code}',
					   step_number = {step_number},
					   percentage = {percentage},
					   status = '{status}',
					   warning_threshold = '{warning_threshold}'
				   WHERE
					   id = '{id}'
				""";
		return query


	def update_time(self, id, time_unit, time_unit_category, time_unit_value):
		query = f"""
		           UPDATE
				       time
				   SET
				       time_unit = '{time_unit}',
					   time_unit_category = '{time_unit_category}',
					   time_unit_value = {time_unit_value}
				   WHERE
					   id = '{id}'
				""";
		return query

	def update_workflow_case(self, id, legacy_id, name, description):
		query = f"""
		           UPDATE
				       workflow_case
				   SET
				       legacy_id = '{legacy_id}',
					   name = '{name}',
					   description = '{description}'
				   WHERE
					   id = '{id}'
				""";
		return query


	def update_stepworkflow_casemap(self, workflow_case_id, step_id, status):
		query = f"""
				   UPDATE
					   stepworkflow_casemap
				   SET
					   status = '{status}'
				   WHERE
					   workflow_case_id = '{workflow_case_id}'
				   AND
					   step_id = '{step_id}'
				""";
		return query
		

	def update_report(self, id, report_text, optional_document_url):
		query = f"""
		           UPDATE
				       report
				   SET
				       report_text = '{report_text}',
					   optional_document_url = '{optional_document_url}'
				   WHERE
					   id = '{id}'
				""";
		return query
