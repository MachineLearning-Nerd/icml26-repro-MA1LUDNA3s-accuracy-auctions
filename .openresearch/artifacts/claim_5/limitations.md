# Limitations and deviations

The author's unpublished raw Figure 2 data were unavailable, and the released script imports missing modules. This is an independent reimplementation. The plateau sweep ends at 65,536 rather than the released script's 2^24 maximum, but uses ten seeds at every point and is non-toy. It follows the paper's mean distance 0.5 rather than the code's conflicting 0.4. Exact zero-bid payer status is computed; no candidate-count proxy is used.
