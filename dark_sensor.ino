const int ldrPin = A0;
const int ledPin = 8;
int threshold = 200;
void setup() {

Serial.begin(9600);

pinMode(ledPin, OUTPUT);

}
void loop() {
int lightValue = analogRead(ldrPin);
Serial.println(lightValue);
if (lightValue > threshold) {
digitalWrite(ledPin, HIGH);
}
else {
digitalWrite(ledPin, LOW);
}
delay(200);
}
