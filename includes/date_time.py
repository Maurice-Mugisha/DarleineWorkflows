import datetime
import pytz



class DateTimeProvider:


	# Python instance variables
	month_end_dictionary = {"1":31, "2":29, "3":31, "4":30, "5":31, "6":30, "7":31, "8":31, "9":30, "10":31, "11":30, "12":31}
	next_month_dictionary = {"1":2, "2":3, "3":4, "4":5, "5":6, "6":7, "7":8, "8":9, "9":10, "10":11, "11":12, "12":1}


	def __init__(self, timezone_string):
		self.timezone_string = timezone_string

	def set_time_zone(self, set_timezone):
		self.set_timezone = set_timezone


	def get_relative_date_object(self):
		datetime_object = datetime.datetime.now()
		relative_time_zone_string = self.timezone_string
		relative_time_zone = pytz.timezone(relative_time_zone_string)
		datetime_object = relative_time_zone.localize(datetime_object)
		return datetime_object
	

	def get_date(self):
		datetime_object = self.get_relative_date_object()
		return datetime_object.strftime("%Y-%m-%d")
	

	def get_time(self):
		datetime_object = self.get_relative_date_object()
		return datetime_object.strftime("%T:%M:%p")
	

	def get_date_and_time(self):
		datetime_object = self.get_relative_date_object()
		return datetime_object.strftime("%Y-%m-%d") + " " + datetime_object.strftime("%T:%M:%p")
	

	def get_relative_readable_date(self):
		datetime_object = self.get_relative_date_object()
		return datetime_object.strftime("%B %d, %Y")
	

	def get_relative_readable_date_and_time(self):
		datetime_object = self.get_relative_date_object()
		return datetime_object.strftime("%c")
	

	def get_relative_date_from_now(self, number_of_days):

		date_time_object = self.get_relative_date_object()
		year = date_time_object.year
		month = date_time_object.month
		day = date_time_object.day
		date = str(year) + "-" + str(month) + "-" + str(day)
		current_month_end = self.month_end_dictionary[str(month)]
		excess = 0
		sum = number_of_days + day

		if sum > current_month_end:

			excess = number_of_days + day - current_month_end

			while excess > 0:

				next_month = self.next_month_dictionary[str(month)]
				next_month_days = self.month_end_dictionary[str(month)]

				if month > next_month:
					year = year + 1

				if (excess - next_month_days) > 0:
					month = next_month
					excess = excess - next_month_days
				else:
					day = excess
					date = str(year) + "-" + str(next_month) + "-" + str(excess)
					break
		else:
			date = str(year) + "-" + str(month) + "-" + str((number_of_days + day))

		return date
	




# End of class file