# The Conn 使用指南

本指南说明如何使用 The Conn 框架完成 AI 辅助开发任务。框架设计理念请参阅 `ai_prompts/core/core.md`。

---

## 工作流程

### 流程一：从需求到规划

**场景**: 收到外部需求文档（PRD、技术方案等），需要拆解为可执行的开发任务。

**步骤**:

1. **生成或讨论后生成 Context 文档**（技术方案确定后）：
   ```
   @{技术方案文档}/讨论结果（建议对讨论结果生成文档后使用） @context_generation.md 帮我生成 Context 文档
   ```
   → 输出到 `.the_conn/context/` 目录

2. **生成 Epic 规划**：
   ```
   @{需求文档} @epic_template.md 帮我生成 Epic 规划
   ```
   → 输出到 `epics/{EPIC-ID}/README.md`

3. **生成 Feature 规划**：
   ```
   @{需求文档} @feature_template.md 帮我生成 Feature 规划
   ```
   → 输出到 `epics/{EPIC-ID}/features/{FEAT-ID}/README.md`

4. **生成 Story**：
   ```
   @{需求文档} @story_template.md 帮我拆解为 Story
   ```
   → 输出到 `epics/.../stories/{STORY-ID}.md`

5. 审查 AI 生成的文档，确认后提交

### 流程二：从 Story 到 Task

**场景**: Story 已就绪，需要为 AI 准备任务执行材料。

**步骤**:

1. 使用模板生成任务简报：
   ```
   @{Story文件} @task_generation.md 帮我生成 Task
   ```

2. AI 会在 `.the_conn/ai_workspace/{TASK-ID}/` 下生成：
   - `task.md` - 任务简报（强调 BDD/TDD 测试先行）
   - `context.manifest.json` - 上下文清单

3. 审查生成的文件，补充必要的上下文引用

### 流程三：执行开发任务

**场景**: Task 已准备好，开始 AI 辅助编码。

**步骤**:

1. 启动任务：
   ```
   @{TASK-ID 文件夹} 开始任务
   ```

2. AI 按 BDD/TDD 流程执行：
   - 先创建/更新 `.feature` 文件和测试代码
   - 再实现业务逻辑使测试通过
   - 运行测试验证

3. 审查代码，提出修改意见或确认通过

### 流程四：任务闭环

**场景**: 代码实现完成，需要同步文档并归档。

**步骤**:

1. 同步 Story 文档：
   ```
   @{原始Story文件} @story_synchronization.md 开始分析
   ```

2. 生成变更摘要：
   ```
   @change_summary.md 生成本次任务的变更摘要
   ```

3. 审查并提交所有变更

---

## 模板速查

| 模板 | 用途 | 输入 | 输出位置 |
|-----|------|-----|---------|
| `context_generation.md` | 生成 Context 文档 | 技术方案 | `.the_conn/context/` |
| `epic_template.md` | 生成 Epic 规划 | 需求文档 | `epics/{EPIC-ID}/` |
| `feature_template.md` | 生成 Feature 规划 | 需求/Epic | `epics/.../features/` |
| `story_template.md` | 生成 Story | 需求/Feature | `epics/.../stories/` |
| `task_generation.md` | 生成 Task 简报 | Story 文件 | `.the_conn/ai_workspace/` |
| `story_synchronization.md` | 同步 Story | Story + 代码 | 更新原 Story |
| `change_summary.md` | 生成变更摘要 | 任务记录 | `.the_conn/ai_workspace/` |

---

## 目录约定

```
.the_conn/
├── context/                # 项目上下文知识库
│   ├── 00_ARCHITECTURE.md      # 全局架构
│   ├── 10_xxx_DESIGN.md        # 模块设计
│   └── 20_xxx_SPECIFICATION.md # API 规范
├── ai_prompts/
│   ├── core/Core.md        # 框架核心说明
│   └── templates/          # 所有模板
└── ai_workspace/{TASK-ID}/ # 任务工作区

epics/
└── {EPIC-ID}/
    ├── README.md           # Epic 规划
    └── features/{FEAT-ID}/
        ├── README.md       # Feature 规划
        └── stories/{STORY-ID}.md
```
