from ..project.views import ping


def test_ping():
    """
    Test ping
    """
    data = ping()
    assert data == {'message': 'ok'}
