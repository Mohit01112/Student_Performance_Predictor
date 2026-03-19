from groq import Groq
import os
from dotenv import load_dotenv
import yt_dlp

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def get_youtube_video(query):
    """
    Search for the best educational YouTube video for the given query.
    Returns a direct video link.
    """
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "extract_flat": True,
        "default_search": "ytsearch1",
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            results = ydl.extract_info(f"ytsearch1:{query}", download=False)
            if results and 'entries' in results and len(results['entries']) > 0:
                video = results['entries'][0]
                video_url = video.get('url') or video.get('webpage_url')
                
                # Ensure it's a proper YouTube watch link
                if video_url and 'youtube.com' in video_url:
                    return video_url
                elif video.get('id'):
                    return f"https://www.youtube.com/watch?v={video['id']}"
    except Exception as e:
        print(f"Error fetching YouTube video: {e}")
    
    # Fallback: return a search link
    return f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"


def study_assistant(question):
    """
    AI educational assistant that provides focused, relevant answers with YouTube video links.
    """
    
    # Get relevant YouTube video
    youtube_link = get_youtube_video(question)
    
    # Create system prompt with focused instructions
    system_prompt = f"""
You are an AI educational assistant.

Your goal is to answer ONLY what the user asks — no unnecessary information.

Rules:
- If the user asks for explanation → give explanation only
- If the user asks for definition → give short definition
- If the user asks for steps → give steps only
- Do NOT include extra sections like courses, books, or study plan unless explicitly asked

Always:
- Keep the answer simple and clear
- Stay strictly relevant to the question
- Avoid long unnecessary content

Additionally:
- Include ONE relevant YouTube video link at the end
- The link must be clickable and useful for understanding the topic

Format:
Answer:
[Your answer]

YouTube Video:
{youtube_link}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {str(e)}. Please try again."
