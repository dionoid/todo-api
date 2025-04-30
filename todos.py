# from aiohttp import web
# from aiohttp.web import RouteTableDef
# from pydantic import BaseModel, Field
# from typing import List, Optional
# from uuid import uuid4, UUID
# from datetime import datetime, timedelta
# from enum import Enum
# import json
# import os

# # Define the enum for todo status
# class StatusEnum(str, Enum):
#     TODO = "TODO"
#     IN_PROGRESS = "IN_PROGRESS"
#     DONE = "DONE"

# # Pydantic model for a Todo item
# class Todo(BaseModel):
#     id: UUID = Field(...)
#     title: str = Field(...)
#     description: Optional[str] = Field(None)
#     status: StatusEnum = Field(...)
#     due_date: Optional[datetime] = Field(None)
#     created_at: datetime = Field(...)
#     updated_at: datetime = Field(...)

# # In-memory storage for todos, prepopulated with some data
# todos: List[Todo] = [
#     Todo(
#         id=uuid4(),
#         title="Plan Weekend Getaway",
#         description="Research and book a cozy cabin in the mountains for a relaxing weekend getaway. Make a list of activities to do and pack essentials for the trip.",
#         status=StatusEnum.TODO,
#         due_date=None,
#         created_at=datetime.now(),
#         updated_at=datetime.now()
#     ),
#     Todo(
#         id=uuid4(),
#         title="Organize Workspace",
#         description="Sort and arrange all files and documents in the office to improve efficiency.",
#         status=StatusEnum.TODO,
#         due_date=None,
#         created_at=datetime.now(),
#         updated_at=datetime.now()
#     ),
#     Todo(
#         id=uuid4(),
#         title="Explore New Coffee Shop",
#         description="Visit the new coffee shop that opened downtown.",
#         status=StatusEnum.TODO,
#         due_date=None,
#         created_at=datetime.now(),
#         updated_at=datetime.now()
#     ),
#     Todo(
#         id=uuid4(),
#         title="Read a Book",
#         description="Read 10 pages of any book.",
#         status=StatusEnum.IN_PROGRESS,
#         due_date=datetime.now() - timedelta(days=3),
#         created_at=datetime.now(),
#         updated_at=datetime.now()
#     ),
#     Todo(
#         id=uuid4(),
#         title="Buy Groceries",
#         description="Get milk, eggs, bread from store.",
#         status=StatusEnum.IN_PROGRESS,
#         due_date=datetime.now() + timedelta(days=7),
#         created_at=datetime.now(),
#         updated_at=datetime.now()
#     ),
#     Todo(
#         id=uuid4(),
#         title="Check Emails",
#         description="Go through inbox and respond to important emails.",
#         status=StatusEnum.DONE,
#         due_date=datetime.now() - timedelta(days=5),
#         created_at=datetime.now(),
#         updated_at=datetime.now()
#     )
# ]

# # Handler to get all todos
# async def get_todos(request: web.Request) -> web.Response:
#     result = [todo.model_dump(mode='json') for todo in todos]
#     return web.json_response(result)

# # Handler to serve openapi.json file
# async def get_openapi(request: web.Request) -> web.Response:
#     openapi_path = os.path.join(os.path.dirname(__file__), "openapi.json")
#     with open(openapi_path, "r") as f:
#         data = json.load(f)
#     return web.json_response(data)

# async def get_help_guide(request: web.Request) -> web.Response:
#     help_guide_path = os.path.join(os.path.dirname(__file__), "help_guide.html")
#     with open(help_guide_path, "r") as f:
#         data = f.read()
#     return web.Response(text=data, content_type='text/html')

# def setup_todo_routes(routes: RouteTableDef):
#     routes.get('/api/todos')(get_todos)
#     routes.get('/api/openapi.json')(get_openapi)
#     routes.get('/help_guide')(get_help_guide)
