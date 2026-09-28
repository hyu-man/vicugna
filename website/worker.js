// 幕（2026-09-28 本人「一旦このサイトは非表示にしておいて」）
// 全リクエストをこの静かなページで受ける。棚の本体は public/ に無傷のまま。
// 戻すとき：wrangler.toml の main と run_worker_first を外して deploy。
const CURTAIN = `<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>vicugna</title>
<style>
body{margin:0;min-height:100svh;display:grid;place-content:center;background:#f6f3eb;color:#737667;
font-family:'Hiragino Maru Gothic ProN','Yu Gothic',sans-serif;letter-spacing:.3em;font-size:13px}
</style>
</head>
<body>じゅんびちゅう。</body>
</html>`;

export default {
  async fetch() {
    return new Response(CURTAIN, {
      status: 200,
      headers: {
        "content-type": "text/html; charset=utf-8",
        "x-robots-tag": "noindex, nofollow",
        "cache-control": "no-store",
      },
    });
  },
};
