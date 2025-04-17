from deep_translator import GoogleTranslator
import os

def translate_srt(input_path, target_lang='th', output_dir="static/subtitles"):
    os.makedirs(output_dir, exist_ok=True)

    # สร้างชื่อไฟล์ใหม่
    base = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(output_dir, f"{base}_translated_{target_lang}.srt")

    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    translated_lines = []
    for line in lines:
        if line.strip().isdigit() or '-->' in line or line.strip() == "":
            translated_lines.append(line)
        else:
            translated = GoogleTranslator(source='auto', target=target_lang).translate(line.strip())
            translated_lines.append(translated + '\n')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(translated_lines)

    return output_path

def srt_to_vtt(srt_path):
    vtt_path = srt_path.replace(".srt", ".vtt")
    with open(srt_path, "r", encoding="utf-8") as srt_file:
        lines = srt_file.readlines()

    with open(vtt_path, "w", encoding="utf-8") as vtt_file:
        vtt_file.write("WEBVTT\n\n")
        for line in lines:
            if "-->" in line:
                line = line.replace(",", ".")  # VTT ใช้ . แทน ,
                # เพิ่ม 00: หากไม่มีชั่วโมง
                time_start, time_end = line.split(" --> ")
                time_start = "00:" + time_start
                time_end = "00:" + time_end
                vtt_file.write(f"{time_start} --> {time_end}\n")
            else:
                vtt_file.write(line)

    return vtt_path



