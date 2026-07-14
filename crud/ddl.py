


class DDL:

	def  __init__(self, instance_name):
		self.instance_name = instance_name

	def  __str__(self):
		return self.instance_name


	def set_database_connection_object(self, database_connection):
		self.database_connection = database_connection

	def get_DDL(self):
		DDLQueryList = []

		DDLQueryList.append("""
		    CREATE TABLE IF NOT EXISTS workspace(
		        id VARCHAR(50) NOT NULL,
				name VARCHAR(255) NOT NULL,
				description TEXT NOT NULL,
				language VARCHAR(255) NOT NULL,
				organization_type VARCHAR(255) NOT NULL,
				email VARCHAR(255) NOT NULL,
				country VARCHAR(255) NOT NULL,
				PRIMARY KEY(id)
		    );
		""")

		DDLQueryList.append("""
		    CREATE TABLE IF NOT EXISTS workspace_user(
		        id VARCHAR(50) NOT NULL,
				first_name VARCHAR(255) NOT NULL,
				last_name VARCHAR(255) NOT NULL,
				job_title VARCHAR(255) NOT NULL,
				email VARCHAR(255) NOT NULL,
				password VARCHAR(255) NOT NULL,
				workspace_id VARCHAR(50) NOT NULL,
				PRIMARY KEY(id),
				CONSTRAINT FKEY_1_1 FOREIGN KEY(workspace_id) REFERENCES workspace(id) ON UPDATE CASCADE ON DELETE CASCADE
		    );
		""")

		DDLQueryList.append("""
		    CREATE TABLE IF NOT EXISTS role(
		        id VARCHAR(50) NOT NULL,
				name VARCHAR(255) NOT NULL,
				description TEXT NOT NULL,
				PRIMARY KEY(id)
		    );
		""")

		DDLQueryList.append("""
		    CREATE TABLE IF NOT EXISTS privilege(
		        id VARCHAR(50) NOT NULL,
				name VARCHAR(255) NOT NULL,
				description TEXT NOT NULL,
				PRIMARY KEY(id)
		    );
		""")

		DDLQueryList.append("""
		    CREATE TABLE IF NOT EXISTS workflow(
		        id VARCHAR(50) NOT NULL,
				name VARCHAR(255) NOT NULL,
				description TEXT NOT NULL,
				is_mandatory VARCHAR(10) NOT NULL,
				number_of_steps INTEGER NOT NULL,
				status VARCHAR(50) NOT NULL,
				workspace_id VARCHAR(50) NOT NULL,
				PRIMARY KEY(id),
				CONSTRAINT FKEY_1_2 FOREIGN KEY(workspace_id) REFERENCES workspace(id) ON UPDATE CASCADE ON DELETE CASCADE
		    );
		""")

		DDLQueryList.append("""
		    CREATE TABLE IF NOT EXISTS step(
		        id VARCHAR(50) NOT NULL,
				name VARCHAR(255) NOT NULL,
				description TEXT NOT NULL,
				code VARCHAR(10) NOT NULL,
				step_number INTEGER NOT NULL,
				percentage DECIMAL NOT NULL,
				status VARCHAR(50) NOT NULL,
				warning_threshold DECIMAL NOT NULL,
				workflow_id VARCHAR(50) NOT NULL,
				PRIMARY KEY(id),
				CONSTRAINT FKEY_2_0 FOREIGN KEY(workflow_id) REFERENCES workflow(id) ON UPDATE CASCADE ON DELETE CASCADE
		    );
		""")

		DDLQueryList.append("""
		    CREATE TABLE IF NOT EXISTS time(
		        id VARCHAR(50) NOT NULL,
				time_unit VARCHAR(50) NOT NULL,
				time_unit_category VARCHAR(50) NOT NULL,
				time_unit_value DECIMAL NOT NULL,
				step_id VARCHAR(50) NOT NULL,
				PRIMARY KEY(id),
				CONSTRAINT FKEY_3_0 FOREIGN KEY(step_id) REFERENCES step(id) ON UPDATE CASCADE ON DELETE CASCADE
		    );
		""")

		DDLQueryList.append("""
		    CREATE TABLE IF NOT EXISTS workflow_case(
		        id VARCHAR(50) NOT NULL,
				legacy_id VARCHAR(255),
				name VARCHAR(255) NOT NULL,
				description TEXT NOT NULL,
				PRIMARY KEY(id)
		    );
		""")

		DDLQueryList.append("""
		    CREATE TABLE IF NOT EXISTS report(
		        id VARCHAR(50) NOT NULL,
				report_text TEXT,
				optional_document_url TEXT,
				submission_time_stamp VARCHAR(30) NOT NULL,
				workflow_case_id VARCHAR(50) NOT NULL,
				step_id VARCHAR(50) NOT NULL,
				user_id VARCHAR(50) NOT NULL,
				PRIMARY KEY(id),
				CONSTRAINT FKEY_4_0 FOREIGN KEY(workflow_case_id) REFERENCES workflow_case(id) ON UPDATE CASCADE ON DELETE CASCADE,
				CONSTRAINT FKEY_3_1 FOREIGN KEY(step_id) REFERENCES step(id) ON UPDATE CASCADE ON DELETE CASCADE,
				CONSTRAINT FKEY_5_0 FOREIGN KEY(user_id) REFERENCES workspace_user(id) ON UPDATE CASCADE ON DELETE CASCADE
		    );
		""")

		DDLQueryList.append("""
		    CREATE TABLE IF NOT EXISTS workspacerolemap(
			    workspace_id VARCHAR(50) NOT NULL,
				role_id VARCHAR(50) NOT NULL,
				PRIMARY KEY(workspace_id, role_id),
				CONSTRAINT FKEY_1_3 FOREIGN KEY (workspace_id) REFERENCES workspace(id) ON UPDATE CASCADE ON DELETE CASCADE,
				CONSTRAINT FKEY_6_0 FOREIGN KEY (role_id) REFERENCES role(id) ON UPDATE CASCADE ON DELETE CASCADE
			);
		""")

		DDLQueryList.append("""
		    CREATE TABLE IF NOT EXISTS workflowworkflow_casemap(
			    workflow_id VARCHAR(50) NOT NULL,
				workflow_case_id VARCHAR(50) NOT NULL,
				PRIMARY KEY(workflow_id, workflow_case_id),
				CONSTRAINT FKEY_2_1 FOREIGN KEY(workflow_id) REFERENCES workflow(id) ON UPDATE CASCADE ON DELETE CASCADE,
				CONSTRAINT FKEY_4_1 FOREIGN KEY(workflow_case_id) REFERENCES workflow_case(id) ON UPDATE CASCADE ON DELETE CASCADE
			);
		""")

		DDLQueryList.append("""
		    CREATE TABLE IF NOT EXISTS steprolemap(
			    step_id VARCHAR(50) NOT NULL,
				role_id VARCHAR(50) NOT NULL,
				PRIMARY KEY(step_id, role_id),
				CONSTRAINT FKEY_3_2 FOREIGN KEY(step_id) REFERENCES step(id) ON UPDATE CASCADE ON DELETE CASCADE,
				CONSTRAINT FKEY_6_1 FOREIGN KEY(role_id) REFERENCES role(id) ON UPDATE CASCADE ON DELETE CASCADE
			);
		""")

		DDLQueryList.append("""
		    CREATE TABLE IF NOT EXISTS roleprivilegemap(
			    role_id VARCHAR(50) NOT NULL,
				privilege_id VARCHAR(50) NOT NULL,
				PRIMARY KEY(role_id, privilege_id),
				CONSTRAINT FKEY_6_2 FOREIGN KEY(role_id) REFERENCES role(id) ON UPDATE CASCADE ON DELETE CASCADE,
				CONSTRAINT FKEY_7_0 FOREIGN KEY(privilege_id) REFERENCES step(id) ON UPDATE CASCADE ON DELETE CASCADE
			);
		""")

		DDLQueryList.append("""
		    CREATE TABLE IF NOT EXISTS userrolemap(
			    user_id VARCHAR(50) NOT NULL,
				role_id VARCHAR(50) NOT NULL,
				PRIMARY KEY(user_id, role_id),
				CONSTRAINT FKEY_5_1 FOREIGN KEY(user_id) REFERENCES workspace_user(id) ON UPDATE CASCADE ON DELETE CASCADE,
				CONSTRAINT FKEY_6_1 FOREIGN KEY(role_id) REFERENCES role(id) ON UPDATE CASCADE ON DELETE CASCADE
			);
		""")

		DDLQueryList.append("""
		    CREATE TABLE IF NOT EXISTS userstepmap(
			    user_id VARCHAR(50) NOT NULL,
				step_id VARCHAR(50) NOT NULL,
				PRIMARY KEY(user_id, step_id),
				CONSTRAINT FKEY_5_1 FOREIGN KEY(user_id) REFERENCES workspace_user(id) ON UPDATE CASCADE ON DELETE CASCADE,
				CONSTRAINT FKEY_3_3 FOREIGN KEY(step_id) REFERENCES step(id) ON UPDATE CASCADE ON DELETE CASCADE
			);
		""")

		DDLQueryList.append("""
		    CREATE TABLE IF NOT EXISTS stepworkflow_casemap(
			    step_id VARCHAR(50) NOT NULL,
				workflow_case_id VARCHAR(50) NOT NULL,
				PRIMARY KEY(step_id, workflow_case_id),
				CONSTRAINT FKEY_3_2 FOREIGN KEY(step_id) REFERENCES step(id) ON UPDATE CASCADE ON DELETE CASCADE,
				CONSTRAINT FKEY_4_2 FOREIGN KEY(workflow_case_id) REFERENCES workflow_case(id) ON UPDATE CASCADE ON DELETE CASCADE
			);
		""")

		return DDLQueryList




	def generate_DDL(self):
		connection_cursor = self.database_connection.cursor()
		DDLQueryList = self.get_DDL()
		for i in range(0, len(DDLQueryList)):
			connection_cursor.execute(DDLQueryList[i])
		print("Successfully initialized/updated the database relational/physical schema")
		self.database_connection.commit()
		self.database_connection.close()
