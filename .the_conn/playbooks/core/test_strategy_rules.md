# 测试策略规范

本文档定义 The Conn 框架中的测试策略和 Story 类型判断规则。

---

## Story 类型与测试策略

| Story 类型     | 验收标准 | 测试策略     | Story Type     | 判断依据                          |
| -------------- | -------- | ------------ | -------------- | --------------------------------- |
| 用户功能 Story | 功能清单 | 单元测试     | `dev`          | 有用户界面交互或业务流程          |
| 技术实现 Story | 技术清单 | 单元测试     | `dev`          | 技术基础设施、工具、框架配置      |
| Bug 修复 Story | 测试清单 | 单元+回归    | `bug_fix`      | 修复已有功能的缺陷                |
| E2E Story      | BDD 场景 | BDD E2E 测试 | `e2e_test`     | Feature 级集成测试，验证完整流程  |
| Epic E2E Story | BDD 场景 | BDD E2E 测试 | `e2e_test`     | Epic 级集成测试，跨 Feature 流程  |
| 性能测试 Story | 性能指标 | 性能测试     | `perf_test`    | 有性能要求或性能瓶颈风险的功能点  |

---

## 测试金字塔与职责边界

### 测试层级结构

```
           E2E 测试（少量）
        ┌─────────────────┐
        │  Feature E2E    │  验证完整用户旅程
        │  Epic E2E       │  测试跨 Feature 集成
        └─────────────────┘
             /        \
       ┌──────────────────┐
       │  单元测试（大量）  │  验证函数/模块逻辑
       └──────────────────┘
```

### 测试层级职责

| 测试层级 | 职责范围                       | 执行速度 | 数量占比 | Story 类型      |
| -------- | ------------------------------ | -------- | -------- | --------------- |
| 单元测试 | 验证单个函数/类的逻辑正确性    | 快       | 70-80%   | 所有普通 Story  |
| E2E 测试 | 验证完整业务流程的端到端集成   | 慢       | 10-20%   | E2E Story       |
| 性能测试 | 验证系统在压力下的表现         | 很慢     | 5-10%    | 性能测试 Story  |

### 为什么 Story 级不使用 BDD？

**原因**：

1. **避免重复**：Story 级 BDD + Feature E2E 会测试相同的业务逻辑
2. **降低维护成本**：减少测试代码量，BDD 场景变更时只需修改一处（E2E Story）
3. **加快反馈速度**：单元测试执行更快，更适合 TDD 开发流程
4. **保持层次清晰**：单元测试验证实现细节，E2E 测试验证业务流程

**测试覆盖策略**：

- ✅ 每个普通 Story → 单元测试（快速验证逻辑）
- ✅ 每个 Feature → E2E Story（验证集成）
- ✅ 关键路径 → Epic E2E Story（验证跨功能流程）

---

## Story 类型判断标准

### 1. 普通 Story（单元测试）

包括用户功能 Story 和技术实现 Story，统一使用功能清单验收。

**特征**：

- ✅ 实现具体的功能模块或技术组件
- ✅ 可通过单元测试充分验证
- ✅ 使用功能清单作为验收标准

**示例**：

- 用户登录模块（包含表单验证、密码加密、错误处理）
- 订单处理逻辑（包含状态管理、数据校验）
- 缓存层实现（包含读写、过期策略）
- 日志框架配置（包含格式化、级别控制）

### 2. Bug 修复 Story（单元+回归测试）

**特征**：

- ✅ 修复已有功能的缺陷
- ✅ 需要回归测试验证
- ✅ 使用测试清单验证修复效果

**示例**：

- 修复登录失败时的错误提示
- 修复并发访问导致的数据不一致
- 修复边界条件处理错误

### 3. E2E Story（BDD 测试）

**特征**：

- ✅ 验证多个 Story 集成后的完整流程
- ✅ 从用户视角测试端到端业务场景
- ✅ 使用 BDD 场景描述用户旅程

**示例**：

- STORY-99: E2E_Auth_Flow（验证注册→登录→权限检查的完整流程）
- STORY-99: E2E_Order_Flow（验证下单→支付→发货的完整流程）
- STORY-999: Epic_E2E_User_Journey（验证跨 Feature 的完整用户旅程）

### 4. 性能测试 Story（性能测试）

**特征**：

- ✅ 验证系统在压力下的表现
- ✅ 明确的性能指标（响应时间、吞吐量、并发等）
- ✅ 使用性能指标作为验收标准

**示例**：

- STORY-97: Performance_DataSync（验证数据同步的性能表现）
- STORY-97: Performance_API（验证 API 接口的响应时间和吞吐量）
- STORY-997: Performance_System（验证整体系统的性能容量）

**性能测试场景**：

- 负载测试：正常负载下的性能表现
- 压力测试：超出正常负载的稳定性
- 容量测试：找到系统性能拐点
- 峰值测试：瞬时高峰的应对能力
- 稳定性测试：长时间运行的稳定性

---

## 测试文件组织规范

### 单元测试路径

**按编程语言习惯组织**：

| 语言       | 测试路径规则                     | 示例                                                         |
| ---------- | -------------------------------- | ------------------------------------------------------------ |
| Go         | 与源代码同目录，`*_test.go`      | `src/pkg/sender/buffer.go`<br>`src/pkg/sender/buffer_test.go` |
| Python     | 独立 `tests/` 目录，镜像源码结构 | `src/theconn/init.py`<br>`tests/test_init.py`               |
| JavaScript | 与源代码同目录或 `__tests__/`    | `src/utils.js`<br>`src/__tests__/utils.test.js`             |
| Java       | `src/test/java/` 镜像包结构      | `src/main/java/com/example/Service.java`<br>`src/test/java/com/example/ServiceTest.java` |

### BDD 测试路径

**统一按功能模块分组**（不跟 Epic 走）：

```
tests/bdd/features/{module}/
├── auth/
│   ├── login_flow.feature
│   └── register_flow.feature
├── payment/
│   ├── checkout_flow.feature
│   └── refund_flow.feature
└── user/
    └── profile_flow.feature
```

**Step Definitions 路径**（根据语言）：

- Go: `tests/bdd/*_test.go`
- Python: `tests/bdd/steps/*.py`
- JavaScript: `tests/bdd/steps/*.js`

**路径规则**：

- ✅ Feature 按业务模块（auth, payment, user）分组
- ✅ 一个 E2E Story 对应一个 .feature 文件
- ❌ 不要按 Epic 或 Feature ID 组织 BDD 目录

---

## Feature E2E 测试决策

**多维度评估模型**（需满足任意一条）：

| 维度       | 触发条件                     | 权重 |
| ---------- | ---------------------------- | ---- |
| 功能完整性 | Feature 包含完整的用户流程   | 高   |
| 集成复杂度 | 涉及 3+ 个模块/服务交互      | 高   |
| 任务复杂度 | Story 平均复杂度 ≥ 5.0       | 中   |
| 风险等级   | 核心业务功能、支付、安全相关 | 高   |
| 用户可见度 | 5+ 个用户功能 Story          | 中   |
| Story 数量 | Feature 包含 6+ 个 Story     | 低   |

**决策规则**：

- 高权重触发 1 条 → 建议 E2E 测试
- 中权重触发 2 条 → 建议 E2E 测试
- 低权重触发 + 其他 → 建议 E2E 测试

---

## 性能测试决策

**触发条件**（满足任意一条）：

- 预期有高并发场景
- 涉及大数据量处理
- 有明确的性能指标要求
- 存在已知的性能瓶颈风险
- 实时性要求严格

**测试时机**：Feature 功能开发完成后，单独规划性能测试 Story

**性能测试范围**：

- Feature 性能测试：STORY-97（单个 Feature 的性能）
- 系统性能测试：STORY-997（整体系统的性能）

**性能测试工具**：

- 负载生成：JMeter, Gatling, Locust, K6
- 监控分析：Prometheus, Grafana, New Relic
- APM 工具：Jaeger, Zipkin

**生成方式**：使用 `@playbooks/planning/performance_test_story.md` 生成

---

## Bug Fix Story 说明

**使用场景**：

- 已完成的 Story 发现缺陷
- 生产环境发现问题
- 测试覆盖不足导致的遗漏

**测试策略**：

- 修复验证测试：先写测试复现 Bug，修复后测试通过
- 回归测试：确保修复不破坏现有功能
- 边界测试：测试相似场景是否也存在问题

**ID 规则**：

- 格式：`STORY-{父序号}.{子序号}`
- 示例：STORY-01.1, STORY-01.2

**生成方式**：使用 `@playbooks/planning/bug_fix_story.md` 生成

---

**最后更新**: 2025-12-16
