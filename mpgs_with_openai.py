import json
import os

from scrapegraphai.graphs import SmartScraperGraph

# 从环境变量中获取 OpenAI API Key
openai_api_key = os.getenv("OPENAI_API_KEY")

graph_config = {
    "llm": {
        "api_key": openai_api_key,
        "model": "openai/gpt-4o-mini",
    },
    "tts_model": {
        "api_key": openai_api_key,
        "model": "tts-1",
        "voice": "alloy"
    },
    "output_path": "audio_summary.mp3",
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
