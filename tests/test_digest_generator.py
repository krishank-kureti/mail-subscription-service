# tests/test_digest_generator.py
import pytest
from src.database import db
from src.digest_generator import generate_digest_for_user

@pytest.fixture
def setup_db():
    # Set up a mock user for testing
    db['users'] = {
        'test@example.com': {
            'id': 101,
            'preferences': {
                'topics': ['Technology'],
                'sources': ['Mock 1']
            }
        }
    }
    db['logs'] = [] # Clear logs

def test_generate_digest_success(setup_db):
    """Test the full digest generation flow for a user."""
    result = generate_digest_for_user('test@example.com')
    
    assert result['status'] == "success"
    # Check that the template engine (US-007) was called
    assert "<h1>Your Daily News Digest" in result['html']
    # Check that the mock API (US-006) was called
    assert "Tech Headline 1" in result['html']
    # Check that logging (for US-009) is working
    assert len(db['logs']) == 1
    assert db['logs'][0]['status'] == 'success'

def test_generate_digest_user_not_found(setup_db):
    """Test for a user that does not exist."""
    result = generate_digest_for_user('nouser@example.com')
    assert result['status'] == "error"
    assert result['message'] == "User not found"