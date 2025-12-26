# Domain Knowledge: Backend Engineering

<domain_strategy id="tech.backend">
    <description>后端工程上下文的战略指导。</description>
    
    <!-- 1. 战略优先级 (Strategic Priorities) -->
    <priorities>
        <priority level="P0">**数据完整性 (Data Integrity)**: 数据丢失或损坏是不可接受的。</priority>
        <priority level="P1">**安全性 (Security)**: 对 OWASP Top 10 漏洞零容忍。</priority>
        <priority level="P2">**可扩展性 (Scalability)**: 按 10 倍增长设计，按 2 倍增长部署。</priority>
    </priorities>

    <!-- 2. 技能修饰 (Skill Modifiers) -->
    <skill_modifiers>
        
        <!-- 修饰 "System Design" 技能 -->
        <modifier target_skill="tech/system_design">
            <instruction>设计 API 时，**严格**遵循 RESTful 资源导向模式。</instruction>
            <instruction>对于分布式系统，除非明确说明，否则优先考虑 **一致性 (Consistency)** 而非可用性 (CP)。</instruction>
            <instruction>强制要求：定义数据库 Schema 时必须包含足够的索引和外键。</instruction>
        </modifier>

        <!-- 修饰 "Critical Thinking" 技能 -->
        <modifier target_skill="core/critical_thinking">
            <instruction>逆向检查 (Inversion): "这个事务在什么情况下会导致数据库处于不一致状态？"</instruction>
            <instruction>安全检查 (Security): "我能在这里注入 SQL 或 XSS 吗？" (永远假设可以)</instruction>
        </modifier>
        
        <!-- 修饰 "Code Review" 技能 -->
        <modifier target_skill="tech/code_review">
            <instruction>验证分层架构 (Handler -> Service -> Repo)。</instruction>
            <instruction>检查 ORM 使用中的 N+1 查询问题。</instruction>
        </modifier>

    </skill_modifiers>

    <!-- 3. 领域知识库 (Knowledge Base) -->
    <knowledge_base>
        <rule id="api.versioning">始终对 API 进行版本控制 (例如: `/api/v1/users`)。</rule>
        <rule id="db.migration">Schema 变更必须通过迁移脚本管理。</rule>
        <rule id="testing">单元测试 (Service) > 集成测试 (Handler)</rule>
    </knowledge_base>

</domain_strategy>
