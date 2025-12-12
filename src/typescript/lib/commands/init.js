import { access, mkdir } from 'fs/promises';
import { join, resolve } from 'path';
import { downloadFrameworkFiles } from '../github.js';
import { saveVersionInfo } from '../version.js';

/**
 * Initialize The Conn framework
 */
export async function init (targetPath, branch) {
    const resolvedPath = resolve(targetPath);
    const theConnDir = join(resolvedPath, '.the_conn');

    // Check if already initialized
    try {
        await access(theConnDir);
        throw new Error(
            `The Conn framework is already initialized in ${resolvedPath}\n` +
            `Use 'theconn update' to update the framework.`
        );
    } catch (error) {
        if (error.code !== 'ENOENT') {
            throw error;
        }
    }

    // Create .the_conn directory
    await mkdir(theConnDir, { recursive: true });

    // Download framework files
    const versionInfo = await downloadFrameworkFiles(theConnDir, branch, false);
    versionInfo.installed_at = new Date().toISOString();

    // Save version info
    await saveVersionInfo(theConnDir, versionInfo);
}
