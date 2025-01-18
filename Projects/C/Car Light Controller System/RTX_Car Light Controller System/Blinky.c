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

OS_TID t_LightController; // Declare variable to store the task id

//Insert the global variables, enum and TickFct function
unsigned char cnt;

unsigned char SM2_Clk;
void TimerISR() {
   SM2_Clk = 1;
}

enum SM2_States { SM2_NONAME, SM2_LightOffEngineOff, SM2_LightOnEngineOff, SM2_WaitBut, SM2_LightOnEngineOn, SM2_LightOnLongEngineOff, SM2_LightBlinkOffEngineOn, SM2_LightBlinkOnEngineOn, SM2_LightOffEngineOn } SM2_State;

TickFct_IlluminateLamp() {
   switch(SM2_State) { // Transitions
      case -1:
         SM2_State = SM2_LightOffEngineOff;
         break;
         case SM2_LightOffEngineOff:
         if (1) {
            SM2_State = SM2_WaitBut;
         }
         break;
      case SM2_LightOnEngineOff:
         if (!(((A0 || !A0) && A1) || (A0 && A1)) && cnt <= 100) {
            SM2_State = SM2_LightOnEngineOff;
            cnt ++;
         }
         else if ((A0 && !A1) && cnt > 100) {
            SM2_State = SM2_LightOffEngineOff;
         }
         else if (!A0 && !A1) {
            SM2_State = SM2_LightOnLongEngineOff;
            cnt = 0;
         }
         else if (A0 && A1) {
            SM2_State = SM2_LightBlinkOffEngineOn;
         }
         else if ((A0 || !A0) && A1) {
            SM2_State = SM2_LightOnEngineOn;
         }
         break;
      case SM2_WaitBut:
         if (A0 && !A1) {
            SM2_State = SM2_LightOnEngineOff;
            cnt = 0;
         }
         else if (!((A0 && !A1) || (!A0 && A1))) {
            SM2_State = SM2_WaitBut;
         }
         else if (!A0 && A1) {
            SM2_State = SM2_LightOffEngineOn;
         }
         break;
      case SM2_LightOnEngineOn:
         if (1) {
            SM2_State = SM2_LightOffEngineOn;
         }
         break;
      case SM2_LightOnLongEngineOff:
         if (cnt <= 50) {
            SM2_State = SM2_LightOnLongEngineOff;
            cnt ++;
         }
         else if (cnt > 50) {
            SM2_State = SM2_LightOffEngineOff;
         }
         break;
      case SM2_LightBlinkOffEngineOn:
         if (A0 && cnt > 5) {
            SM2_State = SM2_LightBlinkOnEngineOn;
         }
         else if (A0 && cnt <= 5) {
            SM2_State = SM2_LightBlinkOffEngineOn;
            cnt ++;
         }
         else if (!A0) {
            SM2_State = SM2_LightOffEngineOff;
         }
         break;
      case SM2_LightBlinkOnEngineOn:
         if (A0 && cnt > 5) {
            SM2_State = SM2_LightBlinkOffEngineOn;
         }
         else if (A0 && cnt <= 5) {
            SM2_State = SM2_LightBlinkOnEngineOn;
            cnt ++;
         }
         else if (!A0) {
            SM2_State = SM2_LightOffEngineOff;
         }
         break;
      case SM2_LightOffEngineOn:
         if (!A0 && !A1) {
            SM2_State = SM2_LightOffEngineOff;
         }
         break;
      default:
         SM2_State = SM2_LightOffEngineOff;
   } // Transitions

   switch(SM2_State) { // State actions
      case SM2_LightOffEngineOff:
         B0 = 1;

         B1 = 0;

         B2 = 0;

         B3 = 0;

         B4 = 0;

         B6 = 0;

         B7 = 0;
         break;
      case SM2_LightOnEngineOff:
         B0 = 0;

         B1 = 1;

         B2 = 0;
         break;
      case SM2_WaitBut:
         break;
      case SM2_LightOnEngineOn:
         B0 = 0;

         B1 = 0;

         B3 = 1;
         break;
      case SM2_LightOnLongEngineOff:
         B1 = 0;

         B2 = 1;
         break;
      case SM2_LightBlinkOffEngineOn:
         B1 = 0;

         B6 = 0;

         B7 = 1;
         break;
      case SM2_LightBlinkOnEngineOn:
         B1 = 0;

         B6 = 1;

         B7 = 0;
         break;
      case SM2_LightOffEngineOn:
         B0 = 0;

         B3 = 0;

         B4 = 1;
         break;
      default: // ADD default behaviour below
      break;
   } // State actions

}


//Change the name of the State_Machine_Name appropriately
__task void State_Machine_LightController(void) {

   const unsigned int taskperiod = 200; // Copy task period value in milliseconds here
   os_itv_set(taskperiod);

   // Copy initial state assignment statement here
   SM2_State = -1;

   while(1) {
	read_input(); //method to initialize appropriate inputs 	
    //Call TickFct function from here
	TickFct_IlluminateLamp();
	write_led(); //method to write values to LED
	os_itv_wait();
   } // while (1)
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
  //taskname_id = os_tsk_create (State_Machine_Name, 0);
  t_LightController = os_tsk_create (State_Machine_LightController, 0);

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
