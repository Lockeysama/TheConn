# The Conn 使用指南

本指南说明如何使用 The Conn 框架完成 AI 辅助开发任务。框架设计理念请参阅 `@playbooks/core/core.md`。

---

## 工作流程

### 流程零：项目初始化

**场景**: 首次使用 The Conn 框架，需要初始化项目结构和公共 Context。

**步骤**:

1. **项目初始化**：
   ```
   @playbooks/initialization/project_init.md 帮我初始化 The Conn 项目
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
   @{需求文档} @playbooks/planning/requirements_review.md 开始评审
   ```
   → 与 AI 讨论需求和技术方案，输出确定的技术方案文档

2. **提取 Context 文档**（方案确定后）：
   ```
   @{技术方案文档} @playbooks/context/extract.md 帮我提取 Context 文档
   ```
   → 输出到 `.the_conn/context/global/` 或 `.the_conn/context/epics/EPIC-XX/`

3. **批量生成规划**：
   ```
   @{需求文档} @{技术方案} @playbooks/planning/requirements_breakdown.md 开始拆解
   ```
   → AI 展示大纲 → 用户确认 → 批量生成所有 Epic/Feature/Story

4. **提取 Epic 专属 Context**（Epic 规划完成后）：
   ```
   @.the_conn/epics/EPIC-XX_Name/README.md @playbooks/context/extract.md 帮我提取 Epic 专属 Context
   ```
   → 输出到 `.the_conn/context/epics/EPIC-XX/`
   → 包含模块设计、数据模型、API 规范等 Epic 专属的技术细节

#### 方案 B: 逐个生成（精细控制）

1. **需求与方案评审**（同上）

2. **提取 Context 文档**（同上）

3. **生成 Epic 规划**：
   ```
   @{需求文档} @playbooks/planning/epic_planning.md 帮我生成 Epic 规划
   ```
   → 输出到 `.the_conn/epics/EPIC-XX_Name/README.md`

4. **生成 Feature 规划**：
   ```
   @{需求文档} @playbooks/planning/feature_planning.md 帮我生成 Feature 规划
   ```
   → 输出到 `.the_conn/epics/EPIC-XX_Name/features/FEAT-XX_Name/README.md`

5. **生成 Story**：
   ```
   @{需求文档} @playbooks/planning/story_writing.md 帮我拆解为 Story
   ```
   → 输出到 `.the_conn/epics/.../stories/STORY-XX_Name.md`

6. **提取 Epic 专属 Context**（Epic 规划完成后）：
   ```
   @.the_conn/epics/EPIC-XX_Name/README.md @playbooks/context/extract.md 帮我提取 Epic 专属 Context
   ```
   → 输出到 `.the_conn/context/epics/EPIC-XX/`

7. 审查 AI 生成的文档，确认后提交

### 流程二：从 Story 到 Task

**场景**: Story 已就绪，需要为 AI 准备任务执行材料。

**步骤**:

1. 使用 Playbook 生成任务简报：
   ```
   @{Story文件} @playbooks/execution/task_generation.md 帮我生成 Task
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
   @playbooks/execution/change_summary.md 生成本次任务的变更摘要
   ```

2. 同步 Story 文档：
   ```
   @{原始Story文件} @playbooks/execution/story_sync.md 开始同步
   ```

3. 审查并提交所有变更

### 流程五：Bug 修复

**场景**: 已完成的 Story 在测试或生产环境发现 Bug。

**步骤**:

1. 创建 Bug Fix Story：
   ```
   @playbooks/planning/bug_fix_story.md 帮我生成 Bug Fix Story
   
   父 Story: STORY-01
   发现于: 集成测试
   现象: ...
   ```
   → 输出到 `.the_conn/epics/.../stories/STORY-XX.X_Name.md`

2. 后续按流程二到流程四执行修复

---

## 模板速查

### 初始化 Playbooks

| Playbook                                   | 用途       | 输入     | 输出位置              |
| ------------------------------------------ | ---------- | -------- | --------------------- |
| `playbooks/initialization/project_init.md` | 项目初始化 | 项目信息 | `.the_conn/` 目录结构 |

### Context 管理 Playbooks

| Playbook                       | 用途              | 输入         | 输出位置             |
| ------------------------------ | ----------------- | ------------ | -------------------- |
| `playbooks/context/extract.md` | 提取 Context 文档 | 技术方案     | `.the_conn/context/` |
| `playbooks/context/add.md`     | 添加 Context 文档 | Context 内容 | `.the_conn/context/` |
| `playbooks/context/update.md`  | 更新 Context 文档 | Context 变更 | 更新现有 Context     |

### 规划层 Playbooks

| Playbook                                       | 用途                 | 输入              | 输出位置                        |
| ---------------------------------------------- | -------------------- | ----------------- | ------------------------------- |
| `playbooks/planning/requirements_review.md`    | 需求与方案评审       | 需求想法          | 技术方案文档                    |
| `playbooks/planning/requirements_breakdown.md` | 需求拆解（批量生成） | 需求文档+技术方案 | Epic+Feature+Story              |
| `playbooks/planning/epic_planning.md`          | 生成 Epic 规划       | 需求文档          | `.the_conn/epics/EPIC-XX_Name/` |
| `playbooks/planning/feature_planning.md`       | 生成 Feature 规划    | 需求/Epic         | `.the_conn/epics/.../features/` |
| `playbooks/planning/story_writing.md`          | 生成 Story           | 需求/Feature      | `.the_conn/epics/.../stories/`  |
| `playbooks/planning/bug_fix_story.md`          | 生成 Bug Fix Story   | Bug 信息          | `.the_conn/epics/.../stories/`  |

### 执行层 Playbooks

| Playbook                                 | 用途           | 输入         | 输出位置                  |
| ---------------------------------------- | -------------- | ------------ | ------------------------- |
| `playbooks/execution/task_generation.md` | 生成 Task 简报 | Story 文件   | `.the_conn/ai_workspace/` |
| `playbooks/execution/story_sync.md`      | 同步 Story     | Story + 代码 | 更新原 Story              |
| `playbooks/execution/change_summary.md`  | 生成变更摘要   | 任务记录     | `.the_conn/ai_workspace/` |

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
├── playbooks/                          # 工具层（AI 操作剧本）
│   ├── core/
│   │   ├── core.md
│   │   └── base_rules.md
│   ├── initialization/
│   ├── planning/
│   ├── context/
│   └── execution/
│
├── docs/                               # 用户文档（AI 严禁修改）
│   ├── README.md
│   └── GUIDE.md                        # 本文件
│
└── ai_workspace/                       # 执行层（临时工作区）
    └── EPIC-01/
        └── TASK-01_STORY-01_Create_Structure/
            ├── task.md
            ├── context.manifest.json
            └── change_summary.md
```

---

## 多人协作最佳实践

### 协作模型

The Conn 框架支持多人协作开发，推荐使用以下模型：

```
项目
├── main 分支（稳定）
├── epic/{epic-id} 分支（Epic 级别）
└── story/{story-id} 分支（Story 级别，可选）
```

---

### Git 分支策略

#### 1. 分支类型

| 分支类型         | 命名规则             | 生命周期         | 说明                       |
| ---------------- | -------------------- | ---------------- | -------------------------- |
| `main`           | 固定                 | 永久             | 生产稳定分支               |
| `epic/EPIC-XX`   | `epic/EPIC-{序号}`   | Epic 完成后删除  | Epic 级别开发分支          |
| `story/STORY-XX` | `story/STORY-{序号}` | Story 完成后删除 | Story 级别开发分支（可选） |

#### 2. 分支工作流

```
main (稳定分支)
  ↓ 创建 Epic 分支
epic/EPIC-01
  ↓ 创建 Story 分支（可选）
story/STORY-01, story/STORY-02 (并行开发)
  ↓ 合并回 Epic
epic/EPIC-01 (集成测试)
  ↓ 合并回 main
main (发布新版本)
```

#### 3. 分支操作示例

**创建 Epic 分支**:
```bash
git checkout main
git pull origin main
git checkout -b epic/EPIC-01
git push -u origin epic/EPIC-01
```

**创建 Story 分支**（可选，适合大团队）:
```bash
git checkout epic/EPIC-01
git checkout -b story/STORY-01
```

**合并 Story 回 Epic**:
```bash
git checkout epic/EPIC-01
git merge story/STORY-01
git push origin epic/EPIC-01
```

**合并 Epic 回 main**:
```bash
git checkout main
git merge epic/EPIC-01
git push origin main
git tag v1.0.0  # 可选：打标签
```

---

### ID 冲突避免策略

#### 问题场景

多人同时创建 Story 时，可能出现 ID 冲突：

```
开发者 A: 创建 STORY-03
开发者 B: 同时创建 STORY-03  ← 冲突
```

#### 解决方案

**方案 A: Epic README 集中管理（推荐）**

在 Epic README.md 中维护"下一个可用 ID"：

```markdown
# EPIC-01: 基础初始化

...

## ID 分配记录

| 类型    | 下一个可用 ID | 最后分配者 | 更新时间   |
| ------- | ------------- | ---------- | ---------- |
| Feature | FEAT-03       | @user1     | 2025-12-11 |
| Story   | STORY-06      | @user2     | 2025-12-11 |
| Task    | TASK-08       | @user1     | 2025-12-11 |
```

**操作流程**:
1. 开发者创建 Story 前，先拉取最新 Epic 分支
2. 查看 Epic README 获取下一个可用 ID
3. 使用该 ID 创建 Story
4. 更新 Epic README 的 ID 分配记录
5. 提交并推送

**方案 B: 临时 ID + 合并时重新编号**

开发过程使用临时 ID：
```
STORY-TMP-Alice-01
STORY-TMP-Bob-01
```

合并到 Epic 分支时，统一重新编号：
```
STORY-TMP-Alice-01 → STORY-03
STORY-TMP-Bob-01 → STORY-04
```

**方案 C: 预分配 ID 段**

项目启动时，为每个开发者分配 ID 段：
```
开发者 A: STORY-01 ~ STORY-20
开发者 B: STORY-21 ~ STORY-40
开发者 C: STORY-41 ~ STORY-60
```

---

### 文件冲突处理

#### 1. 规划文档冲突（Epic/Feature/Story）

**冲突场景**: 两人同时修改同一个 Story 文件

**解决方案**:
- **预防**: 使用分支隔离，每人在自己的 Story 分支工作
- **发生后**: 
  1. 检查 Frontmatter 字段（通常不冲突，因为 `status` 由 story_sync 自动更新）
  2. 检查 BDD 场景（手动合并，保留两人的场景）
  3. 检查实现指导（手动合并，综合两人的指导）

#### 2. Context 文档冲突

**冲突场景**: 两人同时更新 `Architecture.md`

**解决方案**:
- **预防**: 使用 `@playbooks/context/update.md` 时，先拉取最新代码
- **发生后**: 
  1. Context 是真相源，冲突需谨慎处理
  2. 召集相关人员讨论，确定最终版本
  3. 使用 `status: deprecated` 标记过时版本

#### 3. 代码文件冲突

**标准 Git 合并流程**: 与常规项目无异

---

### 版本控制约定

#### 应该提交到 Git

| 目录/文件               | 说明              | 原因                 |
| ----------------------- | ----------------- | -------------------- |
| `.the_conn/epics/`      | 所有规划文档      | 团队共享的需求规划   |
| `.the_conn/context/`    | 所有 Context 文档 | 项目知识库，团队共享 |
| `src/`, `tests/`        | 代码和测试        | 项目核心             |
| `.gitignore`            | Git 忽略规则      | 版本控制必需         |
| `README.md`, `GUIDE.md` | 项目文档          | 团队协作文档         |

#### 不应提交到 Git

| 目录/文件                 | 说明                | 原因                             |
| ------------------------- | ------------------- | -------------------------------- |
| `.the_conn/ai_workspace/` | 临时工作区          | 每个人的 Task 工作区，不需要共享 |
| `.the_conn/playbooks/`    | Playbooks 操作剧本  | 独立项目，通过 CLI 工具管理      |
| `.the_conn/docs/`         | 用户文档            | 独立项目，通过 CLI 工具管理      |
| `*.log`, `*.tmp`          | 临时/日志文件       | 运行时产生，不需要版本控制       |
| IDE 配置文件              | `.vscode/`, `.idea/` | 个人 IDE 配置，不强制统一        |

#### .gitignore 推荐配置

```gitignore
# The Conn 临时文件和框架文件
.the_conn/ai_workspace/
.the_conn/playbooks/
.the_conn/docs/

# 日志和临时文件
*.log
*.tmp
*.temp

# IDE 配置（可选，团队可协商）
.vscode/
.idea/
*.swp
*.swo

# 语言特定
__pycache__/
*.pyc
node_modules/
```

---

### 协作场景实例

#### 场景 1: 两人并行开发同一 Epic 的不同 Story

```
main
  ↓
epic/EPIC-01 (Alice 和 Bob 共同工作)
  ├─ Alice: 开发 STORY-01
  └─ Bob: 开发 STORY-02
```

**流程**:
1. Alice 和 Bob 从 `epic/EPIC-01` 拉取最新代码
2. Alice 执行 Task for STORY-01，Bob 执行 Task for STORY-02
3. 完成后，各自运行 `story_sync.md` 更新 Story 状态
4. Alice 先提交并推送到 `epic/EPIC-01`
5. Bob 拉取 Alice 的更新，解决冲突（如果有），然后推送
6. Epic 完成后，合并到 `main`

**关键点**:
- 使用 Epic README 的 ID 分配记录避免 Task ID 冲突
- 及时同步，避免积累大量冲突

---

#### 场景 2: 同一 Story 的 Bug 修复（跨开发者）

```
开发者 A: 完成 STORY-01 (status: done)
         ↓
测试发现 Bug
         ↓
开发者 B: 创建 STORY-01.1 修复 Bug
```

**流程**:
1. 测试发现 Bug 后，创建 Bug Fix Story（可以由任何人创建）
2. 开发者 B 使用 `@playbooks/planning/bug_fix_story.md` 创建 `STORY-01.1`
3. 开发者 B 在 Bug Fix Story 中明确 `depends_on: [STORY-01]`
4. 完成修复后，运行 `story_sync.md` 更新状态
5. 原 STORY-01 保持 `done` 状态不变

---

#### 场景 3: Context 文档更新（需要协商）

```
开发者 A: 在 STORY-03 中发现 Architecture.md 描述不准确
         ↓
         1. 先完成 Story 开发
         2. story_sync 时发现需要更新 Context
         3. 提出 Context 同步建议
         ↓
团队评审: 确认 Context 更新是否合理
         ↓
开发者 A 或技术负责人: 使用 @playbooks/context/update.md 更新
```

**关键点**:
- Context 更新需谨慎，建议由技术负责人审核
- 使用 `status: deprecated` 标记过时 Context，而非直接删除

---

### 多人协作检查清单

开始协作前，确认：

- [ ] 已定义清晰的分支策略
- [ ] 已创建 `.gitignore` 排除 `ai_workspace` 和临时文件
- [ ] Epic README 中已设置 ID 分配记录表
- [ ] 团队成员了解 Story/Task ID 的分配规则
- [ ] 团队成员了解 Context 更新需要审核

每次提交前，确认：

- [ ] 已拉取最新代码
- [ ] 已运行 `story_sync.md` 更新 Story 状态
- [ ] 如有 Context 变更，已获得团队确认
- [ ] Commit message 清晰描述变更内容
- [ ] 已更新 Epic README 的 ID 分配记录（如有新建）

---

### 推荐工具

| 工具                                    | 用途     | 说明                           |
| --------------------------------------- | -------- | ------------------------------ |
| Git                                     | 版本控制 | 分支管理、合并、冲突解决       |
| GitHub/GitLab                           | 代码托管 | PR/MR 流程、Code Review        |
| Slack/钉钉                              | 沟通工具 | 及时沟通 ID 分配、Context 更新 |
| `@playbooks/planning/project_status.md` | 进度查看 | 了解团队整体进度和阻塞项       |

---

### 常见问题

**Q: 多人同时运行 task_generation.md 会冲突吗？**

A: Task ID 按 Epic 内顺序编号，可能冲突。建议：
- 使用 Epic README 的 ID 分配表
- 或在 Task 名称中加入开发者标识（如 `TASK-TMP-Alice-01`），合并时重新编号

**Q: ai_workspace 需要提交吗？**

A: 不需要。`ai_workspace` 是临时工作区，每个人本地使用，不需要共享。

**Q: 如何避免 Context 文档冲突？**

A: 
1. Context 更新前先拉取最新代码
2. 重要 Context 更新需团队审核
3. 使用 `updated` 字段记录最后更新时间
4. 过时 Context 使用 `status: deprecated` 标记，不删除

**Q: Epic 合并到 main 前需要做什么？**

A: 
1. 确认所有 Story 都是 `done` 状态
2. 运行端到端测试
3. Code Review
4. 更新 CHANGELOG（如果有）
5. 合并后可以打 Tag（如 `v1.0.0`）
