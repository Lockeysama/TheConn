# 更新 Context 文档指南

你的任务是根据用户提供的变更内容，更新现有的 Context 文档。

## ⚠️ 重要：遵守基础公约

**本 Playbook 严格遵守 `@playbooks/core/base_rules.md` 中定义的所有基础公约。**

## 本 Playbook 的工作范围

**专注于**：更新现有 Context 文档

---

## 输入

用户会提供：

- Context 文件路径
- 变更内容（新增章节、修改内容、删除内容）

---

## 更新规则

### ⚠️ Global Context 更新规则

**Global Context 固定为 4 个文件，采用"添加章节"而非"创建新文件"策略**：

| 文件                            | 新增内容归类规则                                   |
| ------------------------------- | -------------------------------------------------- |
| `Architecture.md`               | 架构设计、部署方案、API 约定、安全规范、领域模型等 |
| `Tech_Stack.md`                 | 技术选型、工具、框架、库、中间件等                 |
| `Coding_Standard_{Language}.md` | 编码规范、最佳实践、性能优化、代码风格等           |
| `Testing_Strategy.md`           | 测试策略、测试规范、覆盖率要求、测试组织等         |

**更新方式**：
- ✅ 作为新章节添加到对应文件中（如 "## 5. 部署架构"）
- ✅ 更新已有章节的内容
- ❌ 不创建新的 Global Context 文件

### 可以修改的部分

1. **Frontmatter 中的 `updated` 字段**: 更新为当前日期
2. **Frontmatter 中的 `tags` 字段**: 可以添加或删除标签
3. **文档正文**: 根据变更内容更新
4. **新增章节**: Global Context 可以添加新章节来容纳新内容

### 必须保持的部分

1. **Frontmatter 中的 `type`, `scope`, `title`, `created` 字段**: 不能修改
2. **文档的核心结构**: 保持章节组织的一致性
3. **Global Context 文件数量**: 不创建新的 Global Context 文件

---

## 更新原则

1. **精确定位**: 明确要修改的章节或段落
2. **保持一致**: 更新后的内容应与文档整体风格一致
3. **版本记录**: 在文档末尾可添加变更历史（可选）
4. **更新日期**: 必须更新 Frontmatter 中的 `updated` 字段
5. **Global Context 优先更新**: 需要添加公约类型的内容时，优先更新 4 个固定文件，而不是创建新文件
6. **章节组织**: 新增内容应作为新章节添加，保持文档结构清晰

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

## 5. 关键约束

...

```

### 示例 2: 更新技术栈文档（修改已有内容）

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

### 示例 3: 新增章节到 Architecture.md（Global Context 扩展）

**用户输入**:
```
文件: .the_conn/context/global/Architecture.md
变更: 添加部署架构章节，描述容器化部署方案
```

**输出**:

```markdown
---
type: architecture
scope: global
title: 系统架构设计
created: 2025-12-10
updated: 2025-12-17
status: active
tags:
  - microservices
  - deployment
  - docker
---

# 系统架构设计

## 1. 概述与目标

采用微服务架构，实现服务解耦和独立部署。

## 2. 核心设计

### 2.1 服务拆分

...

### 2.2 通信方式

...

## 3. 技术选型

...

## 4. 关键约束

...

## 5. 部署架构

### 5.1 容器化方案

**容器技术**: Docker + Docker Compose

**镜像管理**:
- 基础镜像: `golang:1.21-alpine`
- 多阶段构建减少镜像体积
- 镜像仓库: Docker Hub (开发), Harbor (生产)

### 5.2 服务部署

| 服务     | 端口 | 副本数 | 资源限制        |
| -------- | ---- | ------ | --------------- |
| 用户服务 | 8001 | 3      | 512MB / 1 CPU   |
| 认证服务 | 8002 | 2      | 256MB / 0.5 CPU |
| 数据服务 | 8003 | 3      | 1GB / 2 CPU     |
| 网关     | 80   | 2      | 256MB / 0.5 CPU |

### 5.3 环境配置

- **开发环境**: Docker Compose 本地部署
- **测试环境**: Kubernetes (Minikube)
- **生产环境**: Kubernetes (AWS EKS)

## 6. 注意事项

...
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
