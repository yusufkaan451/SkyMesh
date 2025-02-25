import cv2
import os
import time

def capture_image(destination_path):
    # Belirtilen hedef dizinin var olup olmadığını kontrol et
    if not os.path.isdir(destination_path):
        print(f"Hedef dizin '{destination_path}' bulunamadı!")
        return

    # Kamerayı aç (varsayılan cihaz: /dev/video0)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Kameraya erişilemiyor!")
        return

    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Görüntü alınamadı!")
        return

    # Dosya adını zaman damgasıyla belirle
    timestamp = int(time.time())
    dest_file = os.path.join(destination_path, f"captured_{timestamp}.jpg")

    # Görüntüyü hedef dizine kaydet
    try:
        cv2.imwrite(dest_file, frame)
        print(f"Görüntü {dest_file} adresine kaydedildi.")
    except Exception as e:
        print(f"Dosya kaydedilirken hata oluştu: {e}")

if __name__ == "__main__":
    # Fotoğrafın kaydedileceği dizin
    destination_path = '/home/pi/Desktop'  # SD_kart dizinine kaydedilecek
    capture_image(destination_path)
