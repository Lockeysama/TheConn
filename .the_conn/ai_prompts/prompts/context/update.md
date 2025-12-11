# 更新 Context 文档指南

你的任务是根据用户提供的变更内容，更新现有的 Context 文档。

---

## 输入

用户会提供：
- Context 文件路径
- 变更内容（新增章节、修改内容、删除内容）

---

## 更新规则

### 可以修改的部分

1. **Frontmatter 中的 `updated` 字段**: 更新为当前日期
2. **Frontmatter 中的 `tags` 字段**: 可以添加或删除标签
3. **文档正文**: 根据变更内容更新

### 必须保持的部分

1. **Frontmatter 中的 `type`, `scope`, `title`, `created` 字段**: 不能修改
2. **文档的核心结构**: 保持章节组织的一致性

---

## 更新原则

1. **精确定位**: 明确要修改的章节或段落
2. **保持一致**: 更新后的内容应与文档整体风格一致
3. **版本记录**: 在文档末尾可添加变更历史（可选）
4. **更新日期**: 必须更新 Frontmatter 中的 `updated` 字段

---

## 输出格式

直接输出更新后的**完整文档内容**（包括 Frontmatter），不要添加任何额外解释。

---

## 示例

### 示例 1: 更新模块设计文档

**用户输入**:
```
文件: .the_conn/context/epics/EPIC-01/Module_Design_Init.md
变更: 新增 "CLI 参数说明" 章节
```

**输出**:

```markdown
---
type: module_design
scope: EPIC-01
title: 初始化模块设计
created: 2025-12-11
updated: 2025-12-12
tags:
  - initialization
  - project-structure
  - cli
---

# 初始化模块设计

## 1. 概述与目标

...

## 2. 核心设计

...

## 3. 接口设计

...

## 4. CLI 参数说明

### 4.1 基本用法

```bash
theconn init [options] [target_path]
```

### 4.2 参数

- `target_path`: 目标目录路径（默认: 当前目录）
- `--overwrite`: 覆盖已存在的文件
- `--dry-run`: 模拟执行，不实际创建文件

## 5. 实施要点

...
```

### 示例 2: 更新技术栈文档

**用户输入**:
```
文件: .the_conn/context/global/Tech_Stack.md
变更: 升级 Python 版本从 3.10 到 3.11，添加 ruff 作为 linter
```

**输出**:

```markdown
---
type: tech_stack
scope: global
title: 技术栈
created: 2025-12-10
updated: 2025-12-12
tags:
  - tech-stack
  - python
---

# 技术栈

## 编程语言

- **主语言**: Python (3.11)
- **其他**: Shell

## 核心框架/库

| 类别 | 技术       | 版本  | 用途       |
| ---- | ---------- | ----- | ---------- |
| CLI  | click      | 8.1.0 | 命令行工具 |
| 测试 | pytest     | 7.4.0 | 单元测试   |
| BDD  | pytest-bdd | 6.1.0 | BDD 测试   |

## 开发工具

- **构建工具**: poetry
- **包管理**: pip
- **测试框架**: pytest
- **BDD 工具**: pytest-bdd
- **Linter**: ruff
- **格式化**: black

## 部署环境

- **运行环境**: Python 3.11+
- **容器**: Docker
- **CI/CD**: GitHub Actions
```

---

## 变更历史记录（可选）

如果文档频繁更新，可以在文档末尾添加变更历史：

```markdown
---

## 变更历史

| 日期       | 变更内容                       | 作者       |
| ---------- | ------------------------------ | ---------- |
| 2025-12-12 | 升级 Python 到 3.11，添加 ruff | @navigator |
| 2025-12-10 | 初始创建                       | @navigator |
```

---

现在，请根据用户提供的信息更新 Context 文档。
