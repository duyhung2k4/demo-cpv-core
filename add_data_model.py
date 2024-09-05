import face_recognition
import pickle
import os

# Tải mô hình hiện có từ file
model_file = "user.pkl"
with open(model_file, 'rb') as f:
    known_face_encodings, known_face_names = pickle.load(f)

# Hàm để thêm nhiều người mới từ thư mục
def add_new_faces_from_directory(directory_path, new_name):
    # Lặp qua tất cả các file ảnh trong thư mục
    for image_file in os.listdir(directory_path):
        image_path = os.path.join(directory_path, image_file)
        
        # Tải ảnh và mã hóa khuôn mặt
        new_image = face_recognition.load_image_file(image_path)
        new_face_encodings = face_recognition.face_encodings(new_image)
        
        if len(new_face_encodings) > 0:
            # Lấy mã hóa khuôn mặt đầu tiên
            new_face_encoding = new_face_encodings[0]
            
            # Thêm mã hóa khuôn mặt và tên vào mô hình hiện có
            known_face_encodings.append(new_face_encoding)
            known_face_names.append(new_name)
            
            print(f"Đã thêm khuôn mặt từ {image_file} vào mô hình.")
        else:
            print(f"Không tìm thấy khuôn mặt trong {image_file}.")
    
    # Lưu lại mô hình đã cập nhật vào file
    with open(model_file, 'wb') as f:
        pickle.dump((known_face_encodings, known_face_names), f)
    
    print(f"Đã thêm tất cả các ảnh từ thư mục {directory_path} vào mô hình.")

# Thêm tất cả ảnh từ thư mục train_faces_obama vào mô hình
directory_path = "train_faces/trump"
new_name = "Trump"  # Tên của người mới
add_new_faces_from_directory(directory_path, new_name)
