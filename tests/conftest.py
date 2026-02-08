"""Pytest configuration and fixtures"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import json


@pytest.fixture
def sample_api_response():
    """Sample DOJ API response"""
    return {
        "hits": {
            "total": {"value": 100},
            "hits": [
                {
                    "_source": {
                        "ORIGIN_FILE_NAME": "EFTA00796097.pdf",
                        "ORIGIN_FILE_URI": "https://www.justice.gov/epstein/files/DataSet 9/EFTA00796097.pdf",
                        "documentId": "d92d2de6",
                        "fileSize": 1321323,
                        "totalWords": 8004,
                        "startPage": 14,
                        "endPage": 16,
                        "isChunked": True,
                        "indexedAt": "2026-01-30T18:04:12Z",
                    }
                },
                {
                    "_source": {
                        "ORIGIN_FILE_NAME": "EFTA01216870.pdf",
                        "ORIGIN_FILE_URI": "https://www.justice.gov/epstein/files/DataSet 9/EFTA01216870.pdf",
                        "documentId": "3323f11c",
                        "fileSize": 2481090,
                        "totalWords": 11727,
                        "startPage": 24,
                        "endPage": 30,
                        "isChunked": True,
                        "indexedAt": "2026-01-30T19:04:23Z",
                    }
                },
            ],
        }
    }


@pytest.fixture
def mock_requests_get(sample_api_response):
    """Mock requests.get to return sample API response"""
    with patch("requests.Session.get") as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = sample_api_response
        mock_response.content = json.dumps(sample_api_response).encode()
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response
        yield mock_get


@pytest.fixture
def temp_lib_data(tmp_path, monkeypatch):
    """Create temporary lib_data folder for testing"""
    lib_data = tmp_path / "lib_data"
    lib_data.mkdir()
    monkeypatch.chdir(tmp_path)
    return lib_data
