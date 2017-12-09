/*
  AnalogReadSerial
  Reads an analog input on pin 0, prints the result to the serial monitor.
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.
 
 This example code is in the public domain.
 
 Upload this to the Arduino using the Arduino IDE!
 */
int ledPin=11;
int ledValue=0;

// the setup routine runs once when you press reset:
void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  if(Serial.available()>0){
    ledValue=Serial.read();
    analogWrite(ledPin,ledValue);
    Serial.print(ledValue);
    Serial.flush();
  }    
}
