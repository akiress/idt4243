#include <SoftwareSerial.h> //Include RFID library
#include <LEDStrip.h> //Include LED Strip library

#define rxPin 2 //pin 2 on arduino is used for receiving tagID from RFID reader
#define txPin 6 //Not required for reading, you could ignore this

#define STRIP_LENGTH 40 //40 LEDs on the strip
#define WHITE 0xffffff  //Hex code for white color

int enable = 3; //pin 3 on arduino is used for enabling and disabling RFID reader
int valid;
int SDI = 4; //Red wire (not the red SV wire!)
int CKI = 5; //Green wire

SoftwareSerial RFID = SoftwareSerial(rxPin, txPin); //Initializing Software serial communication. RFID is a object of SoftwareSerial constructor
LEDStrip strip1(SDI, CKI, STRIP_LENGTH); //Initializing LED strip. strip1 is a object of LEDStrip constructor

void setup() {
  Serial.begin(9600); //This is necessary to see your outpt on your laptop screen
  pinMode(enable, OUTPUT); //Initializing enable(pin 3 on arduino) pin as output. It is used to enable or disable the RFID reader
  RFID.RFIDinit(); //Initializing RFID reader
}

/*
void loop() //this loop will run forever
{
  RFID.RFIDinit(); //Initializing RFID reader once again. This is necessary before reading the tag
  valid = RFID.Readtag(); //Read the tagID
  if (valid == 1) //if there is a tag the valid will be 1 else it will be -1
  {
    Serial.print("ID: "); //Print out RFID code
    Serial.println(RFID.rfidArray); //After reading the tag. TagID will be stored in rfidArray
    RFID.disableRFID(enable); //Deactivate reader
    delay(1000); //1 second delay
    RFID.flush(); //flush out previous data
    RFID.enableRFID(enable); //activate the reader again;
  }
}

*/

/*
void loop()
{
  for(int i = 0; i < STRIP_LENGTH; i++)
  {
    strip1.setLED(i, WHITE);
  }
  strip1.post_frame();
  delay(1);
}

*/
