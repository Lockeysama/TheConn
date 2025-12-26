# Skill: System Design (系统设计)

<skill_meta>
    <name>System Design (系统设计)</name>
    <type>Tech-Methodology (技术方法论)</type>
    <description>Creates technical architecture diagrams and specifications for features.</description>
    <inputs>
        <arg name="requirements">Clarified requirements from Product Manager</arg>
        <arg name="domain_strategy">Strategic constraints (The Adverb)</arg>
    </inputs>
    <outputs>
        <result name="design_doc">Markdown or Mermaid content</result>
    </outputs>
</skill_meta>

## 🧠 设计维度 (Design Dimensions)

### 1. CAP Theorem Analysis (CAP 定理分析)
- **Consistency (一致性)**: 所有节点是否看到相同的数据？
- **Availability (可用性)**: 每个请求是否都能得到响应？
- **Partition Tolerance (分区容错性)**: 网络分区时系统能否继续运行？
- **Decision**: 选择 CP (金融/支付) 或 AP (社交 feed/点赞)。

### 2. Failure Mode Analysis (故障模式分析)
- **Single Point of Failure (单点故障)**: 识别并消除。
- **Circuit Breaking (熔断)**: 当依赖项变慢时如何处理？
- **Retry Strategy (重试策略)**: 幂等性是重试的前提。

### 3. Data Modeling (数据建模)
- **Access Patterns (访问模式)**: 读重还是写重？
- **Schema Design (Schema 设计)**: 规范化 (SQL) vs 反规范化 (NoSQL)。

### 4. Security & Compliance
*   **Checklist**: AuthN/AuthZ, Data Encryption, PII protection.

## 🔌 接口定义 (Signature)

```typescript
function DesignSystem(
  Requirements: RequirementSpec,
  DomainContext: StrategyContext
): DesignResult;
```
