# CS361-Team7-Micro-Services2

This microservice generates and returns a random number.

# How to Run This Microservice

1. Create and activate the virtual environment

    `python3 -m venv venv`

    `source venv/bin/activate`      # Linux/macOS


2. Install dependencies

    `pip install -r requirements.txt`

3. Start the microservice

    `python3 app.py`

Expected output:

    Running on http://127.0.0.1:5001


 

 # Communication Contract

This contract describes how to programmatically request and receive data from the Random Number Generator microservice.
- If no range is provided, it will default to 1-20. 

- If a maximum number is provided, the minimum number will default to 1.

- If only the minimum number is provided or the minimum number is greater than the maximum number, an error will be returned.
### How to Request Data
Endpoint:
GET /random-number

Query Parameters:

Parameter | Type | Description
--------- | ---- | -----------
min | int | minimum value for range (default 1 if not provided)
max | int | maximum value for range (default 20 if not provided)

Example Request:
```
import requests

response = requests.get(
    "http://localhost:5001/random-number",
    params={
        "min": 5,
        "max": 10
    }
)

print(response.json())
```
-------

### How to Receive Data

Successful JSON Response Format:

```
{
    'max': 10, 'min': 5, 'number': 7
}
```

---------

Error Response Format:

```
{
    'error': 'min value greater than max value'
}
```

```
{
    'error': 'if min value is provided, max value must also be provided'
}
```

Example (Processing the Response in Python):
```
if response.status_code == 200:
    min_val = data.get("min_val")
    max_val = data.get("max_val")
    random_num = data.get("result")

    # print data on seperate lines formatted
    print(f"\tmin:\t{min_val}\n\tmax:\t{max_val}\n\trandom:\t{random_num}")
elif response.status_code == 400:
    print(f"\t400: {data.get('error')}")
else:
    print("\tgeneral error")
```
---------