# TSMAbsVolatility

```
[LegacyColorValue = true]; 

{ TSMAbsVolatility: Volatility as the sum of the absolute price changes
  Copyright 1998-1999, PJ Kaufman. All rights reserved }

	inputs: length(20);
	vars:	vlty(0);

	vlty = TSMAbsVolatility(close, length);
	plot1(vlty,"TSMAVlty");

[LegacyColorValue = true]; 

{ TSMAbsVolatility: Volatility as the sum of the absolute price changes
  Copyright 1998-1999, PJ Kaufman. All rights reserved }

	inputs: price(numericseries), length(numericsimple);
	vars:	n(0), diff(0);

	n = length;
	if currentbar < length then n = currentbar;
	diff = absvalue(price - price[1]);
	TSMAbsVolatility = summation(diff, length);
	
```