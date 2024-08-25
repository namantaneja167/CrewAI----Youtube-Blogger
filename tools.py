from crewai_tools import YoutubeVideoSearchTool
from dotenv import load_dotenv
import os

load_dotenv()

yt_tool = YoutubeVideoSearchTool(
    # config=dict(
    #     llm=dict(
    #         provider="ollama", # or google, openai, anthropic, llama2, ...
    #         config=dict(
    #             model="llama3.1:8b-instruct-q4_1",
    #             base_url = 'http://127.0.0.1:11434/v1',
    #             # temperature=0.5,
    #             # top_p=1,
    #             # stream=true,
    #         ),
    #     ),
    #     embedder=dict(
    #         provider="ollama", # or openai, ollama, ...
    #         config=dict(
    #             model="llama3.1:8b-instruct-q4_1",
    #             base_url = 'http://127.0.0.1:11434/v1',
    #             # task_type="retrieval_document",
    #             # title="Embeddings",
    #         ),
    #     ),
    # ),
    youtube_video_url='https://www.youtube.com/watch?v=qcqlbf27CWg'
)
