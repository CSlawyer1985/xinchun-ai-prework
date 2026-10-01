import assert from 'node:assert/strict'
import { existsSync, readFileSync } from 'node:fs'
import { spawnSync } from 'node:child_process'
import test from 'node:test'
import { fileURLToPath } from 'node:url'
import path from 'node:path'

const projectRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const distRoot = path.join(projectRoot, 'docs', '.vitepress', 'dist')

test('首页显示报名关闭状态且不再显示合适性入口或报名表', () => {
  const build = spawnSync('npm', ['run', 'docs:build'], {
    cwd: projectRoot,
    encoding: 'utf8'
  })

  assert.equal(build.status, 0, `${build.stdout}\n${build.stderr}`)

  const syllabusPath = path.join(distRoot, 'courses', '00_上期课程大纲.html')
  assert.ok(existsSync(syllabusPath), '应构建上期课程大纲独立页面')

  const homeHtml = readFileSync(path.join(distRoot, 'index.html'), 'utf8')
  const syllabusHtml = readFileSync(syllabusPath, 'utf8')

  assert.match(homeHtml, /报名关闭期/)
  assert.doesNotMatch(homeHtml, /看看合不合适|第四期报名进行中|xeikezlmp0\.feishu\.cn\/share\/base\/form/)
  assert.match(syllabusHtml, /第四期报名已截止/)
  assert.doesNotMatch(syllabusHtml, /xeikezlmp0\.feishu\.cn\/share\/base\/form/)
  assert.match(syllabusHtml, /公益课程/)
  assert.match(syllabusHtml, /不代表下期课程承诺/)
  assert.match(syllabusHtml, /资料：先导课 \+ 6 节主课 \+ 返场课逐字稿/)
  assert.match(syllabusHtml, /返场课｜复盘、分享与再出发/)
  assert.match(syllabusHtml, /嘉宾和分享主题每期不同/)
  assert.match(syllabusHtml, /8 份逐字稿/)
})
