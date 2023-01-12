// C++ code
//

void setup()
{
  
  pinMode(12, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  int v = analogRead(A0);
  if(v<15){
 
    digitalWrite(12, HIGH);
  }else{
    digitalWrite(12, LOW);
  }
  Serial.println(v);
}
