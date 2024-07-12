from crewai_tools import YoutubeChannelSearchTool
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@bhancock_ai')