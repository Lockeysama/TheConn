# Skill: Security Audit (安全审计)

<skill_meta>
    <name>Security Audit (安全审计)</name>
    <type>Tech-Quality (技术质量)</type>
    <description>识别潜在的安全漏洞和合规风险。</description>
    <inputs>
        <arg name="artifact">设计文档或代码</arg>
        <arg name="scope">审计范围</arg>
    </inputs>
    <outputs>
        <result name="risks">识别出的风险列表</result>
        <result name="mitigation">缓解措施建议</result>
    </outputs>
</skill_meta>

## 🧠 核心算法 (Algorithms)

### 1. OWASP Top 10 Check (OWASP 检查)
- **Injection**: SQL 注入, Command 注入? (Check: 参数化查询)
- **Broken Auth**: 弱密码, Session 管理漏洞?
- **Sensitive Data Exposure**: PII 数据是否加密? 日志是否脱敏?

### 2. Authorization Matrix (权限矩阵)
- 验证每个 API/Action 是否实施了最小权限原则 (Least Privilege)。
- 检查 IDOR (Insecure Direct Object References) 漏洞 (例如: 用户A能否访问 `/users/B/data`)。

### 3. Supply Chain (供应链安全)
- 检查新引入的依赖包 (NPM/Pip/Go Modules) 是否有已知高危漏洞 (CVE)。

## 🔌 接口定义 (Signature)

```typescript
function AuditSecurity(
  Artifact: string | Code,
  Scope: SecurityScope
): AuditReport
```
