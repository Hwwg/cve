#!/usr/bin/env python3
"""
Simple search URL parser utility.
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
    
    print("=" * 70)
    print("Google Search URL 解析结果")
    print("=" * 70)
    print(f"\n📎 原始URL:")
    print(f"   {parser.url}\n")
    
    print("🔍 解析出的参数:")
    print(f"   搜索关键词 (q):    {parser.get_search_query()}")
    print(f"   原始查询 (oq):     {parser.get_original_query()}")
    print(f"   来源标识 (sourceid): {parser.get_source_id()}")
    
    print(f"\n📋 所有查询参数:")
    for key, value in parser.get_all_params().items():
        # 截断过长的值以便显示
        display_value = value if len(value) <= 50 else value[:47] + "..."
        print(f"   • {key:12} = {display_value}")
    
    print("\n" + "=" * 70)
    print("📊 搜索结果概述")
    print("=" * 70)
    print(f"\n对于搜索词 '{parser.get_search_query()}'，Google 通常返回以下类型的结果：\n")
    print("1. 📖 字典定义 - 单词 'test' 的含义、发音、词源")
    print("2. 🎓 在线测试平台 - 各类在线考试和测验网站")
    print("3. 💻 软件测试 - 测试框架、方法论、最佳实践")
    print("4. 🏥 医学检测 - COVID-19检测、血液检测等")
    print("5. 📚 教育资源 - 标准化考试（SAT、GRE等）")
    
    print("\n💡 相关搜索建议:")
    related_searches = [
        "test online", "test meaning", "test definition",
        "covid test", "software testing", "test drive"
    ]
    for i, search in enumerate(related_searches, 1):
        print(f"   {i}. {search}")
    
    print("\n" + "=" * 70)
    print("📄 详细文档")
    print("=" * 70)
    print("\n✓ URL 参数详细解析: URL_ANALYSIS.md")
    print("✓ 搜索结果完整分析: SEARCH_RESULTS.md")
    print("✓ 使用说明和 API: README.md")
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
