# Acceleration Indicator

```
[LegacyColorValue = true]; 

{ TSMAcceleration: Acceleration
  Copyright 1999, P.J.Kaufman. All rights reserved.
}
  inputs:  length(20);

  plot1(TSMAcceleration(close,length),"TSMAccel");

[LegacyColorValue = true]; 

{ TSMAcceleration: Acceleration
  Copyright 1999, P.J.Kaufman. All rights reserved.
}
  inputs: price(numericseries), length(numericsimple);
  vars: veloc(0);

  veloc = (price - price[length]) / length;
  TSMacceleration = veloc - veloc[1];

```
