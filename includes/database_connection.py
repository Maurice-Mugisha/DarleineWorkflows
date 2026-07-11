import psycopg2
import psycopg2.extras


class DatabaseConnection:


    database_connection_object = None
    auth_credentials_file_name = ""


    def __init__(self, auth_credentials_file_name):
        self.set_auth_credentials_file_name(auth_credentials_file_name)
        credentials_dictionary = self.read_auth_file()
        database_name = credentials_dictionary["database"]
        host_ip = credentials_dictionary["host"]
        database_user = credentials_dictionary["user"]
        user_password = credentials_dictionary["password"]
        database_port = credentials_dictionary["port"]
        self.database_connection_object = psycopg2.connect(database=database_name, host=host_ip, user=database_user, password=user_password, port=database_port)


    def set_auth_credentials_file_name(self, auth_credentials_file_name):
        self.auth_credentials_file_name = auth_credentials_file_name


    def get_database_connection_object(self):
        return self.database_connection_object


    def read_auth_file(self):
        credentials_dictionary = {}
        auth_file = open(self.auth_credentials_file_name, "r")

        for line in auth_file:
            line_word_list = line.replace("\n", "").split("=#=")
            if len(line_word_list) > 1:
                credentials_dictionary[line_word_list[0]] = line_word_list[1]
            else:
                continue
        auth_file.close()
        return credentials_dictionary
