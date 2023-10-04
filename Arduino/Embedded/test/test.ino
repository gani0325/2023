int led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(led, LOW);
  Serial.write("OFF\n");
  delay(1000);

  digitalWrite(led, HIGH);
  Serial.write("ON\n");
  delay(1000);
}

