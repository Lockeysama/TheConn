# The Conn 使用指南

本指南说明如何使用 The Conn 框架完成 AI 辅助开发任务。框架设计理念请参阅 `ai_prompts/core/core.md`。

---

## 工作流程

### 流程零：项目初始化

**场景**: 首次使用 The Conn 框架，需要初始化项目结构和公共 Context。

**步骤**:

1. **项目初始化**：
   ```
   @prompts/initialization/project_init.md 帮我初始化 The Conn 项目
   ```
   → 创建目录结构：`.the_conn/epics/`, `.the_conn/context/`, `.the_conn/ai_workspace/`

2. **定义初始公共 Context**：
   根据项目特点，创建必要的全局 Context：
   - `Architecture.md` - 系统架构
   - `Tech_Stack.md` - 技术栈
   - `Coding_Standard_{Language}.md` - 编码规范
   - `Testing_Strategy.md` - 测试策略

### 流程一：从需求到规划

**场景**: 收到外部需求文档（PRD、用户故事等），需要拆解为可执行的开发任务。

**步骤**:

#### 方案 A: 批量生成（推荐，快速高效）

1. **需求与方案评审**：
   ```
   @{需求文档} @prompts/planning/requirements_review.md 开始评审
   ```
   → 与 AI 讨论需求和技术方案，输出确定的技术方案文档

2. **提取 Context 文档**（方案确定后）：
   ```
   @{技术方案文档} @prompts/context/extract.md 帮我提取 Context 文档
   ```
   → 输出到 `.the_conn/context/global/` 或 `.the_conn/context/epics/EPIC-XX/`

3. **批量生成规划**：
   ```
   @{需求文档} @{技术方案} @prompts/planning/requirements_breakdown.md 开始拆解
   ```
   → AI 展示大纲 → 用户确认 → 批量生成所有 Epic/Feature/Story

#### 方案 B: 逐个生成（精细控制）

1. **需求与方案评审**（同上）

2. **提取 Context 文档**（同上）

3. **生成 Epic 规划**：
   ```
   @{需求文档} @prompts/planning/epic_planning.md 帮我生成 Epic 规划
   ```
   → 输出到 `.the_conn/epics/EPIC-XX_Name/README.md`

4. **生成 Feature 规划**：
   ```
   @{需求文档} @prompts/planning/feature_planning.md 帮我生成 Feature 规划
   ```
   → 输出到 `.the_conn/epics/EPIC-XX_Name/features/FEAT-XX_Name/README.md`

5. **生成 Story**：
   ```
   @{需求文档} @prompts/planning/story_writing.md 帮我拆解为 Story
   ```
   → 输出到 `.the_conn/epics/.../stories/STORY-XX_Name.md`

6. 审查 AI 生成的文档，确认后提交

### 流程二：从 Story 到 Task

**场景**: Story 已就绪，需要为 AI 准备任务执行材料。

**步骤**:

1. 使用 Prompt 生成任务简报：
   ```
   @{Story文件} @prompts/execution/task_generation.md 帮我生成 Task
   ```

2. AI 会在 `.the_conn/ai_workspace/EPIC-XX/TASK-XX_STORY-XX_Name/` 下生成：
   - `task.md` - 任务简报（强调 BDD/TDD 测试先行）
   - `context.manifest.json` - 上下文清单

3. 审查生成的文件，补充必要的上下文引用

**注意**: Task ID 在 Epic 内顺序编号，一个 Story 可能对应多个 Task（开发、测试、修复）

### 流程三：执行开发任务

**场景**: Task 已准备好，开始 AI 辅助编码。

**步骤**:

1. 启动任务：
   ```
   @.the_conn/ai_workspace/EPIC-XX/TASK-XX_STORY-XX_Name/ 开始任务
   ```

2. AI 按 BDD/TDD 流程执行（Step 1-5）：
   - 先创建/更新 `.feature` 文件和测试代码
   - 再实现业务逻辑使测试通过
   - 运行测试验证

3. **人工 Review 检查点** ⚠️：
   - 审查代码实现
   - 审查测试覆盖
   - 确认符合预期

4. 确认通过后，执行任务闭环（Step 6-7）：
   ```
   请继续执行 Step 6 和 Step 7 完成任务闭环
   ```
   - AI 自动生成变更摘要
   - AI 自动同步 Story 状态

### 流程四：任务闭环

**场景**: 代码实现完成，需要同步文档并归档。

**步骤**:

**注意**: 如果在流程三执行了任务闭环（Step 6-7），则此步骤已自动完成，无需重复执行。

如果需要单独执行：

1. 生成变更摘要：
   ```
   @prompts/execution/change_summary.md 生成本次任务的变更摘要
   ```

2. 同步 Story 文档：
   ```
   @{原始Story文件} @prompts/execution/story_sync.md 开始同步
   ```

3. 审查并提交所有变更

### 流程五：Bug 修复

**场景**: 已完成的 Story 在测试或生产环境发现 Bug。

**步骤**:

1. 创建 Bug Fix Story：
   ```
   @prompts/planning/bug_fix_story.md 帮我生成 Bug Fix Story
   
   父 Story: STORY-01
   发现于: 集成测试
   现象: ...
   ```
   → 输出到 `.the_conn/epics/.../stories/STORY-XX.X_Name.md`

2. 后续按流程二到流程四执行修复

详细流程参见 `BUG_WORKFLOW_GUIDE.md`。

---

## 模板速查

### 初始化模板

| Prompt                                   | 用途       | 输入     | 输出位置              |
| ---------------------------------------- | ---------- | -------- | --------------------- |
| `prompts/initialization/project_init.md` | 项目初始化 | 项目信息 | `.the_conn/` 目录结构 |

### Context 管理 Prompts

| Prompt                       | 用途              | 输入         | 输出位置             |
| ---------------------------- | ----------------- | ------------ | -------------------- |
| `prompts/context/extract.md` | 提取 Context 文档 | 技术方案     | `.the_conn/context/` |
| `prompts/context/add.md`     | 添加 Context 文档 | Context 内容 | `.the_conn/context/` |
| `prompts/context/update.md`  | 更新 Context 文档 | Context 变更 | 更新现有 Context     |

### 规划层 Prompts

| Prompt                                       | 用途                 | 输入              | 输出位置                        |
| -------------------------------------------- | -------------------- | ----------------- | ------------------------------- |
| `prompts/planning/requirements_review.md`    | 需求与方案评审       | 需求想法          | 技术方案文档                    |
| `prompts/planning/requirements_breakdown.md` | 需求拆解（批量生成） | 需求文档+技术方案 | Epic+Feature+Story              |
| `prompts/planning/epic_planning.md`          | 生成 Epic 规划       | 需求文档          | `.the_conn/epics/EPIC-XX_Name/` |
| `prompts/planning/feature_planning.md`       | 生成 Feature 规划    | 需求/Epic         | `.the_conn/epics/.../features/` |
| `prompts/planning/story_writing.md`          | 生成 Story           | 需求/Feature      | `.the_conn/epics/.../stories/`  |
| `prompts/planning/bug_fix_story.md`          | 生成 Bug Fix Story   | Bug 信息          | `.the_conn/epics/.../stories/`  |

### 执行层 Prompts

| Prompt                                 | 用途           | 输入         | 输出位置                  |
| -------------------------------------- | -------------- | ------------ | ------------------------- |
| `prompts/execution/task_generation.md` | 生成 Task 简报 | Story 文件   | `.the_conn/ai_workspace/` |
| `prompts/execution/story_sync.md`      | 同步 Story     | Story + 代码 | 更新原 Story              |
| `prompts/execution/change_summary.md`  | 生成变更摘要   | 任务记录     | `.the_conn/ai_workspace/` |

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
- Epic 目录: `EPIC-01_Base_Init/`
- Feature 目录: `FEAT-01_Init_Project/`
- Story 文件: `STORY-01_Create_Structure.md`
- Task 目录: `TASK-01_STORY-01_Create_Structure/`
- Context 文件: `Module_Design_DataStream.md`

---

## 目录约定

```
.the_conn/
├── epics/                              # 规划层
│   └── EPIC-01_Base_Init/
│       ├── README.md
│       └── features/
│           └── FEAT-01_Init_Project/
│               ├── README.md
│               └── stories/
│                   ├── STORY-01_Create_Structure.md
│                   └── STORY-01.1_Fix_Bug.md
│
├── context/                            # 知识层
│   ├── global/                         # 公共 Context
│   │   ├── Architecture.md
│   │   └── Tech_Stack.md
│   └── epics/                          # Epic 专属 Context
│       └── EPIC-01/
│           └── Module_Design_Core.md
│
├── ai_prompts/                         # 工具层
│   ├── core/core.md
│   └── templates/
│
├── ai_workspace/                       # 执行层
│   └── EPIC-01/
│       └── TASK-01_STORY-01_Create_Structure/
│           ├── task.md
│           ├── context.manifest.json
│           └── change_summary.md
│
├── README.md
├── GUIDE.md                            # 本文件
└── BUG_WORKFLOW_GUIDE.md
```
