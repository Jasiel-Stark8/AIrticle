from flask import Flask, request
from api.v1.views import auth
from api.v1.views import autosave
from api.v1.views import gpt
from app import app, db
