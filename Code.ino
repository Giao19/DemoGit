#include <Servo.h>
Servo myServo; 
int btn1 = 7;
int btn2 = 6;
int chanservo = 10;
int ang1 = 0;
int ang2 =60;
int rl1 = 9;
int i;
int rl2 = 8;
int temp;


void setup() {
  Serial.begin(9600);
  myServo.attach(chanservo);

  pinMode(btn1, INPUT_PULLUP);
  pinMode(btn2, INPUT_PULLUP);

  pinMode(rl1, OUTPUT);
  pinMode(rl2, OUTPUT);
}
void loop()
{ 
  int t=0;
  myServo.write(ang2);
  delay(1500);
  for(i=0;i<=1;i++)
  {
      myServo.write(ang2);
      digitalWrite(rl1, LOW);
      digitalWrite(rl2, HIGH);
      
      for(int j =0;j<=200;j++)
      {
        temp = analogRead(0);
        delay(1);
        if(temp>0 && t<100)
        {
          Serial.println(temp);
          t=t+1;
        }
       }
       delay(500);
       digitalWrite(rl1, HIGH);
       digitalWrite(rl2, LOW);
             for(int j =0;j<=200;j++)
      {
        temp = analogRead(0);
        delay(1);
        if(temp>0 && t<100)
        {
          Serial.println(temp);
           t=t+1;
        }
       }
       delay(1000);
   }
   myServo.write(ang1);
   digitalWrite(rl1, LOW);
   digitalWrite(rl2, LOW);
   delay(300000);
}
