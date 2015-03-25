const int analogInPin = A1;
const int OutPin = 13;
const int OutPin2 = 12;
const int analogInPin2 = A2;
int sensorValue = 0;
int sensorValue2 = 0;

void setup() {
  Serial.begin(9600);
  pinMode(OutPin, OUTPUT);
  pinMode(OutPin2, OUTPUT);
}

void loop() {
  sensorValue = analogRead(analogInPin);
  sensorValue2 = analogRead(analogInPin2);

  if(sensorValue > 1000){
    digitalWrite(OutPin, HIGH);
  }else{
    digitalWrite(OutPin, LOW);
  }

  if(sensorValue2 > 900){
    digitalWrite(OutPin2, HIGH);
  }else{
    digitalWrite(OutPin2, LOW);
  }

  Serial.print("sensor1 = " );
  Serial.println(sensorValue);
  Serial.print("sensor2 = " );
  Serial.println(sensorValue2);
  delay(100);
}
