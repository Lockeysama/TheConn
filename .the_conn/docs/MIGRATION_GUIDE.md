# The Conn - 命令系统迁移指南

本文档帮助你从传统的 Playbook 使用方式迁移到新的 `@tc` 命令系统。

---

## 🎯 主要变化

### 1. 命令前缀变化

| 旧方式 | 新方式 |
|--------|--------|
| `@main <命令>` | `@tc.md <命令>` |
| `@playbooks/planning/story_writing.md` | `@tc.md story` |

### 2. 命令结构

新的命令系统采用**二级参数结构**：

```bash
@tc.md <模块> <命令> [参数]
```

**模块**：
- `plan` - 规划模块
- `ctx` - 上下文模块
- `exec` - 执行模块

**常用命令支持一级快捷方式**：

```bash
@tc.md story          # 等同于 @tc.md plan story
@tc.md status         # 等同于 @tc.md plan status
@tc.md task           # 等同于 @tc.md exec task
```

### 3. 缩写支持

每个命令都支持缩写：

```bash
# 完整命令
@tc.md plan breakdown
@tc.md ctx extract
@tc.md exec task

# 缩写（更快）
@tc.md plan bd
@tc.md ctx e
@tc.md exec t

# 首字母缩写
@tc.md plan s         # story
@tc.md plan f         # feature
@tc.md plan e         # epic
```

---

## 📋 命令对照表

### 规划相关

| 旧命令/Playbook | 新命令 | 缩写 |
|----------------|--------|------|
| `@planning/project_status.md` | `@tc.md status` | `@tc.md plan st` |
| `@planning/next_step_advisor.md` | `@tc.md next` | `@tc.md plan n` |
| `@planning/epic_planning.md` | `@tc.md epic` | `@tc.md plan e` |
| `@planning/feature_planning.md` | `@tc.md feature` | `@tc.md plan f` |
| `@planning/story_writing.md` | `@tc.md story` | `@tc.md plan s` |
| `@planning/bug_fix_story.md` | `@tc.md bugfix` | `@tc.md plan bf` |
| `@planning/requirements_review.md` | `@tc.md plan review` | `@tc.md plan rv` |
| `@planning/requirements_breakdown.md` | `@tc.md plan breakdown` | `@tc.md plan bd` |
| `@planning/requirements_change.md` | `@tc.md plan change` | `@tc.md plan chg` |

### 上下文相关

| 旧命令/Playbook | 新命令 | 缩写 |
|----------------|--------|------|
| `@context/extract.md` | `@tc.md ctx extract` | `@tc.md ctx e` |
| `@context/add.md` | `@tc.md ctx add` | `@tc.md ctx a` |
| `@context/update.md` | `@tc.md ctx update` | `@tc.md ctx u` |
| `@context/search.md` | `@tc.md ctx search` | `@tc.md ctx s` |

### 执行相关

| 旧命令/Playbook | 新命令 | 缩写 |
|----------------|--------|------|
| `@execution/task_generation.md` | `@tc.md task` | `@tc.md exec t` |
| `@execution/story_sync.md` | `@tc.md sync` | `@tc.md exec sy` |
| `@execution/change_summary.md` | `@tc.md summary` | `@tc.md exec sum` |

### 初始化

| 旧命令/Playbook | 新命令 |
|----------------|--------|
| `@initialization/project_init.md` | `@tc.md init` |

---

## 🔄 迁移示例

### 示例 1：创建 Story

**旧方式**：
```bash
@planning/story_writing.md 创建用户登录功能
```

**新方式**：
```bash
# 一级快捷命令（推荐）
@tc.md story 创建用户登录功能

# 二级完整命令
@tc.md plan story 创建用户登录功能

# 缩写
@tc.md plan s 创建用户登录功能
```

### 示例 2：查看项目状态

**旧方式**：
```bash
@planning/project_status.md
```

**新方式**：
```bash
# 一级快捷命令（推荐）
@tc.md status

# 二级完整命令
@tc.md plan status

# 缩写
@tc.md plan st
```

### 示例 3：需求拆解

**旧方式**：
```bash
@planning/requirements_breakdown.md 拆解 requirements.md
```

**新方式**：
```bash
# 二级完整命令
@tc.md plan breakdown requirements.md

# 缩写（推荐）
@tc.md plan bd requirements.md
```

### 示例 4：添加 Context

**旧方式**：
```bash
@context/add.md 添加架构文档
```

**新方式**：
```bash
# 二级完整命令
@tc.md ctx add --type=architecture

# 缩写（推荐）
@tc.md ctx a --type=architecture
```

### 示例 5：生成 Task

**旧方式**：
```bash
@execution/task_generation.md STORY-01
```

**新方式**：
```bash
# 一级快捷命令（推荐）
@tc.md task STORY-01

# 二级完整命令
@tc.md exec task STORY-01

# 缩写
@tc.md exec t STORY-01
```

---

## 🌟 新功能优势

### 1. 更简洁

```bash
# 旧方式：需要记住完整路径
@planning/story_writing.md

# 新方式：简单命令
@tc.md story
```

### 2. 更灵活

```bash
# 可以使用完整命令
@tc.md plan story 用户登录

# 也可以使用缩写
@tc.md plan s 用户登录

# 还可以使用一级快捷
@tc.md story 用户登录
```

### 3. 更友好

```bash
# 内置帮助系统
@tc.md help
@tc.md help plan
@tc.md list

# 智能建议
@tc.md next
```

### 4. 更高效

```bash
# 批量操作
@tc.md plan bd requirements.md

# 快速查看
@tc.md status
@tc.md next
```

---

## 📚 学习资源

### 必读文档

1. **[快速开始指南](QUICK_START.md)** - 5 分钟上手
2. **[命令参考手册](COMMANDS.md)** - 完整命令列表
3. **[命令映射表](COMMAND_MAPPING.md)** - 命令与 Playbook 对照

### 推荐顺序

```
第一步：阅读 QUICK_START.md
   ↓
第二步：尝试基本命令（init, story, status, next）
   ↓
第三步：查看 COMMANDS.md 了解所有命令
   ↓
第四步：使用 COMMAND_MAPPING.md 作为参考
```

---

## ⚠️ 兼容性说明

### 完全兼容

旧的 Playbook 路径方式**仍然完全支持**：

```bash
# 这些仍然可以使用
@planning/story_writing.md
@execution/task_generation.md
@context/add.md
```

### 推荐迁移

虽然旧方式仍然可用，但**强烈推荐**使用新的 `@tc` 命令系统：

✅ 更简洁
✅ 更易记
✅ 更高效
✅ 更友好

---

## 🎓 快速上手

### 3 个必会命令

```bash
@tc.md help       # 查看帮助
@tc.md list       # 列出所有命令
@tc.md next       # 获取下一步建议
```

### 5 个常用命令

```bash
@tc.md init       # 初始化
@tc.md story      # 创建 Story
@tc.md status     # 查看状态
@tc.md task       # 生成 Task
@tc.md sync       # 同步状态
```

### 完整工作流

```bash
@tc.md init                          # 1. 初始化
@tc.md epic 用户系统                 # 2. 创建 Epic
@tc.md feature 用户认证              # 3. 创建 Feature
@tc.md story 登录功能                # 4. 创建 Story
@tc.md task STORY-01                 # 5. 生成 Task
# ... 开发过程 ...
@tc.md sync STORY-01                 # 6. 同步状态
@tc.md next                          # 7. 查看下一步
```

---

## 💡 小贴士

### 1. 使用缩写提高效率

```bash
# 不必每次都打完整命令
@tc.md plan bd    # 而不是 breakdown
@tc.md plan st    # 而不是 status
@tc.md ctx a      # 而不是 add
```

### 2. 优先使用一级快捷命令

```bash
# 对于常用命令，直接使用一级形式
@tc.md story      # 而不是 @tc.md plan story
@tc.md status     # 而不是 @tc.md plan status
@tc.md task       # 而不是 @tc.md exec task
```

### 3. 善用帮助系统

```bash
# 不确定时，查看帮助
@tc.md help
@tc.md help plan

# 查看所有命令
@tc.md list

# 获取建议
@tc.md next
```

---

## 🔗 相关链接

- [快速开始指南](QUICK_START.md)
- [命令参考手册](COMMANDS.md)
- [命令映射表](COMMAND_MAPPING.md)
- [README](README.md)

---

**开始使用新的 @tc.md 命令系统，享受更高效的开发体验！** 🚀

