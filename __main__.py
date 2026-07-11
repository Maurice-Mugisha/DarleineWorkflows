import os

from includes.database_connection import DatabaseConnection
from crud.ddl import DDL
from crud.selection import Select
from includes.date_time import DateTimeProvider
from includes.country import Country
from includes.country_phone_code import Country
from includes.business_logic_functions import *
from datetime import datetime
import json

import time
from datetime import datetime




selection_object = Select("Umucyo selection object 1")

# Client continent
client_continent = "Africa"

# Client country name
client_country_name = "Rwanda"

# Client capital city
client_capital_city = "Kigali"

# Date and timezone relative to a particular country
timezone_string = client_continent + os.sep + client_capital_city
date_and_time_object = DateTimeProvider(timezone_string)


authentication_directory = "auth"
authentication_file = "auth.txt"
auth_credentials_file_name = authentication_directory + os.sep + authentication_file
database_connection_facility = DatabaseConnection(auth_credentials_file_name)
database_connection_object = database_connection_facility.get_database_connection_object()

query_executor = database_connection_object

ddl_obj = DDL(query_executor)
ddl_obj.generate_DDL()
