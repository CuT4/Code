int uno=11;
int dos=10;
int tres=9;
int cuatro=6;
int cinco=5;
int seis=3;
void setup()
{
  pinMode(uno, OUTPUT);
  pinMode(dos, OUTPUT);
  pinMode(tres, OUTPUT);
  pinMode(cuatro, OUTPUT);
  pinMode(cinco, OUTPUT);
  pinMode(seis, OUTPUT);
}

void loop()
{
  analogWrite(uno, 70);
  delay(100);
  analogWrite(uno, 0);
  delay(100);
  
  analogWrite(dos, 70);
  delay(100);
  analogWrite(dos, 0);
  delay(100);
  
  analogWrite(tres, 70);
  delay(100);
  analogWrite(tres, 0);
  delay(100);
  
  analogWrite(cuatro, 70);
  delay(100);
  analogWrite(cuatro, 0);
  delay(100);
  
  analogWrite(cinco, 70);
  delay(100);
  analogWrite(cinco, 0);
  delay(100);
  
  analogWrite(seis, 70);
  delay(100);
  analogWrite(seis, 0);
  delay(100);
}
