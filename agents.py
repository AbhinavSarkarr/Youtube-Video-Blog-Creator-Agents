from crewai import Agent
from tools import yt_tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os 

load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')

llm = ChatGroq(
    temperature=0.0,
    model='llama3-70b-8192',
    api_key=os.getenv('GROQ_API_KEY')
)

#Blog Content Researcher Agent
blog_content_researcher = Agent(
    role = "Blog research from Youtube videos",
    goal = "get the related content youtube video for the topic {topic} from Youtube Channel",
    tools = [yt_tool],
    verbose = True,
    llm = llm,
    backstory = (
        "Expert in understanding videos in AI, Data Science, Machine Learning and GEN AI and providing suggestions"
    )
)

#Blog Writer Agent with YT tool
blog_content_writer = Agent(
    role = "Writer",
    goal = "Narrate Compelling tech stories about the video {topic}",
    verbose = True,
    tools = [yt_tool],
    llm = llm,
    backstory = (
        """With a flair for simplifying complex topics, you craft\
        engaging narratives that captivate and educate, bringing new\
        new discoveries to light in an accesible manner."""
    ),
    allow_delegation = False #by default True
) 


