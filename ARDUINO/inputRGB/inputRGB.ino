String rojo;
String verde;
String azul;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available()==0){}
  rojo=Serial.readString();
  //rojo=rojo.toInt();
  // string to integer function: .toInt()
  Serial.println("Rojo: ");
  Serial.println(rojo);
  

  while (Serial.available()==0){}
  verde=Serial.readString();
  //verde=verde.toInt();
  // string to integer function: .toInt()
  Serial.println("Verde: ");
  Serial.println(verde);
  

  while (Serial.available()==0){}
  azul=Serial.readString();
  //azul=azul.toInt();
  // string to integer function: .toInt()
  Serial.println("Azul: ");
  Serial.println(azul);
  
}
