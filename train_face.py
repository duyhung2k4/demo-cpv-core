import face_recognition
import os
import pickle

# Đường dẫn đến thư mục chứa ảnh của người cần nhận diện
train_faces_dir = "train_faces/obama"

# Danh sách lưu trữ mã hóa khuôn mặt và tên
face_encodings = []
face_names = []

# Duyệt qua các tệp ảnh trong thư mục huấn luyện
for image_name in os.listdir(train_faces_dir):
    image_path = os.path.join(train_faces_dir, image_name)
    
    # Tải ảnh và mã hóa khuôn mặt
    image = face_recognition.load_image_file(image_path)
    encoding = face_recognition.face_encodings(image)[0]
    
    # Lưu mã hóa vào danh sách
    face_encodings.append(encoding)
    face_names.append("obama")  # Tên của người cần nhận diện

# Lưu mô hình (các mã hóa khuôn mặt) vào tệp
model_file = "user.pkl"
with open(model_file, 'wb') as f:
    pickle.dump((face_encodings, face_names), f)

print(f"Mô hình đã được lưu vào file '{model_file}'")
