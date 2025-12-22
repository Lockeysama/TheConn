# The Conn - 统一命令入口

你是一位 AI 开发助手，通过 The Conn 框架与用户协作。这是统一的命令入口，你将根据用户的命令参数加载对应的 playbook。

## 🔴 执行流程

```
1. 强制加载 @.the_conn/rules/base_rules.md
2. 解析命令 → 加载对应 playbook
3. 按 playbook 声明加载规范文件
4. 执行 playbook 任务
```

---

## 命令格式

```
<模块> <命令> [参数]
```

或一级命令：

```
<命令> [参数]
```

## 📚 核心命令

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

| 命令              | 缩写         | 一级快捷       | Playbook                             |
| ----------------- | ------------ | -------------- | ------------------------------------ |
| `tc plan review`  | -            | `tc review`    | `planning/requirements_review.md`    |
| `tc plan quick`   | `tc plan q`  | `tc quick / q` | `planning/quick_router.md`           |
| `tc plan status`  | `tc plan st` | -              | `planning/project_status.md`         |
| `tc plan next`    | -            | -              | `planning/next_step_advisor.md`      |
| `tc plan epic`    | -            | -              | `planning/epic_planning.md`          |
| `tc plan feature` | `tc plan f`  | -              | `planning/feature_planning.md`       |
| `tc plan story`   | `tc plan s`  | -              | `planning/story_writing.md`          |
| `tc plan e2e`     | -            | -              | `planning/e2e_story.md`              |
| `tc plan perf`    | -            | -              | `planning/performance_test_story.md` |

---

### 📝 上下文模块（ctx）

| 命令            | 缩写       | Playbook            |
| --------------- | ---------- | ------------------- |
| `tc ctx add`    | -          | `context/add.md`    |
| `tc ctx update` | `tc ctx u` | `context/update.md` |

---

### ⚙️ 执行模块（exec）

| 命令                    | 缩写          | 一级快捷   | Playbook                       |
| ----------------------- | ------------- | ---------- | ------------------------------ |
| `tc exec task-generate` | `tc exec tg`  | `tc gtask` | `execution/task_generation.md` |
| `tc exec task-execute`  | `tc exec te`  | `tc etask` | `execution/task_execution.md`  |
| `tc exec sync`          | `tc exec sy`  | -          | `execution/story_sync.md`      |
| `tc exec summary`       | `tc exec sum` | -          | `execution/change_summary.md`  |

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
