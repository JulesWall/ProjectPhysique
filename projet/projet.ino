/* 
 According to : 
  HTU21D Humidity Sensor Example Code
  By: Nathan Seidle
  SparkFun Electronics
  Date: September 15th, 2013
  License: This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).

  CO2 sensor exemple code
  author : lg.gang(lg.gang@qq.com)
  version :  V1.0
  date :  2016-7-6
  GNU Lesser General Public License
 */

#include <Wire.h>
#include "SparkFunHTU21D.h"
#include <SoftwareSerial.h>

HTU21D myHumidity;
SoftwareSerial mySerial(10, 11); // RX, TX
unsigned char hexdata[9] = {0xFF,0x01,0x86,0x00,0x00,0x00,0x00,0x00,0x79}; //Read the gas density command /Don't change the order


void setup()
{
  Serial.begin(9600);
  analogReference(DEFAULT);
  myHumidity.begin();
  mySerial.begin(9600);
}

void loop()
{
  // humidity 
  float humd = myHumidity.readHumidity(); 
  // temperature 
  float temp = myHumidity.readTemperature();
  // time
  float time = millis()/1000.0;

   mySerial.write(hexdata,9);
   delay(2500);
   

long hi,lo,CO2;
for(int i=0,j=0;i<9;i++)
 {
  if (mySerial.available()>0){
     
     int ch=mySerial.read();

    if(i==2){hi=ch;}   //High concentration
    if(i==3){lo=ch;}   //Low concentration
    if(i==8){CO2=hi*256+lo;}  //CO2 concentration

       } 

}
Serial.print("/time : ");
Serial.print(time);
Serial.print("/CO2  : ");
Serial.print(CO2);
Serial.print("   /temperature : ");
Serial.print(temp);
Serial.print("   /humidity : ");
Serial.println(humd);

}

