# 📚 Doc Generator

AI文档生成器，自动生成项目文档、API文档、README。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📝 README自动生成
- 📖 API文档生成
- 💬 代码注释生成
- 📋 用户手册生成
- 📊 变更日志生成
- 🤝 贡献指南生成

## 🚀 快速开始

```bash
pip install openai

python generator.py
```

## 📖 使用

```python
from doc_generator import create_generator

generator = create_generator()

# 生成README
readme = generator.generate_readme(
    "My Project",
    "一个很棒的项目",
    ["特性1", "特性2"],
    ["Python", "Flask"]
)

# 生成API文档
docs = generator.generate_api_docs(code, "Python")

# 生成代码注释
code_with_docs = generator.generate_docstrings(code, "Python", "google")

# 生成用户手册
manual = generator.generate_user_manual("My Project", ["功能1", "功能2"])

# 生成变更日志
changelog = generator.generate_changelog([
    {"version": "1.0.0", "changes": ["新增功能A", "修复Bug B"]}
])
```

## 📁 项目结构

```
doc-generator/
├── generator.py   # 文档生成器核心
└── README.md
```

## 📄 许可证

MIT License
