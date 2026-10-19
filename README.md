# Browser Watermark-Removal Test Data


This repository contains a small, first-party record of five manually selected video-watermark test cases. It is a transparent test log, not a comparison of products and not evidence that the same outcome will occur on other files.


## What the dataset says


Each row records the sample description, input/output byte counts, elapsed time, and the observed result supplied by the site owner. All five samples were reported as H.264, 640 × 360, 24 fps, four seconds, and 96 frames. The source videos are not included. The run date and hardware details for these five rows were not supplied, so this repository does not claim them.


Three rows report that a mark or text was not visible in the output. One reports that a pale corner mark remained visible. Two report visible blur artifacts or other repeated marks. “Not visible” is only the reported observation for that sample; it is not a quality guarantee or a statement that original pixels were recovered.


## Reproduce the report


Run the validator with Python 3:


```sh
python scripts/validate_and_report.py
```


The script validates required fields and numeric formats, then prints the rows as a Markdown table. It does not process media, infer image quality, or calculate a generalized success rate.


## Method and limits


- The measurements are owner-supplied first-party observations; the underlying media files are not included for independent reruns.
- Elapsed time means the reported time from starting processing until the page displayed completion.
- Byte counts are copied verbatim as integer byte values; seconds are retained to the reported precision.
- These cases should not be treated as a representative sample, cross-device benchmark, or promise for other videos.
- Do not use this data to infer codec compatibility beyond the listed samples.


## Related tool


For information about the site's browser-based tools, visit the [EraseWatermark homepage](https://erasewatermark.net/).

The site describes a browser-based workflow that uses a user-selected fixed region for a stationary visible mark: [EraseWatermark video tool](https://erasewatermark.net/ai-video-watermark-remover/). The page also states its limits and includes a separate, later generated-sample demonstration; the five rows here are the distinct owner-supplied tests in `data/video-sample-results.csv`.


## Licenses


- `scripts/validate_and_report.py`: MIT License (`LICENSE`).
- `data/video-sample-results.csv` and this README: Creative Commons Attribution 4.0 International (`DATA-LICENSE.md`).
