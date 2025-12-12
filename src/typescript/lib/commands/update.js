import { access } from 'fs/promises';
import { join, resolve } from 'path';
import chalk from 'chalk';
import { downloadFrameworkFiles } from '../github.js';
import { loadVersionInfo, saveVersionInfo } from '../version.js';

/**
 * Update The Conn framework
 */
export async function update (targetPath, branch = null) {
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

    // Use current branch if not specified
    if (!branch) {
        branch = currentVersion.branch || 'main';
        console.log(chalk.blue(`ℹ️  Using current branch: ${branch}`));
    }

    // Download framework files (update mode preserves user data)
    const versionInfo = await downloadFrameworkFiles(theConnDir, branch, true);
    versionInfo.installed_at = currentVersion.installed_at;
    versionInfo.updated_at = new Date().toISOString();

    // Save version info
    await saveVersionInfo(theConnDir, versionInfo);
}
