import cv2
import os

# Menginisialisasi kamera dengan nomor 0 (kamera utama)
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # Mengatur lebar video
cam.set(4, 480)  # Mengatur tinggi video

# Membuat folder dataset jika belum ada
if not os.path.exists("dataset"):
    os.makedirs("dataset")

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Meminta pengguna memasukkan ID numerik untuk pengenalan wajah
face_id = input('\n Masukkan ID pengguna dan tekan <return> ==> ')

print("\n [INFO] Menginisialisasi pengambilan gambar wajah. Hadapkan kamera dan tunggu ...")

count = 0

while True:
    ret, img = cam.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        count += 1
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h, x:x+w])
        cv2.imshow('image', img)
    
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    elif count >= 10:
        break

print("\n [INFO] Keluar dari pengambilan gambar. Membersihkan...")
cam.release()
cv2.destroyAllWindows()
