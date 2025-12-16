# The Conn Playbooks 操作手册

本文档介绍 The Conn 框架的所有 AI 操作剧本（Playbooks），用于生成和管理项目的规划文档、任务执行和同步闭环。

---

## Playbooks 分类

### 初始化 Playbooks

用于项目初始化。

| Playbook 文件                              | 用途                         |
| ------------------------------------------ | ---------------------------- |
| `playbooks/initialization/project_init.md` | 初始化项目结构和公共 Context |

### Context 管理 Playbooks

用于知识库管理。

| Playbook 文件                  | 用途                        |
| ------------------------------ | --------------------------- |
| `playbooks/context/extract.md` | 从技术方案提取 Context 文档 |
| `playbooks/context/add.md`     | 添加新 Context 文档         |
| `playbooks/context/update.md`  | 更新现有 Context 文档       |
| `playbooks/context/search.md`  | 搜索相关 Context 文档       |

### 规划层 Playbooks

用于需求评审、拆解和创建规划文档。

| Playbook 文件                                  | 用途                                     |
| ---------------------------------------------- | ---------------------------------------- |
| `playbooks/planning/requirements_review.md`    | 需求与技术方案评审                       |
| `playbooks/planning/requirements_breakdown.md` | 需求拆解（批量生成 Epic/Feature/Story）  |
| `playbooks/planning/requirements_change.md`    | 需求变更管理                             |
| `playbooks/planning/project_status.md`         | 项目状态查看                             |
| `playbooks/planning/epic_planning.md`          | 生成 Epic 规划文档                       |
| `playbooks/planning/feature_planning.md`       | 生成 Feature 规划文档                    |
| `playbooks/planning/story_writing.md`          | 生成 Story 文件（type: dev）             |
| `playbooks/planning/bug_fix_story.md`          | 生成 Bug Fix Story 文件（type: bug_fix） |

### 执行层 Playbooks

用于完整的任务执行流程（开发 + 测试 + 同步 + 总结）。

| Playbook 文件                            | 用途                                |
| ---------------------------------------- | ----------------------------------- |
| `playbooks/execution/task_generation.md` | 生成任务简报（包含完整执行流程）    |
| `playbooks/execution/story_sync.md`      | 同步 Story 状态（任务闭环的一部分） |
| `playbooks/execution/change_summary.md`  | 生成变更摘要（任务闭环的一部分）    |

### 核心指南

| 文档                           | 内容                |
| ------------------------------ | ------------------- |
| `playbooks/core/core.md`       | AI 领航员敏捷工作流 |
| `playbooks/core/base_rules.md` | 基础公约与规则      |

---

## 工作流程图

### 标准开发流程

```
0. 初始化阶段
   └── @playbooks/initialization/project_init.md → 初始化项目结构
                ↓
1. 评审阶段
   └── @playbooks/planning/requirements_review.md → 需求与方案评审
                ↓
2. 规划阶段
   ├── @playbooks/context/extract.md → 提取 Context
   ├── 方案 A（推荐）:
   │   └── @playbooks/planning/requirements_breakdown.md → 批量生成 Epic/Feature/Story
   └── 方案 B（精细控制）:
       ├── @playbooks/planning/epic_planning.md → 逐个创建 Epic
       ├── @playbooks/planning/feature_planning.md → 逐个创建 Feature
       └── @playbooks/planning/story_writing.md → 逐个创建 Story
                ↓
3. 准备阶段
   └── @playbooks/execution/task_generation.md → 生成任务简报（含闭环流程）
                ↓
4. 执行阶段
   ├── AI 执行 Step 1-5（开发 + 测试）
   ├── 人工 Review 检查点 ⚠️
   └── AI 执行 Step 6-7（生成摘要 + 同步 Story）← 显式确认后自动执行
```

### Bug Fix 流程

```
Story 完成并合并
        ↓
   发现 Bug ❌
        ↓
1. 创建 Bug Fix Story
   └── bug_story_template.md
        ↓
2. 执行修复
   └── 使用标准工作流
        ↓
3. 同步更新
   └── 更新 Story 状态为 done
```

---

## 关键概念

### ID 命名规范

| 类型    | 格式                    | 示例         |
| ------- | ----------------------- | ------------ |
| Epic    | `EPIC-{序号}`           | `EPIC-01`    |
| Feature | `FEAT-{序号}`           | `FEAT-01`    |
| Story   | `STORY-{序号}`          | `STORY-01`   |
| Bug Fix | `STORY-{序号}.{子序号}` | `STORY-01.1` |
| Task    | `TASK-{序号}`           | `TASK-01`    |

### Story 类型与状态

**Type**: `dev` (新功能) | `bug_fix` (缺陷修复)

**Status**: `pending` (未完成) | `done` (已完成)

### 文件命名规范

**格式**: `{ID}_{PascalCaseName}.md`

**示例**:
- `EPIC-01_Base_Init/`
- `STORY-01_Create_Structure.md`
- `TASK-01_STORY-01_Create_Structure/`

### Task 与 Story 关系

- **1:1** - 正常：一个 Story → 一个 Task
- **1:N** - 迭代：一个 Story → 多个 Task（开发 + 优化 + 修复）

---

## 快速使用

### 项目初始化

```
@playbooks/initialization/project_init.md 帮我初始化 The Conn 项目
```

### 评审需求和方案

```
@{需求文档} @playbooks/planning/requirements_review.md 开始评审
```

### 批量生成规划

```
@{需求文档} @{技术方案} @playbooks/planning/requirements_breakdown.md 开始拆解
```

### 提取 Context

```
@{技术方案文档} @playbooks/context/extract.md 帮我提取 Context 文档
```

### 单独创建 Story

```
@{需求描述} @playbooks/planning/story_writing.md 帮我生成 Story
```

### 创建 Bug Fix Story

```
@playbooks/planning/bug_fix_story.md 帮我生成 Bug Fix Story

父 Story: STORY-01
发现于: 集成测试
现象: ...
```

### 生成任务简报

```
@{Story文件} @playbooks/execution/task_generation.md 帮我生成 Task
```

### 执行任务（含自动闭环）

```
@.the_conn/ai_workspace/EPIC-XX/TASK-XX_STORY-XX_Name/ 开始任务
# AI 执行 Step 1-5
# 人工 Review
# 确认后：请继续执行 Step 6-7 完成任务闭环
```

---

## 目录结构

```
.the_conn/
├── epics/                          # 规划层
│   └── EPIC-01_Base_Init/
│       └── features/
│           └── FEAT-01_Init_Project/
│               └── stories/
│                   └── STORY-01_Create_Structure.md
│
├── context/                        # 知识层
│   ├── global/                     # 公共 Context
│   │   ├── Architecture.md
│   │   └── Tech_Stack.md
│   └── epics/                      # Epic 专属 Context
│       └── EPIC-01/
│           └── Module_Design.md
│
├── playbooks/                      # 工具层（AI 操作剧本）
│   ├── core/
│   │   ├── core.md
│   │   └── base_rules.md
│   ├── initialization/
│   ├── planning/
│   ├── context/
│   └── execution/
│
├── docs/                           # 用户文档（AI 严禁修改）
│   ├── README.md                   # 本文件
│   └── GUIDE.md                    # 使用指南
│
└── ai_workspace/                   # 执行层（临时工作区）
    └── EPIC-01/
        └── TASK-01_STORY-01_Create_Structure/
            ├── task.md
            └── context.manifest.json
```

---

## 相关资源

- **核心工作流**: `@playbooks/core/core.md`
- **基础公约**: `@playbooks/core/base_rules.md`
- **使用指南**: `@docs/GUIDE.md`
