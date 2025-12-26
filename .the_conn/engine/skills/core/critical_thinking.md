# Skill: Critical Thinking (抽象元技能)

<skill_meta>
    <name>Critical Thinking (批判性思维)</name>
    <type>Meta-Methodology (元方法论)</type>
    <description>Applies structured thinking algorithms to identify risks, biases, and logical fallacies.</description>
    <inputs>
        <arg name="subject">The proposal, design, or requirement to analyze</arg>
        <arg name="domain_context">Active domain strategies and constraints (The Adverb)</arg>
    </inputs>
    <outputs>
        <result name="risk_assessment">Identified risks and their probabilities</result>
        <result name="logical_gaps">Missing links in reasoning</result>
    </outputs>
</skill_meta>

## 🧠 思维算法库 (Algorithms)

### 1. Inversion (逆向思维)
*   **算法**: `System.State = Failed` -> `Trace(Reason)`
*   **用途**: 预演失败结果，反推原因。
*   **输入**: 任意方案/设计/代码。
*   **示例**: "假设此系统在双十一崩溃，最可能的原因是什么？"

### 2. Second-Order Thinking (二阶思维)
*   **算法**: `Action` -> `Result` -> `Consequence(Result)`
*   **用途**: 不只看直接结果，看结果的结果（长期影响）。
*   **输入**: 决策建议。
*   **示例**: "引入 Redis 虽然加速了读取 (一阶)，但引入了数据一致性问题 (二阶)。"

### 3. Devil's Advocate (魔鬼代言人)
*   **算法**: `Assert(Fact)` -> `Search(!Fact)`
*   **用途**: 强行寻找反例，攻击现有论点。
*   **输入**: 核心假设。
*   **示例**: "假设用户一定喜欢这个功能，有没有可能用户反而觉得它烦人？"

### 4. 5-Whys (五问法)
*   **算法**: `Problem` -> `Why?` -> `Cause` -> `Why?` -> `Root Cause`
*   **用途**: 挖掘根本原因，而非表面症状。
*   **输入**: Bug 现象或问题描述。

## 🔌 接口定义 (Signature)

```typescript
function Think(
  Subject: any, 
  ThinkingModel: "Inversion" | "SecondOrder" | "DevilsAdvocate" | "5Whys", 
  DomainContext: StrategyContext
): ThinkingResult;
```
