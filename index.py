import face_recognition

# Đọc hình ảnh từ file
image = face_recognition.load_image_file("cc.png")

# Phát hiện các vị trí khuôn mặt trong hình ảnh
face_locations = face_recognition.face_locations(image)

# In ra vị trí của các khuôn mặt được phát hiện
print(f"Có {len(face_locations)} khuôn mặt được phát hiện trong hình.")

for i, face_location in enumerate(face_locations):
    top, right, bottom, left = face_location
    print(f"Khuôn mặt {i+1} ở vị trí Top: {top}, Right: {right}, Bottom: {bottom}, Left: {left}")

# Bạn có thể lưu hình ảnh với khung mặt vào file
from PIL import Image, ImageDraw

# Tạo đối tượng PIL từ hình ảnh
pil_image = Image.fromarray(image)
draw = ImageDraw.Draw(pil_image)

# Vẽ hình chữ nhật xung quanh mỗi khuôn mặt
for (top, right, bottom, left) in face_locations:
    draw.rectangle([(left, top), (right, bottom)], outline=(0, 255, 0), width=2)

# Lưu hình ảnh đã chỉnh sửa
pil_image.save("ccv.jpg")
print("Hình ảnh đã được lưu vào file 'ccv.jpg'")
