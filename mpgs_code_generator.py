import os
from typing import List
import json
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from scrapegraphai.graphs import CodeGeneratorGraph

class Parameter(BaseModel):
    name: str = Field(description="The name of the field")
    description: str = Field(description="The description of the project")
    type: str = Field(description="The type of the field, e.g. 'string', 'int', 'float', 'enum'")
    # parameters: List["Parameter"] = Field(description="The children of the field")


class Parameters(BaseModel):
    parameters: List[Parameter]

graph_config = {
    "llm": {
        # "model": "ollama/mistral",
        "model": "ollama/llama3.2",
        "temperature": 0.7,
        "format": "json",  # Ollama 需要显式指定格式
        "base_url": "http://localhost:11434",  # 设置 Ollama URL
        # "max_tokens": 100000,
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
    "output_file_name": "extra_mpgs_data.py",
}

code_generator_graph = CodeGeneratorGraph(
    prompt="Extract detailed information about the fields (with their children) in both the request body and response body for the following API: 'https://ap-gateway.mastercard.com/api/documentation/apiDocumentation/rest-json/version/100/operation/Transaction:%20%20Authorize.html?locale=en_US'. Expected Output Format: A dictionary containing two keys, 'request_body' and 'response_body', where each key has a value that is another dictionary with the field names as keys and their respective children as values.",
    # 也接受已下载的 HTML 代码的字符串
    source="https://ap-gateway.mastercard.com/api/documentation/apiDocumentation/rest-json/version/100/operation/Transaction:%20%20Authorize.html?locale=en_US",
    schema=Parameters,
    config=graph_config,
)

result = code_generator_graph.run()
json.dumps(result, indent=4)