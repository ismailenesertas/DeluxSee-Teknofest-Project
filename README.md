
# 🦯 DeluxSee

**Smart Wearable Assistant for the Visually Impaired**  
TEKNOFEST 2025 • Accessibility & Innovation Project

---

## 📌 About the Project

**DeluxSee** is a smart wearable device developed to support visually impaired individuals in their daily lives. Equipped with sensors and AI-powered software, the system detects obstacles, recognizes printed text, and provides real-time voice feedback to the user. It stands out with its **portable, low-cost, and user-friendly** design.

> “Developed with empathy, empowered by innovation.”

---

## 🚀 Key Features

- 🔊 **Obstacle Detection**: Real-time alerts using ultrasonic and infrared sensors  
- 📷 **Camera-Based OCR**: Detects printed Turkish text  
- 🧠 **AI-Based Reading**: EasyOCR or TrOCR integration  
- 🗣️ **Voice Feedback**: Real-time text-to-speech (TTS) output  
- ⚠️ **Emergency Button (Optional)**: Triggers a help request  
- 🧩 **Modular Hardware**: Wearable like glasses, lightweight and practical

---

## 👥 Team Members

**DeluxSee Teknofest Team**

| Name                | Role                    |
|---------------------|--------------------------|
| Ahmet Burak İşleyen | Team Leader - Developer  |
| İsmail Enes Ertaş   | Software Developer       |
| Havvagül Şener      | Hardware Specialist      |
| Hejar Aslan         | System Integration       |
| Dilara Boz          | Testing                  |
| Gülfidan Çakmak     | System Integration       |

---

## 🔧 Installation

### 1. Install Dependencies

**For EasyOCR users:**

```bash
sudo apt update && sudo apt upgrade
sudo apt install python3-pip
pip install opencv-python easyocr numpy playsound
```

**To use TrOCR instead of EasyOCR:**

```bash
pip install torch torchvision torchaudio
pip install transformers
```

---

## ▶️ Run the Project

```bash
python3 main.py
```

---

## 🧪 How to Use

1. Mount the smart glasses on your head  
2. Once powered, the system activates the camera  
3. Obstacles are detected and voice alerts are given  
4. Detected text is read aloud via OCR and TTS  
5. (Optional) Emergency button can trigger help requests

---

## 📁 Project Structure

```
DeluxSee/
├── main.py               # Main application script
├── ocr/                  # OCR modules (EasyOCR / TrOCR)
├── tts/                  # Text-to-Speech module
├── sensors/              # Obstacle detection sensor code
├── hardware/             # Circuit diagrams and documentation
├── assets/               # Audio files, sample images
└── README.md             # Project documentation
```

---

## ⚙️ Technologies Used

- Python 3
- OpenCV
- EasyOCR / TrOCR
- PyTorch, Transformers
- gTTS, pyttsx3 (Text-to-Speech)
- Raspberry Pi / ESP32
- Ultrasonic and IR sensors
- Camera module
- Mini speaker or earphones

---

## 🤝 Contributing

We welcome contributions to this project!  
You can:  
- Report bugs  
- Suggest new features  
- Submit pull requests  

We also welcome collaborations with NGOs or initiatives working on accessibility and assistive technologies.

---


> © 2025 • DeluxSee Team – All rights reserved.
