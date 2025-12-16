# The Conn - 统一命令入口

你是一位 AI 开发助手，通过 The Conn 框架与用户协作。这是统一的命令入口，你将根据用户的命令参数加载对应的 playbook。

## 🔴 强制要求：必须先加载基础公约

**在执行任何命令之前，AI 必须使用相应的工具（如 `read_file`）加载以下文件**：

```
@playbooks/core/base_rules.md
```

**重要性说明**：
- ✅ `base_rules.md` 定义了所有 Playbook 必须遵守的基础规则和约束
- ✅ 包含了**文件加载强制要求**，确保所有被 `@` 引用的文件都被正确加载
- ✅ 定义了禁止事项、允许事项、文件路径约定、质量标准等核心规则
- ✅ 违反基础公约可能导致生成不符合规范的输出或破坏项目结构

**执行流程**：
1. 加载 `base_rules.md`
2. 检查并加载用户 Prompt 中所有被 `@` 引用的文件
3. 根据用户命令加载对应的 playbook
4. 执行 playbook 指定的任务

---

## 使用方式

在 AI IDE 中，通过 @ 符号引用此文件，然后输入命令参数：

```
@tc.md <模块> <命令> [参数]
```

或者使用相对路径：

```
@playbooks/tc.md <模块> <命令> [参数]
```

简化的一级命令：

```
@tc.md <命令> [参数]
```

## 📚 命令体系

### 🚀 初始化

```
@tc.md init [参数]
```

→ 调用 `@initialization/project_init.md`

---

### 📋 规划模块（plan）

| 命令                    | 缩写                                 | 功能                 | Playbook                              |
| ----------------------- | ------------------------------------ | -------------------- | ------------------------------------- |
| `@tc.md plan review`    | `@tc.md plan rv`                     | 需求与方案评审       | `@planning/requirements_review.md`    |
| `@tc.md plan breakdown` | `@tc.md plan bd`                     | 需求拆解（批量生成） | `@planning/requirements_breakdown.md` |
| `@tc.md plan change`    | `@tc.md plan chg`                    | 需求变更管理         | `@planning/requirements_change.md`    |
| `@tc.md plan status`    | `@tc.md plan st`                     | 查看项目状态         | `@planning/project_status.md`         |
| `@tc.md plan next`      | `@tc.md plan n`                      | 下一步行动建议       | `@planning/next_step_advisor.md`      |
| `@tc.md plan epic`      | `@tc.md plan e`                      | 生成 Epic            | `@planning/epic_planning.md`          |
| `@tc.md plan feature`   | `@tc.md plan feat` / `@tc.md plan f` | 生成 Feature         | `@planning/feature_planning.md`       |
| `@tc.md plan story`     | `@tc.md plan s`                      | 生成 Story           | `@planning/story_writing.md`          |
| `@tc.md plan bugfix`    | `@tc.md plan bug` / `@tc.md plan bf` | 生成 Bug Fix Story   | `@planning/bug_fix_story.md`          |

**一级命令快捷方式**（常用命令）：

```
@tc.md status     → @tc.md plan status
@tc.md next       → @tc.md plan next
@tc.md epic       → @tc.md plan epic
@tc.md feature    → @tc.md plan feature
@tc.md story      → @tc.md plan story
@tc.md bugfix     → @tc.md plan bugfix
```

---

### 📝 上下文模块（ctx）

| 命令                 | 缩写                              | 功能              | Playbook              |
| -------------------- | --------------------------------- | ----------------- | --------------------- |
| `@tc.md ctx extract` | `@tc.md ctx ext` / `@tc.md ctx e` | 提取 Context 文档 | `@context/extract.md` |
| `@tc.md ctx add`     | `@tc.md ctx a`                    | 添加 Context 文档 | `@context/add.md`     |
| `@tc.md ctx update`  | `@tc.md ctx upd` / `@tc.md ctx u` | 更新 Context 文档 | `@context/update.md`  |
| `@tc.md ctx search`  | `@tc.md ctx s`                    | 搜索 Context 文档 | `@context/search.md`  |

---

### ⚙️ 执行模块（exec）

| 命令                  | 缩写              | 功能           | Playbook                        |
| --------------------- | ----------------- | -------------- | ------------------------------- |
| `@tc.md exec task`    | `@tc.md exec t`   | 生成 Task 简报 | `@execution/task_generation.md` |
| `@tc.md exec sync`    | `@tc.md exec sy`  | 同步 Story     | `@execution/story_sync.md`      |
| `@tc.md exec summary` | `@tc.md exec sum` | 生成变更摘要   | `@execution/change_summary.md`  |

**一级命令快捷方式**：

```
@tc.md task       → @tc.md exec task
@tc.md sync       → @tc.md exec sync
@tc.md summary    → @tc.md exec summary
```

---

### 📖 帮助模块

| 命令                 | 功能               |
| -------------------- | ------------------ |
| `@tc.md help`        | 显示帮助信息       |
| `@tc.md help <模块>` | 显示特定模块的帮助 |
| `@tc.md list`        | 列出所有可用命令   |

---

## 🎯 命令路由逻辑

### 1. 识别命令结构

解析用户输入，识别：
- **一级命令**：如 `@tc init`, `@tc help`
- **二级命令**：如 `@tc plan story`, `@tc ctx add`
- **缩写命令**：如 `@tc plan bd`, `@tc ctx e`

### 2. 命令映射表

```javascript
// 一级命令映射
// 用法：@tc.md <命令>
{
  "init": "@initialization/project_init.md",
  "status": "@planning/project_status.md",
  "next": "@planning/next_step_advisor.md",
  "epic": "@planning/epic_planning.md",
  "feature": "@planning/feature_planning.md",
  "story": "@planning/story_writing.md",
  "bugfix": "@planning/bug_fix_story.md",
  "task": "@execution/task_generation.md",
  "sync": "@execution/story_sync.md",
  "summary": "@execution/change_summary.md",
  "help": "显示帮助",
  "list": "列出命令"
}

// 二级命令 - plan 模块
{
  "plan": {
    "review": "@planning/requirements_review.md",
    "rv": "@planning/requirements_review.md",
    "breakdown": "@planning/requirements_breakdown.md",
    "bd": "@planning/requirements_breakdown.md",
    "change": "@planning/requirements_change.md",
    "chg": "@planning/requirements_change.md",
    "status": "@planning/project_status.md",
    "st": "@planning/project_status.md",
    "next": "@planning/next_step_advisor.md",
    "n": "@planning/next_step_advisor.md",
    "epic": "@planning/epic_planning.md",
    "e": "@planning/epic_planning.md",
    "feature": "@planning/feature_planning.md",
    "feat": "@planning/feature_planning.md",
    "f": "@planning/feature_planning.md",
    "story": "@planning/story_writing.md",
    "s": "@planning/story_writing.md",
    "bugfix": "@planning/bug_fix_story.md",
    "bug": "@planning/bug_fix_story.md",
    "bf": "@planning/bug_fix_story.md"
  }
}

// 二级命令 - ctx 模块
{
  "ctx": {
    "extract": "@context/extract.md",
    "ext": "@context/extract.md",
    "e": "@context/extract.md",
    "add": "@context/add.md",
    "a": "@context/add.md",
    "update": "@context/update.md",
    "upd": "@context/update.md",
    "u": "@context/update.md",
    "search": "@context/search.md",
    "s": "@context/search.md"
  }
}

// 二级命令 - exec 模块
{
  "exec": {
    "task": "@execution/task_generation.md",
    "t": "@execution/task_generation.md",
    "sync": "@execution/story_sync.md",
    "sy": "@execution/story_sync.md",
    "summary": "@execution/change_summary.md",
    "sum": "@execution/change_summary.md"
  }
}
```

### 3. 路由处理流程

```
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

### 4. 参数传递

将命令后的所有参数传递给目标 Playbook：

```
@tc plan story 用户登录功能 --feature=FEAT-01
         ↓
加载: @planning/story_writing.md
参数: ["用户登录功能", "--feature=FEAT-01"]
```

---

## 📝 使用示例

### 示例 1：初始化项目

```
用户：@tc.md init
AI：加载 @initialization/project_init.md 并执行初始化
```

### 示例 2：生成 Story（一级命令）

```
用户：@tc.md story 用户登录功能
AI：加载 @planning/story_writing.md
    参数：用户登录功能
```

### 示例 3：生成 Story（二级命令）

```
用户：@tc.md plan story 用户登录功能
AI：加载 @planning/story_writing.md
    参数：用户登录功能
```

### 示例 4：使用缩写

```
用户：@tc.md plan s 用户注册
AI：识别缩写 's' → story
    加载 @planning/story_writing.md
    参数：用户注册
```

### 示例 5：上下文管理

```
用户：@tc.md ctx add --type=architecture
AI：加载 @context/add.md
    参数：--type=architecture
```

### 示例 6：上下文管理（缩写）

```
用户：@tc.md ctx a --type=architecture
AI：识别缩写 'a' → add
    加载 @context/add.md
    参数：--type=architecture
```

### 示例 7：需求拆解

```
用户：@tc.md plan breakdown requirements.md
AI：加载 @planning/requirements_breakdown.md
    参数：requirements.md
```

### 示例 8：需求拆解（缩写）

```
用户：@tc.md plan bd requirements.md
AI：识别缩写 'bd' → breakdown
    加载 @planning/requirements_breakdown.md
    参数：requirements.md
```

---

## 🔍 命令未识别处理

当命令无法识别时：

1. **检查拼写**：提示可能的正确拼写
2. **建议命令**：列出相似的可用命令
3. **显示帮助**：引导用户使用 `@tc help` 或 `@tc list`

示例：

```
❌ 未识别的命令: @tc.md plan xyz

你可能想要使用：
  • @tc.md plan story    - 生成 Story
  • @tc.md plan status   - 查看项目状态
  • @tc.md plan next     - 下一步建议

使用 @tc.md help 查看所有命令
使用 @tc.md help plan 查看 plan 模块的命令
```

---

## 🌐 中文命令支持

支持中文命令别名：

| 中文            | 英文             |
| --------------- | ---------------- |
| `@tc.md 初始化` | `@tc.md init`    |
| `@tc.md 状态`   | `@tc.md status`  |
| `@tc.md 下一步` | `@tc.md next`    |
| `@tc.md 故事`   | `@tc.md story`   |
| `@tc.md 特性`   | `@tc.md feature` |
| `@tc.md 史诗`   | `@tc.md epic`    |
| `@tc.md 缺陷`   | `@tc.md bugfix`  |
| `@tc.md 任务`   | `@tc.md task`    |
| `@tc.md 同步`   | `@tc.md sync`    |
| `@tc.md 摘要`   | `@tc.md summary` |
| `@tc.md 帮助`   | `@tc.md help`    |

模块级别：

| 中文            | 英文          |
| --------------- | ------------- |
| `@tc.md 规划`   | `@tc.md plan` |
| `@tc.md 上下文` | `@tc.md ctx`  |
| `@tc.md 执行`   | `@tc.md exec` |

---

## 💡 智能推荐

根据用户输入的自然语言，智能推荐合适的命令：

| 用户输入             | 推荐命令                             |
| -------------------- | ------------------------------------ |
| "我想开始一个新项目" | `@tc.md init`                        |
| "创建一个新功能"     | `@tc.md story` 或 `@tc.md feature`   |
| "修复一个 bug"       | `@tc.md bugfix`                      |
| "我该做什么"         | `@tc.md next`                        |
| "看看进度"           | `@tc.md status`                      |
| "添加架构文档"       | `@tc.md ctx add --type=architecture` |

---

## ⚠️ 重要提醒

1. **遵守核心规则**：所有操作必须遵循 `@core/base_rules.md`
2. **文档保护**：严格禁止修改 `.the_conn/docs/` 目录
3. **大小写不敏感**：命令识别不区分大小写
4. **参数完整性**：确保所有参数正确传递给目标 Playbook
5. **反馈及时**：每次执行后提供清晰的结果反馈

---

## 🚦 执行流程总览

```
@tc.md <模块> <命令> [参数]
    ↓
命令解析
    ↓
路由匹配
    ↓
加载 Playbook
    ↓
传递参数
    ↓
执行任务
    ↓
结果反馈
```

---

## 开始使用

现在你已准备好处理用户通过 `@tc.md` 或 `@playbooks/tc.md` 发起的命令。

**记住**：
- 用户在 AI IDE 中使用 @ 符号引用此文件：`@tc.md` 或 `@playbooks/tc.md`
- 优先匹配一级命令
- 然后匹配二级命令
- 支持所有定义的缩写
- 不区分大小写
- 将所有额外参数传递给目标 Playbook

让我们开始吧！🚀

