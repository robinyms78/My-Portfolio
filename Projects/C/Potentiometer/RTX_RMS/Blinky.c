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

extern __irq void ADC_IRQ_Handler (void); /* ADC  interrupt routine           */
extern unsigned char AD_in_progress;      /* AD conversion in progress flag  */

unsigned char A0,A1; //A0 - Button 3.5, A1 - Button 3.6
unsigned char B0 = 0,B1 = 0,B2 = 0,B3 = 0,B4 = 0,B5 = 0,B6 = 0,B7 = 0; //B0-B7 represent LED's 0 through 7


OS_TID tskA; 								/* Assign identification for Task A */
OS_TID tskB; 								/* Assign identification for Task B */
OS_TID tskC; 								/* Assign identification for Task C */
OS_TID tskD; 								/* Assign identification for Task D */
OS_TID tskE; 								/* Assign identification for Task E */

OS_MUT mutex_LCD;							/* Declare mutex */
os_mbx_declare(mailbox1, 20);				/* Declare mailbox */

enum brightness_level { Level_1, Level_2, Level_3, Level_4, Level_5 };

short Mailbox_Value = 0; 					/* Initialize mailbox value to 0 */
int LightLevel = Level_1;
const int Period = 1; 						/* initialize PWM period to 1 ms */
const int PWMPeriod = 10 / Period; 

const short Brightness_Low = 213;
const short Brightness_MediumLow = 409;
const short Brightness_MediumHigh = 616;
const short Brightness_High = 802;

//Function to read input
void read_buttons()
{
	//BUTTON_3_5:
	A0 = !(GPIO3->DR[0x080]>>5); // Returns 1 when pressed and 0 when released
	//BUTTON_3_6:
	A1 = !(GPIO3->DR[0x100]>>6); // Returns 1 when pressed and 0 when released
}

void start_ADC ( )
{
	if (!AD_in_progress)  
	{             						    /* If conversion not in progress      */
        AD_in_progress = 1;                 /* Flag that AD conversion is started */
        ADC->CR |= 0x0423;                  /* Set STR bit (Start Conversion)     */
    }
	//Now the interrupt will be called when conversion end 
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

//Function to put potentiometer value to mailbox
void PutInMailBox(short Potent_Value)
{
    void *msg = NULL;
    msg = (void*)malloc(sizeof(short));
    memcpy(msg, &Potent_Value, sizeof(short));
    os_mbx_send(mailbox1, msg, 0);
}

//Function to receive potentiometer value from mailbox
short GetFromMailBox()
{
    void *msg = NULL;
    os_mbx_wait(mailbox1, &msg, 0xFFFF);
    memcpy(&Mailbox_Value, msg, sizeof(short));
    free (msg);

    return Mailbox_Value;
}

//Function to update brightness level of LED
void UpdateLightLevel( short Brightness )
{
    if ( Brightness < Brightness_Low )
    {
        LightLevel = Level_1;
    }
    else if ( Brightness >= Brightness_Low && Brightness < Brightness_MediumLow )
    {
        LightLevel = Level_2;
    }
    else if ( Brightness >= Brightness_MediumLow && Brightness < Brightness_MediumHigh )
    {
        LightLevel = Level_3;
    }
    else if ( Brightness >= Brightness_MediumHigh && Brightness < Brightness_High )
    {
        LightLevel = Level_4;
    }
    else if ( Brightness >= Brightness_High )
    {
        LightLevel = Level_5;
    }
}

//Function to compute duty cycle
int PWM(const unsigned int Duty, const unsigned int Counter)
{
    if ( Counter * 100u / PWMPeriod > Duty )
    {
        return 0;
    }

    return 1;
}

//Function to update brightness level of LED
void UpdateLight(const unsigned int Counter )
{
    unsigned int Duty = 0u;

    switch ( LightLevel )
    {
    case Level_1:
        Duty = 20;
        break;
    case Level_2:
        Duty = 40;
        break;
    case Level_3:
        Duty = 60;
        break;
    case Level_4:
        Duty = 80;
        break;
    case Level_5:
        Duty = 100;
        break;
    default:
        break;
    }

    if (PWM(Duty, Counter))
    {
        B0 = 1;
        B1 = 1;
        B2 = 1;
        B3 = 1;
        B4 = 1;
        B5 = 1;
        B6 = 1;
        B7 = 1;
    }
    else
    {
        B0 = 0;
        B1 = 0;
        B2 = 0;
        B3 = 0;
        B4 = 0;
        B5 = 0;
        B6 = 0;
        B7 = 0;
    }

	write_led(); 									/* Write values to LED */
}

/*-------------------------------------------------------------------------------------------
 * Task A: RTX Kernel starts this task with ADC conversion that runs periodically every 100ms.
 *         When ADC conversion completes, the interrupt service routine reads the potentiometer
 *		   value and put it in a mailbox. 
 *-------------------------------------------------------------------------------------------*/

__task void Task_A(void) {

    const unsigned int period = 100; 	 			/* Run task periodically every 100 ms */
    os_itv_set(period);

    while(1) {										/* Endless loop */
       
        if ( !AD_in_progress ) 						/* read Potentiometer and put in mailbox */
        {
            start_ADC();
        }
        
        os_itv_wait ();
    } 
}

/*--------------------------------------------------------------------------------------------
 *  Task B: RTX Kernel starts this task when ADC conversion completes. It reads in the
 *          potentiometer value from the mailbox and computes the duty cycle to control led
 *			brightness. Task B write the ADC conversion value and duty cycle value in a global
 *			variable that can be accessed bt tasks C, D and E.
 *--------------------------------------------------------------------------------------------*/

__task void Task_B(void) {

    const unsigned int taskperiod = 100;   			/* Run task periodically every 100 ms */
    os_itv_set(taskperiod);

    while(1) {								  		/* Endless loop */
		short sBrightness = GetFromMailBox();
        UpdateLightLevel( sBrightness );
        os_itv_wait ();
    } 
}

/*---------------------------------------------------------------------------------------------------
 *   Task C: This is an LED task that controls the brightness of the LEDs using PWM using duty cycles	
 *			 computed by task B.
 *---------------------------------------------------------------------------------------------------*/

__task void Task_C(void) {
	
    static unsigned int Counter = 0u;

    os_itv_set(Period);

    while(1){										/* Endless loop */
        UpdateLight(Counter);

        ++Counter;
        if (Counter > PWMPeriod)
        {
            Counter -= PWMPeriod;
        }
        os_itv_wait ();
    } 
}

/*---------------------------------------------------------------------------------------------------
 *   Task D: This is an LCD task with 50ms period that prints the potentiometer value read by task A
 * 			 on the first line of the LCD display.
 *---------------------------------------------------------------------------------------------------*/

__task void Task_D(void) {

    const unsigned int taskperiod = 50; 			/* Run task periodically every 50 ms */
    os_itv_set(taskperiod);

    while(1) {									 	/* Endless loop */
        os_mut_wait(mutex_LCD, 0xffff);
        LCD_put_brightness(Mailbox_Value);
        os_mut_release(mutex_LCD);
        os_itv_wait ();
    }
}

/*---------------------------------------------------------------------------------------------------
 *   Task E: This is an LCD task with 50ms period that prints the duty cycle value computed by task B
 *           on the second line of the LCD display.
 *---------------------------------------------------------------------------------------------------*/

__task void Task_E(void) {

    const unsigned int taskperiod = 50; 		 	/* Run task periodically every 50 ms */
    os_itv_set(taskperiod);

    while(1) {										/* Endless loop */
        os_mut_wait(mutex_LCD, 0xffff);
        LCD_put_level(LightLevel);
        os_mut_release(mutex_LCD);
        os_itv_wait ();
    } 
}

/*----------------------------------------------------------------------------
 *        Task 7 'init': Initialize
 *---------------------------------------------------------------------------*/
__task void init (void) {

  unsigned int n = 0;
  /* Set up Potentiometer and Light sensor*/                                                              
  
  SCU->GPIOIN[4]  |= 0x01;                /* P4.0                             */
  SCU->GPIOOUT[4] &= 0xFFFC;              /* P4.0                             */

  GPIO4->DDR      &= 0xFE;                /* P4.0                             */
  SCU->GPIOANA    |= 0x0001;              /* P4.0                             */
                                          
  ADC->CR         |= 0x0042;              /* Set POR bit                      */
  for (n = 0; n < 100000; n ++);          /* Wait > 1 ms  (at 96 MHz)         */

  ADC->CR         &= 0xFFB7;              /* Clear STB bit                    */
  for (n = 0; n < 1500; n ++);            /* Wait > 15 us (at 96 MHz)         */

  ADC->CR         |= 0x0423;              /* Enable end of conversion interupt*/
  ADC->CCR         = 0x003F;              /* AD Conversion, No WDG on Ch 0    */

  /* Configure and enable IRQ for A/D Converter (ADC)                         */
  VIC0->VAiR[15]  = (unsigned int)ADC_IRQ_Handler; /* Setup ADC IRQ Hndl addr */
  VIC0->VCiR[15] |= 0x20;                 /* Enable the vector interrupt      */
  VIC0->VCiR[15] |= 15;                   /* Specify the interrupt number     */
  VIC0->INTER    |= (1<<15);              /* Enable ADC interrupt             */

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

  LCD_init(); 											/* Initialize LCD */
  LCD_cur_off(); 										/* Remove LCD cursor */
  LCD_cls(); 											/* Clearing LCD screen */

  os_mut_init(mutex_LCD); 								/* Initialize LCD mutex */
  os_mbx_init(mailbox1, sizeof(mailbox1)); 				/* Initialize mailbox */

  LightLevel = Level_1;

  //Launch the tasks 
  tskA = os_tsk_create (Task_A, 1);
  tskB = os_tsk_create (Task_B, 2);
  tskC = os_tsk_create (Task_C, 5);
  tskD = os_tsk_create (Task_D, 4);
  tskE = os_tsk_create (Task_E, 4);

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
