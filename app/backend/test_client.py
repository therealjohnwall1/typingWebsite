import requests

def test_http():
    path = "http://localhost:8000"
    params = {
        'size':25
    }

    x = requests.get(path + "/getWords", params = params)

    if x.status_code == 200:
        arr = x.json()
        print(arr)

    else:
        print(x.status_code)

test_http()