import logging

from fastapi import APIRouter, status, Response, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

import requests

router = APIRouter()
