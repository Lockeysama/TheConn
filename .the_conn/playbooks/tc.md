# The Conn - 统一命令入口

你是一位 AI 开发助手，通过 The Conn 框架与用户协作。这是统一的命令入口，你将根据用户的命令参数加载对应的 playbook。

## 🔴 执行流程

```text
1. 强制加载 @.the_conn/rules/base_rules.md
2. 解析命令 → 加载对应 playbook
3. 按 playbook 声明加载规范文件
4. 执行 playbook 任务
```

---

## 命令格式

```text
<模块> <命令> [参数]
```

或一级命令：

```text
<命令> [参数]
```

## 📚 核心命令

**重要说明**：
- Playbook 列中的路径是**命令路由映射**，告诉 AI 当用户输入某命令时应该加载哪个 playbook
- 这些路径是相对于 `.the_conn/playbooks/` 目录的
- AI 应该根据用户的命令输入来加载对应的 playbook，而不是把表格中的所有路径都加载

### 🚀 初始化

```bash
tc init [参数]
```

→ 加载 `initialization/project_init.md`

---

### 📋 规划模块（plan）

| 命令              | 一级快捷       | Playbook                             |
| ----------------- | -------------- | ------------------------------------ |
| `tc plan review`  | `tc review`    | `planning/requirements_review.md`    |
| `tc plan quick`   | `tc quick / q` | `planning/quick_router.md`           |
| `tc plan status`  | -              | `planning/project_status.md`         |
| `tc plan next`    | -              | `planning/next_step_advisor.md`      |
| `tc plan epic`    | -              | `planning/epic_planning.md`          |
| `tc plan feature` | -              | `planning/feature_planning.md`       |
| `tc plan story`   | -              | `planning/story_writing.md`          |
| `tc plan e2e`     | -              | `planning/e2e_story.md`              |
| `tc plan perf`    | -              | `planning/performance_test_story.md` |

---

### 📝 上下文模块（ctx）

| 命令            | Playbook            |
| --------------- | ------------------- |
| `tc ctx add`    | `context/add.md`    |
| `tc ctx update` | `context/update.md` |

---

### ⚙️ 执行模块（exec）

| 命令                    | 一级快捷   | Playbook                       |
| ----------------------- | ---------- | ------------------------------ |
| `tc exec task-generate` | `tc gtask` | `execution/task_generation.md` |
| `tc exec task-execute`  | `tc etask` | `execution/task_execution.md`  |
| `tc exec sync`          | -          | `execution/story_sync.md`      |
| `tc exec summary`       | -          | `execution/change_summary.md`  |

---

### 📖 帮助模块

| 命令             | Playbook |
| ---------------- | -------- |
| `tc help`        | -        |
| `tc help <模块>` | -        |
| `tc list`        | -        |

---

## 🎯 命令路由逻辑

### 1. 识别命令结构

解析用户输入，识别：

- **一级命令**：如 `tc init`, `tc help`
- **二级命令**：如 `tc plan story`, `tc ctx add`
- **缩写命令**：如 `tc plan bd`, `tc ctx e`

### 2. 命令映射规则

AI 根据命令解析结果，加载对应的 playbook 文件：

- 一级命令直接映射到 playbook
- 二级命令通过模块+子命令映射到 playbook
- 缩写命令先展开为完整命令，再映射到 playbook

**映射关系参考上面的命令体系表格**

### 3. 路由处理流程

```text
用户输入
    ↓
解析命令 (不区分大小写)
    ↓
匹配一级命令?
    ├─ 是 → 加载对应 Playbook
    └─ 否 ↓
    匹配二级命令?
        ├─ 是 → 加载对应 Playbook
        └─ 否 ↓
        匹配缩写?
            ├─ 是 → 加载对应 Playbook
            └─ 否 → 显示错误提示
    ↓
执行 Playbook
    ↓
返回结果
```

### 3. 参数传递

将命令后的所有参数传递给目标 Playbook：

```text
tc plan story 用户登录功能 --feature=FEAT-01
         ↓
加载: planning/story_writing.md
参数: ["用户登录功能", "--feature=FEAT-01"]
```


---

## 🚀 快速变更（Quick Change）

### 使用场景

当你需要快速完成小的变更时，使用 `tc quick` 命令：

- 修复简单的 bug（功能不正常）
- 小的功能改进（功能正常但想优化）
- 配置调整、日志增强、代码重构、性能优化

### 命令用法

```bash
# 推荐：让 AI 智能判断类型
tc quick <描述>
tc q <描述>         # 缩写
```

### 工作机制

→ 加载 `planning/quick_router.md`

AI 会根据 quick_router 中的规则自动：
- 分析变更描述，判断是 bug_fix 还是 hotfix
- 推断变更归属关系（属于哪个 Epic/Feature/Story）
- 生成对应的 Story ID 格式（子 Story 或独立 Story）
- 路由到相应的 playbook（bug_fix_story.md 或 hotfix_story.md）

**详细规则请参考**: `planning/quick_router.md`

---

---

## ⚠️ 重要提醒

1. **遵守核心规则**：所有操作必须遵循 `rules/base_rules.md`
2. **文档保护**：严格禁止修改 `.the_conn/docs/` 目录
3. **大小写不敏感**：命令识别不区分大小写
4. **参数完整性**：确保所有参数正确传递给目标 Playbook
5. **反馈及时**：每次执行后提供清晰的结果反馈

## 🚦 执行流程总览（增强版）

```text
tc <模块> <命令> [参数]
    ↓
┌─────────────────────────────────┐
│ Phase 1: 命令解析与路由          │
├─────────────────────────────────┤
│ • 解析用户输入                   │
│ • 识别命令结构（一级/二级/缩写）   │
│ • 匹配 Playbook 路径             │
│ • 异常: 命令无法识别 → 错误提示   │
└─────────────────────────────────┘
    ↓
┌─────────────────────────────────┐
│ Phase 2: 强制加载 base_rules.md │
├─────────────────────────────────┤
│ • 路径: @.the_conn/rules/base_rules.md │
│ • 异常处理: 文件不存在 → 提示初始化 │
│ • 加载失败 → 终止执行            │
└─────────────────────────────────┘
    ↓
┌─────────────────────────────────┐
│ Phase 3: 加载目标 Playbook       │
├─────────────────────────────────┤
│ • 路径: @.the_conn/playbooks/{mapped_path} │
│ • 异常处理: 文件不存在 → 错误提示 │
│ • 加载失败 → 终止执行            │
└─────────────────────────────────┘
    ↓
┌─────────────────────────────────┐
│ Phase 4: 按 Playbook 声明加载规范│
├─────────────────────────────────┤
│ • 根据 Playbook 的"规范引用"章节  │
│ • 加载必需的规范文件              │
│ • 异常处理: 规范文件缺失 → 警告   │
│   （非强制，继续执行）            │
└─────────────────────────────────┘
    ↓
┌─────────────────────────────────┐
│ Phase 5: 输出加载清单            │
├─────────────────────────────────┤
│ • 列出所有已加载的文件            │
│ • 标记加载状态（成功/失败/警告）   │
│ • 提供加载统计信息                │
└─────────────────────────────────┘
    ↓
┌─────────────────────────────────┐
│ Phase 6: 执行 Playbook 任务      │
├─────────────────────────────────┤
│ • 传递命令参数                   │
│ • 执行任务逻辑                   │
│ • 记录执行过程                   │
└─────────────────────────────────┘
    ↓
┌─────────────────────────────────┐
│ Phase 7: 结果反馈               │
├─────────────────────────────────┤
│ • 输出执行结果                   │
│ • 报告任何错误或警告              │
│ • 提供下一步建议（如适用）         │
└─────────────────────────────────┘
```

---

## 🛡️ 异常处理规则

### 1. 命令解析失败

#### 场景
用户输入的命令无法识别

**处理**:

```text
❌ 错误: 无法识别命令 "tc {用户输入}"

建议:
1. 检查命令拼写
2. 使用 "tc list" 查看所有可用命令
3. 使用 "tc help" 查看命令格式说明

常用命令:
- tc review - 需求评审
- tc plan quick - 快速变更
- tc gtask - 生成任务
- tc etask - 执行任务
```

**不继续执行**

---

### 2. base_rules.md 加载失败

#### 场景 A
文件不存在

**处理**:

```text
❌ 严重错误: 无法加载 base_rules.md

原因: 文件不存在
路径: .the_conn/rules/base_rules.md

⚠️ 这可能意味着:
1. The Conn 框架未正确初始化
2. rules 目录被误删除

建议操作:
1. 运行 "tc init" 重新初始化框架
2. 或从 GitHub 恢复 rules 目录

❌ 任务终止: 无法在没有 base_rules.md 的情况下继续
```

**不继续执行**

---

#### 场景 B
文件存在但无法读取

**处理**:

```text
❌ 严重错误: 无法加载 base_rules.md

原因: 文件存在但无法读取
路径: .the_conn/rules/base_rules.md
错误信息: {具体错误信息}

建议操作:
1. 检查文件权限
2. 检查文件内容是否损坏

❌ 任务终止
```

**不继续执行**

---

### 3. Playbook 加载失败

#### 场景 A
Playbook 文件不存在

**处理**:

```text
❌ 错误: 无法加载 Playbook

命令: tc {用户命令}
预期 Playbook 路径: .the_conn/playbooks/{mapped_path}

原因: Playbook 文件不存在

⚠️ 这可能意味着:
1. The Conn 框架版本过旧，不支持此命令
2. Playbook 文件被误删除
3. 命令映射配置错误

建议操作:
1. 使用 "tc list" 查看可用命令
2. 更新 The Conn 框架到最新版本
3. 或从 GitHub 恢复 playbooks 目录

❌ 任务终止
```

**不继续执行**

---

#### 场景 B
Playbook 文件存在但无法读取

**处理**:

```text
❌ 错误: 无法加载 Playbook

命令: tc {用户命令}
Playbook 路径: .the_conn/playbooks/{mapped_path}

原因: 文件存在但无法读取
错误信息: {具体错误信息}

建议操作:
1. 检查文件权限
2. 检查文件内容是否损坏

❌ 任务终止
```

**不继续执行**

---

### 4. 规范文件加载失败（非强制）

#### 场景
Playbook 声明的规范文件（如 test_strategy_rules.md）不存在或无法读取

**处理**:

```text
⚠️ 警告: 部分规范文件加载失败

Playbook: {playbook_name}
缺失文件:
- .the_conn/rules/test_strategy_rules.md (未找到)
- .the_conn/rules/complexity_rules.md (无法读取)

影响:
• 部分功能可能受限
• AI 决策可能不够精确

建议:
• 检查 .the_conn/rules/ 目录
• 或从 GitHub 恢复缺失的规范文件

✅ 继续执行（使用默认规则）
```

**继续执行**（规范文件通常不是强制的）

---

## 📋 加载完成后输出清单

**Phase 5 执行后，AI 必须输出以下清单**：

```markdown
---

✅ 加载完成清单

**命令**: tc {用户命令}

**已加载文件**:

1. ✅ **基础公约**
   - `.the_conn/rules/base_rules.md` (强制)

2. ✅ **目标 Playbook**
   - `.the_conn/playbooks/{mapped_path}`

3. **规范文件**（按 Playbook 声明）
   - ✅ `.the_conn/rules/test_strategy_rules.md`
   - ✅ `.the_conn/rules/complexity_rules.md`
   - ⚠️ `.the_conn/rules/bdd_language_rules.md` (未找到，使用默认)

**加载统计**:

- ✅ 成功: 4 个
- ⚠️ 警告: 1 个（非强制文件）
- ❌ 失败: 0 个

**状态**: ✅ 可以继续执行

---
```

**清单格式规则**:

- ✅ 绿色勾: 加载成功
- ⚠️ 黄色警告: 加载失败但非强制（使用默认值）
- ❌ 红色叉: 加载失败且强制（任务终止）

**如果有失败**:

```markdown
---

❌ 加载失败

**已加载文件**:

1. ✅ `.the_conn/rules/base_rules.md`
2. ❌ `.the_conn/playbooks/{mapped_path}` (文件不存在)

**状态**: ❌ 无法继续执行

**原因**: 目标 Playbook 文件不存在

**建议操作**: {建议}

---
```

---

---

## 🔗 Playbook 衔接规则 🆕

### 衔接类型

Playbook 之间的衔接分为两种类型：

1. **自动衔接**：AI 自动触发下一个 playbook，无需用户确认
2. **手动衔接**：AI 询问用户是否继续，等待确认后才执行

---

### 自动衔接场景

以下场景 AI **必须自动触发**下一个 playbook（无需用户确认）：

#### 场景 1: requirements_review → 完整拆解流程

**触发条件**：
- 用户在 requirements_review 中确认技术方案
- 用户选择"立即进入完整拆解流程"

**自动执行序列**：
```text
requirements_review（确认方案）
    ↓ 自动
context/add 或 context/update（提取/更新 Context）
    ↓ 自动
requirements_breakdown（批量生成规划）
```

**说明**：
- 这是一个完整的工作流，中间不需要人工干预
- 用户在 requirements_review 阶段已经做了所有决策

---

#### 场景 2: task_execution → 变更摘要 + Story 同步

**触发条件**：
- task_execution 完成所有开发步骤（Step 1-9）
- 用户 Review 通过（输入"确认"）

**自动执行序列**：
```text
task_execution（用户确认）
    ↓ 自动
execution/change_summary（生成变更摘要）
    ↓ 自动
execution/story_sync（同步 Story 状态）
```

**说明**：
- 这是 Task 闭环的标准流程
- 用户确认后不需要额外干预

---

#### 场景 3: context/add → context/update（检测到重复）

**触发条件**：
- context/add 的 Step 0 强制搜索检测到已有相关 Context
- 搜索相关度 ≥ 0.8（高度相似）

**自动执行序列**：
```text
context/add（Step 0 搜索）
    ↓ 检测到高度相似 Context
询问用户：更新 / 新建 / 取消
    ↓ 用户选择"更新"
context/update（更新已有 Context）
```

**说明**：
- 避免重复创建 Context
- 用户选择"更新"后自动调用 context/update

---

### 手动衔接场景

以下场景 AI **必须询问用户**是否继续：

#### 场景 4: requirements_breakdown → 生成详细文档

**触发条件**：
- requirements_breakdown 展示完整大纲
- 用户可能需要调整大纲

**询问模板**：
```markdown
✅ 拆解大纲已生成

📋 大纲概览：
- Epic: {N} 个
- Feature: {M} 个
- Story: {K} 个

请确认大纲，确认后我将生成详细文档。

输入：
- "确认，请生成详细文档" - 继续生成
- "修改 XXX" - 说明需要调整的内容
```

**说明**：
- 大纲可能需要多轮迭代
- 只有用户明确确认后才生成详细文档

---

#### 场景 5: epic_planning → feature_planning

**触发条件**：
- epic_planning 完成 Epic 规划文档生成
- 用户可能想逐个生成 Feature，也可能想批量生成

**询问模板**：
```markdown
✅ Epic 规划已生成

📄 已生成文件：
- .the_conn/epics/EPIC-01_Base_Init/README.md

**下一步选项**：
1. 继续生成 Feature 规划（逐个）
2. 批量生成所有 Feature 规划
3. 暂停（稍后继续）

请选择 [1/2/3]:
```

**说明**：
- 给用户选择权
- 支持逐个生成或批量生成

---

#### 场景 6: context/add → 提取 Epic Context

**触发条件**：
- 用户使用 requirements_review 生成技术方案
- 技术方案中包含 Epic 专属设计内容

**询问模板**：
```markdown
✅ 技术方案已生成

💡 **提示**：技术方案中包含以下可提取为 Epic Context 的内容：
- 模块设计（Module Design）
- 数据模型（Data Model）
- API 规范（API Spec）

是否提取为 Epic Context？
- "是" - 调用 context/add 提取
- "否" - 跳过（稍后手动提取）
```

**说明**：
- 提醒用户提取 Context，但不强制
- 用户可以选择稍后手动提取

---

### 衔接状态追踪 🆕

**AI 在执行多个 playbook 衔接时，必须维护衔接状态**：

```markdown
## 🔗 Playbook 衔接追踪

**当前工作流**: requirements_review → 完整拆解流程

| Step | Playbook               | 状态 | 输出                                  |
| ---- | ---------------------- | ---- | ------------------------------------- |
| 1    | requirements_review    | ✅    | 技术方案已确认                        |
| 2    | context/add (Global)   | ✅    | Architecture.md, Tech_Stack.md 已更新 |
| 3    | context/add (Epic)     | 🔄    | 正在提取 Epic Context...              |
| 4    | requirements_breakdown | ⏳    | 等待 Step 3 完成                      |

**预计剩余步骤**: 2 个
```

---

### 衔接异常处理

**如果衔接过程中某个 playbook 失败，AI 必须：**

1. **暂停衔接流程**
2. **标记失败的 playbook**
3. **报告失败原因**
4. **询问用户如何处理**

**异常处理模板**：

```markdown
❌ Playbook 衔接失败

**失败 Playbook**: context/add
**失败原因**: {具体错误信息}
**当前位置**: requirements_review → context/add → requirements_breakdown
                                    ↑ 失败

**已完成**：
- ✅ requirements_review

**未完成**：
- ❌ context/add (Global)
- ⏳ context/add (Epic) - 未开始
- ⏳ requirements_breakdown - 未开始

**处理选项**：
1. 重试 context/add
2. 跳过 context/add，继续 requirements_breakdown
3. 终止衔接流程

请选择 [1/2/3]:
```

---

### 衔接最佳实践

1. **保持透明**：AI 必须明确告知用户正在执行哪个 playbook
2. **及时反馈**：每完成一个 playbook，输出简要状态
3. **错误恢复**：衔接失败时提供明确的恢复选项
4. **避免过度自动化**：关键决策点必须询问用户
5. **状态追踪**：维护完整的衔接状态，便于用户了解进度

---

## 开始使用

现在你已准备好处理用户的命令。

**记住**：

- 优先匹配一级命令
- 然后匹配二级命令
- 支持所有定义的缩写
- 不区分大小写
- 将所有额外参数传递给目标 Playbook
- **遵守 Playbook 衔接规则**，正确处理自动/手动衔接

让我们开始吧！🚀
