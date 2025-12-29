#!/usr/bin/env python3
"""
Dictionary data fetcher for Merriam-Webster.
Attempts to fetch and parse dictionary entries.
"""

import urllib.request
import urllib.error
import json
from typing import Dict, Optional, List


class DictionaryFetcher:
    """Fetcher for dictionary data from Merriam-Webster."""
    
    def __init__(self):
        """Initialize the dictionary fetcher."""
        self.base_url = "https://www.merriam-webster.com/dictionary/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def fetch_word_data(self, word: str) -> Optional[str]:
        """
        Fetch the HTML content for a word from Merriam-Webster.
        
        Args:
            word: The word to look up
            
        Returns:
            HTML content as string, or None if fetch fails
        """
        url = f"{self.base_url}{word}"
        
        try:
            request = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(request, timeout=10) as response:
                html = response.read().decode('utf-8')
                return html
        except urllib.error.URLError as e:
            print(f"❌ 网络错误: {e}")
            print(f"   无法访问: {url}")
            return None
        except Exception as e:
            print(f"❌ 错误: {e}")
            return None
    
    def extract_basic_info(self, html: str, word: str) -> Dict:
        """
        Extract basic information from HTML content.
        
        Note: This is a simple implementation. For production use,
        consider using BeautifulSoup or the official API.
        
        Args:
            html: HTML content
            word: The word being looked up
            
        Returns:
            Dictionary with extracted information
        """
        data = {
            "word": word,
            "url": f"{self.base_url}{word}",
            "status": "fetched",
            "content_length": len(html),
            "has_content": len(html) > 0
        }
        
        # Simple checks for content presence
        if "entry-word" in html:
            data["has_definition"] = True
        if "pronunciation" in html:
            data["has_pronunciation"] = True
        if "etymology" in html:
            data["has_etymology"] = True
            
        return data
    
    def save_raw_html(self, html: str, word: str, filename: Optional[str] = None):
        """
        Save raw HTML to a file.
        
        Args:
            html: HTML content to save
            word: The word (used for default filename)
            filename: Optional custom filename
        """
        if filename is None:
            filename = f"/tmp/{word}_dictionary.html"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"✓ HTML 已保存到: {filename}")
        except Exception as e:
            print(f"❌ 保存失败: {e}")


def main():
    """Main entry point for dictionary fetcher."""
    word = "test"
    
    print("=" * 70)
    print("Merriam-Webster 字典数据获取工具")
    print("=" * 70)
    print(f"\n🔍 查询词条: {word}")
    print(f"📍 目标URL: https://www.merriam-webster.com/dictionary/{word}\n")
    
    fetcher = DictionaryFetcher()
    
    print("⏳ 正在尝试获取数据...")
    html = fetcher.fetch_word_data(word)
    
    if html:
        print(f"✓ 成功获取数据！")
        print(f"  内容长度: {len(html)} 字节")
        
        # 提取基本信息
        info = fetcher.extract_basic_info(html, word)
        print(f"\n📊 数据分析:")
        print(f"  包含定义: {info.get('has_definition', '未检测到')}")
        print(f"  包含发音: {info.get('has_pronunciation', '未检测到')}")
        print(f"  包含词源: {info.get('has_etymology', '未检测到')}")
        
        # 保存原始HTML
        fetcher.save_raw_html(html, word)
        
        # 保存JSON元数据
        json_file = f"/tmp/{word}_metadata.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(info, f, indent=2, ensure_ascii=False)
        print(f"✓ 元数据已保存到: {json_file}")
        
    else:
        print("\n❌ 数据获取失败")
        print("\n可能的原因:")
        print("  1. 网络连接受限（当前环境可能阻止访问某些域名）")
        print("  2. 网站反爬虫保护")
        print("  3. 需要使用官方 API")
        
        print("\n💡 建议:")
        print("  • 查看 DICTIONARY_DATA.md 了解数据结构")
        print("  • 考虑使用 Merriam-Webster 官方 API")
        print("  • 在无网络限制的环境中运行此脚本")
        
        print("\n📚 官方 API 信息:")
        print("  网站: https://dictionaryapi.com/")
        print("  需要: 免费注册获取 API Key")
        print("  优点: 结构化数据、无需解析HTML、符合使用条款")
    
    print("\n" + "=" * 70)
    print("📄 相关文档")
    print("=" * 70)
    print("  • DICTIONARY_DATA.md - 字典数据结构和格式")
    print("  • SEARCH_RESULTS.md - 搜索结果分析")
    print("  • URL_ANALYSIS.md - URL 解析详情")
    print("=" * 70)


if __name__ == "__main__":
    main()
