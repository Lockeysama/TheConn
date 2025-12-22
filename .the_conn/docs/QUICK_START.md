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

### 需求评审与拆解（最常用）

```bash
@tc.md review
# 或完整命令
@tc.md plan review
```

### 快速变更（最常用）

```bash
@tc.md quick "修复登录bug"
# 或缩写
@tc.md q "修复登录bug"
# 或完整命令
@tc.md plan quick "修复登录bug"
```

### 查看项目状态

```bash
@tc.md plan status
```

### 获取下一步建议

```bash
@tc.md plan next
```

### 需求评审与拆解（最常用 ⭐）

```bash
@tc.md review
# 或完整命令
@tc.md plan review
```

AI 会与你讨论需求和技术方案，确认后自动：
1. 初始化 Epic 基础设施
2. 提取/更新 global context
3. 添加 epic context
4. 批量生成 Epic/Feature/Story

### 快速变更（最常用 ⭐）

```bash
@tc.md quick "修复登录按钮样式"
# 或缩写
@tc.md q "优化查询性能"
# 或完整命令
@tc.md plan quick "添加用户头像显示"
```

### 创建规划文档

```bash
# Epic
@tc.md plan epic 用户管理系统

# Feature
@tc.md plan feature 用户认证

# Story
@tc.md plan story 用户登录功能

# E2E Story
@tc.md plan e2e 用户注册流程

# 性能测试 Story
@tc.md plan perf API 响应时间优化
```

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
# 生成 Task 简报（最常用 ⭐）
@tc.md gtask STORY-01
# 或完整命令
@tc.md exec task-generate STORY-01

# 执行 Task（最常用 ⭐）
@tc.md etask
# 或完整命令
@tc.md exec task-execute

# 同步 Story 状态
@tc.md exec sync

# 生成变更摘要
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

### 最常用命令 ⭐

| 命令                        | 一级快捷           | 功能           |
| --------------------------- | ------------------ | -------------- |
| `@tc.md plan review`        | `@tc.md review`    | 需求评审与拆解 |
| `@tc.md plan quick`         | `@tc.md quick / q` | 快速变更       |
| `@tc.md exec task-generate` | `@tc.md gtask`     | 生成 Task      |
| `@tc.md exec task-execute`  | `@tc.md etask`     | 执行 Task      |

### 规划模块（plan）

| 命令                  | 功能           |
| --------------------- | -------------- |
| `@tc.md plan status`  | 项目状态       |
| `@tc.md plan next`    | 下一步建议     |
| `@tc.md plan epic`    | 创建 Epic      |
| `@tc.md plan feature` | 创建 Feature   |
| `@tc.md plan story`   | 创建 Story     |
| `@tc.md plan e2e`     | E2E Story      |
| `@tc.md plan perf`    | 性能测试 Story |

### 上下文模块（ctx）

| 命令                | 功能                   |
| ------------------- | ---------------------- |
| `@tc.md ctx add`    | 添加/提取 Context 文档 |
| `@tc.md ctx update` | 更新 Context 文档      |

### 执行模块（exec）

| 命令                  | 功能       |
| --------------------- | ---------- |
| `@tc.md exec sync`    | 同步 Story |
| `@tc.md exec summary` | 变更摘要   |

---

## 💡 使用技巧

### 1. 最常用命令有一级快捷方式 ⭐

```bash
# 需求评审
@tc.md review              # 一级快捷（推荐）
@tc.md plan review         # 完整命令

# 快速变更
@tc.md quick "描述"        # 一级快捷（推荐）
@tc.md q "描述"            # 超级缩写
@tc.md plan quick "描述"   # 完整命令

# 生成和执行 Task
@tc.md gtask STORY-01      # 一级快捷（推荐）
@tc.md etask               # 一级快捷（推荐）
@tc.md exec task-generate STORY-01  # 完整命令
@tc.md exec task-execute            # 完整命令
```

### 2. 其他命令使用二级形式

```bash
# 规划模块
@tc.md plan story 用户登录
@tc.md plan status

# 上下文模块
@tc.md ctx update Architecture.md

# 执行模块
@tc.md exec sync
@tc.md exec summary
```

### 3. 完整工作流

```bash
# 步骤 1: 初始化项目
@tc.md init

# 步骤 2: 需求评审与拆解（一级快捷）
@tc.md review

# 步骤 3: 生成和执行 Task（一级快捷）
@tc.md gtask STORY-01
@tc.md etask

# 步骤 4: 同步状态
@tc.md exec sync
```

---

## 🎓 工作流示例

### 场景 1：从零开始

```bash
# 1. 初始化项目
@tc.md init

# 2. 需求评审与拆解（一级快捷）
@tc.md review
# AI 与你讨论需求，确认后自动生成所有文档

# 3. 查看生成的文档
# 在 .the_conn/epics/ 目录下查看
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

# 2. 添加技术栈文档
@tc.md ctx add --type=tech_stack

# 3. 更新 Context
@tc.md ctx update Architecture.md
```

---

## 📊 命令对比

### 最常用命令（有一级快捷）⭐

| 功能      | 完整命令                    | 一级快捷           |
| --------- | --------------------------- | ------------------ |
| 需求评审  | `@tc.md plan review`        | `@tc.md review`    |
| 快速变更  | `@tc.md plan quick`         | `@tc.md quick / q` |
| 生成 Task | `@tc.md exec task-generate` | `@tc.md gtask`     |
| 执行 Task | `@tc.md exec task-execute`  | `@tc.md etask`     |

### 其他命令（仅二级形式）

| 功能         | 完整命令              |
| ------------ | --------------------- |
| 项目状态     | `@tc.md plan status`  |
| 下一步       | `@tc.md plan next`    |
| 生成 Story   | `@tc.md plan story`   |
| 生成 Epic    | `@tc.md plan epic`    |
| 生成 Feature | `@tc.md plan feature` |
| E2E Story    | `@tc.md plan e2e`     |
| 性能测试     | `@tc.md plan perf`    |
| 添加 Context | `@tc.md ctx add`      |
| 更新 Context | `@tc.md ctx update`   |
| 同步 Story   | `@tc.md exec sync`    |
| 变更摘要     | `@tc.md exec summary` |


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

## 🔗 Playbook 引用关系

### 主要工作流的 Playbook 调用链

**工作流 1：需求评审与完整拆解**
```
requirements_review.md
  ↓ 调用
epic_init.md → context/add.md → requirements_breakdown.md
```

**工作流 2：快速变更（Bug/Hotfix）**
```
quick_router.md
  ↓ 路由
bug_fix_story.md 或 hotfix_story.md
```

**工作流 3：Task 执行闭环**
```
task_generation.md (引用 context/search.md)
  ↓
task_execution.md
  ↓
change_summary.md → story_sync.md
```

### Context 引用层级

```
Global Context (4个固定文件)
  ├─ Architecture.md
  ├─ Tech_Stack.md
  ├─ Testing_Strategy.md
  └─ Coding_Standard_*.md
       ↓
Epic Context (按需创建)
  ├─ Module_Design_*.md
  ├─ Data_Model_*.md
  └─ ...
       ↓
Task 加载时按需引用 (通过 context/search.md)
```

---

## 🔄 隐含工作流说明

### tc review（完整拆解）

执行 `@tc.md review` 后，AI 会依次调用：
1. **epic_init.md** - 初始化 Epic 目录结构和 README
2. **context/add.md** - 提取/更新全局 Context（如架构、技术栈）
3. **context/add.md** - 添加 Epic 专属 Context（如模块设计）
4. **requirements_breakdown.md** - 批量生成完整规划
   - 生成所有 Epic、Feature、Story 规划文档
   - 自动应用测试策略（E2E、性能测试）
   - 分析依赖关系和开发顺序
   - 使用粒度控制标准（避免过度拆分）

### tc quick（快速变更）

执行 `@tc.md quick "描述"` 后，AI 会：
1. **quick_router.md** - 分析并判断类型
2. 路由到 **bug_fix_story.md** 或 **hotfix_story.md**

### Task 执行闭环

```
tc gtask STORY-XX → task_generation.md
tc etask → task_execution.md
（开发完成后）
tc exec summary → change_summary.md
tc exec sync → story_sync.md
```

---

**现在开始使用 `@tc` 命令，开启高效的 AI 协作开发之旅！** 🚀
