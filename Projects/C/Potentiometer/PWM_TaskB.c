/*
This code was automatically generated using the Riverside-Irvine State machine Builder tool
Version 2.5 --- 4/20/2013 0:17:12 PST
*/

#include "rims.h"

/*Define User Variables and Functions For this State Machine Here.*/
unsigned char H, L;
unsigned char X;

unsigned char SM1_Clk;
void TimerISR() {
   SM1_Clk = 1;
}

enum SM1_States { SM1_NONAME, SM1_Init, SM1_PwmH, SM1_PwmL } SM1_State;

TickFct_State_Machine_1() {
   switch(SM1_State) { // Transitions
      case -1:
         SM1_State = SM1_Init;
         break;
         case SM1_Init:
         if (1) {
            SM1_State = SM1_PwmH;
            X = 0;
         }
         break;
      case SM1_PwmH:
         if (! (X < H)) {
            SM1_State = SM1_PwmL;
            X = 0;
         }
         else if (X < H) {
            SM1_State = SM1_PwmH;
         }
         break;
      case SM1_PwmL:
         if (X < L) {
            SM1_State = SM1_PwmL;
         }
         else if (! (X < L)) {
            SM1_State = SM1_PwmH;
            X = 0;
         }
         break;
      default:
         SM1_State = SM1_Init;
   } // Transitions

   switch(SM1_State) { // State actions
      case SM1_Init:
         B1 = 0;
         H = 8;
         L = 12;
         
         break;
      case SM1_PwmH:
         B1 = 1;
         X = X + 1;
         break;
      case SM1_PwmL:
         B1 = 0;
         X = X + 1;
         
         break;
      default: // ADD default behaviour below
      break;
   } // State actions

}

int main() {

   const unsigned int periodState_Machine_1 = 400;
   TimerSet(periodState_Machine_1);
   TimerOn();
   
   SM1_State = -1; // Initial state
   B = 0; // Init outputs

   while(1) {
      TickFct_State_Machine_1();
      while(!SM1_Clk);
      SM1_Clk = 0;
   } // while (1)
} // Main