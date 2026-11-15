from pathlib import Path
import html

ROOT = Path("巨鲸陨落_V1")
ZH_MD = ROOT / "zh_md"
EN_MD = ROOT / "en_md"
ZH_HTML = ROOT / "zh_html"
EN_HTML = ROOT / "en_html"


def md_to_html(text):
    out = []
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("# "):
            out.append(f"<h1>{html.escape(s[2:])}</h1>")
        elif s.startswith("## "):
            out.append(f"<h2>{html.escape(s[3:])}</h2>")
        else:
            out.append(f"<p>{html.escape(s)}</p>")
    return "\n".join(out)


def page(title, body, nav, lang):
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="../assets/style.css">
</head>
<body><main>
{body}
{nav}
</main></body></html>
"""


EN = {
    "14_谁赢了": """# 14 Who Won

The old sea road had no water.

It was like a drained blood vessel running along the edge of the vault. Water-marks from the Abyssals remained on the walls, many cracked and filled with ash. Lo'an followed Sern forward, gripping the dark blue whale seed. It was cold, not like ice, but like a sliver of deep sea pressed into his palm.

Behind them came the sound of Chitinous entering the water dome.

No shouting. No chaos. Only orderly steps, a pause, then several formations splitting toward different routes.

“They know the seed was taken,” Lo'an said.

“Of course,” Sern answered. “The Chitinous never miss anything that can be counted.”

The passage widened into an old transfer hall. It had once connected several facilities; now only broken bridges and tilted platforms remained. A dozen survivors argued beside a half-buried lift.

The Sunbright survivor was there too, his brow-ring cracked, his face still carrying that proud calm. The Scale-Kin woman held her canister on the other side. Abyssals leaned against the wall. In the corner stood a Chitinous individual, its chest node flickering, clearly severed from the main cluster.

Peoples who might have killed one another minutes earlier now stood in the same hall.

“The lift falls under Sunbright decree,” the Sunbright said. “Command authority boards first.”

The Scale-Kin woman looked at him coldly. “Your command authority just tried to seal us inside a tower.”

“Final order was triggered in error.”

Sern laughed. “You describe murder like a system fault.”

The Chitinous node spoke before the Sunbright could answer.

“Objective incomplete. Victory judgment invalid.”

Everyone turned.

“Phaeton control lost. Earth intervention right unsecured. Whale archive unrecovered. Victory judgment invalid.”

“You have no authority to judge victory,” the Sunbright said.

An old Abyssal lifted his head. “The sea does not record victory. It records what sinks.”

“So you admit defeat?”

“No. I admit you are using the wrong word.”

Silence.

Lo'an stood at the edge, unsure which side he belonged to. He was not Sunbright, Scale-Kin, Chitinous, Abyssal, or Wing-Shiver. He was a low scout drafted into a war, and surviving this long felt stolen.

Yet everyone was arguing over victory.

Charlie felt a familiar absurdity inside him, like players fighting over who won while the server burned.

“Who won?” Lo'an asked.

The question surprised even him.

The Sunbright said, “Order was not destroyed. If decree is remembered, we did not lose.”

The Scale-Kin said, “Preservation remains. If seeds and failure lists survive, we did not lose.”

The Chitinous said, “The cluster still computes. Objective incomplete. Victory nonexistent.”

The Abyssal said, “Water will remember all your claims and wear them down.”

Sern looked at Lo'an. “Hear that? No one won. Every people only refuses to admit it first.”

The ceiling split. Violet sky-light fell into the hall, making every conviction look like a dying thing refusing to lie down.

Lo'an looked at the whale seed.

It said nothing.

It looked more like an answer than any of them.""",
    "15_地球不是战场": """# 15 Earth Was Not the Battlefield

The lift could not be used.

Its shell looked intact, but the inner rails were twisted. Some survivors tried to force it alive. The cabin shook once and coughed black smoke from below. The Sunbright stepped back and stopped mentioning command authority.

“Old sea road,” Sern said.

The Abyssal elder raised his head. “It leads to the outer port, not the surface.”

“There is little worth reaching on the surface now.”

No one argued.

They moved down through the crack behind the transfer hall. The farther they went, the wetter the passage became. Water-marks glowed weakly on the walls, like a dying pulse. The whale seed trembled in Lo'an's palm, answering them.

At the end was an abandoned navigation room.

At its center hung a broken star map. Most layers were damaged, but several inner solar bodies still rotated: Sun, Mercury, Venus, Earth, Mars, Phaeton, Jupiter.

Phaeton stood between Mars and Jupiter.

It was larger than I expected. Routes crossed through it, making it look like a clasp between the inner and outer system. Gold, green, blue, and silver paths stretched from it, and most curved toward one place.

Earth.

Lo'an stared at the young blue-white planet.

So did I.

It was not the Earth I knew. The continents were unfamiliar, the oceans wider, the atmosphere thicker. But I knew it was Earth. My home. The birthplace of my friends.

In this ancient map, Earth was not the battlefield.

It was the objective.

The Sunbright survivor said quietly, “Phaeton was the threshold. All lawful intervention passed through here.”

“Lawful?” Sern said.

“Once. The peoples established shared observation zones on Phaeton to supervise Earth's life stage. Without Phaeton, no one people could stably enter the Earth window.”

The Scale-Kin woman gave a dry laugh. “So you tried to take it.”

“Every people tried to take it.”

The room sank into that sentence.

The Abyssal elder looked at the map. “It was not like this at first. Earth was observed. It was too young, too fragile. Early intervention could ruin it.”

The Chitinous node flashed. “Observation phase ended. Contest phase initiated. Cause: incompatible projections.”

Sern said, “You say that as if you did not cut the southern orbit routes first.”

“Southern orbit threatened cluster proposal.”

“Because your proposal would make future Earth a nest without single voices.”

The Chitinous did not answer.

Lo'an understood. The war was never only for Phaeton. Phaeton stood at the door. The real prize was behind it.

The shape of Earth's future life.

Who would leave genes, who would leave consciousness templates, who would leave myths, who would decide whether future life should obey, hide, link, sink into the sea, or keep roads open.

The star map flickered. Phaeton's projection cracked in sync with the real planet. Routes broke one by one, and every path to Earth turned red.

Warning filled the room.

“Fifth planet stability lost. Earth window closure countdown initiated.”

Earth still turned slowly, distant and quiet, unaware of how many civilizations had fought to own its future.

Lo'an watched it and formed a question that belonged to no people.

If Earth had not chosen, who had the right to choose for it?""",
    "16_第五行星": """# 16 The Fifth Planet

The navigation warning repeated.

“Fifth planet stability lost. Earth window closure countdown initiated.”

Fifth planet.

Lo'an barely reacted. To him, Phaeton had always been the fifth planet: outside Mars, inside Jupiter, holding the routes between the inner and outer system. Birth, service, war, escape. All of it had happened under that fact.

To me, the words were a stone turned over in memory.

There was no fifth planet in my time.

Mercury, Venus, Earth, Mars, then the asteroid belt, then Jupiter. I had learned it in school and seen it in games. Between Mars and Jupiter were countless small bodies, not a complete world.

But here, on the map, there was one.

Phaeton.

I felt the absurdity of watching a piece of astronomy erased from my era.

The map unfolded Phaeton's structure. Outer vault-field broken. Orbital rings detaching. Cracks in the crust spreading like glowing veins. The whale impact marked a black-blue depression whose energy curves were driving toward the core.

“It is piercing the core,” the Scale-Kin woman said.

“The whale would not destroy the fifth planet,” the Sunbright said. “They are witnesses, not destroyers.”

The Abyssal elder whispered, “A witness may close the book when no one will stop writing over it.”

The floor tilted. Everyone slid. Lo'an struck the console, and the whale seed hit its edge. The dark blue core flared, sending a low frequency into the map.

The map changed.

Over the present structure appeared another layer: time.

I saw fragments peel away from the complete planet. Continents broke. Basins vaporized. Orbital rings shattered into arcs. After several slow pulses, Phaeton split into a belt of debris around the Sun.

The image overlapped my memory of the asteroid belt.

Not similar.

The same place.

The same end.

My modern awareness almost tore free of Lo'an. In my time, people said the asteroid belt may never have formed a planet, that Jupiter's gravity prevented accretion. A clean explanation, with no bodies and no whale.

Here was another memory.

Not a rejection of science, but a buried cause beneath the result science could see.

Perhaps humanity saw the stable state of wreckage.

I was seeing the scream that made it.

“It becomes a broken belt,” Lo'an whispered.

Half him. Half me.

Sern looked at him. “What broken belt?”

Lo'an could not answer.

He should not know. In his time, Phaeton had not yet become anything else.

The Sunbright survivor stared at him.

“The later frequency in you comes from after Earth?”

Silence.

Sern stepped in front of Lo'an. “Now is not the time.”

“If he comes from the future, he knows who inherits Earth.”

That sentence fell like a spark into dry grass.

The Scale-Kin woman looked up. The Abyssal elder too. Even the Chitinous node flashed faster.

Who inherits Earth?

I knew the answer.

Or thought I did.

Humans.

But the answer no longer felt simple. Every people in this room seemed to have left some shadow in my body.

The whale seed sounded again.

Earth lit on the map.""",
    "17_生命孵化场": """# 17 The Cradle-Lab

Earth enlarged in the star map.

It hung between them, blue-white light illuminating the broken navigation room. Phaeton's warnings dimmed, as if even the dying planet yielded briefly to the young world.

This Earth had no familiar outline.

Oceans were vast, continents strange, clouds heavy. No cities, no satellites, no trace of later humanity. It turned quietly like a seed not yet opened.

But to the peoples in the room, it was never merely a planet.

Labels unfolded. Blue spectra rose over oceans, green adaptation curves along land, fine consciousness resonance readings above the atmosphere. Lo'an did not understand them. Neither did I. But the others understood enough.

The Sunbright said, “Abstract consciousness threshold unformed.”

The Scale-Kin added, “Large carrier direction unlocked.”

The Abyssal looked at the sea. “The ocean can remember. It cannot yet speak.”

The Chitinous node flashed. “Cluster potential present. Individual isolation risk high.”

Sern said nothing. He watched the routes around Earth, face tightening.

I realized this was not a map.

It was a medical record.

Earth was not home to them, not sacred ground, but a developing life cradle. Ocean, land, atmosphere, gravity, magnetic field, neural potential, consciousness thresholds: measured, tagged, compared.

I felt anger.

Not because they were evil.

Because they were serious.

They were doctors, engineers, gardeners, designers, surrounding a child who could not yet speak and arguing over who that child should become. Each people had reasons. Each had data. Each believed its plan would reduce future suffering.

No one asked Earth.

Of course Earth could not answer.

The map continued.

The Sunbright plan laid gold grids over land: future cities, altars, observation towers, centers of kingship and decree. The Scale-Kin plan sank underground into vaults and sleep layers. The Chitinous plan spread like a dark red nervous system, linking future life into clusters. The Abyssal plan entered the oceans, blue sound-lines riding currents. The Wing-Shiver plan was faintest: silver routes between land, sea, sky, and orbit.

None of the plans was entirely ugly.

None was harmless.

Lo'an felt as if Earth were held down by many transparent hands. Each hand claimed it only wanted to help. If all pressed at once, the seed would be crushed.

“So the war was not for Phaeton,” Lo'an said.

“Phaeton was the door,” Sern answered.

“Behind the door is Earth.”

“Behind the door is future,” the Abyssal elder corrected.

The Sunbright said, “Without guidance, future wastes itself.”

The Scale-Kin said, “Without preservation, future dies from one error.”

The Chitinous said, “Without linking, future individuals repeat loneliness and conflict.”

Sern said coldly, “Without roads, future is only a locked room passed between you.”

Silence again.

Earth turned.

It did not defend itself. It simply reflected ancient sunlight, unaware it would one day grow whales, humans, wars, dreams, and an ordinary person named Charlie Hale.

The whale seed trembled in Lo'an's palm.

It seemed to be looking at Earth too.

Not as a proposal.

As an unfinished answer that had to be protected.""",
    "18_日辉族想要人类跪拜": """# 18 The Sunbright Wanted Humans to Kneel

The Sunbright survivor's name was Soler.

He gave it after the argument ended. Perhaps after seeing all the Earth plans, calling one another only by people-name felt too hollow. Or perhaps with Phaeton breaking, even pride needed a more specific name before death.

“Soler,” he said. “Lower executor of the Third Decree Tower.”

Sern raised an eyebrow. “A name finally grew out of the decree?”

Soler ignored him.

He stood before Earth's projection, broken arm hanging at his side, the sun-ring in his brow cracked. Gold light flickered through the crack, making him look like a damaged idol refusing to fall.

“You think we wanted kneeling,” he said.

No one answered.

Because they did.

Soler looked at the gold grids over Earth's land. “Kneeling is not the purpose. It is a way of remembering. Lower life cannot understand stellar scale. It cannot bear fear without a center. It needs height made visible: sky, tower, king, god. It needs to know something more stable than itself exists.”

“And you put yourselves there,” Sern said.

“Because we can bear it.”

Lo'an felt disgust, and also a weight he could not simply dismiss.

The Sunbright had borne many things. They designed the earliest vault-field, maintained Phaeton's northern orbital cities, and held neutral zones through the early war. For many weaker peoples, Sunbright order had meant food, routes, shelter, tomorrow.

The problem was that they stopped knowing the difference between shelter and ownership.

Soler touched the projection. Gold grids enlarged. On future Earth rose stepped cities. At each center stood a tower, its summit linked to sky observatories. Humanoid creatures knelt in plazas, looking upward as light fell from above. Their bodies were not yet modern humans, but already they had shoulders, hands, eyes made to look up.

Charlie felt his scalp tighten.

The images were too familiar.

Pyramids. Temples. Kingship. Priests. Mandate. Sun gods. Teachers from the sky.

Not identical. This was not Earth history, but Sunbright design. Still, it was close enough to unsettle.

“You wanted future humans raised as watchers of height,” Lo'an said.

Soler looked at him. “To look upward is not shame.”

“What if they have no right to decide whether to bow?”

Soler was silent a moment.

“Choice is a luxury of mature consciousness. A young civilization first needs direction.”

Sern gave a cold smile. “And when it matures, you will say it is not mature enough.”

Soler's face changed.

“You Wing-Shiver speak only of roads. But where do roads lead? Without a center, roads only lose the weak.”

“At least the lost may find their own direction.”

Before Soler could answer, the room shook. Earth's projection twisted, and the Sunbright gold plan overlapped all the others. Under stepped cities appeared Scale-Kin vaults. At plaza edges flickered Chitinous nodes. Abyssal water-song entered the oceans. Wing-Shiver routes crossed the sky.

All plans were forced onto one Earth.

The image was chaotic.

And strangely like the future.

Charlie realized that later humans might not have escaped these designs. Perhaps they carried fragments of all of them: building towers, digging vaults, obeying kings, rebelling against kings, longing for collectives, fearing loss of self, hearing songs from the sea, looking up at the sky.

Soler stared at the mixed image, confused for the first time.

“That will be painful,” he said.

The Abyssal elder answered softly, “Perhaps life was never meant to avoid pain.”

The whale seed sounded once.

In the projection, the kneeling figures blurred. They stood, knelt, stood again, the motions overlapping, as if future had not decided how it would face height.

Lo'an watched and thought: more important than kneeling or refusing was that the future must have the chance to decide for itself."""
}

for name, text in EN.items():
    (EN_MD / f"{name}.md").write_text(text, encoding="utf-8")

names = list(EN.keys())
order = [p.stem for p in sorted(ZH_MD.glob("*.md"))]
for name in names:
    idx = order.index(name)
    prev = order[idx - 1] if idx > 0 else None
    nxt = order[idx + 1] if idx + 1 < len(order) else None
    zh = (ZH_MD / f"{name}.md").read_text(encoding="utf-8")
    en = (EN_MD / f"{name}.md").read_text(encoding="utf-8")
    zh_title = zh.splitlines()[0][2:]
    en_title = en.splitlines()[0][2:]
    prev_link = f'<a href="{prev}.html">上一章</a>' if prev else ""
    next_link = f'<a href="{nxt}.html">下一章</a>' if nxt else ""
    nav = f'<nav class="nav"><span>{prev_link}</span><span><a href="../index.html">目录</a></span><span>{next_link}</span></nav>'
    en_prev = f'<a href="{prev}.html">Previous</a>' if prev else ""
    en_next = f'<a href="{nxt}.html">Next</a>' if nxt else ""
    en_nav = f'<nav class="nav"><span>{en_prev}</span><span><a href="../index_EN.html">Index</a></span><span>{en_next}</span></nav>'
    (ZH_HTML / f"{name}.html").write_text(page(zh_title, md_to_html(zh), nav, "zh-CN"), encoding="utf-8")
    (EN_HTML / f"{name}.html").write_text(page(en_title, md_to_html(en), en_nav, "en"), encoding="utf-8")

print("expanded chapters 14-18")
