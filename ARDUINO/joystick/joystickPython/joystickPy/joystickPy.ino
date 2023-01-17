#define VRX_PIN  A0 // Arduino pin connected to VRX pin
#define VRY_PIN  A1 // Arduino pin connected to VRY pin

void setup() {
  Serial.begin(9600) ;
}

void loop() {
  int xValue = analogRead(VRX_PIN);//Read the analog value of A0 pin, x axis.
  int yValue = analogRead(VRY_PIN);//Read the analog value of A1 pin, y axis.
  // read analog X and Y analog values
  Serial.print(xValue);
  Serial.print(",");
  Serial.println(yValue);
  //Result: 'x,y'
}
