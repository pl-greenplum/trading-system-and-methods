# Apple's high and lows Indicator

```
{ TSM Appel's Highs and Lows
  Copyright 2011, P.J.Kaufman. All rights reserved. }
  
  inputs:	period(10);
  vars:		NHR(0), sumH(0), sumL(0);
  
{ New highs are in MKST volume field
  New Lows are in MKST opint field }
  
  sumH = summation(volume of data2,period);
  sumL = summation(openint of data2,period);
  
  if sumH + sumL <> 0 then NHR = sumH/(sumH + sumL);
  
  Plot1(NHR,"NHR");


```
