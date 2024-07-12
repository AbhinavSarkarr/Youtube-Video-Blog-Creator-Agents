from crewai import Crew, Process
from agents import blog_content_researcher, blog_content_writer
from tasks import research_task, writing_task



crew = Crew(
    agents= [blog_content_researcher, blog_content_writer],
    tasks = [research_task, writing_task],
    process= Process.sequential,
    memory=True,
    cache = True,
    max_rpm=100,
    share_crew=True
)

#Start the task execution process with feedback 

result = crew.kickoff(inputs={'topic': 'CrewAI Tutorial: Complete Crash Course for Beginners'})
print(result)