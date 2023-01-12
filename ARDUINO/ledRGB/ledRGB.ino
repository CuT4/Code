// C++ code
//
int rojo=11;
int azul=10;
int verde=9;

void setup()
{
  pinMode(rojo, OUTPUT);
  pinMode(azul, OUTPUT);
  pinMode(verde, OUTPUT);
  
}

void loop()
{
  analogWrite(rojo, 145);
  analogWrite(azul, 32);
  analogWrite(verde, 75);
  
  
}
