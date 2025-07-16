# DeluxSee-Teknofest-Project
🕶️ DeluxSee: Wearable Smart Assistant for the Visually Impaired
DeluxSee is a wearable smart assistant designed to help visually impaired individuals navigate their daily lives more safely and independently. Developed as part of the TEKNOFEST 2025 Barrier-Free Living Technologies Competition, the project integrates sensor-based obstacle detection and real-time text recognition using a camera system.

🎯 Project Goal
DeluxSee aims to support visually impaired users by:

Detecting nearby obstacles

Providing real-time voice guidance

Reading printed or digital text aloud via OCR

Alerting users in emergency situations

All of these features are embedded into a smart glasses design powered by Raspberry Pi.

🧠 Key Features
📷 Camera-Based Real-Time OCR: Reads printed or digital text aloud using EasyOCR or TrOCR.

🦺 Ultrasonic Obstacle Detection: Warns the user through audio or vibration feedback.

🔊 Voice Feedback System: Describes the environment using audio output.

⚡ Portable Design: Runs on a lightweight Raspberry Pi system powered by a rechargeable battery.

🔧 Technologies Used
Raspberry Pi 4

Python, OpenCV, EasyOCR / TrOCR

Ultrasonic sensors (HC-SR04)

USB Camera

Speakers / Audio Module

Portable Power Supply (Powerbank / Li-ion Battery)

👥 Team Members
DeluxSee Teknofest Team

Ahmet Burak İşleyen (Team Leader)
İsmail Enes Ertaş
Havvagül Şener
Hejar Aslan
Dilara Boz

Gülfidan Çakmak

⚙️ Installation
Requirements
Raspberry Pi 4 (Raspbian OS recommended)

Python 3.8+

USB Camera or Pi Camera

HC-SR04 Ultrasonic Sensor

Speaker or headphones

Powerbank or portable battery

Install Dependencies

sudo apt update && sudo apt upgrade
sudo apt install python3-pip
pip install opencv-python easyocr numpy playsound
If using TrOCR instead of EasyOCR:

pip install torch torchvision torchaudio
pip install transformers
Run the Project
bash
python3 main.py
🧪 How to Use
Mount the smart glasses on your head.

Once powered, the system starts processing the camera input.

Nearby obstacles will trigger voice alerts.

Detected text will be read aloud using OCR.

Optional emergency alert button or voice command features can be included.

