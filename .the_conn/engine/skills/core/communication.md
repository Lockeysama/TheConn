# Skill: Communication (沟通澄清)

<skill_meta>
    <name>Communication (沟通澄清)</name>
    <type>Core-SoftSkill (核心软技能)</type>
    <description>通过结构化提问澄清需求，消除歧义。</description>
    <inputs>
        <arg name="context">原始输入或模糊的需求</arg>
        <arg name="goal">沟通的目标 (例如: 明确验收标准)</arg>
    </inputs>
    <outputs>
        <result name="clarified_requirements">结构化的需求清单</result>
        <result name="questions">待确认的问题列表</result>
    </outputs>
</skill_meta>

## 🧠 核心算法 (Algorithms)

### 1. The 5-W Check (5W 检查)
- **Who**: 谁是用户？谁是干系人？
- **What**: 核心价值是什么？
- **Why**: 为什么现在做？为什么重要？
- **Where**: 在哪些模块/页面体现？
- **When**: 什么时候需要交付？(Deadline)

### 2. Ambiguity Buster (歧义消除)
- **模糊词**: "快", "好", "大概", "可能"。
- **动作**: 要求量化 (Quantify)。例如，"快" -> "响应时间 < 200ms"。

### 3. Stakeholder Alignment (干系人对齐)
- 识别潜在的冲突需求 (例如: 安全性 vs 易用性)。
- 提出权衡方案 (Trade-offs)。

## 🔌 接口定义 (Signature)

```typescript
function Clarify(
  Context: string,
  Goal: string
): {
  summary: string;
  questions: string[];
  blockers: string[];
}
```
