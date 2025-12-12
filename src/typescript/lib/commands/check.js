import { access } from 'fs/promises';
import { join, resolve } from 'path';
import chalk from 'chalk';
import { GitHubClient } from '../github.js';
import { loadVersionInfo } from '../version.js';

/**
 * Check for framework updates
 */
export async function check (targetPath) {
    const resolvedPath = resolve(targetPath);
    const theConnDir = join(resolvedPath, '.the_conn');

    // Check if initialized
    try {
        await access(theConnDir);
    } catch (error) {
        throw new Error(
            `The Conn framework is not initialized in ${resolvedPath}\n` +
            `Use 'theconn init' to initialize the framework.`
        );
    }

    // Load current version info
    const currentVersion = await loadVersionInfo(theConnDir);
    const currentBranch = currentVersion.branch || 'unknown';
    const currentCommit = currentVersion.commit || 'unknown';

    console.log(chalk.cyan(`\n🔍 Checking for updates on branch '${currentBranch}'...\n`));

    try {
        // Get latest commit from GitHub
        const client = new GitHubClient();
        const latestCommit = await client.getBranchCommit(currentBranch);

        // Display version comparison
        console.log(chalk.bold('Version Comparison:'));
        console.log(chalk.cyan('  Current:'), currentCommit.substring(0, 7), chalk.green('✓ Installed'));
        console.log(chalk.cyan('  Latest: '), latestCommit.substring(0, 7), chalk.green('✓ Available'));

        // Check if update is available
        if (currentCommit === latestCommit) {
            console.log(chalk.green('\n✅ You are using the latest version!'));
        } else {
            console.log(chalk.yellow('\n⚠️  A new version is available!'));
            console.log(chalk.cyan(`\nRun 'theconn update' to update to the latest version.`));
        }
    } catch (error) {
        console.error(chalk.red('\n❌ Error checking for updates:'), error.message);
        throw error;
    }
}
