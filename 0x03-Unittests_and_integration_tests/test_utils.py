#!/usr/bin/env python3
"""Unit tests for utils module"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test case class for the access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that access_nested_map returns the correct value
        for given nested_map and path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, missing_key):
        """
        Test that access_nested_map raises KeyError for invalid paths
        and that the exception message matches the missing key.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{missing_key}'")


class TestGetJson(unittest.TestCase):
    """Test case class for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that get_json returns the correct payload
        and that requests.get is called exactly once with the URL.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test case for the memoize decorator"""

    def test_memoize(self):
        """Test that memoize caches method result"""

        class TestClass:
            """A simple class to test memoization"""

            def a_method(self):
                """Method that returns 42"""
                return 42

            @memoize
            def a_property(self):
                """Memoized method that calls a_method"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            obj = TestClass()
            first = obj.a_property
            second = obj.a_property

            self.assertEqual(first, 42)
            self.assertEqual(second, 42)
            mock.assert_called_once()
