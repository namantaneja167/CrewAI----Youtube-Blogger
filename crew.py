from crewai import Crew,Process
from agents import blog_researcher,senior_researcher
from tasks import research_task,review_task

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[blog_researcher,senior_researcher],
  tasks=[research_task,review_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

## start the task execution process with enhanced feedback
result=crew.kickoff(inputs={'link':'https://www.youtube.com/watch?v=qcqlbf27CWg'})
print(result)