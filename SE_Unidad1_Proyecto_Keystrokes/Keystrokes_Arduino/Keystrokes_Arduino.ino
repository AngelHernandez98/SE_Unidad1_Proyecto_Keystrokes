int pushButton[8] = {6, 7, 8, 9, 10, 11, 12, 13};    //pines de los botones
int botones[8] = {0, 0, 0, 0, 0, 0, 0, 0};      //guarda el estado de los botones

void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 8; i++) {
    pinMode(pushButton[i], INPUT_PULLUP); //modo de operacion a pines botones
  }
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i = 0; i < 8; i++) {
    botones[i] = !digitalRead(pushButton[i]);  //lectura botones y guardado negado
  }
  Serial.print("[");
  for (int i = 0; i < 8; i++) {
    Serial.print(botones[i]);
  }
  Serial.print("]");
  Serial.println("");
  delay(100);
}
