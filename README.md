<div align="center">

<a href="https://pixeltable.com">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/hero-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./assets/hero-light.svg">
    <img alt="Pierre Brunelle — Co-Founder & CEO at Pixeltable" src="./assets/hero-dark.svg" width="100%">
  </picture>
</a>

<br/>

[![Pixeltable](https://img.shields.io/badge/Pixeltable-pixeltable.com-4f46e5?style=flat-square&logo=python&logoColor=white)](https://pixeltable.com)
[![Docs](https://img.shields.io/badge/Docs-docs.pixeltable.com-0891b2?style=flat-square&logo=readthedocs&logoColor=white)](https://docs.pixeltable.com)
[![Awesome Apps](https://img.shields.io/badge/Runnable_Apps-Gallery-10b981?style=flat-square&logo=githubcodespaces&logoColor=white)](https://pierrebrunelle.github.io/awesome-pixeltable-apps/)
[![X](https://img.shields.io/badge/@pjlbrunelle-0f172a?style=flat-square&logo=x&logoColor=white)](https://x.com/pjlbrunelle)
[![LinkedIn](https://img.shields.io/badge/in/brunellepe-0a66c2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/brunellepe/)

</div>

---

### What I'm Building

I'm Co-Founder & CEO of **[Pixeltable](https://github.com/pixeltable/pixeltable)** — open-source Python infrastructure that unifies **multimodal storage, incremental computation, vector indexing, tool-calling agents, and FastAPI serving** in a single declarative `app.py`.

<!-- PIXELTABLE-META:START -->
> 📦 **Latest release:** [`v0.7.19`](https://github.com/pixeltable/pixeltable/releases/tag/v0.7.19) &nbsp;·&nbsp; ⭐ **1,640 stars** &nbsp;·&nbsp; 🍴 **231 forks** &nbsp;·&nbsp; 🧪 **[33 runnable example apps](https://pierrebrunelle.github.io/awesome-pixeltable-apps/)**
<!-- PIXELTABLE-META:END -->

---

### Featured Systems, Galleries & Agent Skills

| Repository | What it does | Try / Install |
| :--- | :--- | :--- |
| **[`pixeltable/pixeltable`](https://github.com/pixeltable/pixeltable)** | **The backend agents build with.** Declarative tables (`TableModel`), incremental computed columns, hybrid vector search (`EmbeddingIndex`), media storage, and HTTP serving (`FastAPIRouter`) in one file. | `pip install 'pixeltable[serve]'` |
| **[`awesome-pixeltable-apps`](https://github.com/pierrebrunelle/awesome-pixeltable-apps)** | Curated gallery of self-contained multimodal AI apps & REST APIs built with Pixeltable. Open any app in GitHub Codespaces or deploy to Pixeltable Cloud. | **[Browse Live Gallery →](https://pierrebrunelle.github.io/awesome-pixeltable-apps/)** |
| **[`challenge-the-design`](https://github.com/pierrebrunelle/challenge-the-design)** | Agent skill & plugin that reviews a PR or stack as an ensemble, separates requirements from assumptions, and runs a behavior-preserving deletion pass before checking implementation. | `npx skills add pierrebrunelle/challenge-the-design` |
| **[`marcel-review`](https://github.com/pierrebrunelle/marcel-review)** | Agent skill that reviews a change the way [Marcel Kornacker](https://github.com/mkornacker) reviews it: crisp abstractions, ownership, failure paths, and what the change costs its future readers. | `npx skills add pierrebrunelle/marcel-review` |
| **[`mcp-server-openai`](https://github.com/pierrebrunelle/mcp-server-openai)** & **[`infinite-memory-discord-bot`](https://github.com/pierrebrunelle/infinite-memory-discord-bot)** | Model Context Protocol server bridging Claude & OpenAI models, plus a stateful Discord agent with durable semantic memory backed by Pixeltable. | **[Explore Repos →](https://github.com/pierrebrunelle?tab=repositories)** |

---

### Latest Runnable Pixeltable Apps

<!-- AWESOME-APPS:START -->
_Auto-synced from [`pierrebrunelle/awesome-pixeltable-apps`](https://github.com/pierrebrunelle/awesome-pixeltable-apps) (33 apps total, newest first):_

| App | Architecture & Features | Launch |
| :--- | :--- | :---: |
| **[Delivery-Driver Incident Intake](https://github.com/pierrebrunelle/pixeltable-driver-incident-intake)**<br><sub>2026-10-21</sub> | Incident intake API for delivery drivers: voice note + photo upload, transcription, Pydantic-validated structured records from a vision model, async dispatch routing and SQL export<br><sub>`FastAPI serving` · `Computed columns & UDFs` · `Concurrency` · `Data reads & writes` · `B-tree indexes` · `Media (images)`</sub> | [![Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/pierrebrunelle/pixeltable-driver-incident-intake?quickstart=1) |
| **[Hot-Air Balloon Flight Ops](https://github.com/pierrebrunelle/pixeltable-balloon-flight-ops)**<br><sub>2026-10-20</sub> | Hot-air balloon flight log CLI: idempotent batch imports keyed by content hashes, computed burn/propane/payload columns, pxt revert and pxt rename for recovery, and a fingerprint command that rebuilds the cloud deploy fingerprint with Pixeltable's public hashing helpers<br><sub>`pxt CLI & dashboard` · `Computed columns & UDFs` · `B-tree indexes` · `pixeltable.toml config` · `Pixeltable Cloud`</sub> | [![Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/pierrebrunelle/pixeltable-balloon-flight-ops?quickstart=1) |
| **[Cooking-Class Video Moment Search](https://github.com/pierrebrunelle/pixeltable-cooking-video-search)**<br><sub>2026-10-19</sub> | Video moment search API for cooking classes: frame sampling, vision captions, semantic search that returns the mm:ss moment, scene detection and teaser clips<br><sub>`Media (images)` · `B-tree indexes` · `AI model functions` · `FastAPI serving` · `Computed columns & UDFs`</sub> | [![Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/pierrebrunelle/pixeltable-cooking-video-search?quickstart=1) |
| **[Bus Depot Operations](https://github.com/pierrebrunelle/pixeltable-bus-depot-dashboard)**<br><sub>2026-10-18</sub> | Bus depot operations dashboard: on-time rate and p90 delay per depot and route from custom UDAs, JSON map/filter/sort over per-stop delays, distinct() lookups, a windowed running total and a data-health check for telemetry that failed to parse<br><sub>`pxt CLI & dashboard` · `Computed columns & UDFs` · `B-tree indexes` · `pixeltable.toml config` · `Pixeltable Cloud`</sub> | [![Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/pierrebrunelle/pixeltable-bus-depot-dashboard?quickstart=1) |
| **[Podcast Transcript Search](https://github.com/pierrebrunelle/pixeltable-podcast-transcript-search)**<br><sub>2026-10-17</sub> | Searchable podcast and meeting transcript archive: silence-aware audio chunking, Whisper API transcription, semantic search with mm:ss offsets, and cover-art tiles<br><sub>`Media (images)` · `B-tree indexes` · `AI model functions` · `Computed columns & UDFs`</sub> | [![Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/pierrebrunelle/pixeltable-podcast-transcript-search?quickstart=1) |

<div align="right">
  <sub><a href="https://pierrebrunelle.github.io/awesome-pixeltable-apps/">Browse all 33 runnable apps in the interactive gallery →</a></sub>
</div>
<!-- AWESOME-APPS:END -->

---

### Deep Dives

<details>
<summary><b>⚡ 60-Second Quickstart: One-File Multimodal Backend (<code>app.py</code>)</b></summary>
<br/>

With Pixeltable, your schema, computed columns, vector indexes, and HTTP routes live in a single declarative `app.py` — no separate vector DB, no `for row in ...:` model loops, and no imperative glue:

```python
import pixeltable as pxt
import pixeltable.functions as pxtf
from pixeltable.functions.openai import embeddings
from pixeltable.serving import FastAPIRouter

TableModel = pxt.model_base()


@pxt.udf
def excerpt(text: str, n: int = 120) -> str:
    return text if len(text) <= n else f'{text[:n]}...'


class Docs(TableModel, name='docs'):
    id = pxt.Column(value=pxtf.uuid.uuid7(), primary_key=True)
    title: pxt.String
    body: pxt.String
    image: pxt.Image | None
    summary = excerpt(body)

    __indexes__ = [
        pxt.EmbeddingIndex(column=body, string_embed=embeddings.using(model='text-embedding-3-small'))
    ]


api = FastAPIRouter(name='ingest')
api.add_insert_route(Docs, path='/docs', inputs=[Docs.title, Docs.body, Docs.image], outputs=[Docs.id, Docs.summary])
```

Run locally or deploy the exact same `app.py` to **Pixeltable Cloud**:

```bash
# Local
pip install 'pixeltable[serve]'
pxt init
pxt schema update app.py my_app
pxt service update app.py my_app -f

# Pixeltable Cloud
pxt login
pxt db update pxt://org:db -f
pxt schema update app.py pxt://org:db -f
pxt service update app.py pxt://org:db -f
```

</details>

<details>
<summary><b>🧭 Engineering &amp; Code Review Philosophy: Delete Before You Abstract</b></summary>
<br/>

Whether designing multimodal infrastructure or reviewing pull requests with [`challenge-the-design`](https://github.com/pierrebrunelle/challenge-the-design) and [`marcel-review`](https://github.com/pierrebrunelle/marcel-review), I optimize for a few non-negotiable invariants:

1. **State the problem and a measurable falsifier first.** Separate true requirements from inherited assumptions before writing code.
2. **Delete unnecessary work before adding abstractions.** Run a behavior-preserving deletion pass across the whole ensemble (callers, state, and tests) before introducing new layers.
3. **Every abstraction must earn its keep.** A class or function should represent a crisp contract that can be stated in one sentence—and its docstring should state only what the signature does not.
4. **Declarative state over imperative glue.** If progress and lineage live in rows and computed columns rather than ephemeral in-memory loops, retries, caching, and observability become properties of the table engine.

</details>

<details>
<summary><b>🏗️ Career Arc: Structural Engineering → Decision Science → AI Infrastructure</b></summary>
<br/>

- **[Pixeltable](https://pixeltable.com)** — *Co-Founder & CEO* · Building open-source multimodal AI data infrastructure and Pixeltable Cloud (`pxt://`).
- **[Noteable](https://github.com/noteable-io)** *(acquired by **[Confluent](https://github.com/confluentinc)**)* — *Co-Founder* · Built the collaborative data notebook platform bridging Python, SQL, and interactive analytics, and pioneered early ChatGPT Code Interpreter / Notebook plugin workflows.
- **Amazon & AWS** — *Decision Scientist & Product/Data Leader* · Applied econometrics, optimization, and large-scale cloud data systems across AWS and Amazon consumer/infrastructure teams.
- **Siemens & Structural Engineering** — Started my career in structural engineering and industrial systems, where load paths, safety margins, and failure modes are calculated before anything is built.

</details>
