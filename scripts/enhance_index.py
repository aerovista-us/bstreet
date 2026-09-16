from pathlib import Path
from bs4 import BeautifulSoup
import gzip, base64, re

PATH = Path("index.html")
html = PATH.read_text(encoding="utf-8")
soup = BeautifulSoup(html, "html.parser")

def decode_section(payload):
    return BeautifulSoup(gzip.decompress(base64.b64decode(payload)).decode("utf-8"), "html.parser").section

# Keep MASTER COMPLETE source untouched. This layer only enhances production index.
PAIDFULL = """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"""
PAIDPACKET = """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"""

# Replace paid negotiation page with the enhanced assistance version.
old_paid = soup.find("section", attrs={"data-page":"paidfull"})
new_paid = decode_section(PAIDFULL)
if old_paid:
    old_paid.replace_with(new_paid)

# Add complete paid frontage paperwork as a first-class section if absent.
if not soup.find("section", attrs={"data-page":"paidpacket"}):
    paid_packet = decode_section(PAIDPACKET)
    anchor = soup.find("section", attrs={"data-page":"reportarchive"})
    if anchor:
        anchor.insert_before(paid_packet)
    else:
        soup.find("main", class_="main").append(paid_packet)

# Production privacy/discoverability guard. GitHub Pages remains public by direct URL.
if not soup.find("meta", attrs={"name":"robots"}):
    m=soup.new_tag("meta")
    m["name"]="robots"
    m["content"]="noindex,nofollow,noarchive,nosnippet"
    soup.head.append(m)

# The paid packet is fully printable in-site; avoid a broken public binary-download link.
_paid = soup.find("section", attrs={"data-page":"paidpacket"})
if _paid:
    _a = _paid.select_one(".paid-doc-actions a.primary")
    if _a:
        _a["href"] = "#paidpacket"
        _a["onclick"] = "printPage('paidpacket');return false"
        _a.string = "Print paid packet"

# CSS: paid path + substantial UI presentation layer.
style = soup.find("style")
style.string = (style.string or "") + r"""
/* Paid-frontage negotiation / paperwork enhancements */
.branch-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:14px 0}
.branch{border:1px solid var(--line);border-radius:16px;padding:16px;background:#0b1828}
.branch.gift{border-color:#39796d}.branch.paid{border-color:#7a6335}.branch.stop{border-color:#75434a}
.branch b{display:block;font-size:17px;margin-bottom:5px}.branch small{color:var(--muted)}
.neg-assist{border:1px solid #3b5e78;border-radius:18px;background:linear-gradient(135deg,#0f2236,#0a1828);padding:18px;margin:16px 0}
.neg-assist-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}
.neg-result{margin-top:12px;border-left:4px solid var(--teal);padding:12px 14px;background:rgba(89,224,196,.07);border-radius:0 12px 12px 0}
.neg-result.warn{border-color:var(--gold);background:rgba(255,201,102,.07)}.neg-result.red{border-color:var(--red);background:rgba(255,123,123,.08)}
.script-tree{display:grid;gap:9px;margin-top:12px}.script-node{border:1px solid var(--line);border-radius:13px;background:#0a1727;padding:12px}
.script-node b{color:#aef6e8}.script-node .say{margin-top:6px;color:#e8f2ff;border-left:3px solid #4a7197;padding-left:10px}
.paid-doc-actions{display:flex;gap:9px;flex-wrap:wrap;margin:12px 0}.paid-doc-actions a{display:inline-flex;align-items:center;border:1px solid #46627e;border-radius:10px;background:#10243a;color:white;padding:9px 12px;font-weight:800;text-decoration:none}
.paid-doc-actions a.primary{background:linear-gradient(135deg,#2fc5a8,#448fe3);border:0;color:#04101a}
@media(max-width:900px){.branch-grid{grid-template-columns:1fr}.neg-assist-grid{grid-template-columns:1fr 1fr}}
@media(max-width:600px){.neg-assist-grid{grid-template-columns:1fr}}

/* MASTER COMPLETE — substantial UI pass. Presentation only. */
:root{--side:318px;--glass:rgba(7,17,31,.78);--cyan:#8ff4e2}
body{background:radial-gradient(circle at 82% -12%,rgba(89,224,196,.16),transparent 29%),radial-gradient(circle at 28% 115%,rgba(121,169,255,.10),transparent 30%),linear-gradient(160deg,var(--bg),#091525 55%,#07101c)}
.sidebar{padding:19px 15px 22px;box-shadow:18px 0 48px rgba(0,0,0,.10)}.sidebar::-webkit-scrollbar{width:8px}.sidebar::-webkit-scrollbar-thumb{background:#203953;border-radius:99px}
.brand{padding:3px 4px 14px;border-bottom:1px solid rgba(41,65,93,.75);margin-bottom:13px}.side-status{background:linear-gradient(145deg,rgba(16,36,56,.98),rgba(9,24,39,.96));box-shadow:0 12px 35px rgba(0,0,0,.12)}
.nav-group.ui-group{margin:15px 8px 5px;padding-top:9px;border-top:1px solid rgba(41,65,93,.55)}.nav button{transition:.15s ease;border-radius:11px;padding:9px 10px}.nav button:hover{transform:translateX(2px);text-decoration:none}.nav button.active{box-shadow:inset 3px 0 0 var(--teal),0 8px 22px rgba(0,0,0,.08)}
.topbar{min-height:61px;padding:11px 22px;box-shadow:0 8px 26px rgba(0,0,0,.11)}.topbar-tools{display:flex;align-items:center;gap:7px}
.toolbtn{border:1px solid var(--line);background:#102038;color:#dcecff;border-radius:10px;padding:7px 10px;cursor:pointer;font-size:12px;white-space:nowrap}.toolbtn:hover{border-color:#5f829f;background:#142942}.toolbtn.icon{width:36px;height:36px;padding:0;display:grid;place-items:center;font-size:15px}
.page{padding-top:24px}.page.active{animation:uiFade .22s ease}@keyframes uiFade{from{opacity:.62;transform:translateY(5px)}to{opacity:1;transform:none}}
.section-tools{display:flex;align-items:center;gap:8px;margin:0 0 14px;padding:8px 10px;border:1px solid rgba(41,65,93,.75);background:linear-gradient(90deg,rgba(16,36,56,.85),rgba(10,24,40,.64));border-radius:13px}
.section-tools .st-title{font-size:11px;color:#8fa5bb;text-transform:uppercase;letter-spacing:.10em;font-weight:900}.section-tools .st-grow{flex:1}.section-tools .st-count{color:#7890a7;font-size:11px}.section-tools button{border:1px solid #365470;background:#0d1e31;color:#dcecff;border-radius:9px;padding:6px 9px;font-size:11px;cursor:pointer}
.hero{box-shadow:0 28px 80px rgba(0,0,0,.30);border-color:#36516d}.command-metric{background:linear-gradient(180deg,rgba(15,33,52,.90),rgba(8,21,34,.88));box-shadow:0 11px 28px rgba(0,0,0,.10);min-height:104px}
.dashboard-hub{margin:19px 0 4px;border:1px solid #35556f;border-radius:20px;padding:18px;background:radial-gradient(circle at 96% 0,rgba(89,224,196,.10),transparent 35%),linear-gradient(145deg,#0d2034,#091827)}
.dashboard-hub-head{display:flex;align-items:end;gap:16px;margin-bottom:13px}.dashboard-hub-head .grow{flex:1}.dashboard-hub-head h2{margin:0;font-size:24px}.dashboard-hub-head p{margin:2px 0 0;color:var(--muted);font-size:13px}
.lane-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:11px}.lane{border:1px solid var(--line);border-radius:15px;background:rgba(8,21,34,.74);padding:15px;min-height:163px;display:flex;flex-direction:column}
.lane .lane-k{font-size:10px;text-transform:uppercase;letter-spacing:.12em;font-weight:900;color:var(--teal)}.lane h3{font-size:18px;margin:5px 0}.lane p{color:#aebfd1;font-size:12px;margin:0 0 12px}.lane .lane-actions{display:flex;gap:7px;flex-wrap:wrap;margin-top:auto}
.lane button{border:1px solid #385977;background:#10243a;color:white;border-radius:9px;padding:7px 9px;font-size:11px;cursor:pointer}.lane button.primary{background:linear-gradient(135deg,#2fc5a8,#448fe3);color:#04101a;border:0;font-weight:850}
.bytecast{box-shadow:0 18px 55px rgba(0,0,0,.22)}.byte-icon{box-shadow:0 12px 34px rgba(89,224,196,.18)}.card,.strategy,.doc-card{transition:border-color .15s ease,transform .15s ease,box-shadow .15s ease}.card:hover,.strategy:hover,.doc-card:hover{border-color:#385a78;box-shadow:0 17px 46px rgba(0,0,0,.13)}
.doc-ribbon{display:flex;align-items:center;gap:9px;margin:12px 0 15px;padding:12px 13px;border:1px solid #3c6079;border-radius:14px;background:linear-gradient(90deg,rgba(121,169,255,.08),rgba(89,224,196,.06))}
.doc-ribbon .doc-icon{width:38px;height:38px;border-radius:10px;background:#17324d;color:#b9dcff;display:grid;place-items:center;font-weight:950}.doc-ribbon .doc-copy{flex:1}.doc-ribbon .doc-copy b{display:block}.doc-ribbon .doc-copy small{color:var(--muted)}
.doc-ribbon button,.doc-ribbon a{border:1px solid #456780;background:#10243a;color:white;border-radius:9px;padding:7px 10px;font-size:11px;cursor:pointer;text-decoration:none}.doc-ribbon .print{background:linear-gradient(135deg,#2fc5a8,#448fe3);border:0;color:#04101a;font-weight:850}
details.archive{box-shadow:0 12px 35px rgba(0,0,0,.08)}details.archive>summary{list-style:none;display:flex;align-items:center;gap:8px}details.archive>summary::-webkit-details-marker{display:none}details.archive>summary:before{content:"+";width:24px;height:24px;border-radius:7px;display:grid;place-items:center;background:#17324d;color:#a9d7ff;font-weight:900}details.archive[open]>summary:before{content:"–"}
.page-bottom-nav{display:grid;grid-template-columns:1fr auto 1fr;gap:9px;align-items:center;margin-top:34px;padding-top:17px;border-top:1px solid var(--line)}.page-bottom-nav button{border:1px solid #35536f;background:#0d1e31;color:#dcecff;border-radius:11px;padding:10px 12px;cursor:pointer}.page-bottom-nav button:last-child{text-align:right}.page-bottom-nav .center{font-size:11px;color:#71879e;text-align:center}
.mobile-dock{display:none;position:fixed;z-index:55;left:10px;right:10px;bottom:10px;padding:7px;border:1px solid #35536f;background:rgba(7,17,31,.94);backdrop-filter:blur(14px);border-radius:15px;box-shadow:0 18px 55px rgba(0,0,0,.36);grid-template-columns:repeat(4,1fr);gap:6px}.mobile-dock button{border:0;background:#102038;color:#dcecff;border-radius:10px;padding:8px 5px;font-size:10px}.mobile-dock button b{display:block;font-size:16px}
.search-modal{display:none;position:fixed;inset:0;z-index:120;background:rgba(2,8,14,.78);backdrop-filter:blur(12px);padding:6vh 16px}.search-modal.open{display:block}.search-panel{max-width:790px;margin:auto;border:1px solid #3b5e78;border-radius:20px;background:#0a1727;box-shadow:0 30px 100px rgba(0,0,0,.48);overflow:hidden}
.search-head{display:flex;gap:10px;align-items:center;padding:14px;border-bottom:1px solid var(--line)}.search-head input{flex:1;background:#07121f;border:1px solid #365470;color:white;border-radius:11px;padding:12px 13px;outline:none;font-size:15px}.search-head input:focus{border-color:var(--teal)}.search-head button{border:1px solid var(--line);background:#102038;color:white;border-radius:10px;padding:10px 12px;cursor:pointer}
.search-results{max-height:64vh;overflow:auto;padding:8px}.search-hit{padding:12px 13px;border:1px solid transparent;border-radius:12px;cursor:pointer}.search-hit:hover{background:#102038;border-color:#2e4b65}.search-hit b{display:block;color:#eaf5ff}.search-hit small{display:block;color:#8fa4ba;margin-top:3px;line-height:1.4}.search-empty{padding:28px;text-align:center;color:#8398ad}
body.focus-mode .app{grid-template-columns:1fr}body.focus-mode .sidebar{display:none}body.focus-mode .page{max-width:1180px}
.page[data-page="yesnow"]:before{content:"TIME-SENSITIVE";display:inline-block;margin-bottom:7px;padding:5px 8px;border-radius:999px;background:rgba(255,123,123,.10);border:1px solid rgba(255,123,123,.28);color:#ffb1b1;font-size:10px;font-weight:900;letter-spacing:.12em}
@media(max-width:1040px){.topbar .badge{display:none}.lane-grid{grid-template-columns:1fr 1fr}.topbar-tools .tooltext{display:none}}
@media(max-width:760px){.lane-grid{grid-template-columns:1fr}.section-tools .st-title,.section-tools .st-count{display:none}.topbar-tools .hide-mobile{display:none}.mobile-dock{display:grid}.page{padding-bottom:92px}.page-bottom-nav{grid-template-columns:1fr 1fr}.page-bottom-nav .center{display:none}}
@media print{.section-tools,.page-bottom-nav,.mobile-dock,.search-modal,.doc-ribbon,.topbar-tools{display:none!important}body.print-one .page{display:none!important}body.print-one .page.print-target{display:block!important;page-break-before:auto!important}body.print-one .page.print-target details.archive{display:block!important}body.print-one .page.print-target details.archive>summary{display:none!important}body.print-one .page.print-target .archive-body{display:block!important}}
"""

# Strengthen same-day gift/paid branching without duplicating the detailed packet.
yes = soup.find("section", attrs={"data-page":"yesnow"})
if yes and not yes.find("div", class_="branch-grid"):
    branch = BeautifulSoup(r"""
    <h2>Choose the lane before you leave</h2>
    <div class="branch-grid">
      <div class="branch gift"><b>Gift YES</b><small>Use the same-day gift/cooperation paperwork, survey access and broker notice. No price is introduced.</small><div style="margin-top:10px"><button class="btn" onclick="goPage('samedayfull')">Open gift agreement</button></div></div>
      <div class="branch paid"><b>Gift NO → price YES</b><small>Stop calling it a gift. Capture the fixed price in the paid term sheet and use the paid BLA purchase packet. Normally pay through escrow at recording—not cash in the room.</small><div style="margin-top:10px"><button class="btn gold" onclick="goPage('paidfull')">Negotiation help</button> <button class="btn" onclick="goPage('paidpacket')">Paid packet</button></div></div>
      <div class="branch stop"><b>No / maybe / high demand</b><small>Do not bid against yourself. Write down the response, preserve the friendship, and leave without creating a deal outside your private authority.</small></div>
    </div>
    """, "html.parser")
    last_call = yes.find_all("div", class_="callout")
    if last_call: last_call[-1].insert_before(branch)
    else: yes.append(branch)

# Document kit: make paid conversion explicit.
docs = soup.find("section", attrs={"data-page":"documents"})
if docs and "Paid Frontage" not in docs.get_text():
    insert = BeautifulSoup(r"""
    <div class="doc-card">
      <span class="state">If gift becomes paid</span>
      <h3>Paid Frontage Term Sheet + Conditional BLA Purchase Agreement</h3>
      <p>The moment 1007 requires compensation, stop using the gift agreement/deed as the operative documents. Capture the exact fixed price in the paid term sheet, keep the survey/City/title/lender/no-harm conditions, and normally route payment through title/escrow when the approved BLA can record.</p>
      <div class="strategy-actions no-print"><button class="btn gold" onclick="goPage('paidfull')">Open negotiation assistance</button><button class="btn" onclick="goPage('paidpacket')">Open paid paperwork</button></div>
    </div>
    """, "html.parser")
    cards = docs.find_all("div", class_="doc-card")
    if cards: cards[-1].insert_after(insert.div)
    else: docs.append(insert.div)

# Rebuild the JavaScript page registry from the actual canonical section order.
# The base Powerhouse historically carried several full packet/archive sections that were
# not exposed in its older navigation array; production must make every section reachable.
script = soup.find("script")
js = script.get_text()
import json
_page_pairs = []
for _sec in soup.find_all("section", class_="page"):
    _id = _sec.get("data-page")
    _title = _sec.get("data-title") or _id
    _page_pairs.append(f"[{json.dumps(_id)},{json.dumps(_title)}]")
_registry = "const pages=[" + ",".join(_page_pairs) + "];"
js, _n = re.subn(r"const pages=\[.*?\];", lambda _m: _registry, js, count=1, flags=re.S)
if _n != 1:
    raise RuntimeError("Could not rebuild pages registry")

# Negotiation helper JS.
neg_js = r"""
function fmtMoney(n){return Number(n||0).toLocaleString('en-US',{style:'currency',currency:'USD',maximumFractionDigits:0})}
function saveNegotiationLimits(){
  ['negAnchor','negSameMax','negEconMax'].forEach(id=>{const el=document.getElementById(id);if(el)localStorage.setItem('av_'+id,el.value||'')});
  evaluateNegotiation();
}
function loadNegotiationLimits(){
  ['negAnchor','negSameMax','negEconMax'].forEach(id=>{const el=document.getElementById(id);if(el)el.value=localStorage.getItem('av_'+id)||''});
}
function clearNegotiationLimits(){
  ['negAnchor','negSameMax','negEconMax','negAsk'].forEach(id=>{const el=document.getElementById(id);if(el)el.value='';localStorage.removeItem('av_'+id)});
  const r=document.getElementById('negResult');if(r){r.className='neg-result';r.textContent='Limits cleared. Set your private authority before the live conversation.'}
}
function evaluateNegotiation(){
  const same=Number(document.getElementById('negSameMax')?.value||0);
  const econ=Number(document.getElementById('negEconMax')?.value||0);
  const ask=Number(document.getElementById('negAsk')?.value||0);
  const r=document.getElementById('negResult');if(!r)return;r.className='neg-result';
  if(!ask){r.textContent='Enter the number 1007 asked for. If they have not named a number, ask them to name it first and then stop talking.';return}
  if(!same){r.classList.add('warn');r.innerHTML='<b>No same-call authority is set.</b> Do not agree live. Write down '+fmtMoney(ask)+' and say you need to evaluate the total survey/title/City cost before responding.';return;}
  if(ask<=same){r.innerHTML='<b>Inside your stated same-call ceiling.</b> '+fmtMoney(ask)+' can be conditionally documented if you still want the deal. Repeat the exact price, keep every survey/City/title/lender/no-harm condition, use the paid term sheet, and pay through escrow at recording.';return;}
  if(econ && ask>econ){r.classList.add('red');r.innerHTML='<b>Above your stated economic ceiling.</b> Do not counter upward. Decline or pause. Your fallback is still the one-parcel/two-dwelling strategy and sale of documented upside.';return;}
  r.classList.add('warn');r.innerHTML='<b>Above your same-call authority.</b> Do not negotiate against yourself. Say: “That is more than I am prepared to agree to on the spot. Let me look at the total cost and what still has to be proven, and I will get back to you.”';
}
document.addEventListener('DOMContentLoaded',loadNegotiationLimits);
"""

# Global topbar controls.
topbar = soup.find("div", class_="topbar")
if topbar and not topbar.find("div", class_="topbar-tools"):
    topbar.append(BeautifulSoup(r"""
    <div class="topbar-tools no-print">
      <button class="toolbtn icon" title="Dashboard" onclick="goPage('start')">⌂</button>
      <button class="toolbtn" title="Search this Powerhouse" onclick="openSearch()">⌕ <span class="tooltext">Search</span></button>
      <button class="toolbtn hide-mobile" title="Focus reading mode" onclick="toggleFocus()">◫ <span class="tooltext">Focus</span></button>
      <button class="toolbtn hide-mobile" title="Print current section" onclick="printCurrent()">⎙ <span class="tooltext">Print section</span></button>
    </div>""", "html.parser").div)

# Search and mobile navigation.
if not soup.find(id="siteSearchModal"):
    soup.body.append(BeautifulSoup(r"""
    <div class="search-modal no-print" id="siteSearchModal" onclick="if(event.target===this)closeSearch()">
      <div class="search-panel"><div class="search-head">
        <input id="siteSearchInput" type="search" placeholder="Search property, 1007, survey, lender, deed, paid fallback…" autocomplete="off"/>
        <button onclick="closeSearch()">Close</button>
      </div><div class="search-results" id="siteSearchResults"></div></div>
    </div>
    <div class="mobile-dock no-print">
      <button onclick="goPage('start')"><b>⌂</b>Home</button><button onclick="openSearch()"><b>⌕</b>Search</button>
      <button onclick="printCurrent()"><b>⎙</b>Print</button><button onclick="goNextPage()"><b>→</b>Next</button>
    </div>""", "html.parser"))

# Dashboard action lanes.
start = soup.find("section", attrs={"data-page":"start"})
if start and not start.find("div", class_="dashboard-hub"):
    hub = BeautifulSoup(r"""
    <div class="dashboard-hub no-print">
      <div class="dashboard-hub-head"><div><div class="eyebrow">Owner action center</div><h2>Choose the lane that matches the conversation.</h2>
      <p>The Powerhouse remains one canonical package; these shortcuts open the right existing section and paperwork.</p></div>
      <div class="grow"></div><button class="btn ghost" onclick="printAll()">Print full Powerhouse</button></div>
      <div class="lane-grid">
        <div class="lane"><div class="lane-k">Lane A · preferred first ask</div><h3>1007 agrees to gift</h3><p>Capture the yes, use the same-day agreement / survey access, alert the listing side, then launch survey + title.</p>
        <div class="lane-actions"><button class="primary" onclick="goPage('yesnow')">Open YES path</button><button onclick="printPage('samedayfull')">Print same-day agreement</button><button onclick="printPage('giftfull')">Print gift packet</button></div></div>
        <div class="lane"><div class="lane-k">Lane B · if gift is declined</div><h3>1007 wants to be paid</h3><p>Use the negotiation assistance first. If a price is agreed, switch from the gift lane to the paid BLA purchase packet.</p>
        <div class="lane-actions"><button class="primary" onclick="goPage('paidfull')">Negotiation assistance</button><button onclick="printPage('paidpacket')">Print paid packet</button></div></div>
        <div class="lane"><div class="lane-k">Lane C · after cooperation</div><h3>Prove before spending more</h3><p>Survey, title and written City interpretation decide whether the two-lot path deserves more money.</p>
        <div class="lane-actions"><button class="primary" onclick="goPage('firsttimer')">First-time steps</button><button onclick="goPage('boundary')">Survey / City scope</button><button onclick="goPage('diligence')">Open diligence</button></div></div>
      </div>
    </div>""", "html.parser").div
    bc = start.find(id="bytecast")
    (bc or start).insert_after(hub) if bc else start.append(hub)

# Utilities on each existing section.
pages = soup.find_all("section", class_="page")
page_ids = [p.get("data-page") for p in pages]
doc_pages = {
    "documents":("Document kit",None),
    "giftfull":("Gift transaction packet",None),
    "samedayfull":("Same-day active-sale agreement",None),
    "paidfull":("Paid negotiation guide",None),
    "paidpacket":("Paid frontage purchase packet",None),
    "reportarchive":("Consolidated research record",None)
}
for idx, sec in enumerate(pages):
    pid = sec.get("data-page")
    phase = ("Front door" if pid=="start" else "Property" if pid in {"snapshot","maps"} else "Strategy" if pid in {"options","housefirst","calculator"} else
             "Execution" if pid in {"firsttimer","boundary","yesnow","documents","team","subdivide"} else "Financial / exit" if pid in {"mortgage","roadmap","myplan","scripts"} else "Reference")
    if not sec.find("div", class_="section-tools", recursive=False):
        sec.insert(0, BeautifulSoup(f'<div class="section-tools no-print"><span class="st-title">{phase}</span><span class="st-count">{idx+1:02d} / {len(pages):02d}</span><span class="st-grow"></span><button onclick="goPage(\'start\')">Dashboard</button><button onclick="printPage(\'{pid}\')">Print this section</button></div>', "html.parser").div)
    if not sec.find("div", class_="page-bottom-nav", recursive=False):
        prev_id = page_ids[idx-1] if idx else None; next_id = page_ids[idx+1] if idx < len(pages)-1 else None
        prev_title = pages[idx-1].get("data-title") if idx else ""; next_title = pages[idx+1].get("data-title") if next_id else ""
        prev_btn = f'<button onclick="goPage(\'{prev_id}\')">← {prev_title}</button>' if prev_id else "<span></span>"
        next_btn = f'<button onclick="goPage(\'{next_id}\')">{next_title} →</button>' if next_id else '<button onclick="goPage(\'start\')">Back to dashboard ↑</button>'
        sec.append(BeautifulSoup(f'<div class="page-bottom-nav no-print">{prev_btn}<div class="center">MASTER COMPLETE · section {idx+1} of {len(pages)}</div>{next_btn}</div>', "html.parser").div)

for pid, (label, href) in doc_pages.items():
    sec = soup.find("section", attrs={"data-page":pid})
    if not sec or sec.find("div", class_="doc-ribbon"): continue
    anchor = sec.find("p", class_="lead") or sec.find("div", class_="page-title")
    dl = f'<a href="{href}" download>Download DOCX</a>' if href else ""
    rib = BeautifulSoup(f'<div class="doc-ribbon no-print"><div class="doc-icon">▤</div><div class="doc-copy"><b>{label}</b><small>Print only this document/section without printing the full Powerhouse.</small></div>{dl}<button onclick="toggleArchives(\'{pid}\',true)">Expand</button><button onclick="toggleArchives(\'{pid}\',false)">Collapse</button><button class="print" onclick="printPage(\'{pid}\')">Print document</button></div>', "html.parser").div
    if anchor: anchor.insert_after(rib)

# Group navigation.
js = js + "\n" + neg_js
old_nav = """const nav=document.getElementById('nav');
pages.forEach((p,i)=>{const b=document.createElement('button');b.dataset.target=p[0];b.innerHTML=`<span class="num">${String(i+1).padStart(2,'0')}</span><span>${p[1]}</span><span class="dot"></span>`;b.onclick=()=>goPage(p[0]);nav.appendChild(b)});"""
new_nav = """const nav=document.getElementById('nav');
const navGroups=[['OWNER ACTION',['start','firsttimer','yesnow']],['PROPERTY',['snapshot','maps','boundary']],['MONEY & EXIT',['options','housefirst','calculator','mortgage','roadmap','myplan']],['EXECUTION',['documents','team','subdivide','scripts']],['PACKETS & REFERENCE',['diligence','giftfull','samedayfull','paidfull','paidpacket','reportarchive','sources']]];
const pageMap=Object.fromEntries(pages.map((p,i)=>[p[0],{p,i}]));
navGroups.forEach(([group,ids])=>{const g=document.createElement('div');g.className='nav-group ui-group';g.textContent=group;nav.appendChild(g);ids.forEach(id=>{const item=pageMap[id];if(!item)return;const {p,i}=item;const b=document.createElement('button');b.dataset.target=p[0];b.innerHTML=`<span class="num">${String(i+1).padStart(2,'0')}</span><span>${p[1]}</span><span class="dot"></span>`;b.onclick=()=>goPage(p[0]);nav.appendChild(b)})});"""
js = js.replace(old_nav, new_nav)

ui_js = r"""
function activePageId(){const p=document.querySelector('.page.active');return p?p.dataset.page:'start'}
function printCurrent(){printPage(activePageId())}
function printPage(id){
 const sec=document.querySelector(`.page[data-page="${id}"]`);if(!sec)return;
 const closed=[...sec.querySelectorAll('details.archive')].filter(d=>!d.open);closed.forEach(d=>d.open=true);
 document.body.classList.add('print-one');sec.classList.add('print-target');
 const cleanup=()=>{document.body.classList.remove('print-one');sec.classList.remove('print-target');closed.forEach(d=>d.open=false);window.removeEventListener('afterprint',cleanup)};
 window.addEventListener('afterprint',cleanup);setTimeout(()=>window.print(),70);setTimeout(()=>{if(document.body.classList.contains('print-one'))cleanup()},60000);
}
function toggleArchives(id,open){const sec=document.querySelector(`.page[data-page="${id}"]`);if(sec)sec.querySelectorAll('details.archive').forEach(d=>d.open=open)}
function toggleFocus(){document.body.classList.toggle('focus-mode');try{localStorage.setItem('av1011focus',document.body.classList.contains('focus-mode')?'1':'0')}catch(e){}}
function goNextPage(){const id=activePageId(),i=pages.findIndex(p=>p[0]===id);goPage(pages[(i+1)%pages.length][0])}
function goPrevPage(){const id=activePageId(),i=pages.findIndex(p=>p[0]===id);goPage(pages[(i-1+pages.length)%pages.length][0])}
let _searchIndex=null;
function buildSearchIndex(){return pages.map(p=>{const s=document.querySelector(`.page[data-page="${p[0]}"]`);return{id:p[0],title:p[1],text:(s?s.innerText:'').replace(/\s+/g,' ').trim()}})}
function openSearch(){document.getElementById('siteSearchModal').classList.add('open');const i=document.getElementById('siteSearchInput');i.value='';renderSearch('');setTimeout(()=>i.focus(),40)}
function closeSearch(){document.getElementById('siteSearchModal').classList.remove('open')}
function renderSearch(q){
 if(!_searchIndex)_searchIndex=buildSearchIndex();const box=document.getElementById('siteSearchResults');q=(q||'').trim().toLowerCase();
 const rows=!q?_searchIndex.slice(0,10):_searchIndex.filter(r=>r.title.toLowerCase().includes(q)||r.text.toLowerCase().includes(q)).slice(0,18);
 if(!rows.length){box.innerHTML='<div class="search-empty">No matching section found.</div>';return}
 box.innerHTML=rows.map(r=>{let snip='';if(q){const low=r.text.toLowerCase(),i=low.indexOf(q),st=Math.max(0,i-90),en=Math.min(r.text.length,(i<0?0:i)+q.length+150);snip=i>=0?(st>0?'…':'')+r.text.slice(st,en)+(en<r.text.length?'…':''):r.text.slice(0,220)+'…'}else snip=r.text.slice(0,180)+'…';return `<div class="search-hit" data-id="${r.id}"><b>${r.title}</b><small>${snip.replace(/</g,'&lt;')}</small></div>`}).join('');
 box.querySelectorAll('.search-hit').forEach(el=>el.onclick=()=>{closeSearch();goPage(el.dataset.id)});
}
document.getElementById('siteSearchInput')?.addEventListener('input',e=>renderSearch(e.target.value));
document.addEventListener('keydown',e=>{if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){e.preventDefault();openSearch()}if(e.key==='Escape'&&document.getElementById('siteSearchModal')?.classList.contains('open'))closeSearch();if(e.altKey&&e.key==='ArrowRight')goNextPage();if(e.altKey&&e.key==='ArrowLeft')goPrevPage()});
try{if(localStorage.getItem('av1011focus')==='1')document.body.classList.add('focus-mode')}catch(e){}
"""
pos = js.find("const bytecasts=")
if pos >= 0:
    js = js[:pos] + ui_js + "\n" + js[pos:]
else:
    js += "\n" + ui_js
script.string = js

PATH.write_text(str(soup), encoding="utf-8")

# QA guarantees.
qa = BeautifulSoup(PATH.read_text(encoding="utf-8"), "html.parser")
assert len(qa.find_all("section", class_="page")) == 23
assert qa.find("iframe") is None
assert qa.find("section", attrs={"data-page":"paidpacket"}) is not None
assert qa.find("div", class_="dashboard-hub") is not None
assert qa.find(id="siteSearchModal") is not None
assert "function printPage" in qa.find("script").get_text()
print(f"Enhanced {PATH}: {PATH.stat().st_size} bytes / 23 sections")
