int myPin=12;
void setup()
{
  pinMode(myPin, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  int v = analogRead(A0);
  if(v<600){
    digitalWrite(myPin, HIGH);
  }else{
    digitalWrite(myPin, LOW);
  }
  Serial.println(v);
}
