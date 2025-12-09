# Bug-Story 工作流指南

本文档说明如何在已完成的 Story 发现 BUG 后，使用 Bug-Story 模板进行问题管理和修复。

---

## 📋 工作流总览

```
Story 完成并合并
      ↓
集成/系统测试
      ↓
  发现 BUG ❌
      ↓
┌─────────────────┐
│ 1. 问题分析判断 │
└────────┬────────┘
         ↓
┌─────────────────┐
│ 2. 创建Bug-Story│ ← 使用 bug_story_template.md
└────────┬────────┘
         ↓
┌─────────────────┐
│ 3. 更新父Story  │ ← 在"7. 后续问题追踪"章节添加记录
└────────┬────────┘
         ↓
┌─────────────────┐
│ 4. 执行修复任务 │ ← 走标准的4阶段工作流
└────────┬────────┘
         ↓
┌─────────────────┐
│ 5. 同步闭环更新 │ ← 更新 Bug-Story 和父 Story
└─────────────────┘
```

---

## 🔍 阶段 1: 问题分析判断

### 1.1 确定 BUG 类型

| 类型         | 特征                    | 处理方式                                                  |
| ------------ | ----------------------- | --------------------------------------------------------- |
| **严重回归** | 原有场景失败            | 立即创建 Bug-Story，优先级 high                           |
| **边缘遗漏** | 原场景通过，新场景失败  | 创建 Bug-Story，优先级 medium                             |
| **集成冲突** | 单 Story 正常，集成失败 | 创建 Bug-Story，分析依赖关系                              |
| **生产问题** | 生产环境发现            | 立即创建 Bug-Story，优先级 high，标记 trigger: production |

### 1.2 收集信息清单

在创建 Bug-Story 前，先收集以下信息：

- [ ] **父 Story ID**: 如 DS-104
- [ ] **BUG 现象**: 
  - 测试场景是什么？
  - 预期行为是什么？
  - 实际行为是什么？
- [ ] **复现步骤**: 如何稳定复现？
- [ ] **影响范围**:
  - 原有场景是否还能通过？
  - 是否影响下游 Story？
  - 是否阻塞 Release？
- [ ] **根因线索**: 
  - 怀疑是哪个文件/函数的问题？
  - 是代码错误还是设计遗漏？

---

## 📝 阶段 2: 创建 Bug-Story

### 2.1 确定 Bug-Story ID

**命名规则**: `{PARENT-STORY-ID}.{序号}`

**示例**:
```
父 Story: DS-104
第一个 Bug: DS-104.1
第二个 Bug: DS-104.2
```

### 2.2 确定文件名

**命名规则**: `{Bug-Story-ID}_{简短描述}.md`

**示例**:
```
DS-104.1_Piggybacking_Bug_Fix.md
DS-104.2_Concurrency_Issue.md
PAY-124.1_Timeout_Handling.md
```

### 2.3 使用模板生成

**方式一: 使用 AI 生成**

```bash
# 准备输入信息
cat > /tmp/bug_info.txt <<EOF
父 Story: DS-104
BUG 描述:
  - 测试场景: 在高并发情况下，历史捎带数组顺序错乱
  - 预期: 新事件在前，历史事件按 ID 降序排列
  - 实际: 顺序随机
  - 影响: 接收端可能乱序处理事件
发现阶段: 集成测试
严重程度: high
原场景状态: 原有 6 个场景通过，这是新发现的并发场景
EOF

# 使用 AI 生成 Bug-Story
# 向 AI 发送: "使用 bug_story_template.md 模板，根据以下信息生成 Bug-Story"
# 然后粘贴 bug_info.txt 的内容
```

**方式二: 手动填写**

直接复制 `bug_story_template.md` 的输出格式部分，逐节填写。

### 2.4 保存文件

```bash
# 保存到对应的 stories 目录
epics/EPIC-01_DataStream_Reliable_Signaling/
  └── features/
      └── FEAT-01_Unified_Protocol_And_Sender/
          └── stories/
              ├── DS-104_Dynamic_Piggybacking.md
              └── DS-104.1_Piggybacking_Bug_Fix.md  # ← 新创建
```

---

## 🔄 阶段 3: 更新父 Story

在父 Story 文件末尾的 **"7. 后续问题追踪"** 章节添加记录。

### 3.1 打开父 Story 文件

```bash
# 示例
vim epics/EPIC-01.../stories/DS-104_Dynamic_Piggybacking.md
```

### 3.2 定位到末尾

如果文件末尾没有 **"7. 后续问题追踪"** 章节，则添加：

```markdown
---

## 7. 后续问题追踪

> **注意**: 此章节记录在 Story 完成后，集成/系统测试或生产环境发现的问题。

### 7.1 发现的问题列表

| Bug Story | 问题简述 | 发现阶段 | 严重程度 | 状态 | 修复日期 |
| --------- | -------- | -------- | -------- | ---- | -------- |
|           |          |          |          |      |          |

### 7.2 回归测试记录

- ✅ 原有 6 个 BDD 场景验证通过（验证于: 2025-12-09）

### 7.3 经验总结

（待补充）
```

### 3.3 添加 Bug-Story 记录

在表格中添加一行：

```markdown
| [DS-104.1](./DS-104.1_Piggybacking_Bug_Fix.md) | 并发场景下捎带数组顺序错乱 | integration_test | high | ready_for_dev | - |
```

### 3.4 更新回归测试记录

```markdown
### 7.2 回归测试记录

- ✅ 原有 6 个 BDD 场景仍然通过（验证于: 2025-12-09）
- ⚠️ 发现边缘情况: 高并发下数组顺序问题，已通过 [DS-104.1](./DS-104.1_Piggybacking_Bug_Fix.md) 修复
```

---

## 🔧 阶段 4: 执行修复任务

### 4.1 准备 AI Workspace

```bash
# 为 Bug-Story 创建工作区
mkdir -p .the_conn/ai_workspace/DS-104.1/
```

### 4.2 生成任务简报

使用 `task_generation.md` 模板，从 Bug-Story 生成 `task.md`

### 4.3 准备上下文清单

创建 `context.manifest.json`：

```json
{
  "description": "Context for DS-104.1 bug fix",
  "files": [
    ".the_conn/context/10_DATASTREAM_DESIGN.md",
    "epics/EPIC-01.../stories/DS-104_Dynamic_Piggybacking.md",
    "epics/EPIC-01.../stories/DS-104.1_Piggybacking_Bug_Fix.md"
  ]
}
```

**关键**: 同时包含父 Story 和 Bug-Story，让 AI 理解完整上下文。

### 4.4 执行标准四阶段工作流

1. **规划**: Bug-Story 已完成
2. **准备**: Workspace 和上下文已准备
3. **实现**: AI 根据 Bug-Story 的 BDD 场景修复代码
4. **同步**: 修复完成后更新 Bug-Story

---

## ✅ 阶段 5: 同步闭环更新

### 5.1 Bug-Story 同步

PR 合并后，使用 `story_synchronization.md` 模板：

1. 获取 PR 的 git diff
2. 生成 `change_summary.md`
3. 更新 Bug-Story 的技术实现细节
4. 更新状态为 `done`

### 5.2 父 Story 同步更新

更新父 Story 的 **"7. 后续问题追踪"** 章节：

**更新问题列表状态**:
```markdown
| [DS-104.1](./DS-104.1_Piggybacking_Bug_Fix.md) | 并发场景下捎带数组顺序错乱 | integration_test | high | done | 2025-12-10 |
```

**补充经验总结**:
```markdown
### 7.3 经验总结

- **测试盲区**: 原 BDD 场景缺少并发压力测试，未来应增加多线程场景
- **设计改进**: 在 Piggybacker 中增加线程安全的排序逻辑
- **流程优化**: 建议在 Story 完成前增加并发集成测试环节
```

### 5.3 Feature README 更新

在 Feature 的 README.md 中标记：

```markdown
- **包含的故事**: 
  - `DS-104 (动态历史捎带机制)` ✅
    - `DS-104.1 (并发场景 Bug 修复)` ✅
```

---

## 📊 质量度量

### 跟踪指标

通过后续问题追踪，可以统计：

1. **首次质量通过率**: 
   ```
   无 Bug-Story 的 Story 数量 / 总 Story 数量
   ```

2. **Bug 发现阶段分布**:
   - 集成测试: X%
   - 系统测试: Y%
   - 生产环境: Z%

3. **Bug 严重程度分布**:
   - High: 导致原场景失败或阻塞
   - Medium: 边缘情况遗漏
   - Low: 优化改进

4. **平均修复时间**:
   从 Bug-Story 创建到状态变为 done 的时间

### 改进循环

定期（如每个 Sprint 结束）回顾：

1. **测试盲区模式**: 哪些类型的场景容易遗漏？
2. **设计缺陷模式**: 哪些设计决策容易导致问题？
3. **流程优化**: 如何在更早阶段发现问题？

---

## 🎯 最佳实践

### ✅ 推荐做法

1. **及时创建 Bug-Story**: 发现问题立即创建，不要口头传达
2. **完整记录上下文**: BUG 描述要足够详细，包含复现步骤
3. **建立追溯链接**: 始终在父 Story 中维护后续问题追踪表
4. **回归测试验证**: 修复 Bug 时必须回归原场景
5. **经验总结**: 每个 Bug 都要写经验总结，供团队学习

### ❌ 避免做法

1. **不要静默修复**: 直接修复代码但不创建 Bug-Story（追溯性丢失）
2. **不要合并文件**: 不要把 Bug-Story 合并回父 Story（历史混乱）
3. **不要跳过同步**: Bug 修复后必须更新父 Story 的追踪表
4. **不要过度拆分**: 同一根因的多个现象应该在一个 Bug-Story 中修复
5. **不要忽略回归**: 修复 Bug 时必须验证原场景没有被破坏

---

## 📚 相关模板文件

- **创建 Bug-Story**: `.the_conn/ai_prompts/templates/bug_story_template.md`
- **创建普通 Story**: `.the_conn/ai_prompts/templates/story_template.md`
- **同步 Story**: `.the_conn/ai_prompts/templates/story_synchronization.md`
- **生成任务简报**: `.the_conn/ai_prompts/templates/task_generation.md`
- **核心工作流**: `.the_conn/ai_prompts/core/core.md`

---

## 🆘 常见问题

### Q1: 什么时候创建 Bug-Story，什么时候直接修改原 Story？

**创建 Bug-Story**:
- PR 已经合并
- 在集成/系统测试或生产环境发现
- 问题独立，有明确的修复范围

**修改原 Story**:
- PR 尚未合并，还在开发或审查阶段
- 问题是原验收标准的直接体现（不是新场景）

### Q2: 一个 Story 发现多个 Bug 怎么办？

**独立问题 → 独立 Bug-Story**:
```
DS-104.1 - 并发问题
DS-104.2 - 内存泄漏
DS-104.3 - 边界条件
```

**同一根因 → 单个 Bug-Story**:
在 DS-104.1 的 BDD 场景中添加多个 "场景"。

### Q3: Bug-Story 是否计入 Story Points？

**建议**: 是的，Bug-Story 也应该估算 SP，因为：
- 需要分析、修复、测试的时间
- 有独立的验收标准
- 需要代码审查和合并

### Q4: Bug-Story 状态如何管理？

与普通 Story 一样：
- `ready_for_dev` → `in_progress` → `in_review` → `done`

在父 Story 的追踪表中同步更新状态。

---

**版本**: v1.0  
**最后更新**: 2025-12-09  
**维护者**: @navigator-lead

