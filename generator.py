"""
Doc Generator - AI文档生成器
自动生成项目文档、API文档、README
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime
from pathlib import Path

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class DocGenerator:
    """
    AI文档生成器
    支持：README、API文档、代码注释、用户手册
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_readme(self, project_name: str, description: str, features: List[str] = None, tech_stack: List[str] = None) -> str:
        """生成README"""
        if not self.client:
            return "LLM客户端未配置"

        features_text = "\n".join(f"- {f}" for f in (features or []))
        tech_text = "、".join(tech_stack or [])

        prompt = f"""请为以下项目生成专业的README.md：

项目名称：{project_name}
描述：{description}
特性：
{features_text}
技术栈：{tech_text}

要求：
1. 使用Markdown格式
2. 包含徽章
3. 包含安装、使用、特性、项目结构
4. 专业且吸引人"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_api_docs(self, code: str, language: str = "Python") -> str:
        """生成API文档"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为以下{language}代码生成API文档：

```{language}
{code}
```

要求：
1. 每个函数/方法的详细说明
2. 参数说明
3. 返回值说明
4. 使用示例
5. 错误处理说明"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_docstrings(self, code: str, language: str = "Python", style: str = "google") -> str:
        """生成代码注释"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为以下{language}代码添加{style}风格的文档字符串：

```{language}
{code}
```

要求：
1. 每个函数/类都有文档字符串
2. 使用{style}风格
3. 包含参数、返回值、异常说明
4. 保持代码原有逻辑不变"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_user_manual(self, project_name: str, features: List[str], tech_stack: List[str] = None) -> str:
        """生成用户手册"""
        if not self.client:
            return "LLM客户端未配置"

        features_text = "\n".join(f"- {f}" for f in features)

        prompt = f"""请为{project_name}生成用户手册：

功能：
{features_text}

要求：
1. 快速开始指南
2. 详细功能说明
3. 常见问题解答
4. 故障排除
5. 使用Markdown格式"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4000
        )

        return response.choices[0].message.content

    def generate_changelog(self, changes: List[Dict]) -> str:
        """生成变更日志"""
        if not self.client:
            return "LLM客户端未配置"

        changes_text = json.dumps(changes, ensure_ascii=False, indent=2)

        prompt = f"""请根据以下变更生成CHANGELOG.md：

{changes_text}

要求：
1. 使用Keep a Changelog格式
2. 按版本分组
3. 分类：新增、修复、变更、移除
4. 使用Markdown格式"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_contribution_guide(self, project_name: str, tech_stack: List[str] = None) -> str:
        """生成贡献指南"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为{project_name}生成CONTRIBUTING.md：

要求：
1. 如何提交Issue
2. 如何提交PR
3. 代码规范
4. 测试要求
5. 文档要求"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def save_doc(self, content: str, file_path: str):
        """保存文档"""
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)


def create_generator(**kwargs) -> DocGenerator:
    """创建文档生成器"""
    return DocGenerator(**kwargs)


if __name__ == "__main__":
    generator = create_generator()

    print("Doc Generator")
    print()

    # 测试
    readme = generator.generate_readme(
        "My Project",
        "一个很棒的项目",
        ["特性1", "特性2", "特性3"],
        ["Python", "Flask", "SQLite"]
    )

    print(readme[:500] + "...")
