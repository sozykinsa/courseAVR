// This file is part of a project located at https://github.com/sozykinsa/courseAVR

#include "wdt328.h"

void wdt328enable()
{
    wdt328reset();
    MCUSR = 0;                       // сбрасывание флагов status register                                                           
    WDTCSR |= (1<<WDCE) | (1<<WDE);  // Выставляем биты WDCE и WDE для входа в режим конфигурирования.
    WDTCSR = (1<<WDIE) | (1<<WDP0) | (0<<WDP1) | (0<<WDP2) | (1<<WDP3);
    //WDTCSR = (WDE_bit<<WDCE) | (WDIE_bit<<WDIE) | (WDP0_bit<<WDP0) | (WDP1_bit<<WDP1) | (WDP2_bit<<WDP2) | (WDP3_bit<<WDP3);
}

//сброс сторожевого таймера
void wdt328reset()
{ 
    asm volatile("wdr");
}

void wdt328disable()
{
    wdt328reset();
    WDTCSR |= (1<<WDCE) | (1<<WDE);
    WDTCSR &= (0<<WDE);
}
