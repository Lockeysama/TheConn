# The Conn - 快速开始指南

## 🎯 使用 @tc.md 命令

The Conn 提供了统一的命令入口文件 `tc.md`，让你通过简单的命令操作所有功能。

## 基本用法

### 命令格式

在 AI IDE 中，使用 @ 符号引用 tc.md 文件：

```
@tc.md <模块> <命令> [参数]
```

或使用完整路径：

```
@playbooks/tc.md <模块> <命令> [参数]
```

一级快捷命令：

```
@tc.md <命令> [参数]
```

---

## 🚀 常用命令速查

### 初始化项目

```bash
@tc.md init
```

### 查看项目状态

```bash
@tc.md status
# 或
@tc.md plan status
# 或缩写
@tc.md plan st
```

### 获取下一步建议

```bash
@tc.md next
# 或
@tc.md plan next
# 或缩写
@tc.md plan n
```

### 生成 Story

```bash
# 生成普通 Story（功能开发）
@tc.md story 实现用户登录功能
# 或
@tc.md plan story 实现用户登录功能
# 或缩写
@tc.md plan s 实现用户登录功能

# 生成 E2E Story（集成测试）
@tc.md e2e
@tc.md plan e2e

# 生成性能测试 Story
@tc.md perf
@tc.md plan perf
@tc.md plan performance

# 生成 Bug Fix Story
@tc.md bugfix STORY-01 登录失败
@tc.md plan bugfix STORY-01 登录失败
# 或缩写
@tc.md plan bf STORY-01 登录失败
```

### 生成 Epic

```bash
@tc.md epic 用户管理系统
# 或
@tc.md plan epic 用户管理系统
# 或缩写
@tc.md plan e 用户管理系统
```

### 生成 Feature

```bash
@tc.md feature 用户认证
# 或
@tc.md plan feature 用户认证
# 或缩写
@tc.md plan feat 用户认证
@tc.md plan f 用户认证
```

### 修复 Bug

```bash
@tc.md bugfix STORY-01 登录失败
# 或
@tc.md plan bugfix STORY-01 登录失败
# 或缩写
@tc.md plan bf STORY-01 登录失败
```

### 生成 Task

```bash
@tc.md task STORY-01
# 或
@tc.md exec task STORY-01
# 或缩写
@tc.md exec t STORY-01
```

### 需求拆解

```bash
@tc.md plan breakdown requirements.md
# 或缩写
@tc.md plan bd requirements.md
```

### 添加 Context

```bash
@tc.md ctx add --type=architecture
# 或缩写
@tc.md ctx a --type=architecture
```

### 查看帮助

```bash
@tc.md help
# 或查看特定模块帮助
@tc.md help plan
@tc.md help ctx
@tc.md help exec
```

---

## 📋 命令模块

### 规划模块（plan）

| 命令 | 缩写 | 功能 |
|------|------|------|
| `@tc.md plan review` | `rv` | 需求评审 |
| `@tc.md plan breakdown` | `bd` | 需求拆解 |
| `@tc.md plan change` | `chg` | 需求变更 |
| `@tc.md plan status` | `st` | 项目状态 |
| `@tc.md plan next` | `n` | 下一步建议 |
| `@tc.md plan epic` | `e` | 生成 Epic |
| `@tc.md plan feature` | `feat` / `f` | 生成 Feature |
| `@tc.md plan story` | `s` | 生成 Story |
| `@tc.md plan e2e` | `ee` | 生成 E2E Story |
| `@tc.md plan perf` | `performance` / `p` | 生成性能测试 Story |
| `@tc.md plan bugfix` | `bug` / `bf` | Bug Fix |

**一级快捷命令**：`status`, `next`, `epic`, `feature`, `story`, `bugfix`

### 上下文模块（ctx）

| 命令 | 缩写 | 功能 |
|------|------|------|
| `@tc.md ctx extract` | `ext` / `e` | 提取 Context |
| `@tc.md ctx add` | `a` | 添加 Context |
| `@tc.md ctx update` | `upd` / `u` | 更新 Context |
| `@tc.md ctx search` | `s` | 搜索 Context |

### 执行模块（exec）

| 命令 | 缩写 | 功能 |
|------|------|------|
| `@tc.md exec task` | `t` | 生成 Task |
| `@tc.md exec sync` | `sy` | 同步 Story |
| `@tc.md exec summary` | `sum` | 变更摘要 |

**一级快捷命令**：`task`, `sync`, `summary`

---

## 💡 使用技巧

### 1. 使用缩写提高效率

```bash
# 完整命令
@tc.md plan story 用户登录
@tc.md plan feature 用户管理
@tc.md ctx add --type=architecture

# 缩写命令
@tc.md plan s 用户登录
@tc.md plan f 用户管理
@tc.md ctx a --type=architecture
```

### 2. 一级命令更简洁

常用命令可以直接使用一级形式：

```bash
# 二级命令
@tc.md plan story 用户登录
@tc.md plan status
@tc.md exec task STORY-01

# 一级命令（推荐）
@tc.md story 用户登录
@tc.md status
@tc.md task STORY-01
```

### 3. 中文命令

支持中文命令：

```bash
@tc.md 初始化
@tc.md 状态
@tc.md 故事 用户登录
@tc.md 下一步
```

### 4. 链式操作

```bash
# 步骤 1
@tc.md init

# 步骤 2
@tc.md epic 用户管理系统

# 步骤 3
@tc.md feature 用户认证 --epic=EPIC-01

# 步骤 4
@tc.md story 登录功能 --feature=FEAT-01

# 步骤 5
@tc.md task STORY-01
```

---

## 🎓 工作流示例

### 场景 1：开始新项目

```bash
# 1. 初始化
@tc.md init

# 2. 创建 Epic
@tc.md epic 电商平台

# 3. 创建 Feature
@tc.md feature 商品管理 --epic=EPIC-01

# 4. 创建 Story
@tc.md story 添加商品 --feature=FEAT-01

# 5. 生成 Task
@tc.md task STORY-01

# 6. 查看下一步
@tc.md next
```

### 场景 2：修复 Bug

```bash
# 1. 创建 Bug Fix Story
@tc.md bugfix STORY-05 商品价格显示错误

# 2. 生成 Task
@tc.md task STORY-05.1

# 3. 修复后同步
@tc.md sync STORY-05.1
```

### 场景 3：需求拆解

```bash
# 1. 拆解需求文档
@tc.md plan breakdown requirements.md

# 2. 查看生成的规划
@tc.md status

# 3. 获取下一步建议
@tc.md next
```

### 场景 4：管理 Context

```bash
# 1. 添加架构文档
@tc.md ctx add --type=architecture

# 2. 添加技术栈文档
@tc.md ctx add --type=tech_stack

# 3. 搜索 Context
@tc.md ctx search 架构

# 4. 更新 Context
@tc.md ctx update Architecture.md
```

---

## 📊 命令对比

### 完整命令 vs 缩写

| 功能 | 完整命令 | 缩写命令 |
|------|---------|---------|
| 项目状态 | `@tc.md plan status` | `@tc.md plan st` |
| 下一步 | `@tc.md plan next` | `@tc.md plan n` |
| 生成 Story | `@tc.md plan story` | `@tc.md plan s` |
| 生成 Feature | `@tc.md plan feature` | `@tc.md plan f` |
| 需求拆解 | `@tc.md plan breakdown` | `@tc.md plan bd` |
| 添加 Context | `@tc.md ctx add` | `@tc.md ctx a` |
| 提取 Context | `@tc.md ctx extract` | `@tc.md ctx e` |
| 生成 Task | `@tc.md exec task` | `@tc.md exec t` |

### 二级命令 vs 一级快捷命令

| 功能 | 二级命令 | 一级快捷 |
|------|---------|---------|
| 项目状态 | `@tc.md plan status` | `@tc.md status` |
| 下一步 | `@tc.md plan next` | `@tc.md next` |
| 生成 Story | `@tc.md plan story` | `@tc.md story` |
| 生成 Epic | `@tc.md plan epic` | `@tc.md epic` |
| 生成 Feature | `@tc.md plan feature` | `@tc.md feature` |
| Bug Fix | `@tc.md plan bugfix` | `@tc.md bugfix` |
| 生成 Task | `@tc.md exec task` | `@tc.md task` |
| 同步 Story | `@tc.md exec sync` | `@tc.md sync` |

---

## 🔗 相关文档

- 📘 [命令参考手册](COMMANDS.md) - 完整的命令列表和详细说明
- 📗 [统一入口 Playbook](../playbooks/tc.md) - tc.md 的完整文档
- 📕 [核心规则](../playbooks/core/core.md) - 框架核心规则

---

## 🆘 遇到问题？

1. **不确定用什么命令**：

   ```bash
   @tc.md help
   @tc.md list
   ```

2. **不知道下一步**：

   ```bash
   @tc.md next
   ```

3. **查看项目状态**：

   ```bash
   @tc.md status
   ```

4. **查看模块帮助**：

   ```bash
   @tc.md help plan
   @tc.md help ctx
   @tc.md help exec
   ```

---

**现在开始使用 `@tc` 命令，开启高效的 AI 协作开发之旅！** 🚀
