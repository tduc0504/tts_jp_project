import pyttsx3

# Khởi tạo engine
engine = pyttsx3.init()

# Chọn giọng nữ Nhật Haruka hoặc Ayumi
voices = engine.getProperty('voices')
selected = False
for v in voices:
    if "Haruka" in v.name or "Ayumi" in v.name:
        engine.setProperty('voice', v.id)
        selected = True
        break

if not selected:
    print("Không tìm thấy giọng Haruka/Ayumi, dùng giọng mặc định.")

# Giảm tốc độ đọc
engine.setProperty('rate', 130)  # mặc định ~200

# Đọc file input.txt
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

engine.save_to_file(text, "output.mp3")
engine.runAndWait()

print("Hoàn thành! Kiểm tra file output.mp3")
