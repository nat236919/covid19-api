# Tests (by PyTest)

## Features
|  Test File                  |     Description                       |
| --------------------------- | ------------------------------------- |
| test_get_data.py            | Test Getting data from GitHub source  |
| test_covid_model_api_v1.py  | Test all methods in APIv1 Model       |
| test_covid_model_api_v2.py  | Test all methods in APIv2 Model       |
| test_router_api_v2.py       | (to be created)                       |

## How to use
```console
D:\{your_app_path}> pytest
```

## Result
```console
================================================= test session starts =================================================
platform win32 -- Python 3.8.1, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: D:\{your_app_path}
collected 15 items

test_covid_model_api_v2.py ......... [ 66%]
test_get_data.py .... [100%]

=================================================  15 passed in 12.66s =================================================
```
