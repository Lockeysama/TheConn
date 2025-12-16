# 下一步行动顾问 (Next Step Advisor)

## 用途

当用户不确定下一步应该规划什么 Story 或执行什么任务时，调用此 Playbook。AI 会分析当前项目状态，智能建议下一步行动。

## ⚠️ 重要：遵守基础公约

**本 Playbook 严格遵守 `@playbooks/core/base_rules.md` 中定义的所有基础公约。**

---

## 使用场景

用户可以随时询问：

- "我下一步该做什么？"
- "现在应该规划什么 Story？"
- "Feature 开发到什么程度了？"
- "是否需要补充测试？"

---

## AI 分析流程

### Step 1: 收集当前状态信息

**自动读取以下信息：**

1. **Epic/Feature 结构**
   - 当前活跃的 Epic 是哪个？
   - 该 Epic 下有哪些 Feature？
   - 每个 Feature 包含哪些 Story？

2. **Story 完成状态**
   - 统计各 Story 的 `status` 字段
   - 识别 `pending` 和 `done` 的数量
   - 检查是否有阻塞依赖（`depends_on`）

3. **测试覆盖情况**
   - 是否有 E2E 测试 Story？
   - 是否有集成测试 Story？
   - 各 Story 是否有 BDD 场景？

4. **最近的代码变更**
   - 最近修改了哪些文件？
   - 是否有新的技术债需要处理？

---

### Step 2: 智能分析与建议

根据不同场景，给出定制化建议。

---

## 场景分析与建议模板

### 场景 1: Feature 刚启动

**检测条件：**

- Feature 下只有 1-2 个 Story
- 所有 Story 状态都是 `pending`

**AI 输出：**

```markdown
📍 当前状态：Feature 刚启动

✅ 已完成：
- 创建 FEAT-01: {FeatureName}
- 规划了 2 个功能 Story (STORY-01, STORY-02)

🔍 分析：
- Story 都是用户可见功能 ✓
- 缺少 E2E 测试 Story ⚠️
- Feature 预计包含 3-5 个 Story

💡 建议下一步：
1. 继续规划剩余功能 Story（如果还有）
2. 添加 1 个 E2E 测试 Story：
   - 建议命名：STORY-99_E2E_{FeatureName}_Flow
   - 目的：验证 STORY-01 + STORY-02 的集成流程
3. 确认所有 Story 的依赖关系
4. 开始执行第一个 Story (STORY-01)

🎯 优先级：
高: 规划完整功能 Story
中: 添加测试 Story
低: 优化 Story 描述
```

---

### 场景 2: Feature 开发中

**检测条件：**

- 部分 Story 状态是 `done`
- 部分 Story 状态是 `pending`

**AI 输出：**

```markdown
📍 当前状态：Feature 开发进行中

✅ 已完成：
- STORY-01: {StoryName} ✓
- STORY-02: {StoryName} ✓

🚧 进行中/待开发：
- STORY-03: {StoryName} (pending)
- STORY-04: {StoryName} (pending)

📊 进度：50% (2/4 Story 完成)

🔍 分析：
- STORY-03 依赖 STORY-01 ✓ (依赖已满足)
- STORY-04 无依赖 ✓
- 检测到有 STORY-99 E2E 测试 Story ✓

💡 建议下一步：
1. 继续开发 STORY-03（依赖已满足，可以开始）
2. 并行开发 STORY-04（如果有资源）
3. 完成所有功能 Story 后，执行 STORY-99 E2E 测试

⚠️ 注意事项：
- STORY-03 和 STORY-04 完成后，再执行 E2E 测试
- 建议在 STORY-03 完成时做一次集成测试验证

🎯 里程碑：
当前阶段: 功能开发
下一阶段: E2E 验收测试（预计 2 个 Story 后）
```

---

### 场景 3: Feature 接近完成

**检测条件：**

- 大部分 Story 状态是 `done`
- 只剩 0-2 个 Story 未完成

**AI 输出：**

```markdown
📍 当前状态：Feature 即将完成

✅ 已完成：
- STORY-01: {StoryName} ✓
- STORY-02: {StoryName} ✓
- STORY-03: {StoryName} ✓
- STORY-04: {StoryName} ✓

🚧 待完成：
- STORY-99: E2E_{FeatureName}_Flow (pending)

📊 进度：80% (4/5 Story 完成)

🔍 分析：
- 所有功能 Story 已完成 ✓
- E2E 测试 Story 准备就绪 ✓
- 依赖关系全部满足 ✓

💡 建议下一步：
1. 立即执行 STORY-99 E2E 测试
2. 验证完整的功能流程
3. 检查是否有遗漏的边界场景
4. 准备 Feature 验收文档
5. 如果是 Epic 的最后一个 Feature，考虑 Epic 级别测试

🎉 即将完成：
完成 STORY-99 后，Feature 可以标记为完成！

🔄 后续计划：
- 如果 Epic 还有其他 Feature → 继续开发下一个 Feature
- 如果是 Epic 最后一个 Feature → 执行 Epic E2E 测试
```

---

### 场景 4: 检测到技术债

**检测条件：**

- Story 类型是 `dev`，但标题包含 "Refactor"
- 没有对应的测试计划

**AI 输出：**

```markdown
📍 当前状态：检测到技术债

⚠️ 检测到问题：
- STORY-03: Refactor_{ModuleName}
  - 类型：技术重构
  - 测试覆盖：❌ 无回归测试计划
  - 影响范围：可能影响现有功能

🔍 分析：
重构 Story 如果没有回归测试，可能引入 Bug 而不被发现。

💡 建议下一步：
1. 在 STORY-03 中补充单元测试覆盖
2. 考虑添加 STORY-03.1_Regression_Tests（如果影响用户功能）
3. 确保重构前后的 BDD 测试仍然通过

🛡️ 风险防控：
- 优先级：高
- 建议：先补充测试，再执行重构
- 验证方式：对比重构前后的测试结果
```

---

### 场景 5: Epic 级别统览

**检测条件：**

- Epic 下有多个 Feature
- 需要整体评估进度

**AI 输出：**

```markdown
📍 当前状态：Epic 整体进度

## EPIC-01: {EpicName}

### Feature 进度总览

| Feature | Story 总数 | 已完成 | 进度 | 状态     |
| ------- | ---------- | ------ | ---- | -------- |
| FEAT-01 | 5          | 5      | 100% | ✅ 完成   |
| FEAT-02 | 4          | 2      | 50%  | 🚧 开发中 |
| FEAT-03 | 3          | 0      | 0%   | ⏳ 未开始 |

### 整体进度
- 总 Story 数: 12
- 已完成: 7
- 进度: 58%

### 测试覆盖
- Feature E2E 测试: 2/3 (FEAT-03 缺失)
- Epic E2E 测试: ❌ 未规划

🔍 分析：
- FEAT-01 已完成，可以开始使用 ✓
- FEAT-02 开发进行顺利，预计 1 周完成
- FEAT-03 未开始，建议优先规划测试 Story
- 缺少 Epic 级别的端到端测试

💡 建议下一步：
1. 继续完成 FEAT-02 的剩余 Story
2. 为 FEAT-03 规划测试 Story（建议添加 STORY-99）
3. 规划 Epic 级别 E2E 测试：
   - STORY-999_Epic_E2E_User_Journey
   - 覆盖跨 Feature 的完整用户旅程
4. 设置 Epic 测试里程碑：
   - Week 5: 所有 Feature 完成
   - Week 6: Epic E2E 测试 + 验收

🎯 里程碑：
当前: Feature 开发阶段
下一步: FEAT-02 完成 → FEAT-03 开发
最终: Epic E2E 测试 → Epic 验收
```

---

### 场景 6: 缺少测试 Story（自动检测）

**检测条件：**

- Feature 包含 ≥3 个功能 Story
- 没有编号为 97-99 的测试 Story

**AI 输出：**

```markdown
📍 当前状态：检测到测试覆盖不足

⚠️ 问题：
- FEAT-02: {FeatureName}
  - 功能 Story 数: 4 个
  - E2E 测试 Story: ❌ 无
  - 集成复杂度: ⚠️ 高（涉及数据库 + API）

🔍 分析：
Feature 包含多个功能 Story 且有集成依赖，但缺少 E2E 测试。
建议补充测试 Story 以确保各模块协同工作正常。

💡 建议立即行动：
1. 添加 STORY-99_E2E_{FeatureName}_Flow
2. 规划以下测试场景：
   - Happy Path: 完整功能流程
   - Error Handling: 异常处理
   - Data Consistency: 数据一致性验证
3. 设置测试执行时机：所有功能 Story 完成后

⏰ 建议时机：
- 现在补充（最佳）：在功能开发进行中规划
- 最晚补充：所有功能 Story 完成前

🎯 影响：
- 如果现在规划：开发时可以参考 E2E 场景，避免返工
- 如果延后规划：可能在集成时发现问题，增加修复成本
```

---

## 调用示例

### 示例 1：用户询问

**用户：** "我下一步该做什么？"

**AI 行动：**

1. 读取 `.the_conn/epics/` 目录
2. 分析当前 Epic/Feature/Story 状态
3. 根据场景匹配合适的建议模板
4. 输出定制化的下一步建议

---

### 示例 2：特定 Feature 询问

**用户：** "FEAT-02 现在进展如何？下一步该做什么？"

**AI 行动：**

1. 定位到 FEAT-02 目录
2. 统计 Story 完成情况
3. 检查测试覆盖
4. 输出 Feature 专属的建议

---

## AI 分析检查清单

执行此 Playbook 时，AI 必须：

- [ ] 读取相关的 Epic/Feature/Story 文件
- [ ] 解析所有 Story 的 Frontmatter 状态
- [ ] 统计完成进度
- [ ] 检测测试覆盖情况
- [ ] 识别依赖关系和阻塞项
- [ ] 匹配合适的场景模板
- [ ] 输出可执行的具体建议
- [ ] 标注优先级和时间建议

---

## 输出格式要求

**必须包含：**

1. 📍 当前状态概述
2. ✅ 已完成项列表
3. 🚧 进行中/待办项
4. 🔍 智能分析
5. 💡 具体建议（可执行）
6. 🎯 优先级标注
7. ⚠️ 风险提示（如果有）

---

## 注意事项

1. **建议必须具体可执行**：不要只说"继续开发"，要说明"开发 STORY-03，因为依赖已满足"
2. **优先级明确**：高/中/低，帮助用户决策
3. **考虑依赖关系**：检查 `depends_on` 字段，避免建议有阻塞的 Story
4. **测试覆盖检查**：主动提醒缺失的测试 Story
5. **里程碑感知**：告诉用户当前处于什么阶段，距离完成还有多远

---

现在，请分析项目当前状态，给出下一步行动建议。
