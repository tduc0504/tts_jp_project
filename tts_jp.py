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
engine.setProperty('rate', 130)  # <200 là chậm hơn

# Nhập văn bản từ người dùng
text = input("Nhập văn bản tiếng Nhật muốn đọc: ")

# Tạo file mp3
output_file = "output.mp3"
engine.save_to_file(text, output_file)
engine.runAndWait()

print(f"Hoàn thành! File âm thanh đã được tạo: {output_file}")
