EE175 Senior Design Project code by Allison Hwang 

# === FILES ===

1. FastenerSorterML.ipynb<br />
       - contains code to train the model from the provided dataset.<br />
2. pic_capture_camera.py<br />
       - takes pictures every time interval, then runs picture through model for image detection and identification.<br />
       - this is what we ended up using for demo/open house<br />
3. real_time_camera.py<br />
       - real-time camera feed that is run through model for image detection and identification.<br />
       - old code before we changed to 2.<br />
4. [fastenersorter](https://drive.google.com/drive/folders/1uJurxp6nRdFV1guRVz9-hfrJKwRSHw9s?usp=sharing) folder <br />
       - washer, nut, screw dataset<br />
       - dataset we used for demo/open house<br />
5. [archived](https://drive.google.com/drive/folders/194mSxcmr0wEsQ1eHcdYRuZhqXKjjHnB-?usp=sharing) folder<br />
       - screw, nut, nail dataset<br />
       - archived dataset<br />
6. servo.ino<br />
       - Arduino code for the servos and serial communication with the Python files<br />
       - implemented into [Hailey](https://github.com/Hltn95/fastenersorter/blob/main/ServoControlLoadcellOutput.ino) load cell code.<br />
   




# === DIRECTIONS ===<br />

1. Run .ipynb file for model training. Download the "fastenersorter" dataset. Make sure that file directions/locations are changed accordingly.<br />
2. After training the model, download ".../best.pt" file. This is our object detection/identification model.<br />
3. Run with either real_time_camera.py or pic_capture_camera.py, depending on your preferences. (real_time is live camera feed, pic_capture is snapshot)<br />

