import pyautogui
import pytesseract
import cv2
import numpy as np
from PIL import ImageGrab
import time

# Ganti dengan path ke tesseract.exe di PC kamu
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# SETTING:
target_multiplier = 2.0  # Target cairkan di multiplier berapa
multiplier_region = (600, 300, 200, 100)  # Atur area multiplier (x, y, width, height)
button_position = (700, 800)  # Posisi tombol "Cairkan"

def get_multiplier(region):
    img = ImageGrab.grab(bbox=region)
    img_np = np.array(img)
    gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, config='--psm 7')
    try:
        text = text.lower().replace('x', '').replace('o', '0')
        multiplier = float(text.strip())
        return multiplier
    except:
        return None

print("Bot dimulai... Tekan Ctrl+C untuk berhenti.")

while True:
    multiplier = get_multiplier(multiplier_region)
    if multiplier:
        print(f"Multiplier sekarang: {multiplier}")
        if multiplier >= target_multiplier:
            print("TARGET TERCAPAI! Klik tombol cairkan.")
            pyautogui.click(button_position)
            break
    time.sleep(0.1)
