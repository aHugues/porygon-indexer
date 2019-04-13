import os
from flask import Flask, url_for
import pytest

from web import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

def test_app(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "Flask Dockerized" in str(response.data)