# The Conn - 命令参考手册

## 📖 命令总览

### 命令结构

```
@tc.md <模块> <命令> [参数]
```

或使用一级快捷命令：

```
@tc.md <命令> [参数]
```

---

## 🚀 初始化命令

### `@tc.md init`

**功能**：初始化 The Conn 项目结构

**语法**：

```bash
@tc.md init
```

**示例**：

```bash
用户：@tc.md init
AI：正在初始化项目结构...
    ✅ 创建 .the_conn/ 目录
    ✅ 创建 epics/ 目录
    ✅ 创建 context/ 目录
    ✅ 创建 ai_workspace/ 目录
    初始化完成！
```

**调用的 Playbook**：`@initialization/project_init.md`

---

## 📋 规划模块（plan）

### `@tc.md plan review` / `@tc.md plan rv`

**功能**：需求与方案评审

**语法**：

```bash
@tc.md plan review [文档路径]
@tc.md plan rv [文档路径]
```

**示例**：

```bash
@tc.md plan review requirements.md
@tc.md plan rv
```

**调用的 Playbook**：`@planning/requirements_review.md`

---

### `@tc.md plan breakdown` / `@tc.md plan bd`

**功能**：需求拆解（批量生成 Epic/Feature/Story）

**语法**：

```bash
@tc.md plan breakdown [文档路径]
@tc.md plan bd [文档路径]
```

**示例**：

```bash
@tc.md plan breakdown requirements.md
@tc.md plan bd
```

**调用的 Playbook**：`@planning/requirements_breakdown.md`

---

### `@tc.md plan change` / `@tc.md plan chg`

**功能**：需求变更管理

**语法**：

```bash
@tc.md plan change [Story ID]
@tc.md plan chg [Story ID]
```

**示例**：

```bash
@tc.md plan change STORY-01
@tc.md plan chg STORY-01
```

**调用的 Playbook**：`@planning/requirements_change.md`

---

### `@tc.md status` / `@tc.md plan status` / `@tc.md plan st`

**功能**：查看项目状态

**语法**：

```bash
@tc.md status [--epic=EPIC-ID]
@tc.md plan status [--epic=EPIC-ID]
@tc.md plan st [--epic=EPIC-ID]
```

**示例**：

```bash
@tc.md status
@tc.md status --epic=EPIC-01
@tc.md plan st
```

**调用的 Playbook**：`@planning/project_status.md`

---

### `@tc.md next` / `@tc.md plan next` / `@tc.md plan n`

**功能**：获取下一步行动建议

**语法**：

```bash
@tc.md next [--context=EPIC-ID]
@tc.md plan next [--context=EPIC-ID]
@tc.md plan n
```

**示例**：

```bash
@tc.md next
@tc.md next --context=EPIC-01
@tc.md plan n
```

**调用的 Playbook**：`@planning/next_step_advisor.md`

---

### `@tc.md epic-init` / `@tc.md plan epic-init` / `@tc.md plan ei`

**功能**：初始化 Epic 基础设施（自动编号、创建目录结构）

**语法**：

```bash
@tc.md epic-init <Epic名称>
@tc.md plan epic-init <Epic名称>
@tc.md plan ei <Epic名称>
```

**示例**：

```bash
@tc.md epic-init 用户管理系统
@tc.md plan epic-init 数据分析模块
@tc.md plan ei 电商平台
```

**功能说明**：
- 自动识别下一个可用的 Epic 编号（如 EPIC-01, EPIC-02）
- 创建 Epic 目录：`.the_conn/epics/EPIC-XX_{PascalCaseName}/`
- 创建上下文目录：`.the_conn/context/epics/EPIC-XX/`
- 生成初始 Epic README.md 文件

**调用的 Playbook**：`@planning/epic_init.md`

---

### `@tc.md epic` / `@tc.md plan epic` / `@tc.md plan e`

**功能**：生成 Epic 规划内容

**语法**：

```bash
@tc.md epic <Epic名称> [--description="描述"]
@tc.md plan epic <Epic名称>
@tc.md plan e <Epic名称>
```

**示例**：

```bash
@tc.md epic 用户管理系统
@tc.md plan epic 用户管理系统 --description="完整的用户管理功能"
@tc.md plan e 电商平台
```

**调用的 Playbook**：`@planning/epic_planning.md`

---

### `@tc.md feature` / `@tc.md plan feature` / `@tc.md plan feat` / `@tc.md plan f`

**功能**：生成 Feature

**语法**：

```bash
@tc.md feature <Feature名称> [--epic=EPIC-ID]
@tc.md plan feature <Feature名称>
@tc.md plan feat <Feature名称>
@tc.md plan f <Feature名称>
```

**示例**：

```bash
@tc.md feature 用户认证
@tc.md feature 用户认证 --epic=EPIC-01
@tc.md plan feat 商品管理
@tc.md plan f 订单处理
```

**调用的 Playbook**：`@planning/feature_planning.md`

---

### `@tc.md story` / `@tc.md plan story` / `@tc.md plan s`

**功能**：生成 Story

**语法**：

```bash
@tc.md story <Story标题> [--feature=FEAT-ID] [--epic=EPIC-ID]
@tc.md plan story <Story标题>
@tc.md plan s <Story标题>
```

**示例**：

```bash
@tc.md story 实现用户登录
@tc.md story 实现用户登录 --feature=FEAT-01
@tc.md plan s 用户注册功能
```

**调用的 Playbook**：`@planning/story_writing.md`

---

### `@tc.md bugfix` / `@tc.md plan bugfix` / `@tc.md plan bug` / `@tc.md plan bf`

**功能**：生成 Bug Fix Story

**语法**：

```bash
@tc.md bugfix <父Story ID> <Bug描述>
@tc.md plan bugfix <父Story ID> <Bug描述>
@tc.md plan bug <父Story ID> <Bug描述>
@tc.md plan bf <父Story ID> <Bug描述>
```

**示例**：

```bash
@tc.md bugfix STORY-01 登录失败处理不当
@tc.md plan bug STORY-01 密码验证错误
@tc.md plan bf STORY-05 商品价格显示错误
```

**调用的 Playbook**：`@planning/bug_fix_story.md`

---

## 📝 上下文模块（ctx）

### `@tc.md ctx extract` / `@tc.md ctx ext` / `@tc.md ctx e`

**功能**：提取 Context 文档

**语法**：

```bash
@tc.md ctx extract [文件路径]
@tc.md ctx ext [文件路径]
@tc.md ctx e [文件路径]
```

**示例**：

```bash
@tc.md ctx extract src/architecture.md
@tc.md ctx ext
@tc.md ctx e docs/design.md
```

**调用的 Playbook**：`@context/extract.md`

---

### `@tc.md ctx add` / `@tc.md ctx a`

**功能**：添加 Context 文档

**语法**：

```bash
@tc.md ctx add --type=<类型> [--scope=global|epic] [--epic=EPIC-ID]
@tc.md ctx a --type=<类型>
```

**Context 类型**：

- Global: `architecture`, `tech_stack`, `coding_standard`, `testing_strategy`, `deployment`, `api_convention`, `domain_model`
- Epic: `module_design`, `data_model`, `api_spec`, `integration`, `algorithm`, `protocol`, `migration`

**示例**：

```bash
@tc.md ctx add --type=architecture --scope=global
@tc.md ctx add --type=module_design --scope=epic --epic=EPIC-01
@tc.md ctx a --type=tech_stack
```

**调用的 Playbook**：`@context/add.md`

---

### `@tc.md ctx update` / `@tc.md ctx upd` / `@tc.md ctx u`

**功能**：更新 Context 文档

**语法**：

```bash
@tc.md ctx update <文件名>
@tc.md ctx upd <文件名>
@tc.md ctx u <文件名>
```

**示例**：

```bash
@tc.md ctx update Architecture.md
@tc.md ctx upd Tech_Stack.md
@tc.md ctx u Module_Design_Core.md
```

**调用的 Playbook**：`@context/update.md`

---

### `@tc.md ctx search` / `@tc.md ctx s`

**功能**：搜索 Context 文档

**语法**：

```bash
@tc.md ctx search <关键词>
@tc.md ctx s <关键词>
```

**示例**：

```bash
@tc.md ctx search 架构设计
@tc.md ctx search authentication
@tc.md ctx s 数据库
```

**调用的 Playbook**：`@context/search.md`

---

## ⚙️ 执行模块（exec）

### `@tc.md task` / `@tc.md exec task` / `@tc.md exec t`

**功能**：生成 Task 简报

**语法**：

```bash
@tc.md task <Story ID>
@tc.md exec task <Story ID>
@tc.md exec t <Story ID>
```

**示例**：

```bash
@tc.md task STORY-01
@tc.md exec task STORY-01
@tc.md exec t STORY-05
```

**调用的 Playbook**：`@execution/task_generation.md`

---

### `@tc.md sync` / `@tc.md exec sync` / `@tc.md exec sy`

**功能**：同步 Story 状态

**语法**：

```bash
@tc.md sync <Story ID>
@tc.md exec sync <Story ID>
@tc.md exec sy <Story ID>
```

**示例**：

```bash
@tc.md sync STORY-01
@tc.md exec sync STORY-01
@tc.md exec sy STORY-01
```

**调用的 Playbook**：`@execution/story_sync.md`

---

### `@tc.md summary` / `@tc.md exec summary` / `@tc.md exec sum`

**功能**：生成变更摘要

**语法**：

```bash
@tc.md summary [Task ID]
@tc.md exec summary [Task ID]
@tc.md exec sum [Task ID]
```

**示例**：

```bash
@tc.md summary
@tc.md exec summary TASK-01
@tc.md exec sum TASK-01
```

**调用的 Playbook**：`@execution/change_summary.md`

---

## 📖 帮助命令

### `@tc.md help`

**功能**：显示帮助信息

**语法**：

```bash
@tc.md help
@tc.md help <模块>
```

**示例**：

```bash
@tc.md help
@tc.md help plan
@tc.md help ctx
@tc.md help exec
```

---

### `@tc.md list`

**功能**：列出所有可用命令

**语法**：

```bash
@tc.md list
```

---

## 🔤 命令缩写对照表

### 规划模块（plan）

| 命令 | 缩写 1 | 缩写 2 | 一级快捷 |
|------|--------|--------|---------|
| `plan review` | `rv` | - | ❌ |
| `plan breakdown` | `bd` | - | ❌ |
| `plan change` | `chg` | - | ❌ |
| `plan status` | `st` | - | ✅ `status` |
| `plan next` | `n` | - | ✅ `next` |
| `plan epic` | `e` | - | ✅ `epic` |
| `plan feature` | `feat` | `f` | ✅ `feature` |
| `plan story` | `s` | - | ✅ `story` |
| `plan bugfix` | `bug` | `bf` | ✅ `bugfix` |

### 上下文模块（ctx）

| 命令 | 缩写 1 | 缩写 2 |
|------|--------|--------|
| `ctx extract` | `ext` | `e` |
| `ctx add` | `a` | - |
| `ctx update` | `upd` | `u` |
| `ctx search` | `s` | - |

### 执行模块（exec）

| 命令 | 缩写 1 | 缩写 2 | 一级快捷 |
|------|--------|--------|---------|
| `exec task` | `t` | - | ✅ `task` |
| `exec sync` | `sy` | - | ✅ `sync` |
| `exec summary` | `sum` | - | ✅ `summary` |

---

## 🌐 中文命令对照表

| 英文命令 | 中文命令 |
|---------|---------|
| `@tc.md init` | `@tc.md 初始化` |
| `@tc.md status` | `@tc.md 状态` |
| `@tc.md next` | `@tc.md 下一步` |
| `@tc.md epic` | `@tc.md 史诗` |
| `@tc.md feature` | `@tc.md 特性` |
| `@tc.md story` | `@tc.md 故事` |
| `@tc.md bugfix` | `@tc.md 缺陷` |
| `@tc.md task` | `@tc.md 任务` |
| `@tc.md sync` | `@tc.md 同步` |
| `@tc.md summary` | `@tc.md 摘要` |
| `@tc.md help` | `@tc.md 帮助` |

---

## 🎯 使用场景

### 场景 1：初始化到开发

```bash
@tc.md init                              # 初始化项目
@tc.md epic 用户系统                      # 创建 Epic
@tc.md feature 用户认证 --epic=EPIC-01   # 创建 Feature
@tc.md story 登录功能 --feature=FEAT-01  # 创建 Story
@tc.md task STORY-01                     # 生成 Task
# 开发完成后
@tc.md sync STORY-01                     # 同步状态
@tc.md next                              # 查看下一步
```

### 场景 2：批量规划

```bash
@tc.md plan bd requirements.md   # 拆解需求
@tc.md status                    # 查看生成的规划
@tc.md next                      # 获取建议
```

### 场景 3：Bug 修复

```bash
@tc.md bugfix STORY-05 价格计算错误   # 创建 Bug Fix
@tc.md task STORY-05.1                # 生成 Task
# 修复完成后
@tc.md sync STORY-05.1                # 同步状态
```

### 场景 4：Context 管理

```bash
@tc.md ctx a --type=architecture      # 添加架构文档
@tc.md ctx a --type=tech_stack        # 添加技术栈
@tc.md ctx s 架构                     # 搜索
@tc.md ctx u Architecture.md          # 更新
```

---

## 💡 最佳实践

### 1. 优先使用一级快捷命令

```bash
# 推荐 ✅
@tc.md story 用户登录
@tc.md status
@tc.md next

# 可以，但更长 ⚠️
@tc.md plan story 用户登录
@tc.md plan status
@tc.md plan next
```

### 2. 使用缩写提高效率

```bash
# 完整命令
@tc.md plan breakdown requirements.md
@tc.md ctx extract design.md

# 缩写（更快）✅
@tc.md plan bd requirements.md
@tc.md ctx e design.md
```

### 3. 合理使用参数

```bash
# 带参数一次完成
@tc.md story 用户登录 --feature=FEAT-01 --epic=EPIC-01

# 分步确认（更安全）
@tc.md story 用户登录
# AI 会询问选择 Feature 和 Epic
```

### 4. 查看帮助

```bash
# 不确定命令时
@tc.md help
@tc.md help plan

# 查看所有命令
@tc.md list
```

---

## 🔗 相关文档

- 📘 [快速开始指南](QUICK_START.md)
- 📗 [统一入口 Playbook](../playbooks/tc.md)
- 📕 [核心规则](../playbooks/core/core.md)

---

**💡 提示**：所有命令不区分大小写，`@TC`, `@Tc`, `@tc` 效果相同！
