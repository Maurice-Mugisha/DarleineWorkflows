import os

from includes.database_connection import DatabaseConnection
from crud.ddl import DDL
from includes.date_time import DateTimeProvider

class DDL_INIT:

    def initialize(self):
        client_continent = "Africa"    # Client continent
        client_country_name = "Rwanda" # Client country name
        client_capital_city = "Kigali" # Client capital city

        # Date and timezone relative to a particular country
        timezone_string = client_continent + os.sep + client_capital_city
        date_and_time_object = DateTimeProvider(timezone_string)


        authentication_directory = "auth"
        authentication_file = "auth.txt"
        auth_credentials_file_name = authentication_directory + os.sep + authentication_file
        database_connection_facility = DatabaseConnection(auth_credentials_file_name)
        database_connection_object = database_connection_facility.get_database_connection_object()

        query_executor = database_connection_object

        ddl_obj = DDL("Workflows Platform")
        ddl_obj.set_database_connection_object(query_executor)
        ddl_obj.generate_DDL()
