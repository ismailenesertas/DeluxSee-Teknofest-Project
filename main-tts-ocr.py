import cv2
import pytesseract
import pyttsx3
import numpy as np

# Tesseract yolunu sistemine göre ayarla
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Konuşma hızı
    engine.say(text)
    engine.runAndWait()

def process_image(image):
    # Görüntüyü gri yap
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Eşikleme ile netleştir
    processed = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    return processed

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Kamera açılamadı")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("❌ Kameradan görüntü alınamadı")
                break

            processed = process_image(frame)
            text = pytesseract.image_to_string(processed, lang='tur').strip()

            cv2.imshow('Kamera', frame)
            cv2.imshow('İşlenmiş', processed)

            if text:
                print(f"📝 Tanınan: {text}")
                text_to_speech(text)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("⏹ Çıkılıyor...")
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
