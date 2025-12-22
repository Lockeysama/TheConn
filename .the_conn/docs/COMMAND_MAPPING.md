# The Conn - 命令映射表

本文档展示 `@tc` 命令与底层 Playbook 文件的完整映射关系。

## 📋 完整映射表

### 初始化命令

| @tc.md 命令   | Playbook 路径                     |
| ------------- | --------------------------------- |
| `@tc.md init` | `@initialization/project_init.md` |

---

### 规划模块（plan）

#### 完整命令

| @tc.md 命令                | Playbook 路径                            |
| -------------------------- | ---------------------------------------- |
| `@tc.md plan review`       | `@planning/requirements_review.md`       |
| `@tc.md plan breakdown`    | `@planning/requirements_breakdown.md`    |
| `@tc.md plan change`       | `@planning/requirements_change.md`       |
| `@tc.md plan status`       | `@planning/project_status.md`            |
| `@tc.md plan next`         | `@planning/next_step_advisor.md`         |
| `@tc.md plan epic-init`    | `@planning/epic_init.md`                 |
| `@tc.md plan epic`         | `@planning/epic_planning.md`             |
| `@tc.md plan feature`      | `@planning/feature_planning.md`          |
| `@tc.md plan story`        | `@planning/story_writing.md`             |
| `@tc.md plan e2e`          | `@planning/e2e_story.md`                 |
| `@tc.md plan perf`         | `@planning/performance_test_story.md`    |
| `@tc.md plan bugfix`       | `@planning/bug_fix_story.md`             |

#### 缩写命令

| @tc.md 缩写             | 原命令                  | Playbook 路径                            |
| ----------------------- | ----------------------- | ---------------------------------------- |
| `@tc.md plan rv`        | `@tc.md plan review`    | `@planning/requirements_review.md`       |
| `@tc.md plan bd`        | `@tc.md plan breakdown` | `@planning/requirements_breakdown.md`    |
| `@tc.md plan chg`       | `@tc.md plan change`    | `@planning/requirements_change.md`       |
| `@tc.md plan st`        | `@tc.md plan status`    | `@planning/project_status.md`            |
| `@tc.md plan n`         | `@tc.md plan next`      | `@planning/next_step_advisor.md`         |
| `@tc.md plan ei`        | `@tc.md plan epic-init` | `@planning/epic_init.md`                 |
| `@tc.md plan e`         | `@tc.md plan epic`      | `@planning/epic_planning.md`             |
| `@tc.md plan feat`      | `@tc.md plan feature`   | `@planning/feature_planning.md`          |
| `@tc.md plan f`         | `@tc.md plan feature`   | `@planning/feature_planning.md`          |
| `@tc.md plan s`         | `@tc.md plan story`     | `@planning/story_writing.md`             |
| `@tc.md plan ee`        | `@tc.md plan e2e`       | `@planning/e2e_story.md`                 |
| `@tc.md plan performance` | `@tc.md plan perf`    | `@planning/performance_test_story.md`    |
| `@tc.md plan p`         | `@tc.md plan perf`      | `@planning/performance_test_story.md`    |
| `@tc.md plan bug`       | `@tc.md plan bugfix`    | `@planning/bug_fix_story.md`             |
| `@tc.md plan bf`        | `@tc.md plan bugfix`    | `@planning/bug_fix_story.md`             |

#### 一级快捷命令

| @tc.md 快捷命令    | 等同于                  | Playbook 路径                         |
| ------------------ | ----------------------- | ------------------------------------- |
| `@tc.md status`    | `@tc.md plan status`    | `@planning/project_status.md`         |
| `@tc.md next`      | `@tc.md plan next`      | `@planning/next_step_advisor.md`      |
| `@tc.md epic-init` | `@tc.md plan epic-init` | `@planning/epic_init.md`              |
| `@tc.md epic`      | `@tc.md plan epic`      | `@planning/epic_planning.md`          |
| `@tc.md feature`   | `@tc.md plan feature`   | `@planning/feature_planning.md`       |
| `@tc.md story`     | `@tc.md plan story`     | `@planning/story_writing.md`          |
| `@tc.md e2e`       | `@tc.md plan e2e`       | `@planning/e2e_story.md`              |
| `@tc.md perf`      | `@tc.md plan perf`      | `@planning/performance_test_story.md` |
| `@tc.md bugfix`    | `@tc.md plan bugfix`    | `@planning/bug_fix_story.md`          |

---

### 上下文模块（ctx）

#### 完整命令

| @tc.md 命令          | Playbook 路径         |
| -------------------- | --------------------- |
| `@tc.md ctx extract` | `@context/extract.md` |
| `@tc.md ctx add`     | `@context/add.md`     |
| `@tc.md ctx update`  | `@context/update.md`  |
| `@tc.md ctx search`  | `@context/search.md`  |

#### 缩写命令

| @tc.md 缩写      | 原命令               | Playbook 路径         |
| ---------------- | -------------------- | --------------------- |
| `@tc.md ctx ext` | `@tc.md ctx extract` | `@context/extract.md` |
| `@tc.md ctx e`   | `@tc.md ctx extract` | `@context/extract.md` |
| `@tc.md ctx a`   | `@tc.md ctx add`     | `@context/add.md`     |
| `@tc.md ctx upd` | `@tc.md ctx update`  | `@context/update.md`  |
| `@tc.md ctx u`   | `@tc.md ctx update`  | `@context/update.md`  |
| `@tc.md ctx s`   | `@tc.md ctx search`  | `@context/search.md`  |

---

### 执行模块（exec）

#### 完整命令

| @tc.md 命令           | Playbook 路径                   |
| --------------------- | ------------------------------- |
| `@tc.md exec task`    | `@execution/task_generation.md` |
| `@tc.md exec sync`    | `@execution/story_sync.md`      |
| `@tc.md exec summary` | `@execution/change_summary.md`  |

#### 缩写命令

| @tc.md 缩写       | 原命令                | Playbook 路径                   |
| ----------------- | --------------------- | ------------------------------- |
| `@tc.md exec t`   | `@tc.md exec task`    | `@execution/task_generation.md` |
| `@tc.md exec sy`  | `@tc.md exec sync`    | `@execution/story_sync.md`      |
| `@tc.md exec sum` | `@tc.md exec summary` | `@execution/change_summary.md`  |

#### 一级快捷命令

| @tc.md 快捷命令  | 等同于                | Playbook 路径                   |
| ---------------- | --------------------- | ------------------------------- |
| `@tc.md task`    | `@tc.md exec task`    | `@execution/task_generation.md` |
| `@tc.md sync`    | `@tc.md exec sync`    | `@execution/story_sync.md`      |
| `@tc.md summary` | `@tc.md exec summary` | `@execution/change_summary.md`  |

---

### 帮助命令

| @tc.md 命令   | 功能                                      |
| ------------- | ----------------------------------------- |
| `@tc.md help` | 显示帮助信息（内置功能，无对应 Playbook） |
| `@tc.md list` | 列出所有命令（内置功能，无对应 Playbook） |

---

## 🔄 反向映射（Playbook → 命令）

如果你知道 Playbook 文件，想知道对应的 @tc.md 命令：

| Playbook 文件                        | 推荐命令                | 所有可用命令                                                                 |
| ------------------------------------ | ----------------------- | ---------------------------------------------------------------------------- |
| `initialization/project_init.md`     | `@tc.md init`           | `@tc.md init`                                                                |
| `planning/requirements_review.md`    | `@tc.md plan review`    | `@tc.md plan review`, `@tc.md plan rv`                                       |
| `planning/requirements_breakdown.md` | `@tc.md plan breakdown` | `@tc.md plan breakdown`, `@tc.md plan bd`                                    |
| `planning/requirements_change.md`    | `@tc.md plan change`    | `@tc.md plan change`, `@tc.md plan chg`                                      |
| `planning/project_status.md`         | `@tc.md status`         | `@tc.md status`, `@tc.md plan status`, `@tc.md plan st`                      |
| `planning/next_step_advisor.md`      | `@tc.md next`           | `@tc.md next`, `@tc.md plan next`, `@tc.md plan n`                           |
| `planning/epic_planning.md`          | `@tc.md epic`           | `@tc.md epic`, `@tc.md plan epic`, `@tc.md plan e`                           |
| `planning/feature_planning.md`       | `@tc.md feature`        | `@tc.md feature`, `@tc.md plan feature`, `@tc.md plan feat`, `@tc.md plan f` |
| `planning/story_writing.md`          | `@tc.md story`          | `@tc.md story`, `@tc.md plan story`, `@tc.md plan s`                         |
| `planning/bug_fix_story.md`          | `@tc.md bugfix`         | `@tc.md bugfix`, `@tc.md plan bugfix`, `@tc.md plan bug`, `@tc.md plan bf`   |
| `context/extract.md`                 | `@tc.md ctx extract`    | `@tc.md ctx extract`, `@tc.md ctx ext`, `@tc.md ctx e`                       |
| `context/add.md`                     | `@tc.md ctx add`        | `@tc.md ctx add`, `@tc.md ctx a`                                             |
| `context/update.md`                  | `@tc.md ctx update`     | `@tc.md ctx update`, `@tc.md ctx upd`, `@tc.md ctx u`                        |
| `context/search.md`                  | `@tc.md ctx search`     | `@tc.md ctx search`, `@tc.md ctx s`                                          |
| `execution/task_generation.md`       | `@tc.md task`           | `@tc.md task`, `@tc.md exec task`, `@tc.md exec t`                           |
| `execution/story_sync.md`            | `@tc.md sync`           | `@tc.md sync`, `@tc.md exec sync`, `@tc.md exec sy`                          |
| `execution/change_summary.md`        | `@tc.md summary`        | `@tc.md summary`, `@tc.md exec summary`, `@tc.md exec sum`                   |

---

## 📊 命令层次结构

```
@tc
├── init                          → @initialization/project_init.md
│
├── plan                          
│   ├── review (rv)               → @planning/requirements_review.md
│   ├── breakdown (bd)            → @planning/requirements_breakdown.md
│   ├── change (chg)              → @planning/requirements_change.md
│   ├── status (st)    [快捷: @tc.md status]  → @planning/project_status.md
│   ├── next (n)       [快捷: @tc.md next]    → @planning/next_step_advisor.md
│   ├── epic (e)       [快捷: @tc.md epic]    → @planning/epic_planning.md
│   ├── feature (feat, f) [快捷: @tc.md feature] → @planning/feature_planning.md
│   ├── story (s)      [快捷: @tc.md story]   → @planning/story_writing.md
│   └── bugfix (bug, bf) [快捷: @tc.md bugfix] → @planning/bug_fix_story.md
│
├── ctx
│   ├── extract (ext, e)          → @context/extract.md
│   ├── add (a)                   → @context/add.md
│   ├── update (upd, u)           → @context/update.md
│   └── search (s)                → @context/search.md
│
├── exec
│   ├── task (t)       [快捷: @tc.md task]    → @execution/task_generation.md
│   ├── sync (sy)      [快捷: @tc.md sync]    → @execution/story_sync.md
│   └── summary (sum)  [快捷: @tc.md summary] → @execution/change_summary.md
│
└── help / list                   (内置功能)
```

---

## 🎯 核心 Playbook（不直接调用）

以下是核心规范 Playbook，不通过 @tc.md 命令直接调用，而是被其他 Playbook 引用：

| Playbook 文件                 | 用途           |
| ----------------------------- | -------------- |
| `core/core.md`                | 框架核心文档   |
| `core/base_rules.md`          | 基础公约       |
| `core/test_strategy_rules.md` | 测试策略规范   |
| `core/complexity_rules.md`    | 复杂度评估规范 |
| `core/bdd_language_rules.md`  | BDD 语言配置   |

这些文件通过 `@` 符号在其他 Playbook 中引用，例如：

- `@playbooks/core/base_rules.md`
- `@playbooks/core/test_strategy_rules.md`

---

## 💡 使用建议

### 1. 新手推荐

使用一级快捷命令，简单直接：

```bash
@tc.md init
@tc.md epic 用户系统
@tc.md feature 用户认证
@tc.md story 登录功能
@tc.md task STORY-01
@tc.md status
@tc.md next
```

### 2. 熟练用户

使用缩写提高效率：

```bash
@tc.md init
@tc.md plan e 用户系统
@tc.md plan f 用户认证
@tc.md plan s 登录功能
@tc.md exec t STORY-01
@tc.md plan st
@tc.md plan n
```

### 3. 完整路径（不推荐）

如果你已经习惯了直接使用 Playbook，也可以继续：

```bash
@planning/story_writing.md
@execution/task_generation.md
```

但推荐迁移到 `@tc` 命令以获得更好的用户体验。

---

## 🔗 相关文档

- 📘 [快速开始指南](QUICK_START.md)
- 📗 [命令参考手册](COMMANDS.md)
- 📕 [完整使用指南](GUIDE.md)

---

**最后更新**：2024年

**维护者**：The Conn Framework
