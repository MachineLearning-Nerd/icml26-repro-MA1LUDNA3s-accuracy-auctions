# Method

For `b0<b1`, write the objective as `b*l_i(f)+C(f)` and let `f0,f1` minimize it. Their two optimality inequalities add to `(b1-b0)(l1-l0)<=0`; hence `l1<=l0`. A decreasing loss (or the paper's separating threshold) makes correctness weakly increase. The primary checker exhausts that implication using exact integers; the independent checker enumerates all tie choices on lower envelopes of three affine objectives.
