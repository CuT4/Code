#include <IRremote.h> //This is the librery used to process IR data

int IRpin=9;

void setup() {
  Serial.begin(9600);
  IrReceiver.begin(IRpin);
  
}

void loop() {
  while(IrReceiver.decode() == 0){
    //If it is not receiving data it will do nothing
  }

// IrReceiver.decodedIRData.command makes data readable but the values obtained are not the same as the value writen in the button so I change it below
  
  //Serial.println(IrReceiver.decodedIRData.command);// || 1=12 || 2=24 || 3=94 || 4=8 || 5=28 || 6=90 || 7=66 || 8=82 || 9=74 || right=67 || left=68 || up=9 || down=7

  if(IrReceiver.decodedIRData.command==12){
    Serial.println("Button pressed: 1");
  }
  if(IrReceiver.decodedIRData.command==24){
    Serial.println("Button pressed: 2");
  }
  if(IrReceiver.decodedIRData.command==94){
    Serial.println("Button pressed: 3");
  }
  if(IrReceiver.decodedIRData.command==8){
    Serial.println("Button pressed: 4");
  }
  if(IrReceiver.decodedIRData.command==28){
    Serial.println("Button pressed: 5");
  }
  if(IrReceiver.decodedIRData.command==90){
    Serial.println("Button pressed: 6");
  }
  if(IrReceiver.decodedIRData.command==66){
    Serial.println("Button pressed: 7");
  }
  if(IrReceiver.decodedIRData.command==82){
    Serial.println("Button pressed: 8");
  }
  if(IrReceiver.decodedIRData.command==74){
    Serial.println("Button pressed: 9");
  }
  if(IrReceiver.decodedIRData.command==67){
    Serial.println("Button pressed: right");
  }
  if(IrReceiver.decodedIRData.command==68){
    Serial.println("Button pressed: left");
  }
  if(IrReceiver.decodedIRData.command==9){
    Serial.println("Button pressed: up");
  }
  if(IrReceiver.decodedIRData.command==7){
    Serial.println("Button pressed: down");
  }
  
  delay(200);
  
  IrReceiver.resume();//It updates the receiver so it doesn't read only once and it keeps reading values.
}
