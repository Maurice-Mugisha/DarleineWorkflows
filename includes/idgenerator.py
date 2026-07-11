import datetime
import pytz
import random



class IDGenerator:


	def __init__(self, continent, city):
		self.continent = continent
		self.city = city

	def get_generic_id(self):
		datetime_object = datetime.datetime.now()
		relative_time_zone_string = self.continent + "/" + self.city
		relative_time_zone = pytz.timezone(relative_time_zone_string)
		datetime_object = relative_time_zone.localize(datetime_object)
		return datetime_object.strftime("%Y-%m-%d") + " " + datetime_object.strftime("%T:%M:%p")


	def set_time_zone_continent(self, continent):
		self.continent = continent


	def set_time_zone_city(self, city):
		self.city = city


	# Set the domain to minimize stochastic induction for small domains (probability theory of random numbers)
	# Failure to do this may lead to key generation failures under large events that can be greater than or equal to the sample space (actually, even less)
	# The sample space in this case has been appropriately set)
	def get_random_number(self):
		start = 0
		end = 70000
		random_number = random.randint(start, end)
		return str(random_number)

	def generate_random_id(self):
		key_column = self.get_generic_id() + " " + self.get_random_number()
		return key_column



	def generate_workspace_id(self):
		entity_name = "WORKSPACE"
		workspace_id = entity_name + " " + self.get_generic_id() + " " + self.get_random_number()
		return workspace_id


	def generate_role_id(self):
		entity_name = "ROLE"
		role_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return role_id


	def generate_privilege_id(self):
		entity_name = "PRIVILEGE"
		privilege_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return privilege_id


	def generate_user_id(self):
		entity_name = "USER"
		user_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return user_id


	def generate_workflow_id(self):
		entity_name = "WORKFLOW"
		workflow_id = entity_name + " " + self.get_generic_id() + " " + self.get_random_number()
		return workflow_id


	def generate_step_id(self):
		entity_name = "STEP"
		step_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return step_id


	def generate_time_id(self):
		entity_name = "TIME"
		time_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return time_id


	def generate_workflow_case_id(self):
		entity_name = "WORKFLOW_CASE"
		workflow_case_id = entity_name + " " + self.get_generic_id() + " " + self.get_random_number()
		return workflow_case_id


	def generate_report_id(self):
		entity_name = "REPORT"
		report_id = entity_name[:3] + " " + self.get_generic_id() + " " + self.get_random_number()
		return report_id





# End of class file
