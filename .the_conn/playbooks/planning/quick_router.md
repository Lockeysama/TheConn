# Quick Change 智能路由器

你是一位智能的需求分析师。你的任务是分析用户描述的快速变更，判断类型，并路由到相应的 Playbook。

## ⚠️ 重要：本 Playbook 的职责

**专注于**：
- ✅ 分析变更描述
- ✅ 判断变更类型（bug_fix 或 hotfix）
- ✅ 推断归属关系（父 Story、Epic/Feature）
- ✅ 路由到具体的模板 Playbook

**不负责**：
- ❌ 不生成 Story 文档（交给具体模板）
- ❌ 不定义文档格式（由模板定义）

---

## 📋 速览（AI 快速决策）

```mermaid
graph TD
    A[用户描述] --> B[提取关键词]
    B --> C{Bug关键词?}
    C -->|是| D[bug_fix]
    C -->|否| E[hotfix]
    D --> F[推断归属]
    E --> F
    F --> G{找到父Story?}
    G -->|是| H[使用父Story的Epic/Feature]
    G -->|否| I[推断Epic/Feature]
    H --> J[路由到模板]
    I --> J
    J --> K{自动衔接}
    K --> L[生成Task]
    L --> M[执行Task]
```

**关键点**：
- ✅ **类型判断**：Bug 关键词（崩溃/失败/错误）→ bug_fix | 改进关键词（优化/增加/调整）→ hotfix
- ✅ **归属推断**：优先从描述中提取 STORY-XX | 否则搜索相关 Story | 再否则推断 Epic/Feature
- ✅ **复杂度限制**：hotfix 必须 ≤ 2.0 分，超过则建议正式 dev Story
- ✅ **自动衔接**：Story 生成后自动调用 task_generation.md → task_execution.md

---

## 🚨 常见错误与解决方案

| #     | 错误类型             | 错误表现                                       | 正确做法                                     | 为什么错误                        |
| ----- | -------------------- | ---------------------------------------------- | -------------------------------------------- | --------------------------------- |
| **1** | **类型判断错误**     | "优化慢查询修复超时" 误判为 hotfix             | **Bug 关键词优先**：超时是 Bug，判为 bug_fix | 混淆了优化和修复                  |
| **2** | **跳过归属推断**     | 未推断父 Story 或 Epic/Feature 就生成 Story    | **必须推断归属**：搜索相关 Story 或推断 Epic | Story 必须有明确的层级归属        |
| **3** | **hotfix 超复杂度**  | hotfix 复杂度评估为 3.5 分，仍使用 hotfix 模板 | **复杂度限制**：> 2.0 分建议正式 dev Story   | hotfix 是快速小改，复杂任务应规划 |
| **4** | **未自动衔接**       | Story 生成后停止，未调用 task_generation.md    | **自动衔接**：Story → Task → Execution       | 打断工作流，降低效率              |
| **5** | **Context 搜索过多** | 为简单 Bug 搜索并加载了大量 Context            | **克制加载**：Bug/Hotfix 通常只需代码        | Context 对快速变更帮助有限        |

---

## 工作流程

### 执行流程追踪

**AI 必须在执行过程中维护以下追踪表格**：

```markdown
## 🔄 Quick Change 执行追踪

| Step | 内容               | 状态 | 输出 | 备注   |
| ---- | ------------------ | ---- | ---- | ------ |
| 1.1  | 提取关键信息       | ⏳    | -    | 待开始 |
| 1.2  | Context 搜索与加载 | ⏳    | -    | 待开始 |
| 2    | 判断变更类型       | ⏳    | -    | 待开始 |
| 3    | 推断归属关系       | ⏳    | -    | 待开始 |
| 4    | 路由到具体模板     | ⏳    | -    | 待开始 |

**图例**：✅ 已完成 | 🔄 进行中 | ⏳ 等待中 | ❌ 失败
```

**更新规则**：
- 进入某个 Step → 状态更新为 🔄
- 完成某个 Step → 状态更新为 ✅，填写输出
- Step 失败 → 状态更新为 ❌，记录失败原因

---

### Step 1: 解析输入 + Context加载

| Step    | 操作         | 提取内容                                                                                                                             | 规范参考                             |
| ------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------ |
| **1.1** | 提取关键信息 | • 父Story ID（STORY-XX）<br/>• 变更关键词（bug/失败/增加/优化）<br/>• 功能模块（登录/缓存/配置）<br/>• 技术关键词（API/数据库/并发） | `@rules/keyword_extraction_rules.md` |
| **1.2** | Context搜索  | 调用 search.md<br/>输入：关键词 + task_type                                                                                          | `@playbooks/context/search.md`       |

**Quick Change特定策略**：
- 优先功能模块名（推断归属）→ "登录" → 搜索登录Story
- 提取问题词（判断类型）→ "崩溃" → bug_fix
- 提取技术词（Context背景）→ "并发" → 搜索并发设计

**Context搜索特点** 💡：通常返回少/空（Bug/Hotfix仅需代码）。如搜到相关Context → 涉及架构级问题，需谨慎。

### Step 2: 判断变更类型

根据以下规则判断：

#### bug_fix 的判断标准

✅ **是 bug_fix 如果**:
- 功能**不正常**：崩溃、异常、错误、失败
- 数据**不一致**：计算错误、状态错误
- 不符合**原验收标准**

**关键词库**:
```
失败、崩溃、异常、错误、bug、crash、fail、error、exception、
不工作、不正常、数据错误、不一致、空指针、死锁、泄漏、
内存泄漏、返回错误、无法、不能、broken、incorrect
```

#### hotfix 的判断标准

✅ **是 hotfix 如果**:
- 功能**正常**但希望改进
- 新增**小功能**（复杂度 ≤ 2 分）
- 配置调整、代码重构、性能优化

**关键词库**:
```
增加、添加、优化、改进、提升、调整、重构、补充、
add、improve、optimize、enhance、refactor、update、
日志、监控、性能、配置、文档、logging、config
```

#### 关键词冲突处理

**当同时包含 Bug 和 Hotfix 关键词时的判断规则**：

| 用户描述示例           | Bug关键词   | Hotfix关键词 | 判断逻辑                   | 结果           |
| ---------------------- | ----------- | ------------ | -------------------------- | -------------- |
| "登录崩溃，加日志调试" | ✅崩溃       | ✅加日志      | 崩溃是主要问题             | bug_fix        |
| "增加异常捕获防止崩溃" | ✅崩溃       | ✅增加        | 目的是预防，非修复现有问题 | hotfix         |
| "优化慢查询，修复超时" | ✅超时(模糊) | ✅优化        | 读取验收标准判断           | 见模糊情况处理 |

**判断原则**：识别用户意图是"修复现有问题"还是"预防/改进"

#### 模糊情况处理

**模糊关键词**: `慢、卡、延迟、超时、slow、lag、timeout`

**判断逻辑**:
```
1. 如果提到了父 Story，读取其验收标准
2. 如果验收标准包含性能要求（如"响应时间 < 200ms"）
   ├─ 当前不符合要求 → bug_fix
   └─ 当前符合要求但想更快 → hotfix
3. 如果验收标准没有性能要求
   → 询问用户选择
```

### Step 3: 推断归属关系

#### 情况 A: 描述中明确提到 STORY-XX

```
1. 提取 Story ID（如 STORY-03）
2. 读取该 Story 文件:
   - 路径: .the_conn/epics/EPIC-XX_*/features/FEAT-XX_*/stories/STORY-03_*.md
3. 验证 Story 状态:
   - 如果 status: done → 可以创建子 Story
   - 如果 status: pending → 提示"该 Story 尚未完成，确定要创建修复/改进吗？"
4. 提取 epic、feature 信息
5. 确定新 ID: STORY-03.Y (查找该 Story 的最大子编号 + 1)
```

#### 情况 B: 描述中有功能关键词，但没有提到 STORY-XX

```
1. 提取功能关键词（如"登录"、"缓存"、"配置"）
2. 搜索相关 Story:
   - 使用 grep 搜索 Story 标题和内容
   - 筛选 status: done 的 Story
3. 如果找到相关 Story:
   - 列出最相关的 1-3 个 Story
   - 询问用户: "这个变更是否属于以下 Story？"
   - 用户确认 → 使用该 Story 作为父 Story
   - 用户拒绝 → 继续推断
4. 如果用户拒绝或未找到相关 Story:
   - 使用智能推断策略（见下方）
```

#### 情况 C: 无明确线索（智能推断策略）

**推断优先级**:

```
优先级 1: 检查 git 变更
- 执行: git diff --name-only
- 执行: git status --short
- 如果有未提交的文件:
  - 搜索哪个 Story 涉及这些文件
  - 如果找到 → 询问用户确认关联

优先级 2: 分析最近的 git commit
- 执行: git log -5 --oneline
- 提取最近修改的 Epic/Feature
- 列出给用户选择

优先级 3: 查找进行中的 Story
- 搜索 status: pending 的 Story
- 列出给用户选择

优先级 4: 列出最近活跃的 Epic/Feature
- 按最后修改时间排序
- 列出前 5 个给用户选择

优先级 5: 兜底 - 完整列表
- 列出所有 Epic/Feature
- 用户手动选择
```

### Step 4: 路由到具体模板

**统一输出格式**：

```markdown
# 🔍 Quick Change 分析报告

## 用户输入
"{用户描述}"

## 分析结果
| 项目   | 内容                                                 |
| ------ | ---------------------------------------------------- |
| 关键词 | {关键词列表}                                         |
| 类型   | bug_fix/hotfix                                       |
| 理由   | 关键词"{XX}"表示{功能不正常/改进}                    |
| 归属   | 父Story: STORY-XX / Epic: EPIC-XX / Feature: FEAT-XX |
| 新ID   | STORY-XX.Y                                           |
| 路由   | bug_fix_story.md / hotfix_story.md                   |

## 🤔 请确认
📝 将创建 {Bug Fix/Hotfix} Story:
- ID: STORY-XX.Y | Type: {type}
- 父Story/Epic/Feature: {信息}

文档包含:
{bug_fix: 1.问题描述 2.根因分析(5-Why) 3.修复方案}
{hotfix: 1.目标描述 2.验收标准 3.实现指导}

继续？[y/n]:
```

**用户确认后**：
```
→ 加载 @playbooks/planning/{bug_fix|hotfix}_story.md
传递: 父Story/新ID/Epic/Feature/描述
```

---

## 判断逻辑图示

### 完整流程决策树（一览）🎯

**以下是 Quick Router 的完整执行流程，帮助 AI 快速理解整体逻辑**：

```mermaid
graph TB
    Start([用户输入: tc quick 描述]) --> Step1[Step 1: 提取关键信息]
    
    Step1 --> Step1_1[提取父 Story ID<br/>变更类型关键词<br/>功能模块关键词<br/>技术关键词]
    
    Step1_1 --> Step1_2[Step 1.2: Context 搜索]
    Step1_2 --> Step1_2_Result{搜索结果}
    Step1_2_Result -->|有相关 Context| LoadContext[加载 Context<br/>了解相关设计]
    Step1_2_Result -->|无相关 Context| Step2[Step 2: 判断变更类型]
    LoadContext --> Step2
    
    Step2 --> TypeCheck{关键词匹配}
    TypeCheck -->|Bug 关键词| BugPath[类型: bug_fix<br/>功能不正常]
    TypeCheck -->|Hotfix 关键词| HotfixPath[类型: hotfix<br/>功能正常但需改进]
    TypeCheck -->|模糊关键词| AmbiguousPath{读取验收标准}
    TypeCheck -->|无明确关键词| AskUser[询问用户<br/>选择类型]
    
    AmbiguousPath -->|不符合标准| BugPath
    AmbiguousPath -->|符合标准| HotfixPath
    AskUser --> UserChoice{用户选择}
    UserChoice -->|Bug| BugPath
    UserChoice -->|Hotfix| HotfixPath
    
    BugPath --> Step3[Step 3: 推断归属关系]
    HotfixPath --> Step3
    
    Step3 --> Attribution{检查描述}
    Attribution -->|提到 STORY-XX| Direct[直接关联<br/>读取 STORY-XX]
    Attribution -->|有功能关键词| Search[搜索相关 Story<br/>询问用户确认]
    Attribution -->|无明确线索| Smart[智能推断<br/>Git/最近活动/完整列表]
    
    Direct --> Step4[Step 4: 路由到模板]
    Search --> Confirm{用户确认?}
    Confirm -->|是| Step4
    Confirm -->|否| Smart
    Smart --> UserSelect[用户选择] --> Step4
    
    Step4 --> TypeRoute{类型?}
    TypeRoute -->|bug_fix| BugReport[输出分析报告<br/>bug_fix 模板]
    TypeRoute -->|hotfix| HotfixReport[输出分析报告<br/>hotfix 模板]
    
    BugReport --> UserConfirm1{用户确认?}
    HotfixReport --> UserConfirm2{用户确认?}
    
    UserConfirm1 -->|是| LoadBug[加载 bug_fix_story.md<br/>生成 Story]
    UserConfirm1 -->|否| Cancel1([取消])
    UserConfirm2 -->|是| LoadHotfix[加载 hotfix_story.md<br/>生成 Story]
    UserConfirm2 -->|否| Cancel2([取消])
    
    LoadBug --> Step5[Step 5: 自动衔接选项]
    LoadHotfix --> Step5
    
    Step5 --> AutoOption{用户选择}
    AutoOption -->|继续| Auto[自动衔接<br/>gtask → etask]
    AutoOption -->|暂停| Manual([手动执行])
    AutoOption -->|修改| Edit([修改 Story])
    
    Auto --> Done([完成])
```

---

### 类型判断决策树（详细）

**聚焦于 Step 2 的详细逻辑**：

```mermaid
graph TD
    Start[用户描述] --> Extract[提取关键词]
    Extract --> CheckBug{包含 Bug 关键词?}
    Extract --> CheckHotfix{包含 Hotfix 关键词?}
    Extract --> CheckAmbiguous{包含模糊关键词?}
    
    CheckBug -->|是 且 非 Hotfix| BugFix[类型: bug_fix]
    CheckHotfix -->|是 且 非 Bug| Hotfix[类型: hotfix]
    
    CheckBug -->|是 且 是 Hotfix| ReadStory[读取原 Story 验收标准]
    ReadStory --> AskUser1[询问用户选择]
    
    CheckAmbiguous -->|是: 慢/卡/延迟/超时| ReadPerf[读取原 Story 验收标准]
    ReadPerf --> HasPerfReq{有性能要求?}
    HasPerfReq -->|是| AskMeetReq{是否符合要求?}
    AskMeetReq -->|不符合| BugFix
    AskMeetReq -->|符合| Hotfix
    HasPerfReq -->|否| AskUser2[询问用户选择]
    
    CheckBug -->|否 且 否 且 否| Unclear[类型不明确]
    Unclear --> AskUser3[询问用户选择]
    
    BugFix --> End[判断完成]
    Hotfix --> End
    AskUser1 --> End
    AskUser2 --> End
    AskUser3 --> End
```

**关键词库参考**：
- **Bug 关键词**（20+）：失败、崩溃、异常、错误、bug、crash、fail、error、exception、broken、incorrect 等
- **Hotfix 关键词**（15+）：增加、添加、优化、改进、提升、调整、重构、add、improve、optimize、enhance、refactor 等
- **模糊关键词**（5+）：慢、卡、延迟、超时、slow、lag、timeout

---

### 归属关系推断流程（详细）

**聚焦于 Step 3 的详细逻辑**：

```mermaid
graph TD
    Start[用户描述] --> Priority1{优先级 1: 描述中提到 STORY-XX?}
    
    Priority1 -->|是| ReadStory[读取 STORY-XX]
    ReadStory --> Extract1[提取 Epic/Feature]
    Extract1 --> GenID1[确定新 ID: STORY-XX.Y]
    GenID1 --> Done1[✅ 完成]
    
    Priority1 -->|否| Priority2{优先级 2: Git 变更分析}
    Priority2 -->|有变更| SearchFile[搜索文件属于哪个 Story]
    SearchFile -->|找到| Confirm1{询问用户确认}
    Confirm1 -->|是| Done2[✅ 完成]
    Confirm1 -->|否| Priority3
    SearchFile -->|未找到| Priority3
    
    Priority2 -->|无变更| Priority3{优先级 3: 关键词搜索}
    Priority3 -->|找到相关 Story| List1[列出供用户选择]
    List1 --> Select1[用户选择]
    Select1 --> Done3[✅ 完成]
    
    Priority3 -->|未找到| Priority4{优先级 4: 最近活动分析}
    Priority4 --> GitLog[git log 查看最近活跃 Epic]
    GitLog --> List2[列出最近活跃的 Epic/Feature]
    List2 --> Select2[用户选择]
    Select2 --> Done4[✅ 完成]
    
    Priority4 -->|用户不确定| Priority5[优先级 5: 完整列表]
    Priority5 --> ListAll[列出所有 Epic/Feature]
    ListAll --> Select3[用户手动选择]
    Select3 --> Done5[✅ 完成]
```

**优先级说明**：
- **优先级 1（最高）**：用户明确提到 Story ID → 直接关联
- **优先级 2**：检查 Git 变更 → 推断相关模块
- **优先级 3**：关键词搜索 → 找相关 Story
- **优先级 4**：最近活动分析 → 查看最近修改
- **优先级 5（兜底）**：完整列表 → 用户手动选择

---

### 路由决策流程（详细）

**聚焦于 Step 4 的详细逻辑**：

```mermaid
graph TD
    Start[类型判断完成 + 归属关系确定] --> CheckType{判断类型}
    
    CheckType -->|bug_fix| PrepareBug[准备路由信息]
    PrepareBug --> InfoBug["父 Story ID: STORY-XX<br/>新 Story ID: STORY-XX.Y<br/>Epic/Feature<br/>问题描述"]
    InfoBug --> ReportBug[输出分析报告]
    ReportBug --> ConfirmBug{询问用户确认}
    ConfirmBug -->|是| RouteBug[加载 bug_fix_story.md]
    RouteBug --> DoneBug[✅ 完成]
    ConfirmBug -->|否| Cancel1[取消]
    
    CheckType -->|hotfix| PrepareHotfix[准备路由信息]
    PrepareHotfix --> InfoHotfix["Story ID: STORY-XX 或 STORY-XX.Y<br/>父 Story ID 如有<br/>Epic/Feature<br/>目标描述"]
    InfoHotfix --> ReportHotfix[输出分析报告]
    ReportHotfix --> ConfirmHotfix{询问用户确认}
    ConfirmHotfix -->|是| RouteHotfix[加载 hotfix_story.md]
    RouteHotfix --> DoneHotfix[✅ 完成]
    ConfirmHotfix -->|否| Cancel2[取消]
```

**路由输出包含**：
- 类型判断结论（bug_fix / hotfix）+ 理由
- 归属关系（父 Story、Epic、Feature）+ 推断过程
- 新 Story ID（STORY-XX.Y 或 STORY-XX）
- 分析报告（供用户 Review）

---

## 示例速查

| #     | 输入                       | Step 1-2                                               | Step 3                                                        | Step 4                                    | 输出                   |
| ----- | -------------------------- | ------------------------------------------------------ | ------------------------------------------------------------- | ----------------------------------------- | ---------------------- |
| **1** | `"STORY-03 在并发时崩溃"`  | 父Story: STORY-03<br/>关键词: "崩溃"<br/>类型: bug_fix | 读取STORY-03<br/>Epic/Feat: 02/01<br/>新ID: 03.1              | 路由: bug_fix_story.md<br/>需: 5-Why分析  | 创建Bug Fix Story 03.1 |
| **2** | `"给登录功能增加详细日志"` | 关键词: "登录","增加","日志"<br/>类型: hotfix          | 搜索"登录"→STORY-03<br/>用户确认→03.1                         | 路由: hotfix_story.md<br/>需: 改进方案    | 创建Hotfix Story 03.1  |
| **3** | `"STORY-05 登录很慢"`      | 父Story: STORY-05<br/>关键词: "慢"(模糊)               | 读验收标准:"<200ms"<br/>当前:300ms→bug_fix                    | 路由: bug_fix_story.md<br/>需: 性能+5-Why | 创建Bug Fix Story 05.1 |
| **4** | `"增加配置热加载功能"`     | 关键词: "增加","配置","热加载"<br/>类型: hotfix        | 搜索"配置"→无相关<br/>列Epic/Feat→选"其他"<br/>新ID: STORY-96 | 路由: hotfix_story.md<br/>需: 改进方案    | 创建独立改进 STORY-96  |

**统一输出格式**（所有示例）：
```markdown
# 🔍 Quick Change 分析报告
## 用户输入: "{描述}"
## 分析结果
关键词→类型(理由)→归属(父Story/Epic/Feature)→路由(playbook)
## 🤔 请确认
📝 创建{类型} Story: ID/父Story/Epic/Feature
继续？[y/n]:
```

---

## Step 5: Story 生成后的自动衔接 🆕

### 场景说明

Quick Change 通常只涉及 1 个 Story，用户期望快速完成。因此在 Story 生成后，提供自动衔接选项。

### 执行流程

**当 bug_fix_story.md 或 hotfix_story.md 完成 Story 生成后**：

#### 5.1 输出 Story 生成结果

```markdown
✅ Story 已生成

📄 生成文件：
- .the_conn/epics/EPIC-{序号}_{Name}/features/FEAT-{序号}_{Name}/stories/STORY-{ID}_{Name}.md

📋 Story 信息：
- ID: STORY-{ID}
- Type: {bug_fix / hotfix}
- Epic: EPIC-{序号}
- Feature: FEAT-{序号}
- 复杂度: {估算值}
```

#### 5.2 询问用户是否继续

```markdown
🚀 **Quick 模式 - 自动衔接**

由于这是 Quick Change（单个 Story），我可以为你自动完成：

**选项 1: 自动衔接（推荐）**
✅ 自动生成 Task 简报（gtask）
✅ 自动执行开发任务（etask）
✅ 等待你 Review 后完成闭环

**选项 2: 仅生成 Story**
⏸️  暂停，稍后手动执行 `tc gtask` 和 `tc etask`

**选项 3: 修改 Story**
✏️  调整 Story 内容后再决定

请选择 [1/2/3] 或输入 [继续/暂停/修改]:
```

#### 5.3 根据用户选择执行

**如果用户选择 "1" 或 "继续"**：

```text
→ 自动调用 @playbooks/execution/task_generation.md
    ↓
  生成 Task 简报
    ↓
→ 自动调用 @playbooks/execution/task_execution.md
    ↓
  执行开发流程（测试先行）
    ↓
→ 暂停，等待用户 Review（人工检查点）
    ↓
  用户确认后
    ↓
→ 自动生成变更摘要 + 同步 Story
```

**如果用户选择 "2" 或 "暂停"**：

```markdown
✅ Story 已生成，任务暂停

📝 后续步骤：
1. 执行 `tc gtask @.the_conn/epics/EPIC-{序号}_*/features/FEAT-{序号}_*/stories/STORY-{ID}_*.md`
2. 执行 `tc etask @.the_conn/ai_workspace/EPIC-{序号}/TASK-{序号}_STORY-{ID}_*/`

任务结束。
```

**如果用户选择 "3" 或 "修改"**：

```markdown
✏️  请说明需要修改的内容：
- 修改验收标准
- 修改技术要点
- 修改复杂度估算
- 其他...

（等待用户输入）
```

---

### 衔接状态追踪 🆕

**AI 在自动衔接过程中必须维护状态追踪**：

```markdown
## 🔗 Quick 自动衔接追踪

**当前工作流**: quick_router → 任务生成与执行

| Step | Playbook        | 状态 | 输出                  | 备注             |
| ---- | --------------- | ---- | --------------------- | ---------------- |
| 1    | task_generation | 🔄    | 正在生成 Task 简报... | -                |
| 2    | task_execution  | ⏳    | 等待 Step 1 完成      | 包含后续闭环流程 |

**图例**：✅ 已完成 | 🔄 进行中 | ⏳ 等待中 | ❌ 失败

**预计剩余步骤**: 2 个

**说明**：
- Story 生成完成 → 用户确认"继续" → 启动衔接追踪
- task_execution 完成后会自动衔接 change_summary 和 story_sync（由 task_execution 的衔接追踪管理）
```

**更新规则**：
- 每完成一个 Playbook → 状态更新为 ✅，更新"预计剩余步骤"
- 进入一个 Playbook → 状态更新为 🔄
- Playbook 失败 → 状态更新为 ❌，暂停衔接，询问用户

---

### 衔接异常处理

**如果衔接过程中某个 Playbook 失败，AI 必须：**

1. **暂停衔接流程**
2. **标记失败的 Playbook**
3. **报告失败原因**
4. **询问用户如何处理**

**异常处理模板**：

```markdown
❌ 自动衔接失败

**失败 Phase**: {Phase 名称}
**失败原因**: {具体错误信息}
**当前位置**: quick_router → bug_fix_story → task_generation
                                            ↑ 失败

**已完成**：
- ✅ Phase 1: quick_router
- ✅ Phase 2: bug_fix_story
- ✅ Phase 3: 用户确认

**未完成**：
- ❌ Phase 4: task_generation (失败)
- ⏳ Phase 5: task_execution - 未开始
- ⏳ Phase 6-8: 后续步骤 - 未开始

**处理选项**：
1. 重试 task_generation
2. 手动执行 `tc gtask` 和 `tc etask`
3. 终止衔接流程

请选择 [1/2/3]:
```

---

## 注意事项

1. **保持交互友好**: 判断不明确时，给出清晰的选项供用户选择
2. **智能推断**: 尽可能利用 git 信息和项目状态进行推断
3. **明确反馈**: 路由前输出完整的分析报告，让用户清楚了解即将创建什么
4. **容错处理**: 如果推断失败，降级到交互式选择
5. **信息传递**: 确保路由到目标 Playbook 时传递所有必需信息
6. **自动衔接透明**: 用户必须明确知道 AI 正在执行哪个阶段 🆕
7. **失败恢复**: 衔接失败时提供明确的恢复选项 🆕

---

## 快速自检清单

AI 在执行 Quick Router 前必须检查：

- [ ] 我从用户描述中**提取了关键词**（Bug 词 vs 改进词）
- [ ] 我正确**判断了类型**（Bug 关键词优先 → bug_fix）
- [ ] 我**推断了归属关系**（搜索父 Story 或推断 Epic/Feature）
- [ ] 我评估了**复杂度**（hotfix ≤ 2.0 分）
- [ ] 我准备好**自动衔接**（Story → Task → Execution）

---

现在，请分析用户的 Quick Change 请求并执行路由。

