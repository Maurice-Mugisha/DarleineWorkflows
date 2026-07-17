


class Update:

	def  __init__(self, instance_name):
		self.instance_name = instance_name

	def  __str__(self):
		return self.instance_name


	def update_workspace(self):
		query = f"""
		           UPDATE
				       workspace
				   SET
				       name = %s,
					   description = %s,
					   language = %s,
					   organization_type = %s,
					   email = %s,
					   country = %s
				   WHERE
					   id = %s
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

	def update_workflow(self):
		query = f"""
		           UPDATE
				       workflow
				   SET
				       name = %s,
					   description = %s,
					   is_mandatory = %s,
					   number_of_steps = %s,
					   status = %s
				   WHERE
					   id = %s
				""";
		return query

	def update_step(self):
		query = f"""
		           UPDATE
				       step
				   SET
				       name = %s,
					   description = %s,
					   code = %s,
					   step_number = %s,
					   percentage = %s,
					   status = %s,
					   warning_threshold = %s
				   WHERE
					   id = %s
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

	def update_workflow_case(self):
		query = f"""
		           UPDATE
				       workflow_case
				   SET
				       legacy_id = %s,
					   name = %s,
					   description = %s
				   WHERE
					   id = %s
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


	def update_report(self):
		query = f"""
		           UPDATE
				       report
				   SET
				       report_text = %s,
					   optional_document_url = %s
				   WHERE
					   id = %s
				""";
		return query
