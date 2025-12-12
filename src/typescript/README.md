# The Conn - Node.js CLI

AI-powered development framework CLI for Node.js projects.

## Quick Start

Initialize The Conn framework in your project:

```bash
npx @theconn/cli init
```

## Installation

No installation required! Use `npx` to run the CLI directly.

Alternatively, install globally:

```bash
npm install -g @theconn/cli
theconn init
```

## Commands

- `npx @theconn/cli init` - Initialize The Conn framework
- `npx @theconn/cli update` - Update framework files
- `npx @theconn/cli check` - Check for updates
- `npx @theconn/cli uninstall` - Uninstall framework

### Options

All commands support:
- `--branch <branch>` - GitHub branch to use (default: `main`)
- `--path <path>` - Target directory (default: `.`)
- `--yes` - Skip confirmation prompts (uninstall only)

### Examples

```bash
# Initialize in current directory
npx @theconn/cli init

# Initialize with specific branch
npx @theconn/cli init --branch=v1.0.0

# Initialize in specific directory
npx @theconn/cli init --path=./my-project

# Update to specific version
npx @theconn/cli update --branch=v1.1.0

# Check for updates
npx @theconn/cli check

# Uninstall without confirmation
npx @theconn/cli uninstall --yes
```

## Requirements

- Node.js >= 18.0.0

## Documentation

For full documentation, visit: https://github.com/Lockeysama/TheConn

- [CLI Documentation](https://github.com/Lockeysama/TheConn/blob/main/CLI.md)
- [Development Guide](https://github.com/Lockeysama/TheConn/blob/main/DEVELOPMENT.md)
- [Contributing](https://github.com/Lockeysama/TheConn/blob/main/CONTRIBUTING.md)

## License

MIT License - see [LICENSE](https://github.com/Lockeysama/TheConn/blob/main/LICENSE)
