from pathlib import Path
from bs4 import BeautifulSoup

SRC = Path('AV_1011_N_B_ST_HOMEOWNER_EXIT_POWERHOUSE_MASTER_COMPLETE_2026-09-15.html')
OUT = Path('index.html')

html = SRC.read_text(encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')

soup.title.string = 'AeroVista · 1011 N B St · Homeowner Exit Powerhouse'
meta = soup.new_tag('meta')
meta['name'] = 'description'
meta['content'] = ('AeroVista homeowner decision and action guide for 1011 N B Street: '
                   'property research, boundary strategy, exit options, calculators, Bytecast briefings, '
                   'documents, scripts, subdivision workflow and diligence.')
soup.head.append(meta)

style = soup.find('style')
style.string = (style.string or '') + r'''
/* Owner Command Center enhancements folded directly into the Powerhouse */
.mission-bar{margin:18px 0 0;border:1px solid #3a766e;background:linear-gradient(90deg,rgba(89,224,196,.11),rgba(121,169,255,.06));padding:14px 16px;border-radius:15px;font-size:15px}.mission-bar b{color:#a6f5e6}
.command-metrics{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin-top:16px}.command-metric{border:1px solid var(--line);background:rgba(8,21,34,.72);border-radius:14px;padding:13px}.command-metric .v{font-size:24px;font-weight:950;letter-spacing:-.035em;margin:2px 0}.command-metric small{color:var(--muted)}
.command-status{display:flex;gap:8px;flex-wrap:wrap;margin:15px 0}.command-status span{display:inline-flex;align-items:center;border-radius:999px;padding:6px 9px;font-size:11px;font-weight:850;border:1px solid}.command-status .urgent-state{color:#ffb1b1;background:rgba(255,123,123,.08);border-color:rgba(255,123,123,.30)}.command-status .open-state{color:#ffdda0;background:rgba(255,201,102,.07);border-color:rgba(255,201,102,.30)}.command-status .good-state{color:#a9f1bd;background:rgba(114,220,146,.07);border-color:rgba(114,220,146,.28)}
.command-road{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:12px 0 20px}.command-road .cr{border:1px solid var(--line);border-radius:15px;background:#0b1828;padding:15px}.command-road .cr i{font-style:normal;width:32px;height:32px;border-radius:50%;display:grid;place-items:center;background:#17324d;color:#a9d7ff;font-weight:950;margin-bottom:8px}.command-road .cr b{display:block;font-size:15px}.command-road .cr small{color:var(--muted)}
.quick-actions{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:12px 0 20px}.quick-action{border:1px solid #31536a;border-radius:15px;padding:15px;background:linear-gradient(180deg,#10243a,#0b1828);cursor:pointer;text-align:left;color:white}.quick-action:hover{border-color:#6c91ad;transform:translateY(-1px)}.quick-action b{display:block;font-size:15px}.quick-action small{display:block;color:#9fb1c4;margin-top:3px}.quick-action.primary{background:linear-gradient(135deg,#2fc5a8,#448fe3);color:#04101a;border:0}.quick-action.primary small{color:#0a2d3c}
.bytecast{border:1px solid #3b5e78;background:radial-gradient(circle at 86% 0,rgba(121,169,255,.12),transparent 34%),linear-gradient(135deg,#0f2236,#0a1828);border-radius:20px;padding:19px;margin:18px 0;box-shadow:0 16px 45px rgba(0,0,0,.15)}.byte-head{display:flex;align-items:center;gap:13px}.byte-icon{width:56px;height:56px;border-radius:16px;background:linear-gradient(145deg,var(--teal),var(--blue));display:grid;place-items:center;flex:0 0 auto}.byte-bars{display:flex;align-items:center;gap:3px;height:22px}.byte-bars i{display:block;width:3px;background:#05202a;border-radius:4px;animation:bpulse 1.1s ease-in-out infinite}.byte-bars i:nth-child(1){height:8px}.byte-bars i:nth-child(2){height:18px;animation-delay:.12s}.byte-bars i:nth-child(3){height:12px;animation-delay:.24s}.byte-bars i:nth-child(4){height:20px;animation-delay:.36s}.byte-bars i:nth-child(5){height:10px;animation-delay:.48s}@keyframes bpulse{0%,100%{transform:scaleY(.65)}50%{transform:scaleY(1.05)}}.byte-head h3{margin:0;font-size:21px}.byte-chapters{display:flex;gap:8px;flex-wrap:wrap;margin:13px 0}.byte-chapter{border:1px solid var(--line);background:#0b1828;color:#dcecff;border-radius:999px;padding:7px 10px;cursor:pointer}.byte-chapter.active{border-color:#4f8b82;background:rgba(89,224,196,.10);color:#aaf6e7}.byte-controls{display:flex;align-items:center;gap:8px;flex-wrap:wrap}.byte-controls button{border:1px solid #3d5e79;background:#10243a;color:white;border-radius:10px;padding:8px 11px;cursor:pointer}.byte-controls .play{background:linear-gradient(135deg,#2fc5a8,#448fe3);border:0;color:#04101a;font-weight:850}.byte-transcript{margin-top:12px;color:#aebed0;font-size:13px;max-height:0;overflow:hidden;transition:max-height .24s ease}.byte-transcript.open{max-height:330px;overflow:auto;border-top:1px solid var(--line);padding-top:11px}
.listen-strip{display:flex;align-items:center;gap:11px;border:1px solid #34576e;background:linear-gradient(90deg,rgba(89,224,196,.08),rgba(121,169,255,.05));border-radius:13px;padding:11px 13px;margin:13px 0}.listen-strip .listen-ico{width:36px;height:36px;display:grid;place-items:center;border-radius:10px;background:#16334b;color:#aef6e8;font-weight:950}.listen-strip .listen-copy{flex:1}.listen-strip .listen-copy b{display:block}.listen-strip .listen-copy small{color:var(--muted)}
.stage-strip{margin:13px 0 17px}.stage-label{display:flex;justify-content:space-between;gap:10px;color:var(--muted);font-size:11px}.stage-track{height:8px;background:#172b42;border-radius:999px;overflow:hidden;margin-top:7px}.stage-track span{display:block;height:100%;width:25%;background:linear-gradient(90deg,var(--teal),var(--blue))}
@media(max-width:980px){.command-metrics{grid-template-columns:repeat(2,1fr)}.command-road,.quick-actions{grid-template-columns:1fr 1fr}}@media(max-width:640px){.command-metrics,.command-road,.quick-actions{grid-template-columns:1fr}.byte-head{align-items:flex-start}}@media print{.quick-actions,.byte-controls,.byte-chapters,.listen-strip{display:none!important}.byte-transcript{max-height:none!important;overflow:visible!important}}
'''

start = soup.find('section', attrs={'data-page':'start'})
start['data-title'] = 'Owner Dashboard'
hero = start.find('div', class_='hero')
hero.find('h1').string = 'Your property exit plan, in one place.'
lead = hero.find('p', class_='lead')
lead.string = ('This is your decision book. You can carry the property for now with roommates / short-term income, '
               'but you do not want to keep feeding the mortgage long term. The goal is a controlled exit within roughly '
               'the next year while preserving equity and avoiding a capital-heavy development project.')

decision = hero.find('div', class_='decision')
if decision:
    lab = decision.find('div', class_='label')
    if lab: lab.string = 'Current AeroVista research recommendation'
    big = decision.find('div', class_='big')
    if big:
        big.clear(); big.append(BeautifulSoup('Prove the split. If it is real, test selling the <u>house side first</u> and keeping the vacant buildable lot.','html.parser'))
    sm = decision.find('div', class_='small')
    if sm: sm.string = ('That route can eliminate the mortgage completely while leaving you with a debt-free land asset. '
                         'Selling the empty half first may reduce principal without necessarily reducing the scheduled monthly payment.')

hero.append(BeautifulSoup('''<div class="mission-bar"><b>Current mission:</b> secure 1007’s cooperation before that property changes hands, then prove the frontage / split opportunity with the least possible cash.</div><div class="stage-strip"><div class="stage-label"><span>Current planning stage</span><span>1 of 4 · secure cooperation</span></div><div class="stage-track"><span></span></div></div><div class="command-metrics"><div class="command-metric"><div class="label">Property</div><div class="v">~11,633 sf</div><small>1911 home · ~1,320 sf · APN C3510003001A</small></div><div class="command-metric"><div class="label">Working geometry</div><div class="v">~99' × 117.5'</div><small>Strong reconstruction; licensed survey controls.</small></div><div class="command-metric"><div class="label">Leverage point</div><div class="v">~1' × 30'</div><small>Front-only BLA concept before the 1007 garage area.</small></div><div class="command-metric"><div class="label">Working debt</div><div class="v">$300k–$400k</div><small>Planning assumption; replace with current lender payoff.</small></div></div>''','html.parser'))
hero.insert_after(BeautifulSoup('''<div class="command-status"><span class="urgent-state">1007 actively marketed</span><span class="open-state">Survey / City gate still open</span><span class="good-state">Low-capital proof strategy</span></div>''','html.parser'))

cards = start.select('.grid > .card')
if len(cards)>=3:
    c=cards[0]; c.find('div',class_='label').string='Your immediate objective'; c.find('div',class_='kpi').string='Capture → prove'; c.find('p').string='Get the 1007 cooperation captured, then buy only the survey/title/City information needed to decide whether the split is real.'
    c=cards[1]; c.find('div',class_='label').string='What must be proven'; c.find('div',class_='kpi').string='100.00 ft'; c.find('p').string='Survey-grade frontage plus a City interpretation that supports the future two-lot geometry. Until then, the split remains a strategy hypothesis.'
    c=cards[2]; c.find('div',class_='label').string='The low-cost leverage point'; c.find('div',class_='kpi').string="~1' × 30'"; c.find('p').string='A front-only boundary adjustment may solve the frontage bottleneck while leaving the existing line near the 1007 garage untouched.'

block = BeautifulSoup('''<h2>Your decision sequence</h2><div class="command-road"><div class="cr"><i>1</i><b>Capture cooperation</b><small>Ask for the front-only gift. If 1007 says yes, sign cooperation + survey access that day.</small></div><div class="cr"><i>2</i><b>Prove the geometry</b><small>Survey + title + written City direction. Stop if frontage, structures, lender, title or City treatment fails.</small></div><div class="cr"><i>3</i><b>Re-price the exits</b><small>Get current BPOs for whole, house-side, vacant-side and whole-with-proven-feasibility.</small></div><div class="cr"><i>4</i><b>Choose the exit</b><small>Use the least expensive path that actually solves the mortgage problem while preserving equity.</small></div></div><h2>What do you need right now?</h2><div class="quick-actions no-print"><button class="quick-action primary" onclick="goPage('firsttimer')"><b>Walk me through this</b><small>Start with the first-time homeowner execution guide.</small></button><button class="quick-action" onclick="goPage('yesnow')"><b>1007 just said YES</b><small>Open the same-day capture checklist.</small></button><button class="quick-action" onclick="goPage('calculator')"><b>Run my numbers</b><small>Change debt, values, sale friction and diligence costs.</small></button><button class="quick-action" onclick="goPage('maps')"><b>Show me the geometry</b><small>See the aerials, parcel reconstruction and one-foot issue.</small></button></div>''','html.parser')
callouts = start.find_all('div', class_=lambda x: x and 'callout' in x.split())
if callouts: callouts[-1].insert_before(block)
else: start.append(block)

byte = BeautifulSoup('''<div class="bytecast" id="bytecast"><div class="byte-head"><div class="byte-icon"><span class="byte-bars"><i></i><i></i><i></i><i></i><i></i></span></div><div><div class="eyebrow">Bytecast · owner briefing</div><h3 id="byteTitle">The 1011 big picture</h3><div class="small" id="byteMeta">~2 minute briefing · browser narration</div></div></div><div class="byte-chapters no-print"><button class="byte-chapter active" data-byte="overview" onclick="selectBytecast('overview')">01 · Big picture</button><button class="byte-chapter" data-byte="yes" onclick="selectBytecast('yes')">02 · If 1007 says yes</button><button class="byte-chapter" data-byte="money" onclick="selectBytecast('money')">03 · Money strategy</button><button class="byte-chapter" data-byte="firstweek" onclick="selectBytecast('firstweek')">04 · Your first week</button></div><div class="byte-controls no-print"><button class="play" id="bytePlay" onclick="playBytecast()">▶ Play briefing</button><button onclick="pauseBytecast()">Pause</button><button onclick="stopBytecast()">Stop</button><button onclick="toggleByteTranscript()">Transcript</button><span class="small">Uses a natural voice available on your device.</span></div><div class="byte-transcript" id="byteTranscript"></div></div>''','html.parser')
qa = start.find('div',class_='quick-actions')
if qa: qa.insert_after(byte)

def listen(page_id,key,title,detail):
    sec=soup.find('section',attrs={'data-page':page_id})
    if not sec:return
    strip=BeautifulSoup(f'''<div class="listen-strip no-print"><div class="listen-ico">▶</div><div class="listen-copy"><b>{title}</b><small>{detail}</small></div><button class="btn" onclick="goPage('start');setTimeout(function(){{selectBytecast('{key}');document.getElementById('bytecast').scrollIntoView({{behavior:'smooth'}})}},120)">Listen</button></div>''','html.parser')
    lead=sec.find('p',class_='lead'); (lead or sec.find('div',class_='page-title')).insert_after(strip.div)
listen('yesnow','yes','Hear the same-day YES briefing','Use this before you start signing, scanning, notifying the broker or ordering work.')
listen('housefirst','money','Hear the money-strategy briefing','Why house-side-first currently leads and when vacant-lot-first could still work.')
listen('firsttimer','firstweek','Hear your first-week briefing','A first-time-owner sequence for the neighbor agreement, survey, title and City questions.')

for page_id,html_snip in {
'documents':'<div class="callout gold"><b>Your document-order rule:</b> use the lightest document that matches the stage. The same-day agreement captures intent and cooperation. The survey defines the land. City/title/lender clearance establishes whether the conveyance can close. The final warranty deed transfers the approved area. A notary does not eliminate those steps.</div>',
'roadmap':'<div class="callout"><b>Where you are now:</b> Stage 1 — secure 1007 cooperation and immediately launch survey/title. Do not treat this as a subdivision project until the preliminary survey and written City answers justify Stage 2 spending.</div>',
'team':'<div class="notice"><b>AeroVista does not act for 1007 and does not sign for you.</b> AV organizes the research, strategy, scripts, working drafts and decision gates; you hire and direct the surveyor, title/escrow, attorney, broker, lender and CPA.</div>'}.items():
    sec=soup.find('section',attrs={'data-page':page_id})
    if sec:
        lead=sec.find('p',class_='lead');
        if lead: lead.insert_after(BeautifulSoup(html_snip,'html.parser').div)
my=soup.find('section',attrs={'data-page':'myplan'})
if my:
    t=my.find('div',class_='page-title')
    if t:t.insert_after(BeautifulSoup('<div class="callout"><b>Your default posture today:</b> this is a <b>proof project</b>, not a construction project and not yet a full subdivision project. Your next dollar should buy information that changes a decision.</div>','html.parser').div)

brand=soup.select_one('.brand span')
if brand: brand.string='1011 Owner Exit Powerhouse'
crumb=soup.find(id='crumb')
if crumb: crumb.string='Owner Dashboard'

script=soup.find('script')
js=script.get_text().replace("['start','Start Here']","['start','Owner Dashboard']")
byte_js=r'''
const bytecasts={overview:{title:'The 1011 big picture',meta:'~2 minute briefing · browser narration',text:`Here is the big picture. You own 1011 North B Street, and the goal is not to turn you into a developer. The goal is to spend a relatively small amount of money to prove whether your property has a stronger exit than simply selling it as one ordinary house and lot. Public-record reconstruction strongly suggests the parcel is about ninety-nine feet wide instead of the roughly one hundred feet that could support two conventional fifty-foot-frontage lots. The missing width appears connected to the south one foot of original Lot 2 that is now associated with 1007. The working strategy is a small front-only boundary adjustment, roughly one foot by thirty feet, that returns to the existing line before the neighbor's garage. If a licensed survey and the City confirm that this creates recognized frontage and a workable future split, the property becomes a different financial asset. At that point, you do not automatically finish every development step. You price the choices. The leading outcome is to test selling the house-side parcel, paying the existing mortgage off at closing, and retaining the vacant buildable lot. If the split is not clean, stop spending and sell the documented R-12 upside instead. The core rule is simple: buy certainty, not construction.`},yes:{title:'If 1007 says yes',meta:'~2 minute same-day checklist · browser narration',text:`If 1007 says yes, treat that as a time-sensitive event because the property is already being marketed. First, confirm exactly what yes means: they are willing to gift the small front area if the survey, City, title and lender work show that it does not create a material problem for their property. Second, fill out and sign the conditional boundary gift and active-sale cooperation agreement. Sign the survey-access authorization at the same meeting. If a notary is conveniently available, you can acknowledge the cooperation agreement, but do not use a blank deed or a guessed legal description. Third, scan every signed page and give both sides a complete copy. Fourth, notify the listing agent that a minor boundary-adjustment process is pending. The house can remain for sale; the goal is simply to prevent a buyer or title company from being surprised. Fifth, order the rush survey and open title immediately. If 1007 accepts an offer before the boundary adjustment records, coordinate either completion before their closing or a written buyer-assumption path. The deed comes later, after the surveyor has created the legal description and City, title and any lender conditions have been cleared.`},money:{title:'The money strategy',meta:'~2 minute exit comparison · browser narration',text:`The biggest strategic question is which side to sell first if the split works. Selling the vacant lot sounds intuitive because it feels like selling extra land while keeping your home. The problem is the mortgage. A lender can require a partial release and may require much of the vacant-lot sale proceeds to be applied to principal. A large principal payment does not necessarily lower the scheduled monthly payment unless the lender allows a recast or you refinance. That can leave you with the same house, ongoing maintenance and a payment that is still too high. Selling the house-side parcel can be cleaner. If the sale proceeds are enough to satisfy the mortgage in full, escrow can retire the debt and coordinate the releases while you retain the vacant parcel. That can produce a clean break from the monthly mortgage plus a debt-free land asset and possibly cash at closing. This is still a strategy hypothesis, not an appraisal. Before choosing, get current broker price opinions for the whole property, the future house-side parcel, the future vacant parcel and the whole property with proven split feasibility. Then get the mortgage servicer's payoff, partial-release and recast rules in writing.`},firstweek:{title:'Your first week',meta:'~2 minute first-time-owner briefing · browser narration',text:`If this is your first land and title transaction, keep the first week simple. Before the neighbor conversation, have your government ID, the same-day cooperation agreement, survey-access page, listing-agent notice, a phone scanner, two or three surveyor contacts, a title-company contact and a private spending ceiling. Ask 1007 friend to friend. If they say yes, sign the cooperation and access documents, scan them, notify the listing agent and call the surveyor and title company immediately. If the gift is declined, use the paid fallback only if you have decided in advance that you are willing to pay and you know your ceiling. Your surveyor's first job is not to design houses. It is to prove exact frontage, the common boundary, nearby structures, the proposed front-only adjustment, access, easements and the conceptual future split. Open title on both parcels at the same time. When you have the preliminary survey exhibit, take the two decisive geometry questions to Coeur d'Alene Planning or Engineering and preserve the answer in writing. Do not pay for the next stage until the current stage has answered the question that justifies it.`}};
let currentByte='overview',byteUtter=null;
function selectBytecast(key){if(!bytecasts[key])return;currentByte=key;document.getElementById('byteTitle').textContent=bytecasts[key].title;document.getElementById('byteMeta').textContent=bytecasts[key].meta;document.getElementById('byteTranscript').textContent=bytecasts[key].text;document.querySelectorAll('.byte-chapter').forEach(b=>b.classList.toggle('active',b.dataset.byte===key));stopBytecast();}
function preferredVoice(){if(!('speechSynthesis' in window))return null;const v=speechSynthesis.getVoices();return v.find(x=>/^en-US/i.test(x.lang)&&/natural|premium|enhanced|google|microsoft/i.test(x.name))||v.find(x=>/^en-US/i.test(x.lang))||v.find(x=>/^en/i.test(x.lang))||v[0];}
function playBytecast(){if(!('speechSynthesis' in window)){alert('Browser narration is not available here. Open the transcript instead.');return}if(speechSynthesis.paused){speechSynthesis.resume();document.getElementById('bytePlay').textContent='▶ Playing';return}speechSynthesis.cancel();byteUtter=new SpeechSynthesisUtterance(bytecasts[currentByte].text);byteUtter.rate=.96;const v=preferredVoice();if(v)byteUtter.voice=v;byteUtter.onstart=()=>document.getElementById('bytePlay').textContent='▶ Playing';byteUtter.onend=()=>document.getElementById('bytePlay').textContent='▶ Play briefing';speechSynthesis.speak(byteUtter);}
function pauseBytecast(){if('speechSynthesis' in window&&speechSynthesis.speaking){speechSynthesis.pause();document.getElementById('bytePlay').textContent='▶ Resume'}}
function stopBytecast(){if('speechSynthesis' in window)speechSynthesis.cancel();const b=document.getElementById('bytePlay');if(b)b.textContent='▶ Play briefing';}
function toggleByteTranscript(){document.getElementById('byteTranscript').classList.toggle('open')}
if('speechSynthesis' in window)speechSynthesis.onvoiceschanged=()=>preferredVoice();selectBytecast('overview');
'''
script.string=js.rstrip()+'\n\n'+byte_js+'\n'

OUT.write_text(str(soup),encoding='utf-8')

qa=BeautifulSoup(OUT.read_text(encoding='utf-8'),'html.parser')
assert len(qa.find_all('section',class_='page'))==22
assert qa.find('iframe') is None
assert qa.find(id='bytecast') is not None
assert qa.find('section',attrs={'data-page':'start'}).get('data-title')=='Owner Dashboard'
print(f'Built {OUT} ({OUT.stat().st_size} bytes)')
