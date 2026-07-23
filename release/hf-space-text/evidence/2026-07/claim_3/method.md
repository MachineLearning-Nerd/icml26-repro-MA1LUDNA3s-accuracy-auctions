# Method

The construction satisfies every formal assumption directly. For each training point, kNN includes the point itself and k-1 neighbors, as in the authors' released `smallest_v_for_flip`. The neighbor vote gives the critical bid in closed form, so no numerical optimization or proxy is used. Twenty datasets are run at each of seven sizes for fixed k=31 and independently for k=63. The no-noise control sets every label to +1.
