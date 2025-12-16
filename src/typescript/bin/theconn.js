#!/usr/bin/env node

import { Command } from 'commander';
import chalk from 'chalk';
import { init } from '../lib/commands/init.js';
import { update } from '../lib/commands/update.js';
import { uninstall } from '../lib/commands/uninstall.js';
import { check } from '../lib/commands/check.js';

const program = new Command();

program
    .name('theconn')
    .description('The Conn - AI-powered development framework')
    .version('0.1.6');

program
    .command('init')
    .description('Initialize The Conn framework in a project')
    .option('--branch <branch>', 'GitHub branch to use', 'stable')
    .option('--path <path>', 'Target directory', '.')
    .action(async (options) => {
        try {
            await init(options.path, options.branch);
            console.log(chalk.green('\n✅ Successfully initialized The Conn framework!'));
            console.log(chalk.cyan('\n📁 Location:'), `${options.path}/.the_conn`);
            console.log(chalk.cyan('🌿 Branch:'), options.branch);
            console.log(chalk.yellow('\n📖 Next steps:'));
            console.log('   1. Read .the_conn/docs/GUIDE.md for usage instructions');
            console.log('   2. Add the following to your .gitignore:');
            console.log('      .the_conn/ai_workspace/');
            console.log('      .the_conn/playbooks/');
            console.log('      .the_conn/docs/');
        } catch (error) {
            console.error(chalk.red('❌ Error:'), error.message);
            process.exit(1);
        }
    });

program
    .command('update')
    .description('Update The Conn framework files')
    .option('--branch <branch>', 'GitHub branch to use')
    .option('--path <path>', 'Target directory', '.')
    .action(async (options) => {
        try {
            await update(options.path, options.branch);
            console.log(chalk.green('\n✅ Successfully updated The Conn framework!'));
            console.log(chalk.cyan('\n📁 Location:'), `${options.path}/.the_conn`);
            console.log(chalk.blue('\nℹ️  Your data (epics/, context/, ai_workspace/) has been preserved.'));
        } catch (error) {
            console.error(chalk.red('❌ Error:'), error.message);
            process.exit(1);
        }
    });

program
    .command('uninstall')
    .description('Uninstall The Conn framework (keeps user data)')
    .option('--path <path>', 'Target directory', '.')
    .option('--yes', 'Skip confirmation')
    .action(async (options) => {
        try {
            if (!options.yes) {
                const readline = await import('readline');
                const rl = readline.createInterface({
                    input: process.stdin,
                    output: process.stdout
                });

                await new Promise((resolve) => {
                    rl.question(
                        chalk.yellow('⚠️  Are you sure you want to uninstall The Conn framework? (y/N) '),
                        (answer) => {
                            rl.close();
                            if (answer.toLowerCase() !== 'y') {
                                console.log(chalk.blue('Cancelled.'));
                                process.exit(0);
                            }
                            resolve();
                        }
                    );
                });
            }

            await uninstall(options.path);
            console.log(chalk.green('\n✅ Successfully uninstalled The Conn framework!'));
            console.log(chalk.blue('\nℹ️  Your data (epics/, context/, ai_workspace/) has been preserved.'));
            console.log('   To completely remove, delete the .the_conn directory manually.');
        } catch (error) {
            console.error(chalk.red('❌ Error:'), error.message);
            process.exit(1);
        }
    });

program
    .command('check')
    .description('Check for updates')
    .option('--path <path>', 'Target directory', '.')
    .action(async (options) => {
        try {
            await check(options.path);
        } catch (error) {
            console.error(chalk.red('❌ Error:'), error.message);
            process.exit(1);
        }
    });

program.parse();
