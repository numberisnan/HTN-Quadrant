int last = -1;
int left, right, p;

int leds[7] = {8, 10, 5, 9, 13, 11, 12};

void setup() {
  byte lb[2];
  byte rb[2];
  
  // put your setup code here, to run once:
  for (int i = 0; i < 7; i++) {
    pinMode(leds[i], OUTPUT);
  }
  Serial.begin(9600);

  while(!Serial.available()) {}
  // serial read section
  while (true) {
    if (Serial.available() > 0) {
     Serial.readBytes(lb, 2);
     Serial.readBytes(rb, 2);

     left = lb[1] << 8 | lb[0];
     right = rb[1] << 8 | rb[0];
     
     if (last != -1) {
       digitalWrite(last, LOW);
     }

     p = round(map((right - left), -200, 200, -0.4, 6.4));
      
     digitalWrite(leds[p], HIGH);

     last = leds[p];
   }
 }
}

void loop() {
  
}
