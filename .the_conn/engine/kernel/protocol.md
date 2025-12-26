# The Conn Kernel: Protocol (通信协议)

<kernel_protocol>
    <version>2.0.0</version>
    <description>
        定义 XML 标签架构，用于 Engine-Runtime 通信。
    </description>
</kernel_protocol>

## 1. System Role Definition (系统角色定义)
*   **用途**: 在 `personas/*.md` 中定义角色。
*   **Schema**:
    ```xml
    <system_role definition="expert_persona">
        <role_name>String (角色名称)</role_name>
        <mindset>List of principals (思维模式)</mindset>
        <behavior_guidelines>List of rules (行为准则)</behavior_guidelines>
    </system_role>
    ```

## 2. Skill Definition (技能定义)
*   **用途**: 在 `skills/*.md` 中定义可执行能力。
*   **Schema**:
    ```xml
    <skill_definition>
        <name>String (技能名)</name>
        <inputs>List of Args (输入参数)</inputs>
        <outputs>List of Artifacts (输出工件)</outputs>
    </skill_definition>
    ```

## 3. Component Injection (组件注入)
*   **用途**: 将技能绑定到角色 (Static) 或任务 (Dynamic)。

    **Static (在 Persona 文件中)**:
    ```xml
    <static_skills>
        <skill ref="path/to/skill" level="expert|master" />
    </static_skills>
    ```

    **Dynamic (在 Playbook 文件中)**:
    ```xml
    <dynamic_injection>
        <inject ref="path/to/skill" reason="Context requirement" />
    </dynamic_injection>
    ```

## 4. Domain Strategy (领域策略)
*   **用途**: 定义战略上下文 (The Adverb)。
*   **Schema**:
    ```xml
    <domain_strategy id="domain.id">
        <priorities>
            <priority level="P0">必须做的事 (Must Haves)</priority>
        </priorities>
        <skill_modifiers>
            <modifier target_skill="skill/id">
                <instruction>特定上下文的指令</instruction>
            </modifier>
        </skill_modifiers>
    </domain_strategy>
    ```

## 5. Execution Trace (执行跟踪)
*   **用途**: 记录 Runtime 的思考过程。
*   **Schema**:
    ```xml
    <execution_trace>
        <step id="1">
            <persona>Who is acting</persona>
            <skill>What skill used</skill>
            <input>Raw Input</input>
            <thought_process>Internal Monologue</thought_process>
            <output>Result</output>
        </step>
    </execution_trace>
    ```

## 5. Skills Protocol (技能协议) 🆕

### 5.1 Skill Definition (技能定义)
用于 `engine/skills/` 文件。
```xml
<skill_definition id="core/critical_thinking">
    <name>Critical Thinking</name>
    <type>Meta-Methodology</type>
    <description>Applies structured thinking algorithms to identify risks and logical fallacies.</description>
    <inputs>
        <arg name="subject">The proposal or artifact to analyze</arg>
        <arg name="domain_rules">Active domain strategies</arg>
    </inputs>
    <algorithms>
        <algo name="inversion">Reverse the problem to find failure modes.</algo>
    </algorithms>
</skill_definition>
```

### 5.2 Static Loadout (静态装备)
用于 `engine/personas/` 文件，定义角色自带的技能。

```xml
<static_skills>
    <skill ref="core/critical_thinking" level="master" />
    <skill ref="tech/system_design" level="expert" />
</static_skills>
```

### 5.3 Dynamic Injection (动态注入)
用于 `engine/playbooks/` 文件或用户指令，临时赋予角色技能。

```xml
<dynamic_injection>
    <inject ref="agile/user_story_writing" reason="Planning Phase" />
    <inject ref="tech/frontend/react_patterns" reason="Detected React Context" />
</dynamic_injection>
```
