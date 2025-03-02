import requests
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

def get_video_transcript(video_id):
    """Fetches subtitles from a YouTube video"""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([t["text"] for t in transcript])
        return text
    except Exception as e:
        return f"Error: {e}"

def summarize_text(text):
    """Summarizes text using AI"""
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]["summary_text"]

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    video_id = video_url.split("v=")[1].split("&")[0]
    
    print("[*] Fetching transcript...")
    transcript = get_video_transcript(video_id)
    
    if "Error" not in transcript:
        print("[*] Generating summary...")
        summary = summarize_text(transcript)
        print("\n🔹 Summary:\n", summary)
    else:
        print(transcript)
