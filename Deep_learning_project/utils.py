import re
import pandas as pd
from googleapiclient.discovery import build
from transformers import pipeline
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
import base64
import os

emotion_model = pipeline(
    "text-classification", 
    model="j-hartmann/emotion-english-distilroberta-base", 
    return_all_scores=False
)

EMOJI_MAP = {
    "joy": "😄",
    "sadness": "😢",
    "anger": "😡",
    "fear": "😨",
    "surprise": "😲",
    "disgust": "🤢",
    "neutral": "😐"
}

#Enter API
API_KEY = "Enter your API_key"

def extract_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    return match.group(1) if match else None

def fetch_youtube_comments(video_url, limit=50):
    if not API_KEY:
        raise ValueError("YouTube API key not set! Please paste it in utils.py or set as environment variable.")

    video_id = extract_video_id(video_url)
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    comments = []
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=min(limit, 100),
        textFormat='plainText'
    )
    response = request.execute()

    for item in response.get('items', []):
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    df = pd.DataFrame(comments, columns=["comment"])
    return df

def analyze_emotions(df):
    df["emotion"] = df["comment"].apply(lambda x: emotion_model(x)[0]['label'].lower())
    df["emoji"] = df["emotion"].map(EMOJI_MAP).fillna("😐")
    return df

def generate_wordcloud(df):
    text = " ".join(df["comment"].astype(str).tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    buffer = io.BytesIO()
    plt.figure(figsize=(8, 4))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(buffer, format="png")
    plt.close()
    buffer.seek(0)

    encoded_image = base64.b64encode(buffer.read()).decode()
    return f"data:image/png;base64,{encoded_image}"
