# 项目初始化指南

你的任务是为新项目初始化 The Conn 框架的完整目录结构和基础 Context 文档。

## ⚠️ 重要：遵守基础公约

**本 Playbook 严格遵守 `@playbooks/core/base_rules.md` 中定义的所有基础公约。**

**📋 上下文依赖**：

本 Playbook 依赖以下规范文件（AI 必须先加载）：
- **基础公约**: `@playbooks/core/base_rules.md` - 禁止修改 docs/、命名规范、文件路径约定等

本 Playbook **不依赖**以下规范：
- ❌ `test_strategy_rules.md` - 测试策略由项目自定义
- ❌ `bdd_language_rules.md` - BDD 规范由项目自定义

**原因**: 
- project_init 生成的是**项目级配置文档**，不是框架规范的副本
- 项目可以根据实际情况自定义测试策略和 BDD 规范
- 生成的文档应引用框架规范，而不是复制内容

## 本 Playbook 的工作范围

**专注于**：

- ✅ **创建目录结构**：初始化 The Conn 目录结构
- ✅ **生成初始文档**：创建基础 Context 文档和用户文档

---

## 输入

用户会提供：

- 项目名称
- 项目简介
- 主要编程语言
- 技术栈

---

## 输出要求

### 1. 创建目录结构

```
project_root/
├── .the_conn/
│   ├── docs/                # 用户文档
│   │   ├── README.md
│   │   └── GUIDE.md
│   ├── epics/
│   ├── context/
│   │   ├── global/
│   │   └── epics/
│   ├── playbooks/           # 已存在，不需要创建
│   └── ai_workspace/
│
├── src/
├── tests/
│   └── bdd/
│       └── features/
└── README.md
```

### 2. 生成初始 Context 文档

根据项目类型，在 `.the_conn/context/global/` 下创建以下文档：

#### 必需文档

**Architecture.md** - 系统架构

```yaml
---
type: architecture
scope: global
title: 系统架构
created: {yyyy-mm-dd}
updated: {yyyy-mm-dd}
tags:
  - architecture
---

# 系统架构

## 1. 概述与目标

{项目的核心目标和适用场景}

## 2. 核心设计原则

- {原则1}
- {原则2}

## 3. 系统架构

{架构图或组件说明}

## 4. 主要模块职责

- **{模块1}**: {职责}
- **{模块2}**: {职责}

## 5. 技术栈

- **{类别}**: {技术选型}
```

**Tech_Stack.md** - 技术栈

```yaml
---
type: tech_stack
scope: global
title: 技术栈
created: {yyyy-mm-dd}
updated: {yyyy-mm-dd}
tags:
  - tech-stack
---

# 技术栈

## 编程语言

- **主语言**: {语言} ({版本})
- **其他**: {列表}

## 核心框架/库

| 类别   | 技术     | 版本   | 用途       |
| ------ | -------- | ------ | ---------- |
| {类别} | {技术名} | {版本} | {用途说明} |

## 开发工具

- **构建工具**: {工具}
- **包管理**: {工具}
- **测试框架**: {框架}
- **BDD 工具**: {工具}

## 部署环境

- **运行环境**: {环境}
- **容器**: {Docker/其他}
- **CI/CD**: {工具}
```

**Coding_Standard_{Language}.md** - 编码规范

```yaml
---
type: coding_standard
scope: global
title: {语言} 编码规范
created: {yyyy-mm-dd}
updated: {yyyy-mm-dd}
tags:
  - coding-standard
  - {language}
---

# {语言} 编码规范

## 1. 代码风格

- **命名约定**: {说明}
- **缩进**: {空格/Tab}
- **行宽**: {字符数}

## 2. 最佳实践

- {实践1}
- {实践2}

## 3. 禁止事项

- {禁止1}
- {禁止2}

## 4. 代码组织

- {组织规则}

## 5. 参考资料

- {链接或文档}
```

**Testing_Strategy.md** - 测试策略

```yaml
---
type: testing_strategy
scope: global
title: 测试策略
created: {yyyy-mm-dd}
updated: {yyyy-mm-dd}
tags:
  - testing
---

# 测试策略

## 1. 测试理念

本项目采用**单元测试 + E2E 测试**分层策略。

## 2. 测试工具

| 测试类型 | 工具   | 用途       |
| -------- | ------ | ---------- |
| 单元测试 | {框架} | 函数/类    |
| E2E 测试 | {工具} | 端到端场景 |

## 3. BDD 配置

- **关键字**: 统一使用英文 (Given/When/Then)
- **描述语言**: {中文/英文}
- **Feature 文件位置**: `tests/bdd/features/`
- **Step Definitions 位置**: `tests/bdd/`

## 4. 测试覆盖率目标

- 单元测试: ≥ {百分比}%
- E2E 场景: 核心流程 100%

## 5. 参考规范

详细的测试策略规范请参考 The Conn 框架文档：
- Story 类型与测试策略: `@playbooks/core/test_strategy_rules.md`
- BDD 语言配置规范: `@playbooks/core/bdd_language_rules.md`

使用 The Conn 框架进行开发时，AI 会自动遵循这些规范。
```

### 3. 生成 .gitignore

在 `.the_conn/.gitignore` 中添加：

```gitignore
# AI Workspace (临时工作区，不提交)
ai_workspace/*/

# 保留目录结构
!ai_workspace/.gitkeep
```

---

## 生成原则

1. **文档定位**: 生成的 Context 文档是**项目级配置**，不是框架规范的副本
2. **内容精简**: 只包含项目特定的配置和选择，不重复框架规范
3. **规范引用**: 在文档中引用框架规范文件，而不是复制内容
4. **可定制性**: 允许项目根据实际情况调整配置
5. **Context 文档**: 根据项目实际情况填充内容，不要使用占位符
6. **文件命名**: 严格遵循 PascalCase 规范
7. **Frontmatter**: 所有字段必填，日期使用 `yyyy-mm-dd` 格式
8. **目录权限**: 确保创建的目录有写权限
9. **幂等性**: 重复执行不覆盖已有文件
10. **用户文档保护**: `docs/` 目录下的文档仅在初始化时创建，后续**严格禁止任何 AI Playbook 修改 `docs/` 目录中的任何文件**

---

## 示例

### Go 项目示例

**用户输入**:

```
项目名称: DataStream
项目简介: 高可靠低延迟的信令传输系统
主要语言: Go
技术栈: godog (BDD), testify (单元测试)
```

**生成的 Context**:

- `Architecture.md` - 包含微服务架构说明
- `Tech_Stack.md` - 列出 Go 1.21, godog, testify 等
- `Coding_Standard_Go.md` - Go 编码规范（gofmt, golangci-lint）
- `Testing_Strategy.md` - BDD 中文，godog 配置

---

现在，请根据用户提供的项目信息初始化 The Conn 项目。
