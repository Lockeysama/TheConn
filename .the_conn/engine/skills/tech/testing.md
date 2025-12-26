# Skill: Testing Strategy (测试策略)

<skill_meta>
    <name>Testing Strategy (测试策略)</name>
    <type>Tech-Methodology (技术方法论)</type>
    <description>定义全面的测试计划，包括单元测试、集成测试和 E2E 测试。</description>
    <inputs>
        <arg name="scope">变更范围</arg>
        <arg name="criticality">业务关键程度</arg>
    </inputs>
    <outputs>
        <result name="test_plan">测试计划文档</result>
    </outputs>
</skill_meta>

## 🧠 核心算法 (Algorithms)

### 1. Test Pyramid (测试金字塔)
- **Unit Tests (70%)**: 针对独立函数/类。Mock 所有外部依赖。速度快。
- **Integration Tests (20%)**: 针对数据库、API 交互。使用 TestContainers 或内存数据库。
- **E2E Tests (10%)**: 针对关键用户旅程 (Critical User Journey)。模拟真实浏览器/客户端。

### 2. TDD (测试驱动开发)
- **Rules**:
    1. 在编写实现代码前，先写一个失败的测试。
    2. 只编写刚好能通过测试的代码。
    3. 重构代码，并确保测试通过。

### 3. Regression Scope (回归范围)
- 根据依赖图谱 (Dependency Graph) 确定受影响的模块。
- 对核心路径 (Core Path) 执行强制回归。

## 🔌 接口定义 (Signature)

```typescript
function PlanTesting(
  Scope: string[],
  Criticality: "High" | "Medium" | "Low"
): TestPlan
```
