#!/usr/bin/env python3
"""
Simple search utility for CVE database.
Parses search URLs and extracts query parameters.
"""

import urllib.parse
from typing import Dict, Optional


class SearchParser:
    """Parser for search URLs and query strings."""
    
    def __init__(self, url: str):
        """
        Initialize the search parser with a URL.
        
        Args:
            url: The search URL to parse
        """
        self.url = url
        self.parsed = urllib.parse.urlparse(url)
        self.params = urllib.parse.parse_qs(self.parsed.query)
    
    def get_search_query(self) -> Optional[str]:
        """
        Extract the search query from the URL.
        
        Returns:
            The search query string, or None if not found
        """
        if 'q' in self.params:
            return self.params['q'][0]
        return None
    
    def get_original_query(self) -> Optional[str]:
        """
        Extract the original query from the URL.
        
        Returns:
            The original query string, or None if not found
        """
        if 'oq' in self.params:
            return self.params['oq'][0]
        return None
    
    def get_all_params(self) -> Dict[str, str]:
        """
        Get all query parameters as a dictionary.
        
        Returns:
            Dictionary of parameter names to their first values
        """
        return {k: v[0] for k, v in self.params.items()}
    
    def get_source_id(self) -> Optional[str]:
        """
        Extract the source identifier from the URL.
        
        Returns:
            The source ID, or None if not found
        """
        if 'sourceid' in self.params:
            return self.params['sourceid'][0]
        return None


def main():
    """Main entry point for the search utility."""
    # Example usage with the test URL
    test_url = "https://www.google.com/search?q=test&oq=test&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiPAjIHCAIQABiPAjIGCAMQRRg9MgYIBBBFGDwyBggFEEUYPNIBCDI3NTNqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8"
    
    parser = SearchParser(test_url)
    
    print("Search URL Parser")
    print("=" * 50)
    print(f"URL: {parser.url}")
    print(f"\nSearch Query: {parser.get_search_query()}")
    print(f"Original Query: {parser.get_original_query()}")
    print(f"Source ID: {parser.get_source_id()}")
    print(f"\nAll Parameters:")
    for key, value in parser.get_all_params().items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
