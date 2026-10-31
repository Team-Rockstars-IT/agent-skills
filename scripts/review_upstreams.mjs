// Fetch exact upstream skill resources into a temporary directory, never the catalog.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import crypto from 'node:crypto';
const root = process.argv[2] || fs.mkdtempSync(path.join(os.tmpdir(), 'rockstars-six-'));
const locked = process.argv[3] ? JSON.parse(fs.readFileSync(process.argv[3], 'utf8')) : null;
fs.mkdirSync(root, { recursive: true });
const choices = [
  ['tdd', 'mattpocock/skills', 'skills/engineering/tdd'],
  ['sdd', 'addyosmani/agent-skills', 'skills/spec-driven-development'],
  ['readiness', 'exadel-inc/agentic-readiness-assessment', 'skills/agentic-readiness-assessment'],
  ['wcag', 'humbleteam/accessibility-audit', ''],
  ['seo', 'coreyhaines31/marketingskills', 'skills/seo-audit'],
  ['threat', 'openai/skills', 'skills/.curated/security-threat-model'],
];
async function json(url) {
  const response = await fetch(url, { headers: { 'User-Agent': 'rockstars-reference-review', Accept: 'application/vnd.github+json' } });
  if (!response.ok) throw new Error(`${response.status} ${url}`);
  return response.json();
}
const manifest = [];
for (const [id, repo, prefix] of choices) {
  const metadata = await json(`https://api.github.com/repos/${repo}`);
  const expected = locked?.find(x => x.id === id && x.repo === repo);
  if (locked && !expected) throw new Error(`Missing pinned source: ${id}`);
  const head = await json(`https://api.github.com/repos/${repo}/commits/${expected?.commit || metadata.default_branch}`);
  const tree = await json(`https://api.github.com/repos/${repo}/git/trees/${head.sha}?recursive=1`);
  if (tree.truncated) throw new Error(`Truncated tree: ${repo}`);
  const selected = tree.tree.filter(x => x.type === 'blob' && (
    (prefix ? x.path.startsWith(prefix + '/') : /^(SKILL\.md|references\/)/.test(x.path)) ||
    /^(LICENSE(?:\.txt|\.md)?|NOTICE|README\.md|plugin\.json)$/i.test(x.path)
  ) && /\.(md|txt|yaml|yml|py|js|sh|json)$|(?:^|\/)LICENSE$|(?:^|\/)NOTICE$/i.test(x.path));
  const files = [];
  for (const entry of selected) {
    if (entry.size > 500000) throw new Error(`Unexpected resource size: ${repo}/${entry.path}`);
    const response = await fetch(`https://raw.githubusercontent.com/${repo}/${head.sha}/${entry.path}`);
    if (!response.ok) throw new Error(`${response.status}: ${entry.path}`);
    const content = Buffer.from(await response.arrayBuffer());
    const digest = crypto.createHash('sha256').update(content).digest('hex');
    if (expected && expected.files.find(x => x.path === entry.path)?.sha256 !== digest) throw new Error(`Pinned resource differs: ${id}/${entry.path}`);
    const target = path.join(root, 'upstream', id, entry.path);
    fs.mkdirSync(path.dirname(target), { recursive: true });
    fs.writeFileSync(target, content);
    files.push({ path: entry.path, blob: entry.sha, sha256: digest });
  }
  const record = { id, repo, prefix, commit: head.sha, committedAt: head.commit.committer.date, archived: metadata.archived, licenseHint: metadata.license?.spdx_id || null, files };
  manifest.push(record);
  fs.writeFileSync(path.join(root, 'upstream-manifest.json'), JSON.stringify(manifest, null, 2));
  console.log(JSON.stringify({ id, commit: record.commit, files: files.length, licenseHint: record.licenseHint }));
}
console.log(`REVIEW_ROOT=${root}`);
