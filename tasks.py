from crewai import Task
from tools import yt_tool
from agents import blog_content_researcher, blog_content_writer


#Research Task 

research_task = Task(
    description = (
     """" Identify the video {topic}. \
     Get detailed information about the vudeo from the channel.
     """   
    ),\
    expected_output = "A comprehensive 3 paragraph long report based on the {topic} of video content",
    tool = [yt_tool],
    agent = blog_content_researcher
)

#writing task 
writing_task = Task(
    description = (
        "get the info from the youtube channel on the topic {topic}."
    ),
    expected_output = "Summarize the info from the youtube channel video on the topic {topic} and create the content for the blog.",
    tools = [yt_tool],
    agent = blog_content_writer,
    async_execution = False,
    output_file = "new-blog-post.md"
)