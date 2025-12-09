# AI Prompts 模板库

本目录包含所有 AI 协作开发的 Prompt 模板，用于生成和管理项目的规划文档、任务执行和同步闭环。

---

## 📚 模板分类

### 🎯 规划层模板（Planning Templates）

用于创建和管理 Epic、Feature、Story 的规划文档。

| 模板文件                                         | 用途                  | 使用场景                          |
| ------------------------------------------------ | --------------------- | --------------------------------- |
| [epic_template.md](./epic_template.md)           | 生成 Epic 规划文档    | 定义高层次的业务目标和战略方向    |
| [feature_template.md](./feature_template.md)     | 生成 Feature 规划文档 | 将 Epic 分解为可交付的功能模块    |
| [story_template.md](./story_template.md)         | 生成 AI-Story 文件    | 定义具体的可开发任务和验收标准    |
| [bug_story_template.md](./bug_story_template.md) | 生成 Bug-Story 文件   | 管理已完成 Story 发现的缺陷和修复 |

### 🔧 执行层模板（Execution Templates）

用于 AI 任务执行和上下文管理。

| 模板文件                                         | 用途                  | 使用场景                     |
| ------------------------------------------------ | --------------------- | ---------------------------- |
| [task_generation.md](./task_generation.md)       | 从 Story 生成任务简报 | 为 AI 准备执行任务的核心材料 |
| [context_generation.md](./context_generation.md) | 生成上下文清单        | 为任务选择相关的上下文文档   |

### 🔄 同步层模板（Synchronization Templates）

用于实现与意图的双向同步。

| 模板文件                                               | 用途                  | 使用场景                   |
| ------------------------------------------------------ | --------------------- | -------------------------- |
| [story_synchronization.md](./story_synchronization.md) | 同步 Story 与代码变更 | PR 合并后，更新 Story 文档 |
| [change_summary.md](./change_summary.md)               | 生成代码变更摘要      | 记录每个 Story 的实现细节  |

### 📖 指南文档（Workflow Guides）

| 文档文件                                         | 内容                 | 适用对象   |
| ------------------------------------------------ | -------------------- | ---------- |
| [BUG_WORKFLOW_GUIDE.md](./BUG_WORKFLOW_GUIDE.md) | Bug-Story 完整工作流 | 人类领航员 |
| [../core/core.md](../core/core.md)               | AI 领航员敏捷工作流  | 人类领航员 |

---

## 🔄 工作流程图

### 标准 Story 开发流程

```
1. 规划阶段
   ├── epic_template.md → 创建 Epic
   ├── feature_template.md → 创建 Feature
   └── story_template.md → 创建 Story
                ↓
2. 准备阶段
   ├── context_generation.md → 生成上下文清单
   └── task_generation.md → 生成任务简报
                ↓
3. 执行阶段
   └── AI 根据任务简报实现功能
                ↓
4. 同步阶段
   ├── change_summary.md → 生成变更摘要
   └── story_synchronization.md → 同步 Story
```

### Bug-Story 管理流程

```
Story 完成并合并
        ↓
   发现 BUG ❌
        ↓
1. 创建 Bug-Story
   └── bug_story_template.md
        ↓
2. 更新父 Story
   └── story_template.md (章节 7: 后续问题追踪)
        ↓
3. 执行修复
   └── 使用标准工作流
        ↓
4. 同步更新
   ├── 更新 Bug-Story 状态
   └── 更新父 Story 追踪表
```

---

## 📝 快速使用指南

### 创建新 Story

```bash
# 1. 向 AI 提供需求
"我需要创建一个 Story: 实现用户登录功能"

# 2. 使用模板
"请使用 story_template.md 模板生成 AI-Story"

# 3. AI 返回完整的 Story 内容
# 4. 保存到对应的 stories/ 目录
```

### 创建 Bug-Story

```bash
# 1. 收集 BUG 信息
- 父 Story ID: DS-104
- BUG 现象: 并发场景下数组顺序错乱
- 发现阶段: 集成测试
- 严重程度: high

# 2. 使用模板
"请使用 bug_story_template.md 模板，根据以下信息生成 Bug-Story：
父 Story: DS-104
BUG 描述: ...
"

# 3. AI 返回完整的 Bug-Story 内容
# 4. 保存为 DS-104.1_xxx.md
# 5. 更新父 Story 的"后续问题追踪"章节
```

### 执行任务

```bash
# 1. 创建 workspace
mkdir -p .the_conn/ai_workspace/DS-104/

# 2. 生成任务简报
"请使用 task_generation.md 模板，从 DS-104 Story 生成任务简报"

# 3. 准备上下文清单
"请使用 context_generation.md 模板，为 DS-104 选择相关上下文"

# 4. 执行任务
"请根据任务简报和上下文实现功能"
```

### 同步 Story

```bash
# 1. PR 合并后，获取变更
git diff <commit-range> > /tmp/changes.diff

# 2. 生成变更摘要
"请使用 change_summary.md 模板，总结此次变更"

# 3. 同步 Story
"请使用 story_synchronization.md 模板，更新 DS-104 Story"
```

---

## 🎯 模板使用原则

### 1. **模板即规范**
- 所有生成的文档必须符合模板格式
- 不要随意偏离模板结构
- 模板的每个章节都有明确目的

### 2. **上下文精准投喂**
- 使用 context_generation.md 为每个任务选择相关上下文
- 避免提供过多无关信息
- 上下文清单应该是动态的、任务特定的

### 3. **保持同步**
- 代码变更后必须同步 Story
- Bug 修复后必须更新父 Story 的追踪表
- 文档与代码始终保持一致

### 4. **追溯性**
- 通过 Bug-Story 建立问题追溯链
- 通过 depends_on 字段建立依赖关系
- 通过 parent_story 字段建立父子关系

---

## 📊 模板版本管理

| 模板                     | 版本 | 最后更新   | 变更说明               |
| ------------------------ | ---- | ---------- | ---------------------- |
| story_template.md        | v2.0 | 2025-12-09 | 增加"后续问题追踪"章节 |
| bug_story_template.md    | v1.0 | 2025-12-09 | 新增 Bug-Story 模板    |
| BUG_WORKFLOW_GUIDE.md    | v1.0 | 2025-12-09 | 新增工作流指南         |
| epic_template.md         | v1.0 | -          | 初始版本               |
| feature_template.md      | v1.0 | -          | 初始版本               |
| task_generation.md       | v1.0 | -          | 初始版本               |
| context_generation.md    | v1.0 | -          | 初始版本               |
| story_synchronization.md | v1.0 | -          | 初始版本               |
| change_summary.md        | v1.0 | -          | 初始版本               |

---

## 🔗 相关资源

- **核心工作流文档**: [../core/core.md](../core/core.md)
- **项目上下文库**: `../../context/`
- **AI 工作区**: `../../ai_workspace/`
- **规划文档库**: `../../../epics/`

---

## 🆘 需要帮助？

如果您不确定应该使用哪个模板，请参考：

1. **创建新功能**: story_template.md
2. **修复已知 BUG**: bug_story_template.md
3. **不知道从哪里开始**: 阅读 [BUG_WORKFLOW_GUIDE.md](./BUG_WORKFLOW_GUIDE.md) 和 [core.md](../core/core.md)

---

**维护者**: @navigator-lead  
**最后更新**: 2025-12-09

