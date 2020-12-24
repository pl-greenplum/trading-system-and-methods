# Accumulated Swing Index

```

[LegacyColorValue = true]; 

{ TSM Swing Index: Wilder's Index
  Copyright 1998-1999, PJ Kaufman. All rights reserved } 

	inputs: limitmov(0);

	plot1(TSMSwingIndex(limitmov), "TSMSwing");



[LegacyColorValue = true]; 

{ TSMSwingIndex: Wilder's Index
  Copyright 1998-1999, PJ Kaufman. All rights reserved } 

	inputs: limitmov(numericsimple);
	vars: maxk(0), conda(0), condb(0), condc(0), r(0), pdir(0), lim(0), sindex(0),
			maxbb(50);
{	NOTE: Index results take longer to calculate but are move stable when
		maxbb is replaced by "currentbar" in the stddev calculation near the bottom }

	conda = absvalue(high - close[1]);
	condb = absvalue(low - close[1]);
	condc = high - low;
	pdir = absvalue(close[1] - open[1]);

	maxk = conda;
	if condb > maxk then maxk = condb;

{ value of R based on which condition is greater }
	if conda >= condb and conda >= condc then
		r = conda - .5*condb + .25*pdir;
	if condb >= conda and condb >= condc then
		r = condb - .5*conda + .25*pdir;
	if condc >= conda and condc >= condb then
		r = condc + .25*pdir;

{ Swing index }
	lim = limitmov;
	if lim = 0 then lim = 3.5*stddev(r,maxbb);
	
	if r <> 0 and lim <> 0 then 
		sindex = 50 * (maxk / lim) *( ((close - close[1]) + .5*(close - open) + .25*pdir) / r);
	TSMSwingIndex = sindex;

```

