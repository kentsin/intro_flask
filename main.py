#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-07-24 08:38:48
# @Author  : kentsin (kentsin@gmail.com)
# @Link    : link
# @Version : 0.0.1

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class Msg(BaseModel):
    msg: str

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/name")
async def name(name: str):
    return {"message": "name %" % name}

@app.get("/path/{path_id}")
async def func_demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint"}