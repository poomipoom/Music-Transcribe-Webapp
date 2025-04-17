import yt_dlp
import os
import uuid


def download_audio(youtube_url, output_dir="dowloads", ffmpeg_path="C:/ffmpeg/bin/ffmpeg.exe"):
    import os
    import uuid
    os.makedirs(output_dir, exist_ok=True)
    audio_filename = f"{uuid.uuid4()}"
    output_path = os.path.join(output_dir, audio_filename)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': ffmpeg_path,
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

        
    final_audio_path = output_path + ".mp3"

    if not os.path.exists(final_audio_path):
        raise FileNotFoundError(f"⚠️ ไม่พบไฟล์ mp3 ที่: {final_audio_path}")
    
    print(f"✅ ไฟล์เสียงดาวน์โหลดสำเร็จที่: {final_audio_path}")
    return final_audio_path
