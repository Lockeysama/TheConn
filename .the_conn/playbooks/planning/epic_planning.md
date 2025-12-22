# Epic 规划生成指南

根据需求文档生成 Epic 规划文件。

## ⚠️ 重要：遵守基础公约

**本 Playbook 严格遵守 `@playbooks/core/base_rules.md` 中定义的所有基础公约。**

**📋 规范引用**：

本 Playbook 依赖以下规范文件（AI 必须先加载）：
- **基础公约**: `@playbooks/core/base_rules.md` - 禁止事项、文件路径约定、质量标准
- **测试策略**: `@playbooks/core/test_strategy_rules.md` - Story 类型判断、测试决策规则

## 本 Playbook 的工作范围

**专注于**：生成 Epic 规划文档（创建 Epic README.md 文件）

---

## 命名与格式规范

### ID 命名规则

- **格式**: `EPIC-{序号}`
- **序号**: 全局唯一，两位数字，从 01 开始
- **示例**: `EPIC-01`, `EPIC-02`, `EPIC-10`

### 目录命名规则

- **格式**: `EPIC-{序号}_{PascalCaseName}`
- **PascalCase**: 每个单词首字母大写，无分隔符
- **示例**: `EPIC-01_Base_Init`, `EPIC-02_DataStream`

### 文件路径

```
.the_conn/epics/EPIC-{序号}_{PascalCaseName}/README.md
```

**示例**: `.the_conn/epics/EPIC-01_Base_Init/README.md`

### Frontmatter 规范

```yaml
---
id: EPIC-01
status: pending
created: yyyy-mm-dd
depends_on: []
---
```

**字段说明**：

- `status`: `pending` (未完成) 或 `done` (已完成)
- `created`: 格式 `yyyy-mm-dd`
- `depends_on`: 依赖的其他 Epic ID 列表，无依赖写 `[]`

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

## 测试里程碑规划规则

**📋 详细的测试决策规则参考**: `@playbooks/planning/feature_planning.md` 的"自动生成测试 Story"部分

### Epic 级 E2E 测试决策规则（判断树）

```
开始判断
    ↓
是否有跨 Feature 的完整用户旅程？
    ├─ 是 → ✅ 必须 Epic E2E
    └─ 否 ↓
    
Feature 之间是否有强依赖（数据流/业务流）？
    ├─ 是 → ✅ 必须 Epic E2E
    └─ 否 ↓
    
Epic 包含 ≥3 个 Feature？
    ├─ 是 → 💡 建议 Epic E2E
    └─ 否 → ❌ 无需 Epic E2E（Feature 级测试足够）
```

**判断标准**：
- **完整用户旅程**：用户操作跨越多个 Feature（如注册→登录→使用功能）
- **强依赖**：一个 Feature 的输出是另一个 Feature 的输入
- **Feature 数量**：≥3 个时建议增加 Epic 级验证

### Epic 级性能测试决策规则（判断树）

```
开始判断
    ↓
是否有明确的性能 SLA 要求？
    ├─ 是 → ✅ 必须性能测试
    └─ 否 ↓
    
是否涉及高并发场景？
    ├─ 是 → 💡 建议性能测试
    └─ 否 ↓
    
是否有已知的性能瓶颈风险？
    ├─ 是 → 💡 建议性能测试
    └─ 否 → ❌ 无需性能测试（按需添加）
```

### 生成的 Epic 文档中的测试输出格式

**规则**：
1. ✅ 只列出需要的测试 Story 及简要理由
2. ✅ 按功能开发顺序排列
3. ❌ 不包含详细的决策原理说明
4. ❌ 不包含时间规划（Week 1-2 等）

**输出格式**：

```markdown
## 测试里程碑

### Feature 级别测试
各 Feature 根据其特征规划测试 Story（详见各 Feature 规划）

### Epic 级别测试（如果需要）

**STORY-999: Epic_E2E_{EpicName}**
- **类型**: E2E 测试 (type: e2e_test)
- **目的**: 验证跨 Feature 的完整用户旅程
- **理由**: Epic 包含 3 个以上 Feature，需要验证端到端集成
- **测试路径**: `tests/bdd/features/{module}/epic_{name}_flow.feature`
- **执行顺序**: 所有 Feature 完成后

**STORY-997: Performance_{EpicName}**（如果需要）
- **类型**: 性能测试 (type: perf_test)
- **目的**: 验证系统整体性能表现
- **理由**: 存在高并发场景，需要验证系统容量
- **执行顺序**: 所有 Feature 完成后
```

---

## 示例

### 示例 1: 不需要 Epic 级测试的 Epic

```markdown
# EPIC-01: 基础初始化

- **业务价值**: 为用户提供标准化的项目结构，支撑后续 AI 辅助开发
- **范围**: 目录结构初始化、模板文件生成、CLI 工具
- **关键指标**: 目录结构创建成功率 100%，模板文件完整性 100%
- **创建日期**: 2025-12-11

## Features 概览

- FEAT-01: 初始化项目结构
- FEAT-02: 生成模板文件

## 测试里程碑

### Feature 级别测试
各 Feature 根据其特征规划测试 Story（详见各 Feature 规划）

### Epic 级别测试
无需 Epic 级别测试（仅 2 个独立 Feature，无跨 Feature 依赖）
```

### 示例 2: 需要 Epic 级测试的 Epic

```markdown
# EPIC-02: 用户管理系统

- **业务价值**: 提供完整的用户生命周期管理能力
- **范围**: 用户注册、认证、权限、个人资料管理
- **关键指标**: 用户注册成功率 99.9%，认证响应时间 < 200ms
- **创建日期**: 2025-12-17

## Features 概览

- FEAT-01: 用户注册
- FEAT-02: 用户认证
- FEAT-03: 权限管理
- FEAT-04: 个人资料

## 测试里程碑

### Feature 级别测试
各 Feature 根据其特征规划测试 Story（详见各 Feature 规划）

### Epic 级别测试

**STORY-999: Epic_E2E_UserManagement**
- **类型**: E2E 测试 (type: e2e_test)
- **目的**: 验证从注册到使用完整用户旅程
- **理由**: Epic 包含 4 个强依赖的 Feature，需要验证端到端集成
- **测试路径**: `tests/bdd/features/user/epic_user_flow.feature`
- **执行顺序**: 所有 Feature 完成后

**STORY-997: Performance_UserAuth**
- **类型**: 性能测试 (type: perf_test)
- **目的**: 验证用户认证系统的性能表现
- **理由**: 认证是高频访问场景，需要验证并发容量
- **执行顺序**: FEAT-02 完成后
```

---

现在，请根据用户提供的需求文档生成 Epic 规划。
