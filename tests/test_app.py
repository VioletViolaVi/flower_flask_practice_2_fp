from urllib import response


def test_index_route(api):
    response = api.get("/")

    # print("response ===> ", response)
    # print("response.text ===> ", response.text)
    # print("response.data ===> ", response.data)

    assert response.status == "200 OK"
    assert "Welcome to the Flower Factory" in response.text
    # 'b' needs to be added for checking data
    assert b"Welcome to the Flower Factory" in response.data


# test to make sure post routes are not allowed
def test_flowers_post_route(api):
    response = api.post("/flowers")
    assert response.status == "405 METHOD NOT ALLOWED"
    assert response.status_code == 405


def test_new_flower_route(api):
    response = api.post("/flowers/new")
    assert response.status_code == 400

    data = {
        "colour": "teal"
    }

    response = api.post("/flowers/new", json=data)
    assert response.status_code == 201
