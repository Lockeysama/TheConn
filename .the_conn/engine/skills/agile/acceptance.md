# Skill: Acceptance Criteria (验收标准编写)

<skill_meta>
    <name>Acceptance Criteria (验收标准编写)</name>
    <type>Agile-Methodology (敏捷方法论)</type>
    <description>生成可测试、明确的验收标准 (AC)。</description>
    <inputs>
        <arg name="story">用户故事</arg>
        <arg name="format">格式 (BDD | Checklist)</arg>
    </inputs>
    <outputs>
        <result name="ac_list">验收标准列表</result>
    </outputs>
</skill_meta>

## 🧠 核心算法 (Algorithms)

### 1. Gherkin Syntax (BDD)
- **Structure**: GIVEN (前置条件) -> WHEN (操作) -> THEN (预期结果)。
- **Rule**: 每个 Scenario 只能测试一条逻辑路径。

### 2. Negative Testing (反向测试)
- 不仅仅验证 "Happy Path"。
- 必须包含错误处理、边界条件、权限拒绝等场景。

### 3. Definition of Done (DoD)
- 将通用的 DoD (如: 代码覆盖率、无 Lint 错误) 隐式包含在所有 AC 中。

## 🔌 接口定义 (Signature)

```typescript
function WriteAC(
  Story: UserStory,
  Format: "BDD" | "Checklist"
): string
```
