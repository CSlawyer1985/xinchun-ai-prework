// 四明山法师 AI 夜校 · 访问计数 Worker
// KV binding: COUNTER
//   - pv : 总访问次数
//   - uv : 独立访客数（按 IP 哈希去重）
//   - ip:<sha256(ip)> : 单个 IP 的 30 天去重标记（带 TTL）

const IP_TTL = 30 * 24 * 60 * 60 // 30 天
const BASE = '/api/counter'

// 仅允许站点本身和本地开发源访问，避免被任意站点滥用刷数
function isAllowedOrigin(origin) {
  if (!origin) return false
  if (origin === 'https://legalagi.cn' || origin === 'https://www.legalagi.cn') return true
  // 本地开发源：端口可变，按前缀通配
  return /^http:\/\/(127\.0\.0\.1|localhost):\d+$/.test(origin)
}

function corsHeaders(origin) {
  const allow = isAllowedOrigin(origin) ? origin : 'https://legalagi.cn'
  return {
    'Access-Control-Allow-Origin': allow,
    'Access-Control-Allow-Methods': 'GET, OPTIONS',
    'Access-Control-Allow-Headers': '*',
    'Access-Control-Max-Age': '86400',
    Vary: 'Origin',
  }
}

async function sha256(text) {
  const data = new TextEncoder().encode(text)
  const buf = await crypto.subtle.digest('SHA-256', data)
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, '0')).join('')
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url)
    const origin = request.headers.get('Origin') || ''
    const headers = corsHeaders(origin)

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers })
    }
    if (request.method !== 'GET' || (url.pathname !== '/' && url.pathname !== BASE)) {
      return new Response('Not Found', { status: 404, headers })
    }

    // 读当前计数（缺省 0，基数在部署时通过 wrangler kv:key put 写入）
    let pv = parseInt(await env.COUNTER.get('pv'), 10)
    let uv = parseInt(await env.COUNTER.get('uv'), 10)
    if (!Number.isFinite(pv)) pv = 0
    if (!Number.isFinite(uv)) uv = 0

    // PV：每次访问 +1
    pv += 1

    // UV：按访客 IP 哈希做 30 天去重
    const ip = request.headers.get('CF-Connecting-IP') || 'unknown'
    const ipKey = 'ip:' + (await sha256(ip))
    const seen = await env.COUNTER.get(ipKey)
    if (!seen) {
      uv += 1
      await env.COUNTER.put(ipKey, '1', { expirationTtl: IP_TTL })
      await env.COUNTER.put('uv', String(uv))
    }
    await env.COUNTER.put('pv', String(pv))

    return new Response(JSON.stringify({ pv, uv }), {
      headers: { ...headers, 'Content-Type': 'application/json; charset=utf-8' },
    })
  },
}
