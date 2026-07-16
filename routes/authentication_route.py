import os
from fastapi import FastAPI, Request, Depends
from fastapi import APIRouter

from dataclasses import asdict
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from includes.utility_functions import *
from models.login import LoginModel
from models.authenticated_user import AuthenticatedUserModel


router = APIRouter(prefix="/authentication", tags=["authentication"])


@router.post("/login", response_model = AuthenticatedUserModel)
async def login(request: Request, loginModel: LoginModel):
    """
    Simulates a login endpoint.
    In production, validate passwords before updating the session.
    """
    # Store user identity directly inside the secure session cookie
    email = loginModel.email
    authenticated_user, role_list = get_specific_authenticated_user_by_email(email)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    request.session["user"] = asdict(authenticated_user)
    request.session["roles"] = role_list
    send_email(
        "Login confirmation",
        authenticated_user.first_name,
        authenticated_user.email,
        "This is to inform you that your workflows account has been logged into. If this is not you, please report the incident"
    )
    return authenticated_user


@router.post("/logout")
async def logout(request: Request):
    """
    Clears the session dictionary, removing the authentication state.
    """
    if not request.session or len(request.session) == 0:
        return {"message": f"Already logged out"}
    authenticatedUserModel = AuthenticatedUserModel(**request.session["user"])
    request.session.clear()
    return {"message": f"Successfully logged out as {authenticatedUserModel.email}"}
