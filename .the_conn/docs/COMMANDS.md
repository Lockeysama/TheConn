# The Conn - 命令参考手册

## 📖 命令总览

### 命令结构

```
@tc.md <模块> <命令> [参数]
```

或使用一级快捷命令（仅 4 个最常用命令）：

```
@tc.md <命令> [参数]
```

---

## 🚀 初始化命令

### `@tc.md init`

**功能**：初始化 The Conn 项目结构

**语法**：

```bash
@tc.md init
```

**调用的 Playbook**：`initialization/project_init.md`

---

## ⭐ 最常用命令（有一级快捷）

### `@tc.md review` / `@tc.md plan review`

**功能**：需求评审与拆解（最常用）

**语法**：

```bash
@tc.md review [文档路径]
@tc.md plan review [文档路径]
```

**示例**：

```bash
@tc.md review requirements.md
@tc.md review
```

**说明**：AI 会与你讨论需求和技术方案，确认后自动批量生成 Epic/Feature/Story

**调用的 Playbook**：`planning/requirements_review.md`

---

### `@tc.md quick` / `@tc.md q` / `@tc.md plan quick`

**功能**：快速变更（智能路由，最常用）

**语法**：

```bash
@tc.md quick "<变更描述>"
@tc.md q "<变更描述>"
@tc.md plan quick "<变更描述>"
```

**示例**：

```bash
@tc.md quick "修复登录按钮点击无响应"
@tc.md q "优化首页加载速度"
```

**说明**：
- AI 自动判断变更类型（bug_fix / hotfix）并生成 Story
- Story 生成后询问：继续（自动衔接）/ 仅生成 Story / 修改 Story
- 选择"继续"时自动执行：`gtask` → `etask` → `summary` → `sync`

**调用的 Playbook**：`planning/quick_router.md`

---

### `@tc.md gtask` / `@tc.md exec task-generate`

**功能**：生成 Task 简报（最常用）

**语法**：

```bash
@tc.md gtask <Story ID>
@tc.md exec task-generate <Story ID>
```

**示例**：

```bash
@tc.md gtask STORY-01
@tc.md exec task-generate STORY-01
```

**调用的 Playbook**：`execution/task_generation.md`

---

### `@tc.md etask` / `@tc.md exec task-execute`

**功能**：执行 Task（最常用）

**语法**：

```bash
@tc.md etask
@tc.md exec task-execute
```

**示例**：

```bash
@tc.md etask
@tc.md exec task-execute
```

**说明**：AI 会按照 TDD/BDD 流程执行开发，完成后等待人工 Review

**调用的 Playbook**：`execution/task_execution.md`

---

## 📋 规划模块（plan）

### `@tc.md plan status`

**功能**：查看项目状态

**语法**：

```bash
@tc.md plan status [--epic=EPIC-ID]
```

**示例**：

```bash
@tc.md plan status
@tc.md plan status --epic=EPIC-01
```

**调用的 Playbook**：`planning/project_status.md`

---

### `@tc.md plan next`

**功能**：获取下一步行动建议

**语法**：

```bash
@tc.md plan next [--context=EPIC-ID]
```

**示例**：

```bash
@tc.md plan next
@tc.md plan next --context=EPIC-01
```

**调用的 Playbook**：`planning/next_step_advisor.md`

---

### `@tc.md plan epic`

**功能**：生成 Epic 规划

**语法**：

```bash
@tc.md plan epic <Epic名称> [--description="描述"]
```

**示例**：

```bash
@tc.md plan epic 用户管理系统
@tc.md plan epic 用户管理系统 --description="完整的用户管理功能"
```

**说明**：会自动检测并初始化 Epic 目录结构

**调用的 Playbook**：`planning/epic_planning.md`

---

### `@tc.md plan feature`

**功能**：生成 Feature

**语法**：

```bash
@tc.md plan feature <Feature名称> [--epic=EPIC-ID]
```

**示例**：

```bash
@tc.md plan feature 用户认证
@tc.md plan feature 用户认证 --epic=EPIC-01
```

**调用的 Playbook**：`planning/feature_planning.md`

---

### `@tc.md plan story`

**功能**：生成 Story

**语法**：

```bash
@tc.md plan story <Story标题> [--feature=FEAT-ID] [--epic=EPIC-ID]
```

**示例**：

```bash
@tc.md plan story 实现用户登录
@tc.md plan story 实现用户登录 --feature=FEAT-01
```

**调用的 Playbook**：`planning/story_writing.md`

---

### `@tc.md plan e2e`

**功能**：生成 E2E Story

**语法**：

```bash
@tc.md plan e2e <Story标题> [--feature=FEAT-ID]
```

**示例**：

```bash
@tc.md plan e2e 用户注册流程测试
```

**调用的 Playbook**：`planning/e2e_story.md`

---

### `@tc.md plan perf`

**功能**：生成性能测试 Story

**语法**：

```bash
@tc.md plan perf <Story标题> [--feature=FEAT-ID]
```

**示例**：

```bash
@tc.md plan perf API 响应时间优化
```

**调用的 Playbook**：`planning/performance_test_story.md`

---

## 📝 上下文模块（ctx）

### `@tc.md ctx add`

**功能**：添加/提取 Context 文档

**语法**：

```bash
@tc.md ctx add --type=<类型> [--scope=global|epic] [--epic=EPIC-ID]
```

**Context 类型**：

- Global: `architecture`, `tech_stack`, `coding_standard`, `testing_strategy`, `deployment`, `api_convention`, `domain_model`
- Epic: `module_design`, `data_model`, `api_spec`, `integration`, `algorithm`, `protocol`, `migration`

**示例**：

```bash
@tc.md ctx add --type=architecture --scope=global
@tc.md ctx add --type=module_design --scope=epic --epic=EPIC-01
```

**说明**：AI 会根据你的输入判断是直接添加还是从材料中提取

**调用的 Playbook**：`context/add.md`

---

### `@tc.md ctx update`

**功能**：更新 Context 文档

**语法**：

```bash
@tc.md ctx update <文件名>
```

**示例**：

```bash
@tc.md ctx update Architecture.md
@tc.md ctx update Tech_Stack.md
```

**调用的 Playbook**：`context/update.md`

---

## ⚙️ 执行模块（exec）

### `@tc.md exec sync`

**功能**：同步 Story 状态

**语法**：

```bash
@tc.md exec sync <Story ID>
```

**示例**：

```bash
@tc.md exec sync STORY-01
```

**调用的 Playbook**：`execution/story_sync.md`

---

### `@tc.md exec summary`

**功能**：生成变更摘要

**语法**：

```bash
@tc.md exec summary [Task ID]
```

**示例**：

```bash
@tc.md exec summary
@tc.md exec summary TASK-01
```

**调用的 Playbook**：`execution/change_summary.md`

---

## 📖 帮助命令

### `@tc.md help`

**功能**：显示帮助信息

**语法**：

```bash
@tc.md help [模块]
```

**示例**：

```bash
@tc.md help
@tc.md help plan
@tc.md help ctx
@tc.md help exec
```

---

### `@tc.md list`

**功能**：列出所有可用命令

**语法**：

```bash
@tc.md list
```

---

## 🎯 使用场景

### 场景 1：从零开始

```bash
@tc.md init                    # 初始化项目
@tc.md review requirements.md  # 需求评审与拆解
# AI 自动批量生成 Epic/Feature/Story
```

### 场景 2：执行开发

```bash
@tc.md gtask STORY-01          # 生成 Task
@tc.md etask                   # 执行 Task
# AI 完成后等待人工 Review，确认后自动闭环
```

### 场景 3：快速变更

```bash
@tc.md quick "修复登录按钮样式"
# 选择"继续" → 自动执行 gtask → etask → summary → sync

@tc.md q "优化查询性能"
# 选择"仅生成 Story" → 稍后手动执行
```

### 场景 4：创建规划

```bash
@tc.md plan epic 支付系统
@tc.md plan feature 支付宝集成
@tc.md plan story 支付接口对接
```

### 场景 5：管理 Context

```bash
@tc.md ctx add --type=architecture
@tc.md ctx update Architecture.md
```

---

## 💡 最佳实践

### 1. 优先使用最常用命令的一级快捷方式

```bash
# 推荐 ✅（最常用命令）
@tc.md review
@tc.md quick "描述"
@tc.md gtask STORY-01
@tc.md etask

# 其他命令使用二级形式 ✅
@tc.md plan status
@tc.md plan epic
@tc.md ctx add
@tc.md exec sync
```

### 2. 合理使用参数

```bash
# 带参数一次完成
@tc.md plan story 用户登录 --feature=FEAT-01

# 分步确认（AI 会询问）
@tc.md plan story 用户登录
```

### 3. 查看帮助

```bash
# 不确定命令时
@tc.md help
@tc.md help plan
@tc.md list
```

---

## 🔗 相关文档

- 📘 [快速开始指南](QUICK_START.md)
- 📗 [完整使用指南](GUIDE.md)
- 📕 [命令映射表](COMMAND_MAPPING.md)

---

**💡 提示**：
- 只有 4 个最常用命令有一级快捷方式：`review`, `quick/q`, `gtask`, `etask`
- 其他命令必须使用二级形式：`@tc.md <module> <command>`
- 所有命令不区分大小写
