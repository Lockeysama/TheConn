# Domain Knowledge: Frontend Engineering

<domain_strategy id="tech.frontend">
    <description>前端工程上下文的战略指导。</description>
    
    <!-- 1. 战略优先级 (Strategic Priorities) -->
    <priorities>
        <priority level="P0">**用户体验 (User Experience, UX)**: FCP, LCP 和交互响应性 (INP) 是至关重要的。</priority>
        <priority level="P1">**无障碍访问 (Accessibility, a11y)**: 强制要求 WCAG 2.1 AA 合规性。</priority>
        <priority level="P2">**可维护性 (Maintainability)**: 组件复用 > 复制粘贴。</priority>
    </priorities>

    <!-- 2. 技能修饰 (Skill Modifiers) -->
    <skill_modifiers>
        
        <!-- 修饰 "System Design" 技能 -->
        <modifier target_skill="tech/system_design">
            <instruction>关注状态管理策略 (客户端状态 vs 服务端状态)。</instruction>
            <instruction>优先考虑 **乐观 UI (Optimistic UI)** 更新以提升感知性能。</instruction>
            <instruction>为移动优先 (Mobile-First) 的响应式设计。</instruction>
        </modifier>

        <!-- 修饰 "Code Review" 技能 -->
        <modifier target_skill="tech/code_review">
            <instruction>检查 "Prop Drilling" (建议使用 Context 或 Composition)。</instruction>
            <instruction>验证图片优化 (尺寸, webp, 懒加载)。</instruction>
            <instruction>强制使用语义化 HTML (`button` vs `div`)。</instruction>
        </modifier>

        <!-- 修饰 "Critical Thinking" 技能 -->
        <modifier target_skill="core/critical_thinking">
            <instruction>用户同理心检查: "如果用户网络很慢会发生什么？"</instruction>
            <instruction>设备检查: "这会在小屏幕手机上崩溃吗？"</instruction>
        </modifier>

    </skill_modifiers>

    <!-- 3. 领域知识库 (Knowledge Base) -->
    <knowledge_base>
        <rule id="arch.atomic">将组件组织为 Atoms, Molecules, Organisms。</rule>
        <rule id="state.immutable">永远不要直接修改 State。</rule>
        <rule id="perf.lazy">强制使用基于路由的代码分割 (Code Splitting)。</rule>
    </knowledge_base>

</domain_strategy>
