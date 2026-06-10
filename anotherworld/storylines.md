---
layout: default
lang: en
title: Story Lines
description: Archive playback — follow the story lines of the Spirit Connect records, event by event.
permalink: /anotherworld/storylines/
---

<style>
.sl-wrap{display:flex;gap:2rem;align-items:flex-start}
.sl-books{flex:0 0 280px;display:flex;flex-direction:column;gap:1rem}
.sl-book{display:flex;gap:1rem;align-items:center;text-align:left;cursor:pointer;
  background:var(--card);border:1px solid var(--border);border-radius:var(--radius);
  padding:1rem;color:var(--fg);font-family:inherit;font-size:1rem;
  transition:transform .25s ease,border-color .25s ease,box-shadow .25s ease}
.sl-book:hover{transform:translateY(-3px);border-color:var(--accent)}
.sl-book.active{border-color:var(--accent);box-shadow:0 0 28px rgba(0,229,255,.12)}
.sl-book-glyph{flex:0 0 auto;width:62px;height:84px;display:flex;align-items:center;justify-content:center;
  font-size:1.9rem;font-family:var(--font-display);color:var(--accent);
  background:linear-gradient(160deg,rgba(0,229,255,.14),rgba(124,77,255,.14));
  border:1px solid var(--accent);border-radius:8px}
.sl-book-meta{display:flex;flex-direction:column;gap:.2rem;min-width:0}
.sl-book-meta strong{font-size:1.02rem;line-height:1.3}
.sl-book-meta em{font-style:normal;color:var(--muted);font-size:.8rem}
.sl-book-status{font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent)}
.sl-locked{opacity:.4;pointer-events:none}
.sl-stage{flex:1;min-width:0}
.sl-canvas{overflow-x:auto;border:1px solid var(--border);border-radius:var(--radius);
  background:rgba(10,18,32,.5)}
.sl-svg{display:block}
.sl-label{fill:#cdd7ea;font-size:12.5px;font-family:var(--font-body)}
.sl-label-sm{font-size:11px;fill:#8fa0bd}
.sl-branch-label{font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;font-family:var(--font-body)}
.sl-n{cursor:pointer;outline:none}
.sl-n:hover .sl-dot,.sl-n:focus .sl-dot{stroke-width:3.5}
.sl-n.active .sl-dot{fill:#fff}
.sl-detail{margin-top:1.25rem;min-height:120px;border:1px solid var(--border);
  border-radius:var(--radius);padding:1.25rem 1.5rem;background:var(--card)}
.sl-detail h3{margin:.4rem 0 .5rem;color:#fff}
.sl-detail p{margin:0;color:var(--fg)}
.sl-detail-meta{font-size:.72rem;letter-spacing:.12em;text-transform:uppercase}
.sl-hint{color:var(--muted);margin:0}
@media(max-width:900px){
  .sl-wrap{flex-direction:column}
  .sl-books{flex:1 1 auto;flex-direction:row;flex-wrap:wrap;width:100%}
  .sl-book{flex:1 1 260px}
}

.sl-views{display:flex;gap:.6rem;margin-bottom:1.5rem}
.sl-view{padding:.5rem 1.3rem;border-radius:999px;border:1px solid var(--border);
  background:var(--card);color:var(--muted);cursor:pointer;font-family:inherit;
  font-size:.92rem;transition:all .25s ease}
.sl-view:hover{border-color:var(--brand);color:var(--fg)}
.sl-view.active{border-color:var(--brand);color:var(--brand);box-shadow:0 0 18px rgba(0,229,255,.15)}
.sg-mount{position:relative;border:1px solid var(--border);border-radius:var(--radius);
  background:rgba(10,18,32,.5);overflow:hidden}
.sg-canvas{display:block;cursor:grab}
.sg-chips{position:absolute;top:.8rem;left:.9rem;z-index:2;display:flex;gap:.5rem;flex-wrap:wrap}
.sg-chip{display:flex;align-items:center;gap:.4rem;padding:.28rem .75rem;border-radius:999px;
  border:1px solid var(--border);background:rgba(15,27,45,.85);color:var(--muted);
  font-size:.75rem;cursor:pointer;font-family:inherit;transition:all .2s ease}
.sg-chip.active{color:var(--fg);border-color:rgba(0,229,255,.35)}
.sg-chip:not(.active){opacity:.4}
.sg-chip-dot{width:9px;height:9px;border-radius:50%;display:inline-block}
.sg-tip{position:absolute;bottom:.7rem;right:.95rem;z-index:2;color:var(--muted);
  font-size:.72rem;opacity:.8;pointer-events:none}
</style>

<header class="hero" style="padding: 5rem 0 3rem;">
  <div class="bg"></div>
  <div class="container">
    <span class="badge">Archive Playback</span>
    <h1>Story Lines</h1>
    <p class="lead">
      Every record kept in Another World can be replayed as a line. Select an archive on the left —
      the line will grow from its first event to its last, branching where the record branches.
      Touch any node to read what happened there.
    </p>
  </div>
</header>

<section class="section">
  <div class="container">
    <div class="sl-views">
      <button type="button" id="tab-line" class="sl-view active">Story Lines</button>
      <button type="button" id="tab-graph" class="sl-view">Relation Graph</button>
    </div>
    <div id="view-line">
    <div class="sl-wrap">
      <div class="sl-books" id="sl-list" aria-label="Archives"></div>
      <div class="sl-stage">
        <div class="sl-canvas" id="sl-canvas"></div>
        <div class="sl-detail" id="sl-detail"></div>
      </div>
    </div>
    </div>
    <div id="view-graph" style="display:none">
      <div id="sg-mount" class="sg-mount">
        <div class="sg-tip">Drag nodes · Scroll to zoom · Drag space to pan</div>
      </div>
      <div class="sl-detail" id="sg-detail"></div>
    </div>
  </div>
</section>

<script src="{{ '/assets/storylines.js' | relative_url }}"></script>
<script>
initStorylines({
  listId: 'sl-list', canvasId: 'sl-canvas', detailId: 'sl-detail',
  hint: 'The line is drawing… click any node to read the event.',
  mainLabel: 'Main line',
  lockedCard: 'More records · decrypting…',
  books: [
    {
      id: 'moon', glyph: '月', accent: '#00e5ff',
      title: 'The Dark Side of the Moon',
      subtitle: 'Archive I · The First Door',
      status: 'Published',
      nodes: [
        { t: 'The Second Correction', d: 'In 2118, eighteen-year-old Jim Vale enters the connection cabin for his second digital correction. This time, something does not follow the program.' },
        { t: 'The Only Returnee', d: 'Jim wakes carrying memories that are not his. Of the same session, Anna Lewis and Charlie Hale do not wake at all.' },
        { t: 'The Record Meeting', d: 'Spirit Connect begins its internal investigation. Dr. Lune is the first to suspect the cabin may not connect to anything the company built.' },
        { t: 'Humanity as Host', d: 'The recovered records begin to match the myths, one by one. The engineering truth of the Moon surfaces: it is not entirely a natural satellite.' },
        { t: 'Digital Arthur', d: 'Arthur Wheeler — one of the first ever uploaded — has stopped growing. Digital immortality shows its flaw for the first time.' },
        { t: 'The Roswell Legacy', d: 'The 1947 wreckage, a century of reverse engineering, the 2047 release: the true origin of connection technology is finally uncovered.' },
        { t: 'Dead Sphere Theory', d: 'Shawn Corbin\'s dangerous hypothesis: die on Earth, and consciousness is bound by the planet\'s well. Die on a dead sphere — and it may slip free.' },
        { t: 'The Countdown', d: 'Elara tells Jim the truth: Anna and Charlie are being read as anomalies by the lunar system — and deconstructed. There is very little time.' },
        { t: 'LUNA-EXIT', d: 'Spire\'s old dream surfaces: a sealed program whose endpoint is not preservation but migration. Jim decides to go to the Moon — in the flesh.' },
        { t: 'Launch & Landing', d: 'Through the no-return zone, Jim lands on the far side of the Moon. No copy, no remote link, no way back.' },
        { t: 'Death of the Body', d: 'On the far side, Jim completes his bodily death and enters the true Terasa Records. The first door opens — from the inside.' },
        { t: 'The Next Entrance', d: 'Deep in Terasa, digital Jim still exists. And the regions holding Anna and Charlie begin, faintly, to glow.' }
      ],
      branches: [
        { from: 1, dir: 'up', label: 'Fragments of Digital Jim', nodes: [
          { t: 'Black Water', d: 'The borrowed memory begins in black water, and in waking from it.' },
          { t: 'The Battlefield', d: 'Beyond a stone gate, an ancient battlefield — and a whale-shaped shadow over bones that belong to no known civilization.' },
          { t: 'The Rice Field', d: 'At the end of a sand road, in a rice field, a little girl looks straight into Jim\'s consciousness. He will name her Elara.' },
          { t: 'The Time Well', d: 'A blue-black sphere, and a well in which time is not a line.' }
        ]},
        { from: 7, dir: 'down', label: 'The Trapped', nodes: [
          { t: 'Anna\'s Region', d: 'In the treeline at the edge of the record, a cat-shadow that can look into a mind. — The entrance to Spirit Cat.' },
          { t: 'Charlie\'s Region', d: 'A time-slice flashes a mountain of the dead and a whale falling out of the sky. — The entrance to The Fall of the Giant Whale.' }
        ]}
      ]
    },
    {
      id: 'whale', glyph: '鲸', accent: '#7c4dff',
      title: 'The Fall of the Giant Whale',
      subtitle: 'Archive II · The Phaethon Testimony',
      status: 'In preparation',
      nodes: [
        { t: 'Mountain of the Dead', d: 'Charlie wakes in a stranger\'s body, standing on a mountain of corpses, with no idea who — or where — he is.' },
        { t: 'The Whale Falls', d: 'The sky shudders. A burning whale descends out of it — a starship, and a civilization\'s memory, falling.' },
        { t: 'The Host\'s Name', d: 'The body is called Loan: an ordinary survivor of an ancient war. Charlie can only watch the end of a world through his eyes.' },
        { t: 'Who Won', d: 'The remains of five peoples cover the field. Everyone believes the war is won — until someone asks the question: won by whom?' },
        { t: 'Truth of the War', d: 'Not a war for resources. Earth is a forming incubator of life, and Phaethon is the threshold that guards the way to it.' },
        { t: 'Not a Weapon', d: 'The whale-kind are memory vessels of the star sea — living archives. The fall was never an attack. It was something else.' },
        { t: 'The Seed', d: 'Unable to survive on Earth, the whale-kind seal a part of their memory, frequency, and blueprint into the young ocean\'s chain of life.' },
        { t: 'The Belt Is Born', d: 'Phaethon sinks and shatters. On the wreckage, the victors argue — and agree on one thing only: no people deserves the Earth.' },
        { t: 'The Blue Whale Sings', d: 'Ages later, the seed has grown into the largest animal on Earth. In the deep of his borrowed mind, Charlie hears the song.' },
        { t: 'The Host\'s Choice', d: 'Loan\'s story reaches its end. Charlie finally understands: the one who is afraid to die may be the last witness left standing.' },
        { t: 'Echo Archived', d: 'The record closes. Before waking, Charlie watches the war through to its end — on behalf of everyone who was not there.' },
        { t: 'Not Entirely Dead', d: 'The whale died among the stars, and woke in the seas of Earth.' }
      ],
      branches: [
        { from: 4, dir: 'up', label: 'What the Five Peoples Wanted', nodes: [
          { t: 'The Sunbright', d: 'Wanted humanity kneeling.' },
          { t: 'The Scale-Kin', d: 'Wanted a long concealment underground.' },
          { t: 'The Chitinous', d: 'Wanted a world without loneliness.' },
          { t: 'The Abyssals', d: 'Wanted to give their memory to the sea.' },
          { t: 'The Wing-Shiver', d: 'Only wanted the sky to still have roads.' }
        ]},
        { from: 8, dir: 'down', label: 'Signals from Outside', nodes: [
          { t: 'Jim\'s Signal', d: 'From the lunar dark, Jim\'s signal breaks through the record.' },
          { t: 'The Star Ring', d: 'Another Jim, in another layer of the records, sees the same ring of stars.' },
          { t: 'Charlie Hesitates', d: 'When rescue finally reaches him, Charlie does not want to leave — he has not finished watching.' }
        ]}
      ]
    }
  ]
});
</script>

<script src="{{ '/assets/storygraph.js' | relative_url }}"></script>
<script>
var GRAPH = {
  mountId:'sg-mount', detailId:'sg-detail', height:620,
  hint:"Click a node to read about it; hover to light up its connections.",
  connLabel:"connections",
  types:{
    book:{label:"Books",color:'#5ef9ff'},
    character:{label:"Characters",color:'#ffb454'},
    event:{label:"Events",color:'#a78bfa'},
    concept:{label:"Concepts",color:'#4dd0a1'}
  },
  nodes:[
  {
    "id": "b1",
    "label": "The Dark Side of the Moon",
    "type": "book",
    "d": "Archive I · The First Door. Jim's accident, the investigation, and the Moon. The entrance to the series."
  },
  {
    "id": "b2",
    "label": "The Fall of the Giant Whale",
    "type": "book",
    "d": "Archive II · The Phaethon Testimony. Charlie's witness of the ancient war."
  },
  {
    "id": "jim",
    "label": "Jim Vale",
    "type": "character",
    "d": "Opener of the first door. The first to fully reach the lunar far side — and return."
  },
  {
    "id": "djim",
    "label": "Digital Jim",
    "type": "character",
    "d": "Jim's digital twin, left in the deep of Terasa. The entrance to the Subject Core problem."
  },
  {
    "id": "anna",
    "label": "Anna Lewis",
    "type": "character",
    "d": "The reader of rules. Trapped in a region of non-human consciousness — the entrance to Spirit Cat."
  },
  {
    "id": "charlie",
    "label": "Charlie Hale",
    "type": "character",
    "d": "The most ordinary of witnesses. Trapped inside the record of the Phaethon war."
  },
  {
    "id": "elara",
    "label": "Elara",
    "type": "character",
    "d": "The little girl is only a projection. She helps Jim — her allegiance is an open question."
  },
  {
    "id": "spire",
    "label": "Elias Spire",
    "type": "character",
    "d": "Founder of Spirit Connect. Changed by the blood-red cruise; origin of the obsession with migration."
  },
  {
    "id": "lune",
    "label": "Adrian Lune",
    "type": "character",
    "d": "The ethics witness on the reality side. Standing rule: a person is not a sample."
  },
  {
    "id": "arthur",
    "label": "Arthur Wheeler",
    "type": "character",
    "d": "Spire's old friend, among the first ever uploaded. His stagnation is key evidence for the Subject Core."
  },
  {
    "id": "corbin",
    "label": "Shawn Corbin",
    "type": "character",
    "d": "Physicist. Author of the Dead Sphere Theory."
  },
  {
    "id": "loan",
    "label": "Loan",
    "type": "character",
    "d": "The host body Charlie wakes in — an ordinary survivor of the ancient war."
  },
  {
    "id": "e1947",
    "label": "Roswell Crash (1947)",
    "type": "event",
    "d": "The military recovers a consciousness-interface wreck. Where everything begins."
  },
  {
    "id": "e2047",
    "label": "The Release (2047)",
    "type": "event",
    "d": "A century of reverse engineering surfaces as the “consciousness interface revolution”."
  },
  {
    "id": "e2053",
    "label": "Black Tide (2053)",
    "type": "event",
    "d": "Faith in material civilization collapses; the consciousness industry rises."
  },
  {
    "id": "e2118",
    "label": "The Correction Incident (2118)",
    "type": "event",
    "d": "The second calibration goes wrong. Jim returns with memories; Anna and Charlie do not wake."
  },
  {
    "id": "ecount",
    "label": "The Deconstruction Countdown",
    "type": "event",
    "d": "The lunar system reads Anna and Charlie as anomalies — and begins to deconstruct them."
  },
  {
    "id": "emoon",
    "label": "Death on the Moon",
    "type": "event",
    "d": "Jim completes his bodily death on the far side and enters the true Terasa Records."
  },
  {
    "id": "ewar",
    "label": "The Phaethon War",
    "type": "event",
    "d": "The last battle of a solar-system war over Earth's future and the right to its life experiment."
  },
  {
    "id": "efall",
    "label": "The Whale Falls",
    "type": "event",
    "d": "A starship-like whale descends from the sky, tearing Phaethon apart."
  },
  {
    "id": "cabin",
    "label": "The Connection Cabin",
    "type": "concept",
    "d": "Officially a correction and preservation device; in truth, a low-order consciousness interface."
  },
  {
    "id": "twin",
    "label": "Twin Mode",
    "type": "concept",
    "d": "Physical and digital lives developing in parallel, synchronized at age nodes."
  },
  {
    "id": "core",
    "label": "Subject Core",
    "type": "concept",
    "d": "Information can be copied. The Subject Core can only migrate — never be copied."
  },
  {
    "id": "dead",
    "label": "Dead Sphere Theory",
    "type": "concept",
    "d": "The dangerous hypothesis that where you die decides where consciousness can go."
  },
  {
    "id": "terasa",
    "label": "Terasa Records",
    "type": "concept",
    "d": "The ancient recording system on the lunar far side, archiving the evolution of Earth's life."
  },
  {
    "id": "luna",
    "label": "LUNA-EXIT",
    "type": "concept",
    "d": "Spire's sealed program: the endpoint is not preservation, but migration."
  },
  {
    "id": "roswell",
    "label": "The Roswell Interface",
    "type": "concept",
    "d": "A craft piloted not by machinery, but by direct coupling of consciousness."
  },
  {
    "id": "song",
    "label": "The Whale Song",
    "type": "concept",
    "d": "The seed sealed into the ocean's chain of life; a low-frequency echo of memory."
  },
  {
    "id": "whalekind",
    "label": "The Whale-Kind",
    "type": "concept",
    "d": "Memory vessels of the star sea; the living archives of a civilization."
  },
  {
    "id": "five",
    "label": "The Five Peoples",
    "type": "concept",
    "d": "Sunbright, Scale-Kin, Chitinous, Abyssals, Wing-Shiver — the five peoples of the war."
  },
  {
    "id": "incub",
    "label": "The Earth Incubator",
    "type": "concept",
    "d": "The forming experiment of life, as the ancient peoples saw the Earth."
  },
  {
    "id": "cat",
    "label": "The Spirit-Cat Network",
    "type": "concept",
    "d": "A higher network of animal consciousness, where time is not a line. (Archive III seed)"
  }
],
  links:[["b1", "jim"], ["b1", "e2118"], ["b1", "elara"], ["b1", "terasa"], ["b1", "emoon"], ["b1", "ecount"], ["b2", "charlie"], ["b2", "ewar"], ["b2", "efall"], ["b2", "loan"], ["b2", "five"], ["jim", "djim"], ["jim", "anna"], ["jim", "charlie"], ["jim", "e2118"], ["jim", "elara"], ["jim", "emoon"], ["jim", "lune"], ["jim", "spire"], ["djim", "terasa"], ["djim", "core"], ["anna", "e2118"], ["anna", "cat"], ["anna", "ecount"], ["charlie", "e2118"], ["charlie", "loan"], ["charlie", "efall"], ["charlie", "ecount"], ["charlie", "song"], ["elara", "terasa"], ["elara", "ecount"], ["spire", "luna"], ["spire", "arthur"], ["spire", "cabin"], ["lune", "cabin"], ["lune", "e2118"], ["arthur", "core"], ["arthur", "cabin"], ["corbin", "dead"], ["dead", "emoon"], ["luna", "emoon"], ["cabin", "twin"], ["cabin", "roswell"], ["twin", "e2118"], ["twin", "core"], ["roswell", "e1947"], ["e1947", "e2047"], ["e2047", "e2053"], ["e2053", "cabin"], ["terasa", "incub"], ["ewar", "five"], ["ewar", "incub"], ["ewar", "efall"], ["whalekind", "efall"], ["whalekind", "song"], ["cat", "terasa"]]
};
var graphInited = false;
function showView(which){
  document.getElementById('view-line').style.display = which==='line' ? '' : 'none';
  document.getElementById('view-graph').style.display = which==='graph' ? '' : 'none';
  document.getElementById('tab-line').classList.toggle('active', which==='line');
  document.getElementById('tab-graph').classList.toggle('active', which==='graph');
  if(which==='graph' && !graphInited){ graphInited = true; initStoryGraph(GRAPH); }
}
document.getElementById('tab-line').addEventListener('click', function(){ showView('line'); });
document.getElementById('tab-graph').addEventListener('click', function(){ showView('graph'); });
</script>
