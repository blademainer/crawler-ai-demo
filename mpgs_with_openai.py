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
}

smart_scraper_graph = SmartScraperGraph(
    prompt="List all the fields of request body and response body for the API",
    # 也接受已下载的 HTML 代码的字符串
    source="https://ap-gateway.mastercard.com/api/documentation/apiDocumentation/rest-json/version/100/operation/Transaction:%20%20Authorize.html?locale=en_US",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)