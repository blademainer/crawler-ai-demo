import os
from typing import List
import json
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from scrapegraphai.graphs import CodeGeneratorGraph


# ************************************************
# Define the output schema for the graph
# ************************************************


class Project(BaseModel):
    title: str = Field(description="The title of the project")
    description: str = Field(description="The description of the project")


class Projects(BaseModel):
    projects: List[Project]


graph_config = {
    "llm": {
        # "model": "ollama/deepseek-r1:32b",
        # "model": "ollama/llama3.2",
        "model": "ollama/mistral",
        # "temperature": 0.7,
        "format": "json",  # Ollama 需要显式指定格式
        "base_url": "http://localhost:11434",  # 设置 Ollama URL
        # "max_tokens": 5000,
    },
    "verbose": True,
    "headless": True,
    "reduction": 2,
    "max_iterations": {
        "overall": 10,
        "syntax": 3,
        "execution": 3,
        "validation": 3,
        "semantic": 3,
    },
    "output_file_name": "extra_projects_data.py",
}

code_generator_graph = CodeGeneratorGraph(
    prompt="List me all the projects with their description",
    source="https://perinim.github.io/projects/",
    schema=Projects,
    config=graph_config,
)

result = code_generator_graph.run()
json.dumps(result, indent=4)