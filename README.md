EE175 Senior Design Project code by Allison Hwang 

# === FILES ===

1. FastenerSorterML.ipynb
       - contains code to train the model from the provided dataset.
2. pic_capture_camera.py
       - takes pictures every time interval, then runs picture through model for image detection and identification.
       - this is what we ended up using for demo/open house
3. real_time_camera.py
       - real-time camera feed that is run through model for image detection and identification.
       - old code before we changed to 2.
4. [fastenersorter](https://drive.google.com/drive/folders/1uJurxp6nRdFV1guRVz9-hfrJKwRSHw9s?usp=sharing) folder 
       - washer, nut, screw dataset
       - dataset we used for demo/open house
5. [archived](https://drive.google.com/drive/folders/194mSxcmr0wEsQ1eHcdYRuZhqXKjjHnB-?usp=sharing) folder
       - screw, nut, nail dataset
       - archived dataset
6. servo.ino
       - Arduino code for the servos and serial communication with the Python files
       - implemented into [Hailey](https://github.com/Hltn95/fastenersorter/blob/main/ServoControlLoadcellOutput.ino) load cell code.
   




# === DIRECTIONS ===

1. Run .ipynb file for model training. Download the "fastenersorter" dataset. Make sure that file directions/locations are changed accordingly.
2. After training the model, download ".../best.pt" file. This is our object detection/identification model.
3. Run with either real_time_camera.py or pic_capture_camera.py, depending on your preferences. (real_time is live camera feed, pic_capture is snapshot)

