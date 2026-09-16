import assert from 'node:assert/strict'
import { existsSync, readFileSync } from 'node:fs'
import { spawnSync } from 'node:child_process'
import test from 'node:test'
import { fileURLToPath } from 'node:url'
import path from 'node:path'

const projectRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const distRoot = path.join(projectRoot, 'docs', '.vitepress', 'dist')

test('报名者可从首页和导航进入有明确边界说明的上期大纲', () => {
  const build = spawnSync('npm', ['run', 'docs:build'], {
    cwd: projectRoot,
    encoding: 'utf8'
  })

  assert.equal(build.status, 0, `${build.stdout}\n${build.stderr}`)

  const syllabusPath = path.join(distRoot, 'courses', '00_上期课程大纲.html')
  assert.ok(existsSync(syllabusPath), '应构建上期课程大纲独立页面')

  const homeHtml = readFileSync(path.join(distRoot, 'index.html'), 'utf8')
  const syllabusHtml = readFileSync(syllabusPath, 'utf8')

  assert.match(homeHtml, />看看合不合适</)
  assert.match(homeHtml, /\/courses\/00_%E4%B8%8A%E6%9C%9F%E8%AF%BE%E7%A8%8B%E5%A4%A7%E7%BA%B2/)
  assert.match(syllabusHtml, /公益课程/)
  assert.match(syllabusHtml, /不代表下期课程承诺/)
  assert.match(syllabusHtml, /资料：先导课 \+ 6 节主课 \+ 返场课逐字稿/)
  assert.match(syllabusHtml, /返场课｜复盘、分享与再出发/)
  assert.match(syllabusHtml, /嘉宾和分享主题每期不同/)
  assert.match(syllabusHtml, /8 份逐字稿/)
})
