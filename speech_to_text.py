import whisper

# Tải mô hình Whisper và sử dụng GPU nếu có
model = whisper.load_model("base").to("cuda")

# Chuyển đổi âm thanh thành văn bản
result = model.transcribe("2025_3_10_29_5_990_13.mp3")

# In kết quả
print(result["text"])


# Lưu kết quả vào file result.txt
with open("result.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

# In thông báo hoàn tất
print("Kết quả đã được lưu vào result.txt")
