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
    prompt="获取华尔街见闻下资讯栏目下的新闻标题、描述和内容",
    # 也接受已下载的 HTML 代码的字符串
    source="https://wallstreetcn.com/news/global",
    config=graph_config,
)

result = smart_scraper_graph.run()
json.dump(result, open("wallstreetcn_posts.json", "w"), indent=4)
