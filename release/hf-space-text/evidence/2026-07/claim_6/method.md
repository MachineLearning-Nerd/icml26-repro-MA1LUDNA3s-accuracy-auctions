# Method

Three independent 30,000-person routes evaluated the label-value frontier
with five paired trials, 20 alpha values, `v_plus` in `{4,6,8,10,12}`, L2
logistic regression, exact normalized welfare, 99% confidence intervals, an
independent per-class welfare identity, and an equal-value negative control.
They differed materially in how they resolved unpublished implementation
details:

1. Numeric codes with three preprocessing sensitivities.
2. Declared binary demographic mappings and a semantic 14-group one-hot
   occupation recode.
3. The mapped route plus nested selection of `C` from
   `{0.001,0.01,0.1,1,10,100}` using only an inner training split.

After all three missed the preregistered `[20%,26%]` mean band, a fourth route
sought a logically valid falsification. It formalized "up to" as an
existential claim, independently digitized the published vector figure twice,
and tested the arithmetic detector with a corrupted endpoint.
