from urllib import response


def test_index_route(api):
    response = api.get("/")

    assert response.status == "200 ok"
