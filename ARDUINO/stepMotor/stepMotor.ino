#include <Stepper.h>
 
Stepper myStepper(200, 9, 10, 11, 12);
 
void setup() {
  myStepper.setSpeed(110);
}
 
void loop() {  
  myStepper.step(200);
}
