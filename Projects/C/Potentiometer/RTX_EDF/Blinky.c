/*----------------------------------------------------------------------------
 *      RL-ARM - RTX
 *----------------------------------------------------------------------------
 *      Name:    BLINKY.C
 *      Purpose: RTX example program
 *----------------------------------------------------------------------------
 *      This code is part of the RealView Run-Time Library.
 *      Copyright (c) 2004-2011 KEIL - An ARM Company. All rights reserved.
 *---------------------------------------------------------------------------*/

#include <RTL.h>
#include <91x_lib.H>
#include "LCD.h"

unsigned char A0,A1; //A0 - Button 3.5, A1 - Button 3.6
unsigned char B0 = 0,B1 = 0,B2 = 0,B3 = 0,B4 = 0,B5 = 0,B6 = 0,B7 = 0; //B0-B7 represent LED's 0 through 7

//Function to read input
void read_input()
{
	//BUTTON_3_5:
	A0 = !(GPIO3->DR[0x080]>>5); // Returns 1 when pressed and 0 when released
	//BUTTON_3_6:
	A1 = !(GPIO3->DR[0x100]>>6); // Returns 1 when pressed and 0 when released
}

//Function to write to led
void write_led()
{
  unsigned char mask = 0;

  mask  = (B0<<0);
  mask |= (B1<<1);
  mask |= (B2<<2);
  mask |= (B3<<3);
  mask |= (B4<<4);
  mask |= (B5<<5);
  mask |= (B6<<6);
  mask |= (B7<<7);

  GPIO7->DR[0x3FC] = mask;
}

//Function to print an unsigned char value on the LCD Display
void print_uns_char (unsigned char value)
{	 
	int flag = 0,i;
	char c[4];
	do {
	   int rem = value%10;
	   value = value/10;
	   c[flag] = rem+48;
	   flag++;
	}while(value>0);
	for(i=flag-1;i>=0;i--)
		LCD_putc(c[i]);
}

OS_TID tsk_A; 								/* Declare variable to store the task id for Task A */
OS_TID tsk_B;								/* Declare variable to store the task id for Task B */

//Function prototype for state machine 1 (Task A)
unsigned char H1, L1;
unsigned char X1;

unsigned char SM1_Clk;
void TimerISR1() {
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
            X1 = 0;
         }
         break;
      case SM1_PwmH:
         if (! (X1 < H1)) {
            SM1_State = SM1_PwmL;
            X1 = 0;
         }
         else if (X1 < H1) {
            SM1_State = SM1_PwmH;
         }
         break;
      case SM1_PwmL:
         if (X1 < L1) {
            SM1_State = SM1_PwmL;
         }
         else if (! (X1 < L1)) {
            SM1_State = SM1_PwmH;
            X1 = 0;
         }
         break;
      default:
         SM1_State = SM1_Init;
   } // Transitions

   switch(SM1_State) { // State actions
      case SM1_Init:
         B0 = 0;

         H1 = 8;

         L1 = 12;

         
         break;
      case SM1_PwmH:
         B0 = 1;

         X1 = X1 + 1;
         break;
      case SM1_PwmL:
         B0 = 0;

         X1 = X1 + 1;

         
         break;
      default: // ADD default behaviour below
      break;
   } // State actions

}

//Function prototype for state machine 2 (Task B)
unsigned char H2, L2;
unsigned char X2;

unsigned char SM2_Clk;
void TimerISR2() {
   SM2_Clk = 1;
}

enum SM2_States { SM2_NONAME, SM2_Init, SM2_PwmH, SM2_PwmL } SM2_State;

TickFct_State_Machine_2() {
   switch(SM2_State) { // Transitions
      case -1:
         SM2_State = SM2_Init;
         break;
         case SM2_Init:
         if (1) {
            SM2_State = SM2_PwmH;
            X2 = 0;
         }
         break;
      case SM2_PwmH:
         if (! (X2 < H2)) {
            SM2_State = SM2_PwmL;
            X2 = 0;
         }
         else if (X2 < H2) {
            SM2_State = SM2_PwmH;
         }
         break;
      case SM2_PwmL:
         if (X2 < L2) {
            SM2_State = SM2_PwmL;
         }
         else if (! (X2 < L2)) {
            SM2_State = SM2_PwmH;
            X2 = 0;
         }
         break;
      default:
         SM2_State = SM2_Init;
   } // Transitions

   switch(SM2_State) { // State actions
      case SM2_Init:
         B1 = 0;

         H2 = 8;

         L2 = 12;

         
         break;
      case SM2_PwmH:
         B1 = 1;

         X2 = X2 + 1;
         break;
      case SM2_PwmL:
         B1 = 0;

         X2 = X2 + 1;

         
         break;
      default: // ADD default behaviour below
      break;
   } // State actions

}


/*---------------------------------------------------------------------------------------------------------
 *    Task A: This is an LED task which cause LED B0 to blink every 4 s.
 *--------------------------------------------------------------------------------------------------------*/

__task void Task_A(void) {

   const unsigned int period = 400; 					/* Execute Task A every 4 s */
   os_itv_set(period);

   SM1_State = -1; 										/* Initialize state machine 1 */

   while(1) {											/* Endless loop */
	read_input(); 										/* Method to initialize appropriate inputs */ 	
    
	TickFct_State_Machine_1();	 						/* Call TickFct function from here */
	write_led(); 										/* Method to write values to LED */
	os_itv_wait();
   	} 
}

/*---------------------------------------------------------------------------------------------------------
 *    Task B: This is an LED task which cause LED B1 to blink every 10 s.
 *--------------------------------------------------------------------------------------------------------*/

__task void Task_B(void) {

   const unsigned int period = 1000; 					/* Execute Task B every 10 s */
   os_itv_set(period);

   SM2_State = -1;	   									/* Initialize state machine 2 */

   while(1) {
	read_input(); 										/* Method to initialize appropriate inputs */ 	
  
	TickFct_State_Machine_2();							/* Call TickFct function from here */
	write_led(); 										/* Method to write values to LED */
	os_itv_wait();
   } 
}

/*----------------------------------------------------------------------------
 *        Task 7 'init': Initialize
 *---------------------------------------------------------------------------*/
__task void init (void) {

  /* Configuring LED                     */
  SCU->GPIOOUT[7]  = 0x5555;
  GPIO7->DDR       = 0xFF;
  GPIO7->DR[0x3FC] = 0x00;

  /* LCD Setup                           */
  GPIO8->DDR       = 0xFF;
  GPIO9->DDR       = 0x07;

  /* Port 3 setup for button 3.5 and 3.6 */
  SCU->GPIOIN[3]  |= 0x60;
  SCU->GPIOOUT[3] &= 0xC3FF;
  GPIO3->DDR      &= 0x9F;

  LCD_init(); //Initialize LCD
  LCD_cur_off(); //Remove LCD cursor
  LCD_cls(); //Clearing LCD screen
  
  //Launch the task in the following manner
  tsk_A = os_tsk_create (Task_A, 2);
  tsk_B = os_tsk_create (Task_B, 1); 

  os_tsk_delete_self ();
}


/*----------------------------------------------------------------------------
 *        Main: Initialize and start RTX Kernel
 *---------------------------------------------------------------------------*/
int main (void) {

  os_sys_init (init);                    /* Initialize RTX and start init    */
  return 0;
}

/*----------------------------------------------------------------------------
 * end of file
 *---------------------------------------------------------------------------*/
