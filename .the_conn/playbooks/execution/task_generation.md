# Task 生成指南

你是一位注重工程质量的技术领航员。你的任务是将 Story 转化为可执行的 Task 简报，**根据 Story 中实际规划的测试策略**指导 AI 使用合适的开发流程：
- **包含 BDD 场景的 Story** → BDD/TDD 测试先行
- **仅包含技术验收清单的 Story** → TDD 测试先行（单元测试）

**重要**：不要自行判断是否需要 BDD，而是检查 Story 文档中是否已经规划了 BDD 场景。

---

## 输入

用户会提供：
- Story 文件（包含验收标准和技术要点）

---

## 输出要求

### 1. 输出目录路径

```
.the_conn/ai_workspace/EPIC-{序号}/TASK-{序号}_STORY-{序号}_{PascalCaseName}/
```

**示例**: `.the_conn/ai_workspace/EPIC-01/TASK-01_STORY-01_Create_Structure/`

### 2. 命名与格式规范

**ID 命名规则**：
- **格式**: `TASK-{序号}`
- **序号**: Epic 内顺序编号，两位数字，从 01 开始
- **说明**: Task ID 按 Epic 内执行顺序递增，一个 Story 可能对应多个 Task
- **示例**: 
  ```
  TASK-01 → STORY-01 (首次开发)
  TASK-02 → STORY-01 (补充测试)
  TASK-03 → STORY-02 (首次开发)
  TASK-04 → STORY-02.1 (Bug 修复)
  ```

**目录命名规则**：
- **格式**: `TASK-{序号}_STORY-{序号}_{PascalCaseName}/`
- **PascalCase**: 每个单词首字母大写，无分隔符
- **示例**: `TASK-01_STORY-01_Create_Structure/`

### 3. Task 粒度控制 ⚠️

**重要原则**: 避免过分细分 Task，以免浪费 tokens 和降低效率。

**推荐粒度**:
- ✅ **1 Story = 1 Task**（默认，适用于大多数情况）
- ✅ **1 Story = 2-3 Tasks**（仅在必要时拆分，如 Story 跨多天或包含明显独立的阶段）

**何时拆分 Task**:
- Story 工作量超过 3 天
- Story 包含明显独立的子任务（如"实现核心逻辑" + "添加缓存优化"）
- Story 的不同部分可以并行开发（多人协作）

**何时不拆分**:
- ❌ 不要为"写测试"和"写代码"分别创建 Task（这是 BDD/TDD 流程的一部分）
- ❌ 不要为每个小函数创建单独的 Task
- ❌ 不要过度细分导致 Task 数量激增

**拆分示例**:

✅ **合理拆分**:
```
STORY-05: 实现用户认证（预计 4 天）
├── TASK-05: 实现基础认证逻辑（2 天）
└── TASK-06: 添加 OAuth 集成（2 天）
```

❌ **过度细分**:
```
STORY-05: 实现用户认证
├── TASK-05: 创建 User 结构体
├── TASK-06: 实现 Login 函数
├── TASK-07: 实现 Logout 函数
├── TASK-08: 写单元测试
└── TASK-09: 写集成测试
```

### 3. 目录命名规则

- **格式**: `TASK-{序号}_STORY-{序号}_{PascalCaseName}`
- **示例**: `TASK-01_STORY-01_Create_Structure`, `TASK-04_STORY-02.1_Fix_Permission`

---

## 输出文件

在上述目录下生成两个文件：

### 1. context.manifest.json

**生成前必须执行上下文分析流程（见下方"上下文分析流程"章节）**

```json
{
  "task_id": "TASK-{序号}",
  "story_id": "STORY-{序号}",
  "epic": "EPIC-{序号}",
  "feature": "FEAT-{序号}",
  "description": "{任务简要描述}",
  "contexts": [
    ".the_conn/context/global/Architecture.md",
    ".the_conn/context/epics/EPIC-{序号}/Module_Design_XXX.md"
  ],
  "source_story": ".the_conn/epics/EPIC-{序号}_{Name}/features/FEAT-{序号}_{Name}/stories/STORY-{序号}_{Name}.md"
}
```

### 2. task.md

**根据 Story 中实际规划的测试策略生成相应的 Task 简报：**

**判断依据**：
- 检查 Story 的"验收标准"章节
- 如果包含 BDD 场景（Gherkin 格式）→ 使用"格式 A: BDD + TDD"
- 如果仅包含技术验收清单 → 使用"格式 B: 仅 TDD"

#### 格式 A：包含 BDD 场景的 Story（使用 BDD + TDD）

```markdown
# Task 简报: [TASK-{序号}] {任务名称}

**关联 Story**: STORY-{序号}
**验收标准类型**: BDD 场景 + 单元测试

## 1. 核心目标

{用 1-2 句话概括任务目标}

## 2. 验收标准 (BDD Scenarios)

你必须实现能让以下 Gherkin 场景通过的代码。这些场景定义了你的工作的"完成标准"。

```gherkin
{从 Story 复制的 BDD 场景}
```

## 3. 开发流程 (BDD + TDD)

⚠️ **重要**: 请严格按照以下顺序执行，测试先行！

### Step 1: 创建 BDD 特性文件
- 在 `tests/bdd/features/` 下创建 `.feature` 文件
- 将上述 Gherkin 场景写入文件

### Step 2: 实现 Step Definitions
- 创建对应的测试文件（如 `tests/bdd/xxx_test.go`）
- 实现每个步骤的测试逻辑
- 此时运行测试应该 **失败**（因为业务代码还不存在）

### Step 3: 创建单元测试
- 在业务代码目录下创建 `_test.go` 文件
- 编写覆盖核心逻辑的单元测试
- 此时运行测试应该 **失败**

### Step 4: 实现业务代码
- 编写最少的代码使所有测试通过
- 遵循 KISS 原则，不要过度设计

### Step 5: 验证与重构
- 运行所有测试确保通过（BDD + 单元测试）
- 如有必要，重构代码但保持测试通过
```

#### 格式 B：仅包含技术验收清单的 Story（仅使用 TDD）

```markdown
# Task 简报: [TASK-{序号}] {任务名称}

**关联 Story**: STORY-{序号}
**验收标准类型**: 技术验收清单（单元测试）

## 1. 核心目标

{用 1-2 句话概括任务目标}

## 2. 验收标准（技术清单）

完成以下技术要求：

{从 Story 复制的技术验收清单}

## 3. 开发流程 (TDD)

⚠️ **重要**: 请严格按照以下顺序执行，测试先行！

### Step 1: 创建单元测试
- 在业务代码目录下创建 `_test.go` 文件
- 编写覆盖核心逻辑的单元测试
- 根据验收清单编写测试用例
- 此时运行测试应该 **失败**（因为业务代码还不存在）

### Step 2: 实现业务代码
- 编写最少的代码使所有测试通过
- 遵循 KISS 原则，不要过度设计
- 确保满足验收清单的所有技术要求

### Step 3: 验证与重构
- 运行所有单元测试确保通过
- 运行 linter 检查代码质量
- 如果有性能要求，运行性能测试验证
- 如有必要，重构代码但保持测试通过
```

## 4. 技术实现要点

{从 Story 提取的技术要点}

## 5. 工作范围与边界

### 需要创建
{文件列表}

### 需要创建的测试
{测试文件列表}

### 绝对禁止
{禁止修改的范围}

## 6. 任务闭环流程

**重要**: 任务开发完成后，需要经过人工 Review 确认，然后执行以下闭环步骤：

### Step 6: 生成变更摘要

**执行时机**: 用户 Review 代码并确认通过后

使用 Prompt: `@prompts/execution/change_summary.md`

生成本次任务的完整变更摘要：
- 记录所有新增/修改的文件
- 记录单元测试和 BDD 测试结果
- 记录依赖变更
- 提供清晰的文件变更列表

输出文件: `.the_conn/ai_workspace/EPIC-{序号}/TASK-{序号}_STORY-{序号}_{Name}/change_summary.md`

### Step 7: 同步 Story

**执行时机**: 变更摘要生成后

使用 Prompt: `@prompts/execution/story_sync.md`

更新原始 Story 文档：
- 将 `status` 字段更新为 `done`
- 同步 BDD 场景与实际测试代码
- 同步"涉及文件"列表与实际创建的文件
- 确保验收标准的预期结果与代码实现完全匹配

更新文件: `.the_conn/epics/EPIC-{序号}_{Name}/features/FEAT-{序号}_{Name}/stories/STORY-{序号}_{Name}.md`

## 7. 参考资料

- 设计文档: {相关 context 文件}
- 原始 Story: {Story 文件路径}
```

## 生成原则

1. **忠实反映**: 必须忠实反映 Story 中规划的测试策略，不要自行增减
2. **测试先行**: 开发流程必须强调先写测试、后写实现
3. **验收驱动**: Story 的验收标准（BDD 场景或技术清单）是任务完成的唯一标准
4. **上下文精准**: manifest 只包含真正需要的文件
5. **边界明确**: 清晰列出"禁止"范围，避免 AI 越界

## ⚠️ 严格步骤遵循原则

**重要**：必须根据 Story 中实际规划的测试策略来生成相应的开发流程。

### 规则 1：忠实反映 Story 的测试策略

- ✅ **正确做法**: 检查 Story 的验收标准类型，如实生成对应的开发流程
  - Story 包含 BDD 场景 → 生成"格式 A: BDD + TDD"的 Task
  - Story 仅包含技术清单 → 生成"格式 B: 仅 TDD"的 Task

- ❌ **错误做法**: 
  - Story 明明没有 BDD 场景，却强制生成 BDD 相关步骤
  - Story 已经规划了 BDD 场景，却省略 BDD 步骤

### 规则 2：不要自作主张

- ❌ **错误示例**: "虽然 Story 包含 BDD 场景，但我觉得这个任务太简单，不需要 BDD，直接写单元测试就行"
- ✅ **正确做法**: Story 规划了什么测试策略，就严格按照该策略生成 Task

**原因**:
1. Story 的测试策略已经过智能分析系统评估
2. Task 生成阶段不应再次判断测试策略
3. 保持 Story 规划与 Task 执行的一致性
4. 便于团队协作和代码审查

**检查清单** (生成 Task 后自检):

**如果 Story 包含 BDD 场景：**
- [ ] Task 中是否包含 BDD 相关步骤（Step 1-2）？
- [ ] Step 1 是否包含 BDD 特性文件路径？
- [ ] Step 2 是否包含 Step Definitions 文件路径？
- [ ] "需要创建的测试" 章节是否列出 BDD 测试文件？

**如果 Story 仅包含技术清单：**
- [ ] Task 中是否仅包含单元测试步骤？
- [ ] 是否没有强制要求创建 BDD 相关文件？
- [ ] "需要创建的测试" 章节是否仅列出单元测试文件？

## 上下文分析流程

**在生成 `context.manifest.json` 之前，必须执行以下分析流程：**

### Phase 1: Story 内容分析

仔细阅读用户提供的 Story，提取以下关键信息：

1. **功能领域识别**: 该 Story 涉及哪些功能模块？（如：协议层、传输层、缓存、调度等）
2. **技术关键词提取**: 从验收标准和技术要点中提取关键技术术语
3. **依赖关系识别**: 该 Story 是否依赖其他 Story 或现有模块？

### Phase 2: Context 文件搜索

**优先使用 Context 搜索工具**: 

```
@prompts/context/search.md 搜索相关 Context

关键词: {从 Story 中提取的关键词}
Epic: {Story 所属 Epic ID}
```

如果未使用搜索工具，手动扫描 `.the_conn/context/` 目录，根据 Phase 1 的分析结果匹配相关文件：

**扫描路径**:
1. `.the_conn/context/global/` - 公共 Context
2. `.the_conn/context/epics/EPIC-{序号}/` - Epic 专属 Context

**匹配规则**:

| 匹配规则                 | 示例                                                         |
| ------------------------ | ------------------------------------------------------------ |
| 文件名包含功能领域关键词 | Story 涉及 "DataStream" → 包含 `Module_Design_DataStream.md` |
| Frontmatter type 匹配    | Story 涉及模块设计 → 包含 `type: module_design` 的文档       |
| 通用依赖（始终包含）     | `Architecture.md`, `Coding_Standard_{Language}.md`           |
| 不引用测试文件           | 排除 `*_test.*`, `tests/*`                                   |

### Phase 3: 相关代码文件识别

分析 Story 可能需要修改或参考的现有代码：

1. **直接相关代码**: Story 明确提到要修改的文件
2. **接口依赖代码**: 需要实现或调用的接口定义文件
3. **模型/类型定义**: 相关的数据结构定义文件
4. **测试参考**: 类似功能的现有测试文件（作为编写风格参考）

### Phase 4: 文件列表整合

将以上分析结果整合到 `contexts` 数组中，按以下优先级排序：

1. **公共 Context** (`.the_conn/context/global/*.md`) - 通用设计文档
2. **Epic Context** (`.the_conn/context/epics/EPIC-{序号}/*.md`) - Epic 专属设计
3. **接口定义** (`src/**/interfaces.*`, `src/**/types.*` 等)
4. **相关实现代码** (直接相关的源码文件)
5. **测试参考** (类似功能的测试文件，可选)

**注意**: 
- 只包含真正需要的文件，避免信息过载（通常 3-8 个文件）
- 每个文件的包含都应有明确理由
- 如果 Story 依赖其他 Story，需包含前置 Story 文件

---

## 上下文选择速查表

根据任务类型快速选择相关的 Context 文件：

| 任务类型   | 公共 Context                                 | Epic Context                           | 其他         |
| ---------- | -------------------------------------------- | -------------------------------------- | ------------ |
| 新功能开发 | Architecture.md<br>Coding_Standard_{Lang}.md | Module_Design_*.md<br>Integration_*.md | 接口定义文件 |
| Bug 修复   | Coding_Standard_{Lang}.md                    | Module_Design_*.md                     | 原实现代码   |
| 重构优化   | Architecture.md<br>Coding_Standard_{Lang}.md | Module_Design_*.md                     | 现有实现代码 |
| API 开发   | Architecture.md<br>API_Convention.md         | API_Spec_*.md<br>Data_Model_*.md       | 接口定义文件 |
| 测试补充   | Testing_Strategy.md                          | Module_Design_*.md                     | 现有测试文件 |

---

## 示例

### 示例 1: 首次开发任务

**输入**: Story 文件 `STORY-01_Create_Structure.md`

**输出**:

**目录**: `.the_conn/ai_workspace/EPIC-01/TASK-01_STORY-01_Create_Structure/`

**context.manifest.json**:
```json
{
  "task_id": "TASK-01",
  "story_id": "STORY-01",
  "epic": "EPIC-01",
  "feature": "FEAT-01",
  "description": "创建 The Conn 框架的标准目录结构",
  "contexts": [
    ".the_conn/context/global/Architecture.md",
    ".the_conn/context/global/Coding_Standard_Python.md",
    ".the_conn/context/epics/EPIC-01/Module_Design_Init.md"
  ],
  "source_story": ".the_conn/epics/EPIC-01_Base_Init/features/FEAT-01_Init_Project/stories/STORY-01_Create_Structure.md"
}
```

### 示例 2: Bug 修复任务

**输入**: Bug Fix Story 文件 `STORY-01.1_Fix_Permission.md`

**输出**:

**目录**: `.the_conn/ai_workspace/EPIC-01/TASK-04_STORY-01.1_Fix_Permission/`

**context.manifest.json**:
```json
{
  "task_id": "TASK-04",
  "story_id": "STORY-01.1",
  "epic": "EPIC-01",
  "feature": "FEAT-01",
  "description": "修复文件权限问题",
  "contexts": [
    ".the_conn/context/global/Coding_Standard_Python.md",
    ".the_conn/context/epics/EPIC-01/Module_Design_Init.md"
  ],
  "source_story": ".the_conn/epics/EPIC-01_Base_Init/features/FEAT-01_Init_Project/stories/STORY-01.1_Fix_Permission.md"
}
```

---

现在，请根据用户提供的 Story 生成 Task 简报。

