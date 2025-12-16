# Epic 规划生成指南

根据需求文档生成 Epic 规划文件。

## ⚠️ 重要：遵守基础公约

**本 Playbook 严格遵守 `@playbooks/core/base_rules.md` 中定义的所有基础公约。**

## 本 Playbook 的工作范围

**专注于**：生成 Epic 规划文档（创建 Epic README.md 文件）

---

## 输出要求

### 1. 文件路径

```
.the_conn/epics/EPIC-{序号}_{PascalCaseName}/README.md
```

**示例**: `.the_conn/epics/EPIC-01_Base_Init/README.md`

### 2. Epic ID 规则

- **格式**: `EPIC-{序号}`
- **序号**: 全局唯一，两位数字，从 01 开始
- **示例**: `EPIC-01`, `EPIC-02`, `EPIC-10`

### 3. 目录命名规则

- **格式**: `EPIC-{序号}_{PascalCaseName}`
- **PascalCase**: 每个单词首字母大写，无分隔符
- **示例**: `EPIC-01_Base_Init`, `EPIC-02_DataStream`

---

## 输出格式

```markdown
# EPIC-{序号}: {Epic 名称}

- **业务价值**: {一句话说明核心价值}
- **范围**: {包含的功能模块}
- **关键指标**: {可衡量的成功指标}
- **创建日期**: {yyyy-mm-dd}
```

---

## 生成原则

1. **业务价值**: 清晰、可量化，从用户/业务视角描述
2. **范围边界**: 明确包含哪些功能模块，不包含哪些
3. **关键指标**: 必须可通过数据验证（如功能数量、性能指标、测试覆盖率）
4. **命名规范**: Epic 名称使用 PascalCase
5. **粒度控制**: 默认使用较粗的粒度，按大的业务领域划分，避免 Epic 过多过细
6. **测试战略**: 规划 Epic 级别的测试里程碑，确保整体质量保障

---

## 测试里程碑规划 (智能引导)

### 自动分析与建议

生成 Epic 时，AI 需要分析并建议测试里程碑：

**分析维度：**

1. **Epic 规模**: 预计包含多少个 Feature？
   - 1-2 个 Feature → 无需 Epic 级别 E2E 测试
   - 3+ 个 Feature → 建议 1 个 Epic E2E Story

2. **功能复杂度**: Feature 之间是否有集成依赖？
   - 无依赖 → Feature 级别测试即可
   - 有依赖 → 需要跨 Feature 的集成测试

3. **用户旅程**: 是否存在跨 Feature 的完整用户流程？
   - 是 → 必须规划端到端用户旅程测试
   - 否 → Feature 独立测试即可

**AI 输出格式：**

```markdown
## 测试里程碑规划

### Feature 级别测试
- FEAT-01: 预计 1 个 E2E Story（验证用户认证完整流程）
- FEAT-02: 预计 1 个集成测试 Story（验证数据同步）

### Epic 级别测试
- STORY-999_Epic_E2E_User_Journey
  - **描述**: 验证从用户注册到完成核心操作的完整旅程
  - **触发条件**: 所有 Feature 开发完成后
  - **覆盖场景**: 
    - 注册 → 登录 → 核心功能使用 → 数据持久化验证
    - 异常处理和错误恢复流程

### 测试执行时序
Week 1-2: FEAT-01 开发 + Feature 测试
Week 3-4: FEAT-02 开发 + Feature 测试
Week 5: Epic E2E 测试 + 整体验收

### 测试覆盖预估
- 单元测试: 所有 Story 包含
- Feature E2E: 2 个测试 Story
- Epic E2E: 1 个测试 Story
- 预计业务场景覆盖率: 85%
```

### 测试里程碑决策树

```
Epic 规模判断
    ↓
≤ 2 Features → 仅 Feature 级测试
≥ 3 Features → 继续判断
    ↓
Features 有集成依赖？
    ↓
是 → 必须规划 Epic E2E Story
否 → 继续判断
    ↓
存在完整用户旅程？
    ↓
是 → 必须规划 Epic E2E Story
否 → Feature 级测试即可
```

---

## 示例

```markdown
# EPIC-01: 基础初始化

- **业务价值**: 为用户提供标准化的项目结构，支撑后续 AI 辅助开发
- **范围**: 目录结构初始化、模板文件生成、CLI 工具
- **关键指标**: 目录结构创建成功率 100%，模板文件完整性 100%
- **创建日期**: 2025-12-11
```

---

现在，请根据用户提供的需求文档生成 Epic 规划。
