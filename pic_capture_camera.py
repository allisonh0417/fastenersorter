import time
import os
import glob
import subprocess
import serial
from ultralytics import YOLO
import cv2

image_folder = "ee175/pics"
output_file = "ee175/detected_objects.txt"
yolo_model = "/home/deathstarv3/ee175/best.pt"  #yolo model <--- PUT CORRECT FILE DIRECTION

arduino = serial.Serial("/dev/ttyACM0", 9600, timeout=1) #fix /dev/... if necessary
model = YOLO("/home/deathstarv3/ee175/best.pt")

while True:
    timestamp = time.strftime("%Y%m%d_%H%M%S") #timestamp
    image_path = os.path.join(image_folder, f"image_{timestamp}.jpg")
    annotated_path = os.path.join(image_folder, f"annotated_{timestamp}.jpg")

    subprocess.run(["libcamera-still", "-o", image_path, "--width", "800", "--height", "480"]) #take pic
    print(f"Captured: {image_path}")

    results = model(image_path)

    detected_objects = set()
    for result in results:
        for box in result.boxes:
            obj_name = result.names[int(box.cls)]  
            detected_objects.add(obj_name)

    if detected_objects:
        with open(output_file, "a") as f:  
            for obj in detected_objects:
                log_entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {obj} detected\n"
                f.write(log_entry)
                print(log_entry.strip())  # debug
                
                arduino.write(f"{obj}\n".encode()) #send to arduino
                
    image = cv2.imread(image_path)
    annotate = results[0].plot()
    
    cv2.imwrite(annotated_path, annotate)
    print(f"Annotated img saved: {annotated_path}")
    
    #subprocess.run(["DISPLAY=:1","feh", "--geometry", "800x480", annotated_path])
    process1= subprocess.Popen(["feh","--fullscreen",annotated_path]) #display on screen the annotated photo
    time.sleep(2)
    subprocess.run(["pkill","feh"])

    time.sleep(5)
