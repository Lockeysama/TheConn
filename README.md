# The Conn: Naming Philosophy & Mission

[中文版](README.zh.md) | [CLI Documentation](CLI.md) | [Usage Guide](.the_conn/docs/GUIDE.md) | [Development Guide](DEVELOPMENT.md)

## 🚀 Quick Start

**Install the CLI tool and initialize:**

```bash
# Python users
uvx theconn init

# Node.js users
npx theconn-cli init
```

**Start using with AI:**

```bash
# In your AI IDE (e.g., Cursor), use @ symbol with tc.md:
@tc.md init                    # Initialize project
@tc.md review                  # Requirements review (most used)
@tc.md quick "fix login bug"   # Quick change (most used)
@tc.md gtask STORY-01          # Generate task (most used)
@tc.md etask                   # Execute task (most used)
```

**Documentation:**

- 📘 [Complete Usage Guide](.the_conn/docs/GUIDE.md) - Full workflow and best practices
- 📗 [CLI Documentation](CLI.md) - CLI tool installation and management
- 📙 [Command Reference](.the_conn/docs/COMMANDS.md) - All available commands

## 🎯 How It Works

### Core Concept

The Conn creates a structured workspace in your project:

```text
.the_conn/
├── epics/              # 📋 Planning - Your Stories and Features
├── context/            # 📚 Knowledge - Architecture & Design Docs
├── rules/              # ⚖️  Core Rules - Framework constraints (auto-managed)
├── playbooks/          # 🤖 AI Tools - Command system (auto-managed)
├── docs/               # 📖 Documentation (auto-managed)
└── ai_workspace/       # 🔧 Temporary work area (add to .gitignore)
```

### Workflow Overview

The Conn follows a simple 5-stage process:

1. **Initialize** - Set up project structure with `@tc.md init`
2. **Plan** - Convert requirements to Epics, Features, and Stories
3. **Execute** - AI implements Stories with test-first approach
4. **Review** - Human reviews and approves AI's work
5. **Iterate** - Continue with next Story

**Example workflow:**

```bash
@tc.md init                    # Initialize
@tc.md review                  # Requirements review & breakdown
@tc.md gtask STORY-01          # Generate task
@tc.md etask                   # AI executes with TDD/BDD
@tc.md plan next               # Get next step
```

**Quick changes (bug fixes & improvements):**

```bash
@tc.md quick "STORY-03 crashes under high concurrency"
@tc.md q "Add detailed login logs"  # 'q' is shortcut for 'quick'
```

**Key principles:**

- **You Plan, AI Executes** - You define WHAT and WHY; AI handles HOW
- **Context is King** - Maintain architecture docs in `context/` for consistent AI output
- **Test-First** - Always write tests before implementation (BDD/TDD)
- **Human Review** - Always review AI's work before merging
- **Fast Iterations** - Use `@tc.md quick` for small changes while maintaining documentation

For detailed workflows and all commands, see [Complete Usage Guide](.the_conn/docs/GUIDE.md)

## 📚 Documentation

### For Users

- **[Complete Usage Guide](.the_conn/docs/GUIDE.md)** - Full workflow, commands, and best practices
- **[CLI Documentation](CLI.md)** - CLI tool installation and management
- **[Command Reference](.the_conn/docs/COMMANDS.md)** - Quick command lookup

### For Contributors

- **[Development Guide](DEVELOPMENT.md)** - Setup, development, and release process
- **[Contributing Guidelines](CONTRIBUTING.md)** - How to contribute

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
