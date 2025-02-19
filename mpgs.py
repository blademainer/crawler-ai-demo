from langchain_core.prompts import *
from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.prompts import *

graph_config = {
    "llm": {
        "model": "ollama/mistral",
        "temperature": 0,
        "format": "json",  # Ollama 需要显式指定格式
        "base_url": "http://localhost:11434",  # 设置 Ollama URL
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://localhost:11434",  # 设置 Ollama URL
    },
    "verbose": True,
}

smart_scraper_graph = SmartScraperGraph(
    prompt="List all the fields of request body and response body for the API",
    # 也接受已下载的 HTML 代码的字符串
    source="https://ap-gateway.mastercard.com/api/documentation/apiDocumentation/rest-json/version/100/operation/Transaction:%20%20Authorize.html?locale=en_US",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)