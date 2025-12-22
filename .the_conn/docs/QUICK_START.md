# The Conn - 快速开始指南

## 🎯 使用 @tc.md 命令

The Conn 提供了统一的命令入口文件 `tc.md`，让你通过简单的命令操作所有功能。

## 基本用法

### 命令格式

在 AI IDE 中，使用 @ 符号引用 tc.md 文件：

```
@tc.md <模块> <命令> [参数]
```

或使用完整路径：

```
@playbooks/tc.md <模块> <命令> [参数]
```

一级快捷命令：

```
@tc.md <命令> [参数]
```

---

## 🚀 核心命令速查

### 初始化项目

```bash
@tc.md init
```

### 查看项目状态

```bash
@tc.md status
# 或
@tc.md plan status
# 或缩写
@tc.md plan st
```

### 获取下一步建议

```bash
@tc.md next
# 或
@tc.md plan next
```

### 需求评审与拆解

```bash
# 推荐：完整工作流（评审 → 拆解 → 生成）
@tc.md plan review
# AI 会与你讨论需求和技术方案
# 确认后自动批量生成 Epic/Feature/Story
```

### 创建 Epic

```bash
# 创建 Epic（自动处理初始化）
@tc.md epic 用户管理系统
# 或
@tc.md plan epic 用户管理系统
```

**说明**：`tc epic` 会自动检测是否已初始化，如未初始化会先创建目录结构，然后生成 Epic 规划内容。

### 创建 Feature 和 Story

```bash
# 生成 Feature
@tc.md feature 用户认证
# 或
@tc.md plan feature 用户认证
# 或缩写
@tc.md plan f 用户认证

# 生成普通 Story（功能开发）
@tc.md story 实现用户登录功能
# 或
@tc.md plan story 实现用户登录功能
# 或缩写
@tc.md plan s 实现用户登录功能

# 生成 E2E Story（集成测试）
@tc.md e2e
@tc.md plan e2e

# 生成性能测试 Story
@tc.md perf
@tc.md plan perf
```

### 快速变更（⭐ 推荐）

```bash
# 智能判断类型并路由（推荐）
@tc.md quick "STORY-03 在并发时崩溃"
@tc.md q "增加登录详细日志"                    # 缩写
```

**Quick Change 特点**：
- ⚡ **快速**：文档精简但保留关键要素
- 🤖 **智能**：AI 自动判断是 bug 还是改进
- 📊 **完整**：保持 Epic 体系和文档可追溯性
- 🎯 **适用**：复杂度 ≤ 2 分的小变更

### 管理 Context

```bash
# 添加或提取 Context 文档
@tc.md ctx add --type=architecture
# AI 会根据输入自动判断是直接添加还是从材料中提取

# 更新 Context 文档
@tc.md ctx update Architecture.md
# 或缩写
@tc.md ctx u Architecture.md
```

### 执行开发任务

```bash
# 生成 Task 简报（超高频命令）
@tc.md gtask STORY-01
# 或完整命令
@tc.md exec task-generate STORY-01
# 或缩写
@tc.md exec tg STORY-01

# 执行 Task（超高频命令）
@tc.md etask
# 或完整命令
@tc.md exec task-execute
# 或缩写
@tc.md exec te

# 同步 Story 状态
@tc.md sync
# 或
@tc.md exec sync

# 生成变更摘要
@tc.md summary
# 或
@tc.md exec summary
```

### 查看帮助

```bash
@tc.md help
# 或查看特定模块帮助
@tc.md help plan
@tc.md help ctx
@tc.md help exec
```

---

## 📋 命令速查表

### 规划模块（plan）

| 命令                  | 缩写 | 一级快捷    | 功能                 |
| --------------------- | ---- | ----------- | -------------------- |
| `@tc.md plan review`  | -    | -           | 需求评审与拆解       |
| `@tc.md plan status`  | `st` | `status`    | 项目状态             |
| `@tc.md plan next`    | -    | `next`      | 下一步建议           |
| `@tc.md plan epic`    | -    | `epic`      | 创建 Epic            |
| `@tc.md plan feature` | `f`  | `feature`   | 创建 Feature         |
| `@tc.md plan story`   | `s`  | `story`     | 创建 Story           |
| `@tc.md plan quick`   | `q`  | `quick / q` | 快速变更（智能路由） |
| `@tc.md plan e2e`     | -    | `e2e`       | E2E Story            |
| `@tc.md plan perf`    | -    | `perf`      | 性能测试 Story       |

### 上下文模块（ctx）

| 命令                | 缩写 | 功能                   |
| ------------------- | ---- | ---------------------- |
| `@tc.md ctx add`    | -    | 添加/提取 Context 文档 |
| `@tc.md ctx update` | `u`  | 更新 Context 文档      |

### 执行模块（exec）

| 命令                        | 缩写  | 一级快捷  | 功能       |
| --------------------------- | ----- | --------- | ---------- |
| `@tc.md exec task-generate` | `tg`  | `gtask`   | 生成 Task  |
| `@tc.md exec task-execute`  | `te`  | `etask`   | 执行 Task  |
| `@tc.md exec sync`          | `sy`  | `sync`    | 同步 Story |
| `@tc.md exec summary`       | `sum` | `summary` | 变更摘要   |

---

## 💡 使用技巧

### 1. 使用缩写提高效率

高频命令支持缩写：

```bash
# 完整命令
@tc.md plan story 用户登录
@tc.md plan feature 用户管理
@tc.md plan quick "修复登录bug"

# 缩写命令
@tc.md plan s 用户登录
@tc.md plan f 用户管理
@tc.md plan q "修复登录bug"
```

### 2. 一级命令更简洁

常用命令可以直接使用一级形式：

```bash
# 二级命令
@tc.md plan story 用户登录
@tc.md plan status
@tc.md exec task-generate STORY-01

# 一级命令（推荐）
@tc.md story 用户登录
@tc.md status
@tc.md gtask STORY-01
```

### 3. 链式操作

```bash
# 步骤 1: 初始化
@tc.md init

# 步骤 2: 需求评审与拆解
@tc.md plan review
# AI 会与你讨论需求，确认后自动批量生成 Epic/Feature/Story

# 步骤 3: 生成 Task 并执行
@tc.md gtask STORY-01
@tc.md etask

# 步骤 4: 同步完成状态
@tc.md sync
```

---

## 🎓 工作流示例

### 场景 1：开始新项目（推荐流程）

```bash
# 1. 初始化
@tc.md init

# 2. 需求评审与批量拆解
@tc.md plan review
# AI 与你讨论需求和技术方案
# 确认后自动批量生成所有 Epic/Feature/Story

# 3. 查看生成的规划
@tc.md status

# 4. 开始第一个 Story
@tc.md task STORY-01

# 5. 查看下一步
@tc.md next
```

### 场景 2：逐步创建（精细控制）

```bash
# 1. 初始化
@tc.md init

# 2. 创建 Epic
@tc.md epic 电商平台

# 3. 创建 Feature
@tc.md feature 商品管理 --epic=EPIC-01

# 4. 创建 Story
@tc.md story 添加商品 --feature=FEAT-01

# 5. 生成 Task
@tc.md task STORY-01

# 6. 查看下一步
@tc.md next
```

### 场景 3：快速变更（⭐ 推荐）

```bash
# 使用 quick 命令，AI 自动判断类型
@tc.md quick "STORY-05 商品价格显示错误"
# AI 分析: "错误" → bug_fix
# 生成: STORY-05.1 (Bug Fix Story，包含根因分析)

@tc.md quick "给商品列表增加筛选功能"
# AI 分析: "增加" → hotfix  
# 生成: STORY-06 (Hotfix Story，简化流程)

# 后续流程相同
@tc.md task STORY-05.1
@tc.md sync
```

### 场景 4：追溯补录（代码已完成）

```bash
# 情况：你已经手动修改了代码，现在需要补录文档

# 1. 使用 quick 创建 Story
@tc.md quick "修复登录时的空指针检查"
# AI 检测到 git diff 有变更
# 询问: "检测到未提交的变更，是否为追溯模式？"
# 选择: y

# 2. AI 从 git diff 自动填充"涉及文件"
# 3. 你补充验收标准

# 4. 直接生成变更摘要（跳过 Task）
@tc.md summary

# 5. 同步 Story 状态
@tc.md sync
```

### 场景 5：管理 Context

```bash
# 1. 添加或提取 Context 文档
@tc.md ctx add --type=architecture
# AI 会根据你的输入判断是直接添加还是从材料中提取

# 2. 添加技术栈文档
@tc.md ctx add --type=tech_stack

# 3. 更新 Context
@tc.md ctx update Architecture.md
# 或缩写
@tc.md ctx u Architecture.md
```

---

## 📊 命令对比

| 功能         | 完整命令                    | 缩写             | 一级快捷           |
| ------------ | --------------------------- | ---------------- | ------------------ |
| 项目状态     | `@tc.md plan status`        | `@tc.md plan st` | `@tc.md status`    |
| 下一步       | `@tc.md plan next`          | -                | `@tc.md next`      |
| 生成 Story   | `@tc.md plan story`         | `@tc.md plan s`  | `@tc.md story`     |
| 生成 Epic    | `@tc.md plan epic`          | -                | `@tc.md epic`      |
| 生成 Feature | `@tc.md plan feature`       | `@tc.md plan f`  | `@tc.md feature`   |
| 快速变更     | `@tc.md plan quick`         | `@tc.md plan q`  | `@tc.md quick / q` |
| 更新 Context | `@tc.md ctx update`         | `@tc.md ctx u`   | -                  |
| 生成 Task    | `@tc.md exec task-generate` | `@tc.md exec tg` | `@tc.md gtask`     |
| 执行 Task    | `@tc.md exec task-execute`  | `@tc.md exec te` | `@tc.md etask`     |
| 同步 Story   | `@tc.md exec sync`          | `@tc.md exec sy` | `@tc.md sync`      |


---

## 🔗 相关文档

- 📘 [命令参考手册](COMMANDS.md) - 完整的命令列表
- 📗 [完整使用指南](GUIDE.md) - 详细工作流程
- 📕 [命令映射表](COMMAND_MAPPING.md) - 命令与 Playbook 对照

---

## 🆘 遇到问题？

1. **不确定用什么命令**：

   ```bash
   @tc.md help
   @tc.md list
   ```

2. **不知道下一步**：

   ```bash
   @tc.md next
   ```

3. **查看项目状态**：

   ```bash
   @tc.md status
   ```

4. **查看模块帮助**：

   ```bash
   @tc.md help plan
   @tc.md help ctx
   @tc.md help exec
   ```

---

**现在开始使用 `@tc` 命令，开启高效的 AI 协作开发之旅！** 🚀
