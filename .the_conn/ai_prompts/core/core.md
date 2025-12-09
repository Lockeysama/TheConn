# AI 领航员的敏捷工作流

## 引言

本 playbook 为采用 AI 辅助开发的团队，提供了一套端到端的人机协作工作流。它将人类工程师的战略洞察与 AI 的编码执行能力相结合，通过结构化、版本化的项目管理流程，实现高效的开发协作。

---

## 第一部分：核心原则

1. **意图与实现的分离**: 人类领航员定义"做什么"（意图），AI 编码引擎负责"怎么做"（实现）。

2. **规划即代码 (Planning as Code)**: 所有规划（Epics, Features, Stories）都作为 Markdown 文件存放在代码库中，与源代码同步版本化管理。

3. **上下文精准投喂**: 通过清单机制，为每个任务动态组合最相关的上下文，避免信息过载，提升 AI 输出的准确性。

4. **双向同步**: 不仅从"意图"驱动"实现"，也要在"实现"完成后，将变更同步回"意图"，确保文档与代码的持续一致。

---

## 第二部分：项目目录结构

```
my_project/
├── .the_conn/                  # [AI协作层] AI 工具和上下文知识库
│   ├── context/                # [知识层] 项目的全局上下文知识库
│   │   ├── 00_ARCHITECTURE.md
│   │   └── 10_MODULE_DESIGN.md
│   │
│   ├── ai_prompts/             # [工具层] Prompt 模板
│   │   ├── core/
│   │   │   └── core.md
│   │   └── templates/
│   │       ├── story_template.md
│   │       ├── bug_story_template.md
│   │       ├── task_generation.md
│   │       └── ...
│   │
│   └── ai_workspace/           # [执行层] AI 任务的临时工作区
│       └── {TASK-ID}/
│           ├── task.md
│           ├── context.manifest.json
│           └── change_summary.md
│
├── epics/                      # [规划层] 所有规划文档
│   └── {EPIC-ID}/
│       ├── README.md
│       └── features/
│           └── {FEAT-ID}/
│               ├── README.md
│               └── stories/
│                   └── {STORY-ID}_{Name}.md
│
├── src/                        # [实现层] 项目源代码
│
└── tests/                      # [验证层] 所有测试代码
    ├── bdd/
    │   ├── features/           # BDD Gherkin 特性文件
    │   └── step_defs/
    └── unit/
```

---

## 第三部分：四阶段工作流程

### 阶段一：战略规划与意图定义

在 `epics/` 目录下，将业务需求转化为结构化的 Markdown 文件。

1. **定义 Epic 与 Feature**: 通过 `README.md` 文件定义高阶的目标和功能模块。
2. **撰写 Story**: 在 `stories/` 目录下，为每个可开发任务创建详尽的 Story 文件。

### 阶段二：任务执行准备

为 AI 准备好所有执行材料。

1. **生成工作区**: 在 `.the_conn/ai_workspace/{TASK-ID}/` 下创建任务目录。
2. **准备上下文**: 创建 `context.manifest.json` 和 `task.md`。
3. **组装 Prompt**: 加载模板，填充上下文和任务简报，发送给 AI。

### 阶段三：代码实现与审查

AI 根据指令执行开发任务。

1. **AI 生成代码**: 根据 Story 中的 BDD 场景，创建测试和业务逻辑代码。
2. **提交 PR**: AI 将变更提交为 Pull Request。
3. **人类审查**: 领航员审查代码的逻辑、架构符合性。

### 阶段四：同步与闭环

PR 合并后，确保"意图"与"实现"的一致性。

1. **合并 PR**: 领航员将通过审查的 PR 合并。
2. **触发同步**: 使用同步模板更新 Story 文档。
3. **确认提交**: 领航员确认并提交 Story 的更新。

---

## 第四部分：关键概念

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

### 文件命名规则

| 类型 | 格式 | 示例 |
|------|------|------|
| Story | `{ID}_{Name}.md` | `DS-104_Dynamic_Piggybacking.md` |
| Bug Fix | `{ID}_{Name}.md` | `DS-104.1_Concurrency_Fix.md` |

---

## 附录：模板索引

| 用途 | 模板文件 |
|------|----------|
| 生成 Epic | `templates/epic_template.md` |
| 生成 Feature | `templates/feature_template.md` |
| 生成 Story | `templates/story_template.md` |
| 生成 Bug Fix Story | `templates/bug_story_template.md` |
| 生成 Task 简报 | `templates/task_generation.md` |
| 生成 Context 文档 | `templates/context_generation.md` |
| 同步 Story | `templates/story_synchronization.md` |
| 生成变更摘要 | `templates/change_summary.md` |
