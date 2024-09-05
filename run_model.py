import face_recognition
import pickle
import numpy as np
import sys

# Tải mô hình từ file
model_file = "user.pkl"
with open(model_file, 'rb') as f:
    known_face_encodings, known_face_names = pickle.load(f)

# Hàm nhận diện khuôn mặt từ hình ảnh đầu vào
def recognize_face_in_image(input_image_path):
    # Tải ảnh cần nhận diện
    image_to_check = face_recognition.load_image_file(input_image_path)
    
    # Tìm vị trí và mã hóa các khuôn mặt trong ảnh
    face_locations = face_recognition.face_locations(image_to_check)
    face_encodings = face_recognition.face_encodings(image_to_check, face_locations)

    if len(face_locations) == 0:
        return "Không phát hiện được khuôn mặt nào trong hình."
    else:
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # So sánh với khuôn mặt đã huấn luyện
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # Tìm khoảng cách giữa khuôn mặt được phát hiện và khuôn mặt huấn luyện
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            return f"Phát hiện {name} tại vị trí Top: {top}, Right: {right}, Bottom: {bottom}, Left: {left}"

# Nhận diện từ một ảnh thử nghiệm
path_img = sys.stdin.read().strip()
mess = recognize_face_in_image(path_img)
print(mess)
