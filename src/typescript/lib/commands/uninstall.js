import { access, readdir, rm, rmdir } from 'fs/promises';
import { join, resolve } from 'path';
import chalk from 'chalk';

/**
 * Uninstall The Conn framework (keeps user data)
 */
export async function uninstall (targetPath) {
    const resolvedPath = resolve(targetPath);
    const theConnDir = join(resolvedPath, '.the_conn');

    // Check if initialized
    try {
        await access(theConnDir);
    } catch (error) {
        throw new Error(`The Conn framework is not initialized in ${resolvedPath}`);
    }

    // Remove framework files only
    const frameworkItems = [
        'ai_prompts',
        'GUIDE.md',
        'README.md',
        '.version'
    ];

    for (const item of frameworkItems) {
        const itemPath = join(theConnDir, item);
        try {
            await rm(itemPath, { recursive: true, force: true });
        } catch (error) {
            // Ignore if doesn't exist
        }
    }

    // Check if .the_conn is now empty (only user data left)
    try {
        const remainingItems = await readdir(theConnDir);
        if (remainingItems.length === 0) {
            await rmdir(theConnDir);
            console.log(chalk.blue('\nℹ️  Removed empty .the_conn directory'));
        }
    } catch (error) {
        // Ignore errors
    }
}
