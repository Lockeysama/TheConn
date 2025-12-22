import { mkdir, writeFile, rm } from 'fs/promises';
import { join, dirname } from 'path';
import ora from 'ora';

const GITHUB_REPO = 'Lockeysama/TheConn';
const GITHUB_API_BASE = 'https://api.github.com';
const GITHUB_RAW_BASE = 'https://raw.githubusercontent.com';

/**
 * GitHub client for downloading framework files
 */
export class GitHubClient {
    constructor(repo = GITHUB_REPO, token = null) {
        this.repo = repo;
        this.token = token || process.env.GITHUB_TOKEN;
        this.headers = {
            Accept: 'application/vnd.github.v3+json'
        };
        if (this.token) {
            this.headers.Authorization = `token ${this.token}`;
        }
    }

    /**
     * Get the latest commit SHA for a branch
     */
    async getBranchCommit (branch) {
        const url = `${GITHUB_API_BASE}/repos/${this.repo}/branches/${branch}`;
        const response = await fetch(url, {
            headers: this.headers
        });

        if (response.status === 404) {
            throw new Error(`Branch '${branch}' not found in repository ${this.repo}`);
        }

        if (!response.ok) {
            throw new Error(`GitHub API error: ${response.statusText}`);
        }

        const data = await response.json();
        return data.commit.sha;
    }

    /**
     * Download a directory from GitHub recursively
     */
    async downloadDirectory (branch, sourcePath, targetPath, exclude = [], baseSourcePath = null) {
        // On first call, baseSourcePath is null, so we set it to sourcePath
        if (baseSourcePath === null) {
            baseSourcePath = sourcePath;
        }

        const url = `${GITHUB_API_BASE}/repos/${this.repo}/contents/${sourcePath}?ref=${branch}`;
        const response = await fetch(url, {
            headers: this.headers
        });

        if (!response.ok) {
            throw new Error(`Failed to fetch directory: ${response.statusText}`);
        }

        const items = await response.json();
        const itemList = Array.isArray(items) ? items : [items];

        for (const item of itemList) {
            // Calculate relative path from baseSourcePath
            const relativePath = item.path.substring(baseSourcePath.length).replace(/^\//, '');

            // Check if excluded
            if (exclude.some(ex => relativePath.startsWith(ex))) {
                continue;
            }

            if (item.type === 'file') {
                // Download file
                const fileResponse = await fetch(item.download_url);
                const content = await fileResponse.arrayBuffer();
                const targetFile = join(targetPath, relativePath);
                await mkdir(dirname(targetFile), { recursive: true });
                await writeFile(targetFile, Buffer.from(content));
            } else if (item.type === 'dir') {
                // Recurse into directory, passing the same baseSourcePath
                await this.downloadDirectory(branch, item.path, targetPath, exclude, baseSourcePath);
            }
        }
    }

    /**
     * Download a single file from GitHub
     */
    async downloadFile (branch, sourcePath, targetPath) {
        const url = `${GITHUB_RAW_BASE}/${this.repo}/${branch}/${sourcePath}`;
        const response = await fetch(url);

        if (response.status === 404) {
            throw new Error(`File '${sourcePath}' not found in branch '${branch}'`);
        }

        if (!response.ok) {
            throw new Error(`Failed to download file: ${response.statusText}`);
        }

        const content = await response.arrayBuffer();
        await mkdir(dirname(targetPath), { recursive: true });
        await writeFile(targetPath, Buffer.from(content));
    }
}

/**
 * Download The Conn framework files from GitHub
 */
export async function downloadFrameworkFiles (targetDir, branch = 'stable', updateMode = false) {
    const client = new GitHubClient();
    const spinner = ora();

    try {
        // Get commit SHA
        spinner.start(`Fetching branch '${branch}' info...`);
        const commitSha = await client.getBranchCommit(branch);
        spinner.succeed(`Branch: ${branch} (${commitSha.substring(0, 7)})`);

        // Download rules/
        spinner.start('Downloading rules...');
        const rulesDir = join(targetDir, 'rules');
        try {
            await rm(rulesDir, { recursive: true, force: true });
        } catch (error) {
            // Ignore if doesn't exist
        }
        await mkdir(rulesDir, { recursive: true });
        await client.downloadDirectory(branch, '.the_conn/rules', rulesDir, []);
        spinner.succeed('Downloaded rules');

        // Download playbooks/
        spinner.start('Downloading playbooks...');
        const playbooksDir = join(targetDir, 'playbooks');
        try {
            await rm(playbooksDir, { recursive: true, force: true });
        } catch (error) {
            // Ignore if doesn't exist
        }
        await mkdir(playbooksDir, { recursive: true });
        await client.downloadDirectory(branch, '.the_conn/playbooks', playbooksDir, []);
        spinner.succeed('Downloaded playbooks');

        // Download docs/
        spinner.start('Downloading docs...');
        const docsDir = join(targetDir, 'docs');
        try {
            await rm(docsDir, { recursive: true, force: true });
        } catch (error) {
            // Ignore if doesn't exist
        }
        await mkdir(docsDir, { recursive: true });
        await client.downloadDirectory(branch, '.the_conn/docs', docsDir, []);
        spinner.succeed('Downloaded docs');

        // Create directory structure (only in init mode)
        if (!updateMode) {
            spinner.start('Creating directory structure...');
            await mkdir(join(targetDir, 'epics'), { recursive: true });
            await mkdir(join(targetDir, 'context', 'global'), { recursive: true });
            await mkdir(join(targetDir, 'context', 'epics'), { recursive: true });
            await mkdir(join(targetDir, 'ai_workspace'), { recursive: true });
            spinner.succeed('Created directory structure');
        }

        return {
            branch,
            commit: commitSha
        };
    } catch (error) {
        spinner.fail('Failed to download framework files');
        throw error;
    }
}
