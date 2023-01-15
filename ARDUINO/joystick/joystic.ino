#define VRX_PIN  A0 // Arduino pin connected to VRX pin
#define VRY_PIN  A1 // Arduino pin connected to VRY pin

/*
#define LEFT_THRESHOLD  400
#define RIGHT_THRESHOLD 800
#define UP_THRESHOLD    400
#define DOWN_THRESHOLD  800

#define COMMAND_NO     0x00
#define COMMAND_LEFT   0x01
#define COMMAND_RIGHT  0x02
#define COMMAND_UP     0x04
#define COMMAND_DOWN   0x08

*/

int xValue = analogRead(VRX_PIN);
int yValue = analogRead(VRY_PIN); 
//int command = COMMAND_NO;

void setup() {
  Serial.begin(9600) ;
}

void loop() {
  // read analog X and Y analog values
  
  Serial.print("Y:");
  Serial.println(yValue);
  Serial.print("X:");
  Serial.println(xValue);
  delay(200);
}
