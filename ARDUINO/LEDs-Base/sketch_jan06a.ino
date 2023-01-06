int l1=13;
int l2=12;
int l3=11;
void setup() {
  for (int i=0; i<3; i++){
    digitalWrite(l1, HIGH);
    digitalWrite(l2, HIGH);
    digitalWrite(l3, HIGH);
    delay(200);
    digitalWrite(l1, LOW);
    digitalWrite(l2, LOW);
    digitalWrite(l3, LOW);
    delay(200);
  }
}

void loop() {
  digitalWrite(l1, HIGH);
  delay(400);
  digitalWrite(l1, LOW);
  delay(400);
  digitalWrite(l2, HIGH);
  delay(400);
  digitalWrite(l2, LOW);
  delay(400);
  digitalWrite(l3, HIGH);
  delay(400);
  digitalWrite(l3, LOW);
  delay(400);
 
}
