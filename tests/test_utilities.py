from flask_server.src.utilities import process_integer

# pytest tests/
def test_answer():
    assert process_integer(3) == 6