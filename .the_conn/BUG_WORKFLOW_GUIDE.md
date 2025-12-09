# Bug Fix 工作流指南

本文档说明如何在已完成的 Story 发现 Bug 后，使用 Bug Fix Story 进行问题管理和修复。

---

## 工作流总览

```
Story 完成并合并
      ↓
集成/系统测试 或 生产环境
      ↓
  发现 Bug ❌
      ↓
┌─────────────────┐
│ 1. 问题分析     │
└────────┬────────┘
         ↓
┌─────────────────┐
│ 2. 创建 Bug Fix │ ← 使用 bug_story_template.md
│    Story        │
└────────┬────────┘
         ↓
┌─────────────────┐
│ 3. 执行修复     │ ← 标准四阶段工作流
└────────┬────────┘
         ↓
┌─────────────────┐
│ 4. 同步闭环     │ ← 更新 Story 状态为 done
└─────────────────┘
```

---

## 阶段 1: 问题分析

### 1.1 收集信息

在创建 Bug Fix Story 前，先收集以下信息：

- [ ] **父 Story ID**: 如 `DS-104`
- [ ] **Bug 现象**: 
  - 测试场景是什么？
  - 预期行为是什么？
  - 实际行为是什么？
- [ ] **发现阶段**: 集成测试 / 系统测试 / 生产环境
- [ ] **影响范围**: 对功能/用户/系统的影响
- [ ] **根因线索**: 怀疑是哪个文件/函数的问题？

---

## 阶段 2: 创建 Bug Fix Story

### 2.1 确定 ID

**命名规则**: `{PARENT-STORY-ID}.{序号}`

```
父 Story: DS-104
第一个 Bug: DS-104.1
第二个 Bug: DS-104.2
```

### 2.2 确定文件名

**命名规则**: `{ID}_{简短描述}.md`

```
DS-104.1_Concurrency_Fix.md
DS-104.2_Boundary_Check.md
```

### 2.3 使用模板生成

向 AI 提供 Bug 信息，使用 `bug_story_template.md` 生成 Bug Fix Story：

```
请使用 bug_story_template.md 模板，根据以下信息生成 Bug Fix Story：

父 Story: DS-104
发现于: 集成测试
现象:
  - 场景: 高并发情况下调用 xxx
  - 预期: 数据顺序正确
  - 实际: 数据顺序错乱
影响: 接收端可能乱序处理
```

### 2.4 保存文件

保存到对应的 `stories/` 目录：

```
epics/EPIC-01_xxx/
  └── features/FEAT-01_xxx/
      └── stories/
          ├── DS-104_Dynamic_Piggybacking.md
          └── DS-104.1_Concurrency_Fix.md  # ← 新创建
```

---

## 阶段 3: 执行修复

### 3.1 准备工作区

```bash
mkdir -p .the_conn/ai_workspace/DS-104.1/
```

### 3.2 生成任务简报

使用 `task_generation.md` 模板，从 Bug Fix Story 生成 `task.md`

### 3.3 准备上下文清单

创建 `context.manifest.json`：

```json
{
  "task_id": "DS-104.1",
  "description": "DS-104 并发问题修复",
  "files": [
    ".the_conn/context/10_MODULE_DESIGN.md",
    "epics/.../stories/DS-104_Dynamic_Piggybacking.md",
    "epics/.../stories/DS-104.1_Concurrency_Fix.md"
  ],
  "source_story": "epics/.../stories/DS-104.1_Concurrency_Fix.md"
}
```

**关键**: 同时包含父 Story 和 Bug Fix Story，让 AI 理解完整上下文。

### 3.4 执行标准工作流

1. **准备**: 工作区和上下文已准备
2. **实现**: AI 根据 Bug Fix Story 的 BDD 场景修复代码
3. **审查**: 人类领航员审查 PR
4. **合并**: 合并到主分支

---

## 阶段 4: 同步闭环

### 4.1 更新 Bug Fix Story 状态

PR 合并后，使用 `story_synchronization.md` 模板：

1. 获取 PR 的 git diff
2. 生成 `change_summary.md`
3. 更新 Bug Fix Story 状态为 `done`

### 4.2 验证回归测试

确保：
- Bug 修复场景通过
- 父 Story 的原有场景仍然通过

---

## 最佳实践

### ✅ 推荐做法

1. **及时创建 Bug Fix Story**: 发现问题立即创建，不要口头传达
2. **完整记录现象**: Bug 描述要足够详细，包含复现条件
3. **回归测试验证**: 修复 Bug 时必须回归原场景

### ❌ 避免做法

1. **不要静默修复**: 直接修复代码但不创建 Bug Fix Story
2. **不要跳过回归**: 修复 Bug 后必须验证原场景没有被破坏
3. **不要过度修改**: 只修复问题，不做无关的重构

---

## 常见问题

### Q1: 什么时候创建 Bug Fix Story，什么时候修改原 Story？

**创建 Bug Fix Story**:
- PR 已经合并
- 在集成/系统测试或生产环境发现

**修改原 Story**:
- PR 尚未合并，还在开发或审查阶段

### Q2: 一个 Story 发现多个 Bug 怎么办？

**独立问题 → 独立 Bug Fix Story**:
```
DS-104.1 - 并发问题
DS-104.2 - 边界检查
```

**同一根因 → 单个 Bug Fix Story**:
在同一个 Bug Fix Story 的 BDD 场景中添加多个场景。

---

## 相关模板

- **创建 Bug Fix Story**: `templates/bug_story_template.md`
- **创建普通 Story**: `templates/story_template.md`
- **生成任务简报**: `templates/task_generation.md`
- **同步 Story**: `templates/story_synchronization.md`
- **核心工作流**: `core/core.md`
