void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
 
Serial.println("OBD:25,24,23,276,222,1000");
Serial.println("DOB:10,11,12,13,14,15,26");
 delay(5000);
}
