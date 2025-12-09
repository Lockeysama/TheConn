# AI Prompts 模板库

本目录包含所有 AI 协作开发的 Prompt 模板，用于生成和管理项目的规划文档、任务执行和同步闭环。

---

## 模板分类

### 规划层模板

用于创建 Epic、Feature、Story 的规划文档。

| 模板文件 | 用途 |
|----------|------|
| `templates/epic_template.md` | 生成 Epic 规划文档 |
| `templates/feature_template.md` | 生成 Feature 规划文档 |
| `templates/story_template.md` | 生成 Story 文件（type: dev） |
| `templates/bug_story_template.md` | 生成 Bug Fix Story 文件（type: bug_fix） |

### 执行层模板

用于 AI 任务执行和上下文管理。

| 模板文件 | 用途 |
|----------|------|
| `templates/task_generation.md` | 从 Story 生成任务简报 |
| `templates/context_generation.md` | 生成上下文清单 |

### 同步层模板

用于实现与意图的双向同步。

| 模板文件 | 用途 |
|----------|------|
| `templates/story_synchronization.md` | 同步 Story 与代码变更 |
| `templates/change_summary.md` | 生成代码变更摘要 |

### 指南文档

| 文档 | 内容 |
|------|------|
| `BUG_WORKFLOW_GUIDE.md` | Bug Fix 工作流指南 |
| `core/core.md` | AI 领航员敏捷工作流 |

---

## 工作流程图

### 标准开发流程

```
1. 规划阶段
   ├── epic_template.md → 创建 Epic
   ├── feature_template.md → 创建 Feature
   └── story_template.md → 创建 Story
                ↓
2. 准备阶段
   ├── context_generation.md → 生成上下文清单
   └── task_generation.md → 生成任务简报
                ↓
3. 执行阶段
   └── AI 根据任务简报实现功能
                ↓
4. 同步阶段
   ├── change_summary.md → 生成变更摘要
   └── story_synchronization.md → 同步 Story
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

### Story 类型

| Type | 说明 | ID 格式 |
|------|------|---------|
| `dev` | 新功能开发 | `{PREFIX}-{序号}`，如 `DS-104` |
| `bug_fix` | 缺陷修复 | `{父ID}.{序号}`，如 `DS-104.1` |

### Story 状态

| Status | 说明 |
|--------|------|
| `pending` | 未完成 |
| `done` | 已完成 |

### 文件命名

```
{ID}_{Snake_Case_Name}.md
```

示例：`DS-104_Dynamic_Piggybacking.md`

---

## 快速使用

### 创建新 Story

```
# 向 AI 提供需求，使用模板生成
请使用 story_template.md 模板，根据以下需求生成 Story：
{需求描述}
```

### 创建 Bug Fix Story

```
请使用 bug_story_template.md 模板，根据以下信息生成 Bug Fix Story：

父 Story: DS-104
发现于: 集成测试
现象:
  - 场景: ...
  - 预期: ...
  - 实际: ...
```

### 生成任务简报

```
请使用 task_generation.md 模板，从 DS-104 Story 生成任务简报
```

### 同步 Story

```
请使用 story_synchronization.md 模板，更新 DS-104 Story
```

---

## 目录结构

```
.the_conn/
├── context/                # 项目上下文知识库
│   ├── 00_ARCHITECTURE.md
│   └── 10_MODULE_DESIGN.md
│
├── ai_prompts/
│   ├── core/
│   │   └── core.md         # 核心工作流说明
│   └── templates/          # 所有模板
│
├── ai_workspace/           # AI 任务工作区
│   └── {TASK-ID}/
│
├── README.md               # 本文件
├── GUIDE.md                # 使用指南
└── BUG_WORKFLOW_GUIDE.md   # Bug Fix 工作流指南
```

---

## 相关资源

- **核心工作流**: `core/core.md`
- **Bug Fix 指南**: `BUG_WORKFLOW_GUIDE.md`
- **使用指南**: `GUIDE.md`
