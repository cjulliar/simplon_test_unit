import pytest
from source.my_module_mock import f1, f2, fetch_product_price, calculate_tax
# import requests
from unittest.mock import patch


def test_f2_with_fixed_f1():
    with patch('source.my_module_mock.f1', return_value=42) as mock_f1 :
        assert f2() == 420
        mock_f1.assert_called_once()

# def test_calculate_tax():
#     with patch('pricing_module.fetch_product_price', return_value=100.0) as mock_fetch:
#         assert calculate_tax(1) == 20.0  # 20% de 100.0
#         mock_fetch.assert_called_once_with(1)

# def test_calculate_tax_high_value():
#     with patch('pricing_module.fetch_product_price', return_value=10000.0) as mock_fetch:
#         assert calculate_tax(1) == 2000.0
#         mock_fetch.assert_called_once_with(1)

# def test_calculate_tax_zero():
#     with patch('pricing_module.fetch_product_price', return_value=0.0) as mock_fetch:
#         assert calculate_tax(1) == 0.0
#         mock_fetch.assert_called_once_with(1)

# # def test_calculate_tax_api_failure():
# #     with patch('pricing_module.fetch_product_price', side_effect=requests.exceptions.RequestException) as mock_fetch:
# #         with pytest.raises(requests.exceptions.RequestException):
# #             calculate_tax(1)
# #         mock_fetch.assert_called_once_with(1)
