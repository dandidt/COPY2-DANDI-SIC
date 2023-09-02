import os
import numpy as np
import face_recognition

# Path ke folder dataset yang berisi gambar-gambar wajah
dataset_path = "dataset/"

# List untuk menyimpan data latih
face_encodings = []
face_ids = []

for filename in os.listdir(dataset_path):
    if filename.endswith(".jpg"):
        parts = filename.split(".")
        if len(parts) == 4 and parts[0] == "User":
            face_id = parts[1]  # Menggunakan string sebagai ID pengguna
            face_image = face_recognition.load_image_file(os.path.join(dataset_path, filename))
            face_encoding = face_recognition.face_encodings(face_image)[0]
            face_encodings.append(face_encoding)
            face_ids.append(face_id)
        else:
            print(f"File {filename} tidak sesuai format, dilewati.")

# Membuat array numpy dari data latih
face_encodings = np.array(face_encodings)
face_ids = np.array(face_ids)

# Simpan data latih ke dalam file numpy
np.save("face_encodings.npy", face_encodings)
np.save("face_ids.npy", face_ids)

print("Data latih telah disimpan.")
