#!/usr/bin/env python3
"""重建页面：python3 scripts/build.py [--out 路径] [--check-links]
默认输出到仓库 docs/public/tools/ai-consciousness/index.html"""
import json,os,re,subprocess,sys,urllib.request
H=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
subprocess.run([sys.executable,os.path.join(H,"data/evidence.src.py")],cwd=H,check=True)
D=json.load(open(os.path.join(H,"data/evidence.json")))
need=["id","cat","stance","person","date","quote","src","url","status","accessed"]
ids=set()
for x in D["items"]:
    miss=[k for k in need if not x.get(k)]
    assert not miss,(x.get("id"),miss); assert x["id"] not in ids,x["id"]; ids.add(x["id"])
    if x.get("archive"): assert os.path.exists(os.path.join(H,"sources/raw",x["archive"])),x["archive"]
for c in [c for x in D["items"] for c in x.get("cites",[])]: assert c in ids,("cites 指向不存在的 id",c)
mids=set()
for m in D.get("media",[]):
    miss=[k for k in ["id","kind","title","by","date","url","desc","accessed"] if not m.get(k)]
    assert not miss,(m.get("id"),miss); assert m["id"] not in mids and m["id"] not in ids,m["id"]; mids.add(m["id"])
    assert m["kind"] in ("video","audio","image"),m["id"]
    if m["kind"]=="image": assert m.get("license") and os.path.exists(os.path.join(H,"assets/img",m["img"])),("图像需 license 与本地文件",m["id"])
    if m["kind"]=="video": assert m.get("yt"),m["id"]
    if m["kind"]=="audio": assert m.get("mp3") or m.get("yt"),m["id"]
    for r in m.get("rel",[]): assert r in ids,("rel 指向不存在的 id",m["id"],r)
t=open(os.path.join(H,"template/index.template.html")).read()
out=sys.argv[sys.argv.index("--out")+1] if "--out" in sys.argv else os.path.join(H,"../../docs/public/tools/ai-consciousness/index.html")
os.makedirs(os.path.dirname(out),exist_ok=True)
import shutil
shutil.copytree(os.path.join(H,"assets/img"),os.path.join(os.path.dirname(out),"img"),dirs_exist_ok=True)
open(out,"w").write(t.replace("/*DATA*/null",json.dumps(D,ensure_ascii=False).replace("</","<\\/")))
# sources list
with open(os.path.join(H,"sources/SOURCES.md"),"w") as f:
    f.write("# 来源清单（自动生成）\n\n| id | 人物/机构 | 来源 | 链接 | 状态 | 访问日期 | 存档 |\n|---|---|---|---|---|---|---|\n")
    for x in D["items"]: f.write(f"| {x['id']} | {x['person']} | {x['src']} | {x['url']} | {x['status']} | {x['accessed']} | {x.get('archive','')} |\n")
    f.write("\n## 影音图像\n\n| id | 类型 | 标题 | 作者/频道 | 链接 | 许可 | 访问日期 |\n|---|---|---|---|---|---|---|\n")
    for m in D.get("media",[]): f.write(f"| {m['id']} | {m['kind']} | {m['title']} | {m['by']} | {m['url']} | {m.get('license','平台嵌入')} | {m['accessed']} |\n")
print("built",out,len(D["items"]),"items",len(D.get("media",[])),"media")
if "--check-links" in sys.argv:
    for u in sorted({x["url"] for x in D["items"]+D.get("media",[])}|{m["mp3"] for m in D.get("media",[]) if m.get("mp3")}):
        try: c=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=20).status
        except Exception as e: c=getattr(e,"code",str(e)[:40])
        print(c,u)
