import cv2
import easyocr
import numpy as np
import pyttsx3
import time
from PIL import Image, ImageEnhance


# Türkçe seslendirme motoru ayarları
def setup_tts():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Ses hızı

    # Türkçe ses (Tolga) için özel arama
    voices = engine.getProperty('voices')
    turkish_voice = None

    print("Mevcut sesler:")
    for voice in voices:
        print(f"- {voice.name} (ID: {voice.id})")
        if 'Tolga' in voice.name:
            turkish_voice = voice.id
            print(">>> Tolga sesi bulundu!")

    if turkish_voice:
        engine.setProperty('voice', turkish_voice)
        print("Tolga sesi başarıyla ayarlandı")
    else:
        print("Uyarı: Tolga sesi bulunamadı. Alternatif Türkçe ses aranıyor...")
        for voice in voices:
            if 'turkish' in voice.name.lower() or 'tr_' in voice.id:
                engine.setProperty('voice', voice.id)
                print(f"Alternatif Türkçe ses kullanılıyor: {voice.name}")
                break

    return engine


# Görüntü işleme optimizasyonu
def enhance_image(img):
    # Kontrast artırma
    pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    enhancer = ImageEnhance.Contrast(pil_img)
    contrast_img = enhancer.enhance(1.5)

    # Keskinlik artırma
    enhancer = ImageEnhance.Sharpness(contrast_img)
    sharp_img = enhancer.enhance(2.0)

    # Parlaklık ayarı
    enhancer = ImageEnhance.Brightness(sharp_img)
    final_img = enhancer.enhance(1.1)

    return cv2.cvtColor(np.array(final_img), cv2.COLOR_RGB2BGR)


# Ana uygulama
def main():
    # EasyOCR okuyucusunu başlat (Türkçe için)
    reader = easyocr.Reader(['tr'], gpu=False)  # GPU kullanmak için True yapın

    # Kamera başlat
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Hata: Kamera bağlantısı kurulamadı!")
        return

    # Ses motorunu başlat
    tts_engine = setup_tts()

    # Test mesajı
    tts_engine.say("Easy O C R sistemi başlatıldı")
    tts_engine.runAndWait()

    print("Sistem hazır. Metni okutmak için 'r' tuşuna basın. Çıkmak için 'q' tuşuna basın.")

    last_read_time = 0
    read_cooldown = 5  # Okumalar arası minimum bekleme süresi (saniye)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Kameradan görüntü alınamıyor")
            break

        # Görüntüyü göster
        cv2.imshow("EasyOCR - Metin Okuma", frame)

        key = cv2.waitKey(1) & 0xFF

        # 'r' tuşu ile metni oku
        current_time = time.time()
        if key == ord('r') and (current_time - last_read_time) > read_cooldown:
            last_read_time = current_time

            # Görüntüyü iyileştir
            enhanced_frame = enhance_image(frame)

            # Görüntüyü kaydet (isteğe bağlı)
            cv2.imwrite("last_capture.jpg", enhanced_frame)

            # OCR ile metni oku
            results = reader.readtext(enhanced_frame, paragraph=True)

            # Algılanan metinleri birleştir
            detected_text = " ".join([result[1] for result in results])

            if detected_text:
                print(f"Algılanan Metin: {detected_text}")

                # İşlenmiş görüntüyü göster
                cv2.imshow("İşlenmiş Görüntü", enhanced_frame)

                # Metni seslendir
                tts_engine.say(detected_text)
                tts_engine.runAndWait()
            else:
                print("Metin algılanamadı")
                tts_engine.say("Metin algılanamadı")
                tts_engine.runAndWait()

        # Çıkış için 'q' tuşu
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()