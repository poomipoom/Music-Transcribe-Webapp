
import whisper
import os
from deep_translator import GoogleTranslator  # ใช้ deep_translator แทน

def transcribe_audio(audio_path, output_dir="static/subtitles"):
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # โหลดโมเดล Whisper
        model = whisper.load_model("small")  # หรือ "base" เพื่อความเร็ว
        print("Model loaded successfully.")
        
        # ถอดเสียงจากไฟล์เสียงและตรวจจับภาษาอัตโนมัติ
        result = model.transcribe(audio_path)  # ไม่กำหนด language, Whisper จะตรวจจับภาษาจากเสียง
        segments = result["segments"]
        
        # สร้างชื่อไฟล์ SRT จากชื่อไฟล์เสียง
        basename = os.path.splitext(os.path.basename(audio_path))[0]
        srt_path = os.path.join(output_dir, f"{basename}.srt")

        # สร้างตัวแปลภาษา
        detected_language = result["language"]  # ภาษาที่ Whisper ตรวจจับ
        print(f"Detected language: {detected_language}")

        with open(srt_path, "w", encoding="utf-8") as f:
            for i, seg in enumerate(segments, 1):
                start = whisper.utils.format_timestamp(seg["start"])
                end = whisper.utils.format_timestamp(seg["end"])
                text_original = seg["text"].strip()  # ข้อความที่ถอดเสียง
                
                # แปลข้อความจากภาษาที่ตรวจจับเป็นภาษาอังกฤษ
                text_translated = GoogleTranslator(source=detected_language, target='en').translate(text_original)
                f.write(f"{i}\n{start} --> {end}\n{text_translated}\n\n")
        
        print(f"SRT file saved at: {srt_path}")
        return srt_path
    except Exception as e:
        print(f"Error during transcription or translation: {e}")
        return None


