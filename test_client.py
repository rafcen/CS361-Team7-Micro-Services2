import requests

def test_rng(min_input, max_input):
    print("Requesting random number...")
    response = requests.get(
        "http://localhost:5001/random-number",
        params={
            "min_val": min_input,
            "max_val": max_input
        }
    )

    print("Random number response received:")

    data = response.json()

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

def test_error():
    print("Requesting random number...")
    response = requests.get(
        "http://localhost:5001/random-number",
        params={
            "min_val": 10
        }
    )

    print("Random number response received:")

    data = response.json()

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


if __name__ == "__main__":
    print(f"\ntest successful: 10-20")
    test_rng(10, 20)
    print(f"\ntest error: min > max")
    test_rng(10, 5)
    print(f"\ntest error: max must exist if min is provided")
    test_error()
