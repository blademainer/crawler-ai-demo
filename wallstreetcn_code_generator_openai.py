import os
from typing import List
import json
from dotenv import load_dotenv
from pydantic import BaseModel, Field, model_validator
from pydantic import root_validator
from scrapegraphai.graphs import CodeGeneratorGraph
from dotenv import load_dotenv

class Post(BaseModel):
    title: str = Field(description="The title of the post")
    description: str = Field(description="The description of the post")
    content: str = Field(description="The content of the post")


class News(BaseModel):
    news: List[Post]

load_dotenv()

# 从环境变量中获取 OpenAI API Key
openai_api_key = os.getenv("OPENAI_API_KEY")

print(f"openai_api_key: {openai_api_key}")

graph_config = {
    "llm": {
        "api_key": openai_api_key,
        "model": "openai/gpt-4o-mini",
        "max_tokens": 4000,
    },
    "verbose": True,
    "headless": True,
    "reduction": 2,
    "library": "beautifulsoup",
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
    prompt="获取华尔街见闻下资讯栏目下的新闻标题、描述和内容",
    # 也接受已下载的 HTML 代码的字符串
    source="https://api-one-wscn.awtmt.com/apiv1/content/information-flow?channel=global&accept=article&cursor=&limit=20&action=upglide",
    schema=News,
    config=graph_config,
)

result = code_generator_graph.run()
json.dumps(result, indent=4)