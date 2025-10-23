import streamlit as st
import pandas as pd
import plotly.express as px
from utils import fetch_youtube_comments, analyze_emotions, generate_wordcloud

st.set_page_config(page_title="🎬 YouTube Emotion Dashboard", layout="wide")
st.title("🎭 YouTube Emotion Analysis Dashboard")
st.write("Discover the emotional tone behind YouTube comments — joy, anger, sadness, and more!")

video_url = st.text_input("📺 Enter YouTube Video URL (e.g., https://www.youtube.com/watch?v=dQw4w9WgXcQ)")

limit = st.slider("Select number of comments to analyze", 10, 200, 50)

if st.button("🎯 Analyze Emotions"):
    if not video_url.strip():
        st.error("Please enter a valid YouTube video URL.")
    else:
        with st.spinner("Fetching comments and analyzing emotions..."):
            try:
                df = fetch_youtube_comments(video_url, limit)
                df = analyze_emotions(df)

                st.success(f"Fetched and analyzed {len(df)} comments successfully!")

                st.subheader("🗨️ Sample Comments with Emotions")
                for i, row in df.head(10).iterrows():
                    st.write(f"{row['emoji']} **{row['emotion'].capitalize()}** — {row['comment']}")

                emotion_counts = df['emotion'].value_counts().reset_index()
                emotion_counts.columns = ['Emotion', 'Count']
                fig = px.bar(emotion_counts, x='Emotion', y='Count', color='Emotion', title="Emotion Distribution")
                st.plotly_chart(fig, use_container_width=True)

                st.subheader("☁️ Word Cloud of Comments")
                wordcloud_img = generate_wordcloud(df)
                st.image(wordcloud_img, use_container_width=True)

            except Exception as e:
                st.error(f"An error occurred: {e}")
