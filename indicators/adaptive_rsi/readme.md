# Adaptive RSI Indicator

```
[LegacyColorValue = true]; 

{ TSMAdaptive RSI : Adaptive Relative Strength Indicator
  Copyright 1998-1999, P.J.Kaufman. All rights reserved.

  Smoothing function based on RSI }

	input:	period(20);
	plot1 (TSMAdaptiveRSI(period), "TSMARSI");

[LegacyColorValue = true]; 

{ TSMAdaptive RSI : Adaptive Relative Strength Indicator
  Copyright 1998-1999, P.J.Kaufman. All rights reserved.
  Smoothing function based on RSI }

	input:	period(numericsimple);
	vars:	sc(0), ARSI(0);

	if currentbar = 1 then ARSI = close
		else begin
			sc = (absvalue(RSI(close, period) / 100 - .5)*2);
			ARSI = ARSI[1] + sc*(close - ARSI[1]);
			end;
	TSMAdaptiveRSI = ARSI;

```
