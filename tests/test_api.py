# import pytest
# import requests

# def test_duckduckgo_instant_answer_api():
#     # Arrange
#     url = 'https://api.duckduckgo.com/?q=python+programming&format=json'
    
#     # Act
#     response = requests.get(url)
#     body = response.json()
    
#     # Assert
#     assert response.status_code == 200
#     assert 'Python' in body['AbstractText']
#     assert 'python' in body['AbstractText']
#     assert 'Python' in body['AbstractSource']
#     assert 'python' in body['AbstractSource']