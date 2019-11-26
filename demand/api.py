import os
from datetime import datetime, timedelta 
import requests
from requests.auth import AuthBase
from settings import (
    DEMAND_API_URL,
    DEMAND_API_CLIENT_ID,
    DEMAND_API_PASSWORD,
    DEMAND_API_USERNAME,
)
auth_state = None

class DemandAuth(AuthBase):
    """Adds proof of authorization to the request."""

    def __call__(self, r):
        """
        updates the token if necessary
        """
        now = datetime.now()
        if not DemandAuth.auth_state or 'token' not in DemandAuth.auth_state or (DemandAuth.auth_state and DemandAuth.auth_state['expires'] < now):
            auth_request = requests.post(
                f"{DEMAND_API_URL}/auth/v1/token/password",
                json={
                    "clientId": DEMAND_API_CLIENT_ID,
                    "password": DEMAND_API_PASSWORD,
                    "username": DEMAND_API_USERNAME,
                }
            )
            auth_response = auth_request.json()
            DemandAuth.auth_state = {
                "token": auth_response['accessToken'],
                "expires": now + timedelta(seconds=auth_response['expiresIn'])
            }
        r.headers['Authorization'] = f"Bearer {DemandAuth.auth_state['token']}"
        return r

# In a real world scenario this should be in a persistent storage...
DemandAuth.auth_state = None

def api_request(method, path, **kwargs):
    return requests.request(
        method, 
        f"{DEMAND_API_URL}{path}",
        auth=DemandAuth(),
        **kwargs
    )

class DemandApi(object):
    @classmethod
    def countries(cls):
        return api_request(
            "GET",
            "/sample/v1/countries?limit=300"
        ).json()

    @classmethod
    def attributes(cls):
        return api_request(
            "GET",
            "/sample/v1/attributes/gb/en?limit=100"
        ).json()

    @classmethod
    def projects(cls):
        return api_request(
            "GET",
            "/sample/v1/projects"
        ).json()

    @classmethod
    def project(cls, ext_project_id):
        return api_request(
            "GET",
            f"/sample/v1/projects/{ext_project_id}"
        ).json()

    @classmethod
    def create_project(cls, json):
        return api_request(
            "POST",
            f"/sample/v1/projects",
            json=json
        ).json()