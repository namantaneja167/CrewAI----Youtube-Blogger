from crewai import Task
from tools import yt_tool
from agents import blog_researcher,senior_researcher

## Research Task
research_task = Task(
  description=(
    "Write a blog post based on the video content"
  ),
  expected_output='A comprehensive 3 paragraphs long and under 250 words report based on the video content.Use bullet points with proper headings.',
  tools=[yt_tool],
  agent=blog_researcher,
)


review_task = Task(
  description=(
    "Review the blog post and make sure it is accurate and informative. Ask the blog_researcher to make the necessary changes"
  ),
  expected_output='A review of the blog post.A comprehensive 3 paragraphs long and under 250 words report based on the video content.Ask the blog_researcher to make the necessary changes.Use bullet points with proper headings.',
  agent=senior_researcher,
)