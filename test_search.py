#!/usr/bin/env python3
"""
Tests for the search parser utility.
"""

import unittest
from search import SearchParser


class TestSearchParser(unittest.TestCase):
    """Test cases for SearchParser class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_url = (
            "https://www.google.com/search?q=test&oq=test"
            "&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiPAjIHCAIQABiPAjIGCAMQRRg9MgYIBBBFGDwyBggFEEUYPNIBCDI3NTNqMGo3qAIAsAIA"
            "&sourceid=chrome&ie=UTF-8"
        )
        self.parser = SearchParser(self.test_url)
    
    def test_get_search_query(self):
        """Test extraction of search query parameter."""
        query = self.parser.get_search_query()
        self.assertEqual(query, "test")
    
    def test_get_original_query(self):
        """Test extraction of original query parameter."""
        oq = self.parser.get_original_query()
        self.assertEqual(oq, "test")
    
    def test_get_source_id(self):
        """Test extraction of source ID parameter."""
        source_id = self.parser.get_source_id()
        self.assertEqual(source_id, "chrome")
    
    def test_get_all_params(self):
        """Test extraction of all parameters."""
        params = self.parser.get_all_params()
        self.assertIn('q', params)
        self.assertIn('oq', params)
        self.assertIn('sourceid', params)
        self.assertIn('ie', params)
        self.assertEqual(params['q'], "test")
        self.assertEqual(params['ie'], "UTF-8")
    
    def test_url_without_query(self):
        """Test URL without query parameter."""
        parser = SearchParser("https://www.google.com/search")
        self.assertIsNone(parser.get_search_query())
    
    def test_url_with_different_query(self):
        """Test URL with a different query."""
        parser = SearchParser("https://www.google.com/search?q=CVE-2024-1234")
        self.assertEqual(parser.get_search_query(), "CVE-2024-1234")
    
    def test_url_with_encoded_characters(self):
        """Test URL with encoded characters."""
        parser = SearchParser("https://www.google.com/search?q=hello%20world")
        self.assertEqual(parser.get_search_query(), "hello world")


if __name__ == "__main__":
    unittest.main()
