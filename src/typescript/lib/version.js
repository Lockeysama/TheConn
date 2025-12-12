import { readFile, writeFile } from 'fs/promises';
import { join } from 'path';

const VERSION_FILE = '.version';

/**
 * Save version information
 */
export async function saveVersionInfo (theConnDir, versionInfo) {
    const versionFile = join(theConnDir, VERSION_FILE);
    await writeFile(versionFile, JSON.stringify(versionInfo, null, 2), 'utf-8');
}

/**
 * Load version information
 */
export async function loadVersionInfo (theConnDir) {
    const versionFile = join(theConnDir, VERSION_FILE);
    try {
        const content = await readFile(versionFile, 'utf-8');
        return JSON.parse(content);
    } catch (error) {
        // Return empty object if file doesn't exist
        return {};
    }
}
