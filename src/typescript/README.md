# @theconn/cli

Command-line tool for integrating [The Conn](https://github.com/Lockeysama/TheConn) framework into your projects.

## Quick Start

### Using npx (Recommended)

No installation required! Just run:

```bash
# Initialize The Conn framework in current directory
npx @theconn/cli init

# Initialize with specific branch
npx @theconn/cli init --branch=v1.0.0

# Initialize in specific directory
npx @theconn/cli init --path=./my-project
```

## Commands

### `init`

Initialize The Conn framework in a project.

```bash
npx @theconn/cli init [options]
```

**Options:**
- `--branch <branch>` - GitHub branch to use (default: `main`)
- `--path <path>` - Target directory (default: `.`)

**Example:**
```bash
npx @theconn/cli init --branch=main --path=./my-project
```

### `update`

Update The Conn framework files (preserves your data).

```bash
npx @theconn/cli update [options]
```

**Options:**
- `--branch <branch>` - GitHub branch to use (default: current branch)
- `--path <path>` - Target directory (default: `.`)

**Example:**
```bash
npx @theconn/cli update --branch=v1.1.0
```

**Note:** This command only updates framework files (`ai_prompts/`, `GUIDE.md`, `README.md`). Your data (`epics/`, `context/`, `ai_workspace/`) will be preserved.

### `uninstall`

Uninstall The Conn framework (keeps user data).

```bash
npx @theconn/cli uninstall [options]
```

**Options:**
- `--path <path>` - Target directory (default: `.`)
- `--yes` - Skip confirmation prompt

**Example:**
```bash
npx @theconn/cli uninstall --yes
```

**Note:** This command removes framework files but keeps your data. To completely remove the framework, delete the `.the_conn` directory manually.

### `check`

Check for framework updates.

```bash
npx @theconn/cli check [options]
```

**Options:**
- `--path <path>` - Target directory (default: `.`)

**Example:**
```bash
npx @theconn/cli check
```

## What Gets Installed?

When you run `init`, the following structure is created:

```
.the_conn/
├── ai_prompts/         # AI prompt templates
├── epics/              # Your project epics (empty)
├── context/
│   ├── global/         # Global context (empty)
│   └── epics/          # Epic-specific context (empty)
├── ai_workspace/       # Temporary workspace (empty)
├── GUIDE.md            # Usage guide
└── README.md           # Framework docs
```

## Version Management

The framework uses a `.version` file to track the installed version. This allows the CLI to:
- Check for updates
- Update to specific branches/versions
- Maintain version history

## .gitignore

It's recommended to add the following to your `.gitignore`:

```gitignore
.the_conn/ai_workspace/
```

This prevents temporary AI workspace files from being committed.

## Requirements

- Node.js >= 18.0.0

## License

MIT

## Links

- [GitHub Repository](https://github.com/Lockeysama/TheConn)
- [Documentation](https://github.com/Lockeysama/TheConn/blob/main/README.md)
- [Issues](https://github.com/Lockeysama/TheConn/issues)
