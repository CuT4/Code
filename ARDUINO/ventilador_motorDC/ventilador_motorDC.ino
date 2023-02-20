//El diseño del circuito está en mi cuneta de tinkercad.com
void setup()
{
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
}

void loop()
{
 digitalWrite(13, LOW);
  digitalWrite(12, HIGH);
}
