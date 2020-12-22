# BodyMomentum Indicator

```
[LegacyColorValue = true]; 

{TSMBodyMomentum: Candlestick Momentum of the "Body"
 Copyright 1999, P.J.Kaufman. All rights reserved. }

{	Using 14 bars as input, a body momentum greater than
	70 indicates that white dominates; a value less than 20
	indicates that black dominates. }

	inputs: length(14);

	plot1(TSMBodyMomentum(length),"TSMbody");

[LegacyColorValue = true]; 

{TSMBodyMomentum: Candlestick Momentum of the "Body"
 Copyright 1999, P.J.Kaufman. All rights reserved. }

  inputs: length(numericsimple);
  vars:   sumup(0), sumdown(0), body(0), ix(0);

  sumup = 0;
  sumdown = 0;
  for ix = 0 to length - 1 begin
	body = close[ix] - open[ix];
  	if body > 0 then sumup = sumup + body;
	if body < 0 then sumdown = sumdown - body;
	end;
  if sumup + sumdown <> 0 then
		TSMBodyMomentum = sumup*100 / (sumup + sumdown)
	else
		TSMBodyMomentum = 0;

```