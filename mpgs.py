from langchain_core.prompts import *
from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.prompts import *
import json

graph_config = {
    "llm": {
        "model": "ollama/llama3.2",
        "temperature": 0,
        "format": "json",  # Ollama 需要显式指定格式
        "base_url": "http://localhost:11434",  # 设置 Ollama URL
        "max_tokens": 1000000,
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://localhost:11434",  # 设置 Ollama URL
    },
    "verbose": True,
}

smart_scraper_graph = SmartScraperGraph(
    prompt="Extract detailed information about the fields (with their children) in both the request body and response body for the following API: 'https://ap-gateway.mastercard.com/api/documentation/apiDocumentation/rest-json/version/100/operation/Transaction:%20%20Authorize.html?locale=en_US'. Expected Output Format: A dictionary containing two keys, 'request_body' and 'response_body', where each key has a value that is another dictionary with the field names as keys and their respective children as values.",
    # 也接受已下载的 HTML 代码的字符串
    source="https://ap-gateway.mastercard.com/api/documentation/apiDocumentation/rest-json/version/100/operation/Transaction:%20%20Authorize.html?locale=en_US",
    config=graph_config
)

result = smart_scraper_graph.run()
json.dump(result, open("mpgs_api_fields.json", "w"), indent=4)