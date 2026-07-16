import os

from fastapi import Request, HTTPException
import json
from psycopg2.extensions import adapt

from crud.insert import Insert
from crud.selection import Select
from crud.update import Update
from crud.delete import Delete
from includes.database_connection import DatabaseConnection
from includes.idgenerator import IDGenerator
from includes.business_logic_functions import *
from models.authenticated_user import AuthenticatedUserModel
from models.role import RoleModel

import smtplib
import ssl
from email.message import EmailMessage


def get_database_utility_tuple():
    query_executor = get_query_executor()
    selection_object = get_selection_object()
    insertion_object = get_insertion_object()
    update_object = get_update_object()
    deletion_object = get_deletion_object()
    database_utility_tuple = (query_executor, insertion_object, selection_object, update_object, deletion_object)
    return database_utility_tuple

def get_query_executor():
    auth_credentials_file_name = get_authentication_file_name()
    database_connection_facility = DatabaseConnection(auth_credentials_file_name)
    database_connection_object = database_connection_facility.get_database_connection_object()
    query_executor = database_connection_object
    return query_executor

def get_insertion_object():
    insertion_object = Insert("workflows system insertion object")
    return insertion_object

def get_selection_object():
    selection_object = Select("Workflows system selection object")
    return selection_object

def get_update_object():
    update_object = Update("Workflows system update object")
    return update_object

def get_deletion_object():
    deletion_object = Delete("Workflows system deletion object")
    return deletion_object

def get_authentication_file_name():
    authentication_directory = "auth"
    authentication_file = "auth.txt"
    auth_credentials_file_name = authentication_directory + os.sep + authentication_file
    return auth_credentials_file_name

def initialize_roles():
    user_dictionary = {}
    query_executor, insertion_object, selection_object, _, _ = get_database_utility_tuple()
    role_model_list = []
    with open("data/roles.json") as file:
        role_data = json.load(file)
        role_model_list = [RoleModel(**role_dictionary) for role_dictionary in role_data]
    saved_role_list = get_roles(query_executor, selection_object)

    if not saved_role_list or len(saved_role_list) == 0:
        idgenerator_obj = IDGenerator("Africa", "Kigali")
        query_executor, insertion_object, selection_object, _, _ = get_database_utility_tuple() # connection initially closed already, open it up again
        connection_cursor = query_executor.cursor()
        for roleModel in role_model_list:
            role_id = idgenerator_obj.generate_role_id()
            role_query = insertion_object.insert_role(role_id, roleModel.name, roleModel.description)
            connection_cursor.execute(role_query)
        query_executor.commit()
        query_executor.close()


def get_specific_authenticated_user_by_email(email):
    user_dictionary = {}
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    user_dictionary = get_specific_user_by_email(selection_object, query_executor, email)
    authenticated_user = AuthenticatedUserModel(**user_dictionary)
    query_executor, _, selection_object, _, _ = get_database_utility_tuple()
    role_list = get_specific_user_roles(query_executor, selection_object, user_dictionary["id"])
    if len(role_list) > 0:
        authenticated_user.roles = role_list
    else:
        authenticated_user.roles = []

    return (authenticated_user, role_list)


# Helper function to enforce authentication across routes
def get_currently_logged_user_info(request: Request):
    user = request.session.get("user")
    if not user:
        raise HTTPException(status_code=401, detail="You must be authenticated to access this information")
    authenticatedUserModel = AuthenticatedUserModel(**user)
    return authenticatedUserModel


def escape_postgres_string(value: str) -> str:
    """
    Escapes a string value using psycopg2's native adapting engine.
    """
    if value is None:
        return "NULL"

    # adapt() handles single quotes, backslashes, and null bytes
    adapted_value = adapt(value)

    # Returns the properly quoted and escaped string
    return adapted_value.getquoted().decode('utf-8')



def send_email(subject, first_name, recipient_email, message):
    # 1. Define your email credentials and details
    sender_email = "mugmau25@gmail.com"
    sender_password = "zxpe uihn vbzn zcen"  # Use an App Password, NOT your master password!
    if recipient_email is None or len(recipient_email) == 0:
        return

    # 2. Setup the email content
    messageObject = EmailMessage()
    messageObject["Subject"] = subject
    messageObject["From"] = sender_email
    messageObject["To"] = recipient_email
    messageObject.add_alternative(
        format_email_message(subject, first_name, message),
        subtype="html"
    )

    # 3. Create a secure SSL context and send the email
    context = ssl.create_default_context()

    try:
        # Connect via SSL to port 465 (or use port 587 with starttls)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, sender_password)
            server.send_message(messageObject)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

def format_email_message(subject, first_name, message):
    html_content = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{subject}</title>
</head>
<body style="margin:0; padding:20px; background-color:#f4f7fa; font-family:Arial, Helvetica, sans-serif; color:#333333;">

    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="max-width:600px; margin:0 auto; background:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 2px 8px rgba(0,0,0,0.08);">

        <!-- Header -->
        <tr>
            <td style="background:#2563eb; padding:24px; text-align:center;">
                <h2 style="margin:0; color:#ffffff; font-size:24px;">
                    {subject}
                </h2>
            </td>
        </tr>

        <!-- Body -->
        <tr>
            <td style="padding:32px;">
                <p style="margin:0 0 20px; font-size:16px;">
                    Dear <strong>{first_name}</strong>,
                </p>

                <div style="font-size:16px; line-height:1.7; color:#444444;">
                    {message}
                </div>

                <p style="margin-top:32px;">
                    Kind regards,
                </p>

                <p style="margin:0; font-weight:bold; color:#2563eb;">
                    Workflows Team
                </p>

                <p style="margin:4px 0 0; color:#666666; font-size:14px;">
                    Customer Service
                </p>
            </td>
        </tr>

        <!-- Footer -->
        <tr>
            <td style="background:#f8f9fc; padding:18px; text-align:center; color:#888888; font-size:12px; border-top:1px solid #eeeeee;">
                This is an automated email. Please do not reply directly to this message.
            </td>
        </tr>

    </table>

</body>
</html>
"""
    return html_content
