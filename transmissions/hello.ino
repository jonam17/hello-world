// TRANSMISSION 08 // ARDUINO — Hello, World with a pulse (pin 13 LED).

const int LED_PIN = 13;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
  Serial.println("[NODE 00] Hello, World :: firmware online");
}

void loop() {
  digitalWrite(LED_PIN, HIGH); delay(200);  // beat
  digitalWrite(LED_PIN, LOW);  delay(800);  // rest
}
