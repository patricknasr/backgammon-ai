from flask_server.src.utilities import process_integer

# pytest tests/
def test_processing_integer():
    assert process_integer(3) == 6