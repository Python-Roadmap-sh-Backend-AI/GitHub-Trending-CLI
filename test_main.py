import pytest
from unittest.mock import patch
import main


# ----------------------------
# test get data from duration
# ----------------------------
def test_get_data_from_duration():
    assert main.get_data_from_duration("day") is not None
    assert main.get_data_from_duration("week") is not None
    assert main.get_data_from_duration("month") is not None
    assert main.get_data_from_duration("year") is not None


def test_get_data_from_duration_invalid():
    assert main.get_data_from_duration("invalid") is None


# ----------------------------
# test fetch repositories success
# ----------------------------
@patch('main.requests.get')
def test_fetch_repositories_valid(mock_get):
    mock_response = {
        "items": [
            {
                "name": "repo_name",
                "description": "repo_description",
                "language": "Python",
                "stargazers_count": 100,
                "html_url": "https://github.com/test/repo"
            }
        ]
    }

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response
    mock_get.return_value.raise_for_status = lambda: None

    result = main.fetch_repositories("week", 5)

    assert len(result) == 1
    assert result[0]["name"] == "repo_name"


# ----------------------------
# test fetch repositories error
# ----------------------------
@patch('main.requests.get')
def test_fetch_repositories_invalid(mock_get):
    mock_get.side_effect = Exception("API failure")

    with pytest.raises(SystemExit):
        main.fetch_repositories("week", 5)


# ----------------------------
# test display repositories
# ----------------------------
def test_display_repositories(capsys):
    sample_data = [
        {
            "name": "repo1",
            "description": "desc",
            "language": "Python",
            "stargazers_count": 50,
            "html_url": "https://github.com/x/y"
        }
    ]

    main.display_repositories(sample_data)
    captured = capsys.readouterr()

    assert "repo1" in captured.out
    assert "Python" in captured.out
    assert "Stars: 50" in captured.out