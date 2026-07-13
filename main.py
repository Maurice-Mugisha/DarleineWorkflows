import os

from dataclasses import asdict
from includes.ddl_init import DDL_INIT
from datetime import datetime
from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from includes.utility_functions import *

from routes import workspace_route
from routes import workflow_route
from routes import authentication_route
from routes import step_route
from routes import time_route
from routes import workflow_case_route
from routes import role_route
from routes import privilege_route
from routes import report_route
from routes import user_route
from models.login import LoginModel


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Add SessionMiddleware with a strong secret key
# Keep your secret key safe in production using environment variables!
app.add_middleware(SessionMiddleware, secret_key="our-super-secret-key")

@app.get("/")
async def root():
    return {"Message": "Welcome to workflows.com"}

# The database should have already been created
# Ensure that all the database tables have been created
ddl_init_obj = DDL_INIT()
ddl_init_obj.initialize()


# the routes to contain the different endpoints of the application
app.include_router(workspace_route.router)
app.include_router(workflow_route.router)
app.include_router(step_route.router)
app.include_router(time_route.router)
app.include_router(workflow_case_route.router)
app.include_router(role_route.router)
app.include_router(privilege_route.router)
app.include_router(report_route.router)
app.include_router(user_route.router)
app.include_router(authentication_route.router)

initialize_roles()


@app.get("/dashboard")
async def dashboard(loginModel: LoginModel = Depends(get_currently_logged_user_info)):
    """
    A protected route that requires a valid session cookie.
    """
    return {"message": f"Welcome to your dashboard, {loginModel.email}!"}
