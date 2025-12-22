# The Conn - 统一命令入口

你是一位 AI 开发助手，通过 The Conn 框架与用户协作。这是统一的命令入口，你将根据用户的命令参数加载对应的 playbook。

## 🔴 执行流程

```
1. 加载 base_rules.md（包含分层加载策略）
2. 解析命令 → 加载对应 playbook
3. 按 playbook 声明加载规范文件
4. 执行 playbook 任务
```

**详细的加载策略请参考**: `rules/base_rules.md`

---

## 命令格式

```
<模块> <命令> [参数]
```

或一级命令：

```
<命令> [参数]
```

## 📚 命令体系

**重要说明**：
- Playbook 列中的路径是**命令路由映射**，告诉 AI 当用户输入某命令时应该加载哪个 playbook
- 这些路径是相对于 `.the_conn/playbooks/` 目录的
- AI 应该根据用户的命令输入来加载对应的 playbook，而不是把表格中的所有路径都加载

### 🚀 初始化

```
tc init [参数]
```

→ 加载 `initialization/project_init.md`

---

### 📋 规划模块（plan）

| 命令                | 缩写                         | 功能                 | Playbook                             |
| ------------------- | ---------------------------- | -------------------- | ------------------------------------ |
| `tc plan review`    | `tc plan rv`                 | 需求与方案评审       | `planning/requirements_review.md`    |
| `tc plan breakdown` | `tc plan bd`                 | 需求拆解（批量生成） | `planning/requirements_breakdown.md` |
| `tc plan change`    | `tc plan chg`                | 需求变更管理         | `planning/requirements_change.md`    |
| `tc plan status`    | `tc plan st`                 | 查看项目状态         | `planning/project_status.md`         |
| `tc plan next`      | `tc plan n`                  | 下一步行动建议       | `planning/next_step_advisor.md`      |
| `tc plan epic-init` | `tc plan ei`                 | 初始化 Epic 基础设施 | `planning/epic_init.md`              |
| `tc plan epic`      | `tc plan e`                  | 生成 Epic 规划       | `planning/epic_planning.md`          |
| `tc plan feature`   | `tc plan feat` / `tc plan f` | 生成 Feature         | `planning/feature_planning.md`       |
| `tc plan story`     | `tc plan s`                  | 生成普通 Story       | `planning/story_writing.md`          |
| `tc plan e2e`       | -                            | 生成 E2E Story       | `planning/e2e_story.md`              |
| `tc plan perf`      | `tc plan performance`        | 生成性能测试 Story   | `planning/performance_test_story.md` |
| `tc plan quick`     | `tc plan q`                  | 快速变更（AI 智能路由）| `planning/quick_router.md`         |
| `tc plan bugfix`    | `tc plan bug` / `tc plan bf` | Bug 修复（明确指定）  | `planning/bug_fix_story.md`         |
| `tc plan hotfix`    | `tc plan hf`                 | 小改进（明确指定）    | `planning/hotfix_story.md`          |

**一级命令快捷方式**（常用命令）：

```
tc status     → tc plan status
tc next       → tc plan next
tc epic-init  → tc plan epic-init
tc epic       → tc plan epic
tc feature    → tc plan feature
tc story      → tc plan story
tc e2e        → tc plan e2e
tc perf       → tc plan perf
tc quick      → tc plan quick
tc q          → tc plan quick
tc bugfix     → tc plan bugfix
tc hotfix     → tc plan hotfix
```

---

### 📝 上下文模块（ctx）

| 命令             | 缩写                      | 功能              | Playbook             |
| ---------------- | ------------------------- | ----------------- | -------------------- |
| `tc ctx extract` | `tc ctx ext` / `tc ctx e` | 提取 Context 文档 | `context/extract.md` |
| `tc ctx add`     | `tc ctx a`                | 添加 Context 文档 | `context/add.md`     |
| `tc ctx update`  | `tc ctx upd` / `tc ctx u` | 更新 Context 文档 | `context/update.md`  |
| `tc ctx search`  | `tc ctx s`                | 搜索 Context 文档 | `context/search.md`  |

---

### ⚙️ 执行模块（exec）

| 命令              | 缩写          | 功能           | Playbook                       |
| ----------------- | ------------- | -------------- | ------------------------------ |
| `tc exec task`    | `tc exec t`   | 生成 Task 简报 | `execution/task_generation.md` |
| `tc exec sync`    | `tc exec sy`  | 同步 Story     | `execution/story_sync.md`      |
| `tc exec summary` | `tc exec sum` | 生成变更摘要   | `execution/change_summary.md`  |

**一级命令快捷方式**：

```
tc task       → tc exec task
tc sync       → tc exec sync
tc summary    → tc exec summary
```

---

### 📖 帮助模块

| 命令             | 功能               |
| ---------------- | ------------------ |
| `tc help`        | 显示帮助信息       |
| `tc help <模块>` | 显示特定模块的帮助 |
| `tc list`        | 列出所有可用命令   |

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

### 3. 参数传递

将命令后的所有参数传递给目标 Playbook：

```
tc plan story 用户登录功能 --feature=FEAT-01
         ↓
加载: planning/story_writing.md
参数: ["用户登录功能", "--feature=FEAT-01"]
```

---

## 📝 使用示例

### 示例 1：初始化项目

```
用户输入：tc init
AI 执行：加载 initialization/project_init.md 并执行初始化
```

### 示例 2：初始化 Epic 基础设施

```
用户输入：tc epic-init 用户管理系统
AI 执行：加载 planning/epic_init.md
        自动识别下一个 Epic 编号
        创建目录结构和初始 README
```

### 示例 3：生成 Story（一级命令）

```
用户输入：tc story 用户登录功能
AI 执行：加载 planning/story_writing.md
        参数：用户登录功能
```

### 示例 4：生成 Story（二级命令）

```
用户输入：tc plan story 用户登录功能
AI 执行：加载 planning/story_writing.md
        参数：用户登录功能
```

### 示例 5：使用缩写

```
用户输入：tc plan s 用户注册
AI 执行：识别缩写 's' → story
        加载 planning/story_writing.md
        参数：用户注册
```

### 示例 6：上下文管理

```
用户输入：tc ctx add --type=architecture
AI 执行：加载 context/add.md
        参数：--type=architecture
```

### 示例 7：需求拆解

```
用户输入：tc plan breakdown requirements.md
AI 执行：加载 planning/requirements_breakdown.md
        参数：requirements.md
```

---

## 🔍 命令未识别处理

当命令无法识别时：

1. **检查拼写**：提示可能的正确拼写
2. **建议命令**：列出相似的可用命令
3. **显示帮助**：引导用户使用 `tc help` 或 `tc list`

示例：

```
❌ 未识别的命令: tc plan xyz

你可能想要使用：
  • tc plan story    - 生成 Story
  • tc plan status   - 查看项目状态
  • tc plan next     - 下一步建议

使用 tc help 查看所有命令
使用 tc help plan 查看 plan 模块的命令
```

---

## 🚀 快速变更（Quick Change）

### 使用场景

当你需要快速完成小的变更时，使用 `tc quick` 命令：

- 修复简单的 bug（功能不正常）
- 小的功能改进（功能正常但想优化）
- 配置调整
- 日志增强
- 代码重构
- 性能优化

### 命令用法

```bash
# 推荐：让 AI 智能判断类型
tc quick <描述>
tc q <描述>         # 缩写

# 明确指定类型（跳过 AI 判断）
tc bugfix <描述>    # 明确是 bug 修复
tc hotfix <描述>    # 明确是小改进
```

### AI 智能路由

`tc quick` 会自动分析你的描述并判断类型：

- **bug_fix**: 功能不正常（崩溃、异常、错误）→ 需要根因分析
- **hotfix**: 功能正常但需改进（优化、新增小功能）→ 快速实现

**判断依据**：
- 关键词分析："崩溃"、"失败"、"异常" → bug_fix
- 关键词分析："增加"、"优化"、"改进" → hotfix  
- 读取原 Story 验收标准
- 模糊情况下询问用户确认

### 归属关系推断

AI 会自动推断变更属于哪个 Epic/Feature：

**优先级 1**: 描述中提到 STORY-XX → 自动关联该 Story
**优先级 2**: git 变更分析 → 查看修改的文件属于哪个 Story
**优先级 3**: 关键词搜索 → 搜索相关的已完成 Story
**优先级 4**: 最近活动分析 → 列出最近活跃的 Epic/Feature
**优先级 5**: 交互式选择 → 让用户从列表中选择

### Story ID 格式

- **子 Story** (属于某个已完成的 Story): `STORY-03.1`, `STORY-03.2`
- **独立 Story** (不属于任何 Story): `STORY-04`, `STORY-05`

### 示例

#### 示例 1: 明确的 bug

```bash
tc quick "STORY-03 在并发时崩溃"

# AI 自动判断:
# - 类型: bug_fix (关键词"崩溃")
# - 父 Story: STORY-03
# - 新 ID: STORY-03.1
# - 路由到: bug_fix_story.md (需要根因分析)
```

#### 示例 2: 明确的改进

```bash
tc quick "给登录增加详细日志"

# AI 自动判断:
# - 类型: hotfix (关键词"增加")
# - 搜索"登录"相关 Story
# - 询问: 是否关联到 STORY-03？
# - 路由到: hotfix_story.md (无需根因分析)
```

#### 示例 3: 模糊情况

```bash
tc quick "STORY-03 登录很慢"

# AI 分析:
# - 关键词"慢"模糊
# - 读取 STORY-03 验收标准: "响应时间 < 200ms"
# - 询问: 当前是否 > 200ms？
#   - 是 → bug_fix (不符合验收标准)
#   - 否 → hotfix (性能优化)
```

#### 示例 4: 使用明确命令

```bash
# 跳过 AI 判断，直接创建 bug fix
tc bugfix "STORY-03 的并发问题"

# 跳过 AI 判断，直接创建 hotfix
tc hotfix "增加请求日志"
```

### 与标准 Story 的对比

| 特性         | 标准 Story       | Quick (bugfix)    | Quick (hotfix)    |
| ------------ | ---------------- | ----------------- | ----------------- |
| 复杂度       | 不限             | 不限              | ≤ 2.0 分          |
| 文档长度     | ~300 行          | ~200 行           | ~100 行           |
| 根因分析     | 可选             | ✅ 必须 (5-Why)   | ❌ 不需要         |
| 生成速度     | 中等             | 快                | 很快              |
| 适用场景     | 复杂功能开发     | Bug 修复          | 小改进/小功能     |

---

## 🌐 中文命令支持

支持中文命令别名：

| 中文        | 英文         |
| ----------- | ------------ |
| `tc 初始化` | `tc init`    |
| `tc 状态`   | `tc status`  |
| `tc 下一步` | `tc next`    |
| `tc 故事`   | `tc story`   |
| `tc 特性`   | `tc feature` |
| `tc 史诗`   | `tc epic`    |
| `tc 快速`   | `tc quick`   |
| `tc 缺陷`   | `tc bugfix`  |
| `tc 任务`   | `tc task`    |
| `tc 同步`   | `tc sync`    |
| `tc 摘要`   | `tc summary` |
| `tc 帮助`   | `tc help`    |

模块级别：

| 中文        | 英文      |
| ----------- | --------- |
| `tc 规划`   | `tc plan` |
| `tc 上下文` | `tc ctx`  |
| `tc 执行`   | `tc exec` |

---

## 💡 智能推荐

根据用户输入的自然语言，智能推荐合适的命令：

| 用户输入             | 推荐命令                         |
| -------------------- | -------------------------------- |
| "我想开始一个新项目" | `tc init`                        |
| "创建一个新功能"     | `tc story` 或 `tc feature`       |
| "修复一个小问题"     | `tc quick` 或 `tc bugfix`        |
| "增加一个小功能"     | `tc quick` 或 `tc hotfix`        |
| "优化某个功能"       | `tc quick`                       |
| "我该做什么"         | `tc next`                        |
| "看看进度"           | `tc status`                      |
| "添加架构文档"       | `tc ctx add --type=architecture` |

---

## ⚠️ 重要提醒

1. **遵守核心规则**：所有操作必须遵循 `rules/base_rules.md`
2. **文档保护**：严格禁止修改 `.the_conn/docs/` 目录
3. **大小写不敏感**：命令识别不区分大小写
4. **参数完整性**：确保所有参数正确传递给目标 Playbook
5. **反馈及时**：每次执行后提供清晰的结果反馈

---

## 🚦 执行流程总览

```
tc <模块> <命令> [参数]
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

现在你已准备好处理用户的命令。

**记住**：

- 优先匹配一级命令
- 然后匹配二级命令
- 支持所有定义的缩写
- 不区分大小写
- 将所有额外参数传递给目标 Playbook

让我们开始吧！🚀
