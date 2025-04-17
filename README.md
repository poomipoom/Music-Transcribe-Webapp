# 🎵 Music Transcribe Webapp

เว็บแอปสำหรับแปลงเสียงจากวิดีโอ YouTube เป็นซับไตเติล พร้อมแปลภาษาได้อัตโนมัติ

---

## 📦 วิธีติดตั้ง

1. โคลนโปรเจกต์

```bash
git clone https://github.com/poomipoom/Music-Transcribe-Webapp.git
cd Music-Transcribe-Webapp
```

2. ติดตั้ง dependencies

```bash
pip install -r requirements.txt
```

3. รันแอป

```bash
python app.py
```

แล้วเปิดเบราว์เซอร์ไปที่ `http://127.0.0.1:5000`

---

## 🚀 การใช้งาน

- กรอกลิงก์ YouTube ที่ต้องการ
- เลือกภาษาที่ต้องการแปล (รองรับญี่ปุ่น → อังกฤษ)
- ระบบจะประมวลผล แล้วแสดงวิดีโอพร้อมคำบรรยายแปล

---

## 🗂️ โฟลเดอร์สำคัญ

- `templates/` – HTML Template
- `static/subtitles/` – เก็บซับไตเติล
- `downloads/` – เก็บไฟล์เสียง
- `utils/` – รวมฟังก์ชันแยกย่อย (ถอดเสียง, แปล, ดาวน์โหลด)

---

## 🧠 เทคโนโลยีที่ใช้

- Flask
- Whisper by OpenAI
- Pytube
- Deep Translator

---

## 👤 ผู้พัฒนา

**Poomipoom**  
นักศึกษาวิศวกรรม AI

---

## 📝 หมายเหตุ

- ระบบรองรับการประมวลผลเฉพาะคลิป YouTube ที่ *เปิดสาธารณะ* เท่านั้น
- จะลบไฟล์ subtitle/audio เก่าอัตโนมัติเมื่อมีการอัปโหลดใหม่
