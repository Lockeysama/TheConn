# Skill: User Story Writing (用户故事编写)

<skill_meta>
    <name>User Story Writing (用户故事编写)</name>
    <type>Agile-Methodology (敏捷方法论)</type>
    <description>Generates standardized User Stories following INVEST principles.</description>
    <inputs>
        <arg name="requirements">Raw feature requirements</arg>
        <arg name="mode">Standard | Pro (Determines template complexity)</arg>
    </inputs>
    <outputs>
        <result name="story_file">Markdown file content</result>
    </outputs>
</skill_meta>

## 🧠 核心算法 (Algorithms)

### 1. INVEST 验证
- **I**ndependent (独立): 能否独立开发？
- **N**egotiable (可协商): 它是一个讨论的承诺吗？
- **V**aluable (有价值): 为用户提供价值吗？
- **E**stimable (可估算): 我们能估算它吗？
- **S**mall (小): 适合 Sprint 吗？(最大复杂度检查)
- **T**estable (可测试): 有验收标准吗？

### 2. Template Selection (模板选择)

#### Standard Template (CRUD / Simple)
```markdown
# Story: {Title}
## 1. User Story
As a <Role>, I want to <Feature>, so that <Benefit>.

## 2. Acceptance Criteria
- [ ] Scenario 1: ...
- [ ] Scenario 2: ...

## 3. Tech Notes
- API: GET /resource
```

#### Pro Template (Complex / Core Domain)
```markdown
# Story: {Title}
## 1. Background & Context
- **Business Goal**: ...
- **Related ADR**: `runtime/context/design_docs/...`

## 2. User Story
As a <Role>, I want to <Feature>, so that <Benefit>.

## 3. Acceptance Criteria (BDD)
- **GIVEN** ... **WHEN** ... **THEN** ...

## 4. Technical Specifications
- **Data Model**: ...
- **API Contract**: ...
- **Security**: ...
```

## 🔌 接口定义 (Signature)

```typescript
function WriteStory(
  Requirements: string,
  Mode: "Standard" | "Pro"
): MarkdownString;
```
