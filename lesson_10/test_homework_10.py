import pytest
from unittest.mock import patch
from homework_10 import log_event

@pytest.mark.parametrize("username, status, log_method", [
    ('user1', 'success', 'info'),
    ('user2', 'expired', 'warning'),
    ('user3', 'failed', 'error'),
    ('user4', 'unknown', 'error'),
])
def test_log_event(username, status, log_method):
    with patch('logging.getLogger') as mock_get_logger:
        logger = mock_get_logger.return_value
        log_event(username, status)
        getattr(logger, log_method).assert_called_once_with(
            f"Login event - Username: {username}, Status: {status}"
        )
