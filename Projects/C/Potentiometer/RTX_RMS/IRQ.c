/******************************************************************************/
/* IRQ.C: IRQ Handler                                                         */
/******************************************************************************/
/* This file is part of the uVision/ARM development tools.                    */
/* Copyright (c) 2005-2006 Keil Software. All rights reserved.                */
/* This software may only be used under the terms of a valid, current,        */
/* end user licence from KEIL for a compatible version of KEIL software       */
/* development tools. Nothing else gives you the right to use this software.  */
/******************************************************************************/

#include <91x_lib.h>
#include <RTL.h>

extern void PutInMailBox(short Potent_Value);

short Potentiometer = 0;
/* Variable used as semaphore, needed because TIM3 has higher priority than 
   ADC interrupt and could restart the AD conversion that has not still 
   finished                                                                   */
unsigned char AD_in_progress = 0;           /* AD conversion in progress flag     */

__irq void ADC_IRQ_Handler (void) {     /* AD converter interrupt routine     */

    Potentiometer = ADC->DR0 & 0x03FF;    /* AD value for global usage (10 bit) */

    ADC->CR &= 0xFFFE;                    /* Clear STR bit (Start Conversion)   */
    ADC->CR &= 0x7FFF;                    /* Clear End of Conversion flag       */

    VIC0->VAR = 0;                        /* Acknowledge Interrupt              */  
    VIC1->VAR = 0;

    AD_in_progress = 0;                   /* Clear flag, as AD conv finished    */

    PutInMailBox(Potentiometer);
}
