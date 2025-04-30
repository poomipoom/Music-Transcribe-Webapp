from flask import Flask, render_template, request, redirect, url_for
from utils.youtube_downloader import download_audio
from utils.speech_to_text import transcribe_audio
from utils.translate_srt import translate_srt, srt_to_vtt
from urllib.parse import urlparse, parse_qs
import os
import time

app = Flask(__name__)

import os
import glob

def cleanup_sub_files(folder="static/subtitles", extensions=[".vtt", ".srt", ".mp3", ".wav"]):
    deleted = 0
    for ext in extensions:
        for file_path in glob.glob(os.path.join(folder, f"*{ext}")):
            try:
                os.remove(file_path)
                deleted += 1
            except Exception as e:
                print(f"❌ Failed to delete {file_path}: {e}")
    print(f"🧹 Deleted {deleted} old subtitle/audio files.")

def cleanup_mp3_files(folder="D:\Miniproject\Music-transcribe\dowloads", extensions=[".vtt", ".srt", ".mp3", ".wav"]):
    deleted = 0
    for ext in extensions:
        for file_path in glob.glob(os.path.join(folder, f"*{ext}")):
            try:
                os.remove(file_path)
                deleted += 1
            except Exception as e:
                print(f"❌ Failed to delete {file_path}: {e}")
    print(f"🧹 Deleted {deleted} old subtitle/audio files.")


# ดึง video_id จาก YouTube URL
def extract_video_id(youtube_url):
    parsed_url = urlparse(youtube_url)
    if parsed_url.hostname == "youtu.be":
        return parsed_url.path[1:]
    elif parsed_url.hostname in ("www.youtube.com", "youtube.com"):
        if parsed_url.path == "/watch":
            return parse_qs(parsed_url.query).get("v", [None])[0]
    return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    
# download
    
    # transcribe
    
    # translate
    

    cleanup_mp3_files()
    cleanup_sub_files()

    url = request.form["youtube_url"]
    lang = request.form["target_lang"]
    t1 = time.perf_counter()
    audio_path = download_audio(url)
    t2 = time.perf_counter()
    srt_path = transcribe_audio(audio_path)
    t3 = time.perf_counter()
    if srt_path is None:
        return "Error during transcription.", 500
    translated_srt_path = translate_srt(srt_path, lang)
    t4 = time.perf_counter()
    vtt_path = srt_to_vtt(translated_srt_path)
    print(f"⏱️ download: {t2 - t1:.2f}s")
    print(f"⏱️ transcribe: {t3 - t2:.2f}s")
    print(f"⏱️ translate: {t4 - t3:.2f}s")

    # Extract video ID
    # ดึง video_id จาก url เช่น https://www.youtube.com/watch?v=xxxx
    from urllib.parse import urlparse, parse_qs
    video_id = parse_qs(urlparse(url).query).get("v", [""])[0]

    return redirect(url_for("show_result", video_id=extract_video_id(url), vtt_path=os.path.basename(vtt_path)))


@app.route("/result")
def show_result():
    video_id = request.args.get("video_id")
    vtt_path = request.args.get("vtt_path")
    return render_template("result.html", video_id=video_id, vtt_path=vtt_path)

if __name__ == "__main__":
    app.run(debug=True)
