from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()
# current_model_name  = "llama3.1:8b-instruct-q4_1"
# llm = ChatOpenAI(model=current_model_name, base_url='http://127.0.0.1:11434/v1')


blog_researcher=Agent(
    role='Blog Writer from Youtube Videos',
    goal='Write a blog post based on the video content. Use the tools provided to get the video content',
    verbose=True,
    backstory=(
       "Expert in understanding videos from youtube" 
    ),
    tools=[yt_tool],
    allow_delegation=False,
    # llm=llm
)


senior_researcher=Agent(
    role='Senior Reviewer',
    goal='Review the blog post wriiten by blog_researcher based on the video content. Check it for accuracy and informativity. Ask the blog_researcher to make the necessary changes',
    verbose=True,
    backstory=(
       "Expert in reviewing blogs and checking for accuracy and informativity" 
    ),
    # tools=[yt_tool],
    allow_delegation=True,
    # llm=llm
)