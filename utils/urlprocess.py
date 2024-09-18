import os
import requests
from urllib.parse import urlparse
from utils.support import get_file_extension
from utils.fileprocess import read_file_pdf
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    """
    Retrieves the transcript text from a YouTube video.

    Args:
        video_id (str): The ID of the YouTube video.

    Returns:
        str: The transcript text or an error message.
    """
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['vi', 'en'])
        transcript_text = " ".join([entry['text'] for entry in transcript])
        return transcript_text
    except Exception as e:
        return f"Error: {str(e)}"

def get_content(response: requests.Response, type: str) -> str:
    if type=='pdf':
        file_path = os.path.join('uploads','temporary.pdf')
        with open(file_path, 'wb') as file:
            file.write(response.content)
        content = read_file_pdf(file_path)
        os.remove(file_path)
        return content
    elif type=='txt':
        return response.text
    elif type=='youtube-video':
        transcript = get_transcript(urlparse(response.url).query[2:])
        return transcript

class URL:
    def __init__(self, response: requests.Response) -> None:
        self.parsed_url = urlparse(response.url)
        self.type = 'youtube-video' if '/watch' in self.parsed_url.path else get_file_extension(self.parsed_url.path)[1:] if get_file_extension(self.parsed_url.path)[1:] in ('pdf','txt') else None
        self.content = get_content(response, self.type)