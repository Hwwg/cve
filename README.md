# CVE - Search URL Parser

一个用于解析和分析搜索 URL 的 Python 工具。

## 功能特性

- 解析 Google 搜索 URL
- 提取查询参数（搜索词、来源、编码等）
- 支持 URL 编码和解码
- 完整的单元测试覆盖

## 快速开始

### 运行 URL 解析器

```bash
python3 search.py
```

这将解析示例 Google 搜索 URL 并显示：
- URL 参数详情
- 搜索结果类型概述
- 相关搜索建议

### 运行字典获取工具

```bash
python3 fetch_dictionary.py
```

尝试从 Merriam-Webster 获取字典数据（注意：受网络限制影响）。

### 运行测试

```bash
python3 test_search.py -v
```

## 使用示例

```python
from search import SearchParser

# 创建解析器实例
url = "https://www.google.com/search?q=test&sourceid=chrome&ie=UTF-8"
parser = SearchParser(url)

# 获取搜索查询
query = parser.get_search_query()  # 返回: "test"

# 获取来源标识
source = parser.get_source_id()     # 返回: "chrome"

# 获取所有参数
params = parser.get_all_params()    # 返回字典形式的所有参数
```

## 项目结构

```
.
├── README.md                # 项目说明文档
├── URL_ANALYSIS.md          # URL 详细解析文档
├── SEARCH_RESULTS.md        # Google 搜索结果分析文档
├── DICTIONARY_DATA.md       # Merriam-Webster 字典数据结构
├── ACCESSIBLE_DOMAINS.md    # 可访问域名列表和网络限制说明
├── search.py                # 搜索 URL 解析器主程序
├── fetch_dictionary.py      # 字典数据获取工具
└── test_search.py           # 单元测试
```

## 文档

- **项目总结**: [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - 项目完成情况和统计信息
- **URL 参数解析**: [URL_ANALYSIS.md](URL_ANALYSIS.md) - 详细的URL结构和参数说明
- **搜索结果分析**: [SEARCH_RESULTS.md](SEARCH_RESULTS.md) - 搜索结果类型和示例
- **字典数据**: [DICTIONARY_DATA.md](DICTIONARY_DATA.md) - Merriam-Webster 字典数据结构
- **网络访问**: [ACCESSIBLE_DOMAINS.md](ACCESSIBLE_DOMAINS.md) - 可访问域名列表和限制说明
- **API 文档**: 见下方

## API 文档

### SearchParser 类

#### `__init__(url: str)`
初始化解析器。

**参数:**
- `url`: 要解析的搜索 URL

#### `get_search_query() -> Optional[str]`
提取搜索查询词。

**返回:** 搜索查询字符串，如果不存在则返回 None

#### `get_original_query() -> Optional[str]`
提取原始查询词。

**返回:** 原始查询字符串，如果不存在则返回 None

#### `get_source_id() -> Optional[str]`
提取来源标识符。

**返回:** 来源 ID 字符串，如果不存在则返回 None

#### `get_all_params() -> Dict[str, str]`
获取所有查询参数。

**返回:** 包含所有参数的字典

## 测试覆盖

项目包含完整的单元测试，覆盖以下场景：
- 标准 URL 参数提取
- 缺失参数处理
- URL 编码字符解析
- 不同查询类型支持

## 许可证

MIT License
