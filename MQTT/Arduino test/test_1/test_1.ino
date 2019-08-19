void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
 
  // put your main code here, to run repeatedly:
  int i;
  for(i=1;i<=10;i++)
  {
  Serial.print("hi this is this:");
  Serial.println(i);
  delay(1000);
}
}
