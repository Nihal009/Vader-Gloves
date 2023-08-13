#include <MPU6050_tockn.h>
#include <Wire.h>

MPU6050 mpu6050(Wire);

void  setup() {
  Serial.begin(9600);   
  Wire.begin();         
  mpu6050.begin();
  mpu6050.calcGyroOffsets(true);
  pinMode(A1,INPUT);           
   pinMode(12, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(7, OUTPUT);
}

void  loop() {
  mpu6050.update();
  if(mpu6050.getAngleX()>25)   
   {
    Serial.println('w');
    digitalWrite(2, HIGH);
    digitalWrite(2, LOW);
   }                         
  else if(mpu6050.getAngleX()<-25)   
   {
    Serial.println('s');
    digitalWrite(4, HIGH);
    digitalWrite(4, LOW);}   
  else if(mpu6050.getAngleY()>25)    
   {
   Serial.println('a');
   digitalWrite(7, HIGH);
   digitalWrite(7, LOW);
   } 
  else if(mpu6050.getAngleY()<-25)    
   {
   Serial.println('d');
   digitalWrite(12, HIGH);
   digitalWrite(12, LOW);
   }                                                          
}