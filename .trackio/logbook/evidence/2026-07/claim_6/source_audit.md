# Source audit

Primary source: `https://arxiv.org/abs/2606.02435v2`, retrieved
2026-07-23, HTML SHA-256
`abdd0eb6dbcb4bc119c71405ea5e0d944ec598efef39c8c8da776f545916654d`.
Section 7 / Figure 3 states welfare `+23%` and accuracy `-21%` for
label-based values. Appendix C.1 says regularization was fine-tuned but gives
no coefficient or protocol. Appendix C.2 specifies 2018 1-Year New Jersey
ACSIncome, random 30,000-person samples, a 60/40 train/validation split, the 13
features, binary/14-group preprocessing, and categorical noise with
sigma=0.4. It omits the binary mappings, occupation boundaries, seeds, and raw
Figure 3 data.

The judge prompt's phrase "modest accuracy tradeoffs" is not the paper's
description of the label-value endpoint. The paper calls the `+23%/-21%`
endpoint a much larger gap.
