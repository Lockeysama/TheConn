# The Conn: Naming Philosophy & Mission

[中文版](README.zh.md) | [CLI Documentation](CLI.md) | [Development Guide](DEVELOPMENT.md)

## 🚀 Quick Start

Integrate The Conn framework into your project with one command:

**Python users:**

```bash
uvx theconn init
```

**Node.js users:**

```bash
npx theconn-cli init
```

Then read `.the_conn/GUIDE.md` for detailed usage instructions.

## 🎯 How to Use The Conn

### Directory Structure

After initialization, The Conn creates a `.the_conn/` directory in your project:

```text
.the_conn/
├── epics/              # 📋 Planning Layer - Your project roadmap
│   └── EPIC-01_Feature_Name/
│       ├── README.md
│       └── features/
│           └── FEAT-01_Sub_Feature/
│               ├── README.md
│               └── stories/
│                   └── STORY-01_Task_Description.md
│
├── context/            # 📚 Knowledge Layer - Architecture & decisions
│   ├── global/         # Project-wide context
│   │   ├── Architecture.md
│   │   ├── Tech_Stack.md
│   │   └── Coding_Standard.md
│   └── epics/          # Epic-specific context
│       └── EPIC-01/
│           └── Module_Design.md
│
├── ai_prompts/         # 🤖 Tool Layer - AI prompt templates
│   ├── core/
│   ├── prompts/
│   │   ├── initialization/
│   │   ├── planning/
│   │   ├── context/
│   │   └── execution/
│   └── README.md
│
├── ai_workspace/       # 🔧 Execution Layer - Temporary work area
│   └── EPIC-01/
│       └── TASK-01_STORY-01_Name/
│           ├── task.md
│           └── context.manifest.json
│
├── GUIDE.md            # Complete usage guide
└── README.md           # Framework documentation
```

### Complete Workflow (5 Stages)

#### Stage 0: Project Initialization

First-time setup to create structure and foundational context.

```bash
# After running `uvx theconn init` or `npx theconn-cli init`:
# Use AI to initialize the project structure
@prompts/initialization/project_init.md Help me initialize The Conn project
```

This creates:

- Directory structure
- Initial global context (Architecture, Tech Stack, Coding Standards)
- Project conventions

#### Stage 1: From Requirements to Planning

Convert external requirements into actionable development tasks.

##### Step 1: Requirements Review

```bash
@{requirements_doc} @prompts/planning/requirements_review.md Start review
```

- Discuss requirements with AI
- Define technical approach
- Output: Technical solution document

##### Step 2: Extract Context

```bash
@{technical_solution} @prompts/context/extract.md Extract context
```

- Extracts reusable knowledge to `.the_conn/context/global/`
- Creates architecture decisions, patterns, conventions

##### Step 3: Generate Planning (Choose A or B)

###### Option A: Batch Generation (Recommended)

```bash
@{requirements} @{technical_solution} @prompts/planning/requirements_breakdown.md Start breakdown
```

- AI shows outline → You approve → AI generates all Epic/Feature/Story files

###### Option B: Step-by-Step Generation

```bash
# Generate Epic
@{requirements} @prompts/planning/epic_planning.md Generate Epic

# Generate Features
@{requirements} @prompts/planning/feature_planning.md Generate Features

# Generate Stories
@{requirements} @prompts/planning/story_writing.md Generate Stories
```

##### Step 4: Extract Epic-Specific Context

```bash
@.the_conn/epics/EPIC-XX_Name/README.md @prompts/context/extract.md Extract Epic context
```

- Outputs to `.the_conn/context/epics/EPIC-XX/`
- Includes module design, data models, API specs

#### Stage 2: From Story to Task

Prepare execution materials for AI.

```bash
@{Story_file} @prompts/execution/task_generation.md Generate Task
```

Creates in `.the_conn/ai_workspace/EPIC-XX/TASK-XX_STORY-XX_Name/`:

1. `task.md` - Task brief (emphasizes BDD/TDD test-first approach)
2. `context.manifest.json` - Context manifest for this task

#### Stage 3: Execute Development Task

AI-assisted coding with human oversight.

```bash
# Start the task
@.the_conn/ai_workspace/EPIC-XX/TASK-XX_STORY-XX_Name/ Start task
```

AI follows BDD/TDD workflow (Steps 1-5):

1. Create/update `.feature` files (BDD scenarios)
2. Write test code first
3. Implement business logic to pass tests
4. Run tests and verify
5. Code complete

##### ⚠️ Human Review Checkpoint

- Review code implementation
- Review test coverage
- Confirm meets expectations

##### Complete Task Loop (Steps 6-7)

```bash
# After approval
Please continue with Steps 6-7 to complete the task loop
```

AI automatically:

1. Generates change summary
2. Syncs Story status to `done`

#### Stage 4: Task Closure & Sync

If Steps 6-7 weren't executed in Stage 3, run manually:

```bash
# Generate change summary
@prompts/execution/change_summary.md Generate change summary

# Sync Story document
@{original_Story_file} @prompts/execution/story_sync.md Start sync
```

#### Stage 5: Bug Fix Workflow

For bugs discovered in completed Stories:

```bash
@prompts/planning/bug_fix_story.md Generate Bug Fix Story

Parent Story: STORY-01
Found in: Integration testing
Symptoms: ...
```

- Creates `STORY-XX.X_Name.md` (e.g., `STORY-01.1_Fix_Bug.md`)
- Then follow Stages 2-4 to fix

### Key Concepts

#### Planning Hierarchy

```text
Epic (Business Goal)
  └── Feature (Functional Module)
      └── Story (Implementable Task)
          └── Task (AI Execution Unit)
```

#### ID Naming Convention

- Epic: `EPIC-01`, `EPIC-02`, ...
- Feature: `FEAT-01`, `FEAT-02`, ... (per Epic)
- Story: `STORY-01`, `STORY-02`, ... (per Epic)
- Bug Fix: `STORY-01.1`, `STORY-01.2`, ... (inherits parent Story ID)
- Task: `TASK-01`, `TASK-02`, ... (sequential per Epic)

#### The Context System

Context is the "knowledge base" that guides AI to generate code matching your vision:

- **Global Context** (`context/global/`): Shared across entire project
  - Architecture.md - System architecture
  - Tech_Stack.md - Technology choices
  - Coding_Standard.md - Code conventions
  - Testing_Strategy.md - Test approaches

- **Epic Context** (`context/epics/EPIC-XX/`): Epic-specific knowledge
  - Module_Design.md - Module structure
  - Data_Model.md - Data schema
  - API_Spec.md - API contracts
  - Integration_Plan.md - Integration strategy

#### Core Principles

- **You Plan, AI Executes**: You define WHAT and WHY; AI handles HOW
- **Context is King**: Well-maintained context ensures consistent, quality AI output
- **Test-First**: Always create tests before implementation (BDD/TDD)
- **Human Review**: Always review before integration
- **Iterative**: Break complex tasks into Stories, tackle systematically

### Quick Start Example

After initialization, here's a typical first session:

```bash
# 1. Initialize project structure
@prompts/initialization/project_init.md Initialize project

# 2. Define your first Epic (e.g., User Authentication)
@{auth_requirements.md} @prompts/planning/requirements_review.md Review

# 3. Generate planning from approved solution
@{requirements.md} @{tech_solution.md} @prompts/planning/requirements_breakdown.md Breakdown

# 4. Start implementing first Story
@{STORY-01_Login.md} @prompts/execution/task_generation.md Generate Task
@.the_conn/ai_workspace/EPIC-01/TASK-01_STORY-01_Login/ Start task

# 5. Review, approve, and let AI close the loop
Please continue with Steps 6-7
```

### Collaboration Tips

#### For Teams

- Commit `epics/` and `context/` to Git (shared planning and knowledge)
- Add `ai_workspace/` to `.gitignore` (personal temporary work)
- Use branch strategy: `epic/EPIC-XX` for Epic-level work
- Coordinate Story IDs via Epic README

#### For Solo Developers

- Start with global Context (Architecture, Tech Stack)
- Create one Epic at a time
- Review AI output critically - you're the captain
- Keep Context updated as project evolves

For comprehensive workflows, troubleshooting, and advanced features, see `.the_conn/GUIDE.md` after initialization.

## 📚 Documentation

- **[CLI.md](CLI.md)** - CLI usage guide (for users)
- **[DEVELOPMENT.md](DEVELOPMENT.md)** - Development guide (for contributors)
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines
- **[RELEASING.md](RELEASING.md)** - Release process (for maintainers)

## Core Idea: Reclaiming Command for the Human Navigator in the Age of AI

In the new era of AI-driven software development, we face a fundamental choice: do we let developers become passive reviewers of AI-generated code, or do we elevate them to strategic commanders who harness the immense power of AI?

**The Conn was born to champion the latter.**

We reject chaotic, uncontrolled AI generation. We firmly believe that the most exceptional software still originates from human wisdom, foresight, and architectural skill. AI should not be the pilot; it should be the most efficient and reliable engine and crew. The human is the one and only **Navigator** who determines the vessel's course.

## **Our Metaphor: The Bridge of the Starship Enterprise**

To clearly define this philosophy of human-machine collaboration, we frame the entire development process as a voyage through the stars:

- **The Navigator (The Human Developer)**:
    You are the captain, the strategic decision-maker. You are not responsible for tightening every bolt in the engine room, but you must set the final destination (business goals), chart the course through the cosmos (software architecture), and make critical decisions at key moments (technology selection, logic review). Your wisdom and experience are the sole guarantee of a successful voyage.

- **The AI Crew (AI Agents & Tools)**:
    They are efficient and loyal executors. They command powerful engines (code generation), precise sensors (testing and analysis), and reliable defense systems (code fixing). They can perfectly execute any order you give, but they cannot and should not decide the ship's direction.

- **The Bridge (The Development Environment)**:
    This is your command center, where information is gathered and orders are issued.

- **The Conn (This Project's Framework)**:
    This is our project—**The Conn**. It is not the entire bridge, but the most critical station on it: the **command and navigation console**.

## **Why the Name "The Conn"?**

The term "Conn" originates from naval terminology, specifically referring to the **direct command over the ship's movement—its course and speed**. In science fiction like *Star Trek*, when a captain says, **"You have the Conn,"** it signifies the formal transfer of control over the vessel.

By choosing this name, we convey a dual homage and a single declaration:

1. **A Nod to Professionalism**: It represents the rigor and discipline of engineering.
2. **A Tribute to Vision**: It evokes our shared imagination of a future where technology works in synergy with humanity.
3. **Our Declaration**: Through this project, we are formally handing the "Conn"—the command of software development—back to every human developer.

**The Conn framework is the console you use to issue commands and maintain control.** It translates your strategic intent (architecture, task planning) into specific instructions that AI can understand and execute, ensuring the entire process remains firmly under your command.

## **Our Mission**

**The Conn** aims to be the standard collaboration framework for empowering human developers in the age of AI. Our core objectives are:

1. **Empower the Navigator**: To provide a clean, efficient interface and workflow that allows developers to think strategically, issue commands, and review outcomes naturally, rather than getting bogged down in the minutiae of AI interaction.

2. **Standardize the Workflow**: To establish a set of best practices for the "human-plans, AI-executes" model. By providing project scaffolding, standardized command templates, and an agile workflow, we ensure that human-AI collaboration is stable, efficient, and predictable.

3. **Unleash AI, Safely**: As the core interface between human and AI, The Conn will have powerful guardrails to ensure AI's execution always serves human strategic intent, preventing any deviation from the course. This allows developers to confidently delegate repetitive engineering tasks to AI.

4. **Elevate Experience & Quality**: Ultimately, we aim to free developers from tedious coding to focus on creativity, architecture, and complex problem-solving. This will dramatically increase development speed while producing higher-quality, more visionary software products.

---

> **The Conn is more than a toolkit or a scaffold; it is a declaration, a philosophy of work.**
>
> **It declares that in the vast ocean of artificial intelligence, the human is always at the helm.**
>
> **Here, we reaffirm: You have the Conn.**
