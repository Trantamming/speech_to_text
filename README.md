HUONG DAN CAC BUOC THUC HIEN DE "CHUYEN CLIP AM THANH THANH VAN BAN (SPEECH TO TEXT)"

1. Download Visual Studio Code tại website: https://code.visualstudio.com/
   -> Thực hiện cài đặt 

2. Cai dat python voi download tai https://www.python.org/downloads/release/python-3100/

3. Cai dat CUDA va cuDNN (danh cho cac dong may tinh co ho tro GPU cua NVDIA)
   -> Download CUDA Toolkit tại https://developer.nvidia.com/cuda-downloads. Tim version thich hop de download. Sau khi tai xong, tien hanh cai dat
   -> Dowload cuDNN tai https://developer.nvidia.com/search?facet.subcollection[]=Developer%20Zone&facet.subcollection[]=Developer%20Forums&facet.subcollection[]=Technical%20Blog&page=1&sort=relevance&term=cudnn. Tim version thich hop tien hanh cai dat

4. Download package FFmpeg tại https://www.ffmpeg.org/download.html
   -> Thuc hien install: 
      + Giai nen bang phan mem 7zip hoac WinRAR, winzip
      + Dat thu muc da giai nen cua FFmpeg vao ổ đĩa nào bạn muốn. Ví dụ: C:\ffmpeg
      + add "C:\ffmpeg\bin" vao PATH

5. Cai dat packagage openai-whisper : pip install openai-whisper

6. Cai dat goi PyTorch ho tro CUDA bang dong lenh tren Terminal hoac PowerShell:
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

7. Chuan bi file am thanh dinh dang .mp3 luu vao thu muc lam viec

8. Mo Visual Studio Code (VS Code) tao file speech_to_text.py va nhap vao chuong trinh sau: 

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


9. Chạy file với dòng lệnh: python -u speech_to_text.py   

10. Xem lai ket qua output xuat ra tren Terminal hoac mo file result.txt voi phan mem Notepad chang ban de xem
