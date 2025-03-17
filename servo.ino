#include <Servo.h>
Servo myservo; 
Servo a;
Servo b;
Servo c;
Servo d;
int pos = 0;    
String receivedData = "";
void setup() {
    Serial.begin(9600);  
    myservo.attach(9);  
    a.attach(8);
    b.attach(7);
    c.attach(6);
    //receivedData = "bolt";
    a.write(0);
    b.write(0);
    c.write(0);
    myservo.write(0);
}
void loop() {
  a.write(0);
  b.write(0);
  c.write(0);
  myservo.write(0);
    if (Serial.available()) {
        receivedData = Serial.readStringUntil('\n');  
        receivedData.trim();  
        Serial.print("Received: ");
        Serial.println(receivedData);
        receivedData.toLowerCase();
        if (receivedData.indexOf("washer") != -1) {  // If "bolt" is found anywhere
            Serial.println("Washer detected!");
            a.write(80);
            b.write(0);
            c.write(0);
            delay(2000);
            myservo.write(90);
        } 
        else if (receivedData.indexOf("screw") != -1) {  // If "screw" is found anywhere
            Serial.println("Screw detected!");
            a.write(0);
            b.write(80);
            c.write(0);
            delay(2000);
            myservo.write(90);
        } 
        else if (receivedData.indexOf("nut") != -1) {  // If "nail" is found anywhere
            Serial.println("Nut detected!");
            a.write(0);
            b.write(0);
            c.write(80);
            delay(2000);
            myservo.write(90);
            
        }
        delay(2000);
        myservo.write(0);
        a.write(0);
        b.write(0);
        c.write(0);
        delay(1000);
    }
}
