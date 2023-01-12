//It has 4 pins: (5V)(GND)(Trigger)(Echo)
//Trigger: emissor
//Echo: receiver

int Trigger=11;
int Echo=10;
long duration;
int cm=0;
void setup()
{
  Serial.begin(9600);
  pinMode(Trigger, OUTPUT);
  pinMode(Echo, INPUT);
  
}

void loop()
{
  digitalWrite(Trigger, LOW);
  delayMicroseconds(2);
  digitalWrite(Trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(Trigger, LOW);
  duration=pulseIn(Echo, HIGH);
  duration=duration/2;
  cm=duration/29;
  Serial.print("Distancia: ");
  Serial.println(cm);
  delay(1500);
  }
}
//Para el siguiente día: Añadir Zumbador
