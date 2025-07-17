---
# You can also start simply with 'default'
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1920
# some information about your slides (markdown enabled)
title: You don't have an excuse not to code now!
info: |
  ## How to harness vibe coding efficiently
  
  A tech talk about vibe coding capabilities, how we use it, and what's easiest. 
  If you are not a technical person or have not coded in a long time - it's definitely worth coming to try.
# apply unocss classes to the current slide
class: text-center
# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/features/mdc
mdc: true
# open graph
# seoMeta:
#  ogImage: https://cover.sli.dev
---

# You don't have an excuse not to code now!


<div class="abs-br m-6 text-xl">
  <button @click="$slidev.nav.openInEditor()" title="Open in Editor" class="slidev-icon-btn">
    <carbon:edit />
  </button>
  <a href="https://github.com/slidevjs/slidev" target="_blank" class="slidev-icon-btn">
    <carbon:logo-github />
  </a>
</div>

<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->

---
transition: fade-out
---

# Agenda

<div class="space-y-8 mt-10">

<v-clicks>

<div>
<h3 class="text-2xl mb-2">🌟 Gentle intro</h3>
<p class="text-gray-400">Market review of vibe coding tools and capabilities</p>
</div>

<div>
<h3 class="text-2xl mb-2">🌉 Mind the GAP</h3>
<p class="text-gray-400">What is the gap between real product & vibe coded solutions</p>
</div>

<div>
<h3 class="text-2xl mb-2">🏢 AXL</h3>
<p class="text-gray-400">How do we use it and how should we use it at AXL</p>
</div>

</v-clicks>

</div>

---
layout: center
class: text-center
---

# Why not AXL standard template?

<div class="text-3xl mt-12">
Because this presentation was vibe coded as well! 🎉
</div>


---
layout: section
---

# Gentle intro

Market review

---

# Vibe coding

<div style="display: flex; flex-direction: row; align-items: flex-start; gap: 32px; justify-content: center; margin-bottom: 24px;">
  <div style="text-align: center;">
    <img src="../images/image-1.1.png" alt="The Way of Code" style="width:300px; display:block; margin-bottom:8px;" />
    <a href="https://www.thewayofcode.com/" target="_blank">thewayofcode.com</a>
  </div>
  <div style="text-align: center;">
    <img src="../images/image-1.2.png" alt="Karpathy Vibe Coding Tweet" style="width:300px; display:block; margin-bottom:8px;" />
    <a href="https://x.com/karpathy/status/1886192184808149383?lang=en" target="_blank">x.com/karpathy/status/1886192184808149383</a>
  </div>
</div>

---

# LLMs are good at code

<div style="display: flex; flex-direction: row; align-items: flex-start; gap: 32px; justify-content: center; margin-bottom: 24px;">
  <div style="text-align: center;">
    <img src="../images/image-2.1.png" alt="SWE-bench" style="width:300px; display:block; margin-bottom:8px;" />
    <a href="https://github.com/swe-bench/SWE-bench" target="_blank">github.com/swe-bench/SWE-bench</a>
  </div>
  <div style="text-align: center;">
    <img src="../images/image-2.2.png" alt="Aider Leaderboards" style="width:300px; display:block; margin-bottom:8px;" />
    <a href="https://aider.chat/docs/leaderboards/" target="_blank">aider.chat/docs/leaderboards/</a>
  </div>
</div>

---

# Devs are using it a lot!

<div style="text-align: center; margin-bottom: 16px;">
  <img src="../images/image-3.1.png" alt="AI usage by job type" style="width:500px; display:block; margin: 0 auto 8px auto;" />
  <a href="https://www.anthropic.com/news/the-anthropic-economic-index" target="_blank">anthropic.com/news/the-anthropic-economic-index</a>
</div>

---

# Market reacts

<div style="text-align: center; margin-bottom: 16px;">
  <img src="../images/image-4.1.png" alt="AI is already changing how we build software" style="width:500px; display:block; margin: 0 auto 8px auto;" />
  <a href="https://www.redpoint.com/infrared/report/" target="_blank">redpoint.com/infrared/report/</a>
</div>

---

# Sometimes in a bad way

<div style="display: flex; flex-direction: row; align-items: flex-start; gap: 32px; justify-content: center; margin-bottom: 24px;">
  <div style="text-align: center;">
    <img src="../images/image-5.1.png" alt="Thoughts On A Month With Devin" style="width:300px; display:block; margin-bottom:8px;" />
    <a href="https://www.answer.ai/posts/2025-01-08-devin.html" target="_blank">answer.ai/posts/2025-01-08-devin.html</a>
  </div>
  <div style="text-align: center;">
    <img src="../images/image-5.2.png" alt="Debunking Devin YouTube" style="width:300px; display:block; margin-bottom:8px;" />
    <a href="https://www.youtube.com/watch?v=tNmgmwEtoWE" target="_blank">youtube.com/watch?v=tNmgmwEtoWE</a>
  </div>
</div>

---

# But usually with good products

<div class="mt-8">

```mermaid
graph TD
    subgraph Products["🎨 Products"]
        P1[Lovable.dev]
        P2[Bolt.new]
        P3[V0.dev]
        P4[Gemini Canvas]
    end
    
    subgraph Agents["🤖 Agents"]
        A1[Cursor Agents]
        A2[OpenAI Codex]
        A3[Jules by Google]
        A4[Claude Code]
        A5[Gemini CLI]
    end
    
    subgraph Editors["✏️ Editors"]
        E1[Cursor]
        E2[Windsurf]
        E3[VS Code Copilot]
        E4[Zed]
    end
    
    click P1 "https://lovable.dev/" _blank
    click P2 "https://bolt.new/" _blank
    click P3 "https://v0.dev/" _blank
    click P4 "https://gemini.google.com/overview/canvas/" _blank
    
    click A1 "https://cursor.com/agents" _blank
    click A2 "https://openai.com/index/introducing-codex/" _blank
    click A3 "https://jules.google/" _blank
    click A4 "https://www.anthropic.com/claude-code" _blank
    click A5 "https://github.com/google-gemini/gemini-cli" _blank
    
    click E1 "https://cursor.com/" _blank
    click E2 "https://windsurf.com/editor" _blank
    click E3 "https://github.com/microsoft/vscode-copilot-chat" _blank
    click E4 "https://github.com/zed-industries/zed" _blank
    
    style Products fill:#f9f,stroke:#333,stroke-width:2px
    style Agents fill:#bbf,stroke:#333,stroke-width:2px
    style Editors fill:#bfb,stroke:#333,stroke-width:2px
```

</div>

<div class="mt-4 text-center text-sm text-gray-400">
Click on any tool name to learn more
</div>

---

# But usually with good products

<div class="mt-8">

```mermaid
graph LR
    subgraph Products["🎨 Products"]
        P1[Lovable.dev]
        P2[Bolt.new]
        P3[V0.dev]
        P4[Gemini Canvas]
    end
    
    subgraph Editors["✏️ Editors"]
        E1[Cursor]
        E2[Windsurf]
        E3[VS Code Copilot]
        E4[Zed]
    end
    
    subgraph Agents["🤖 Agents"]
        A1[Cursor Agents]
        A2[OpenAI Codex]
        A3[Jules by Google]
        A4[Claude Code]
        A5[Gemini CLI]
    end
    
    P1 --> Editors
    P2 --> Editors
    P3 --> Editors
    
    Editors --> Agents
    
    click P1 "https://lovable.dev/" _blank
    click P2 "https://bolt.new/" _blank
    click P3 "https://v0.dev/" _blank
    click P4 "https://gemini.google.com/overview/canvas/" _blank
    
    click A1 "https://cursor.com/agents" _blank
    click A2 "https://openai.com/index/introducing-codex/" _blank
    click A3 "https://jules.google/" _blank
    click A4 "https://www.anthropic.com/claude-code" _blank
    click A5 "https://github.com/google-gemini/gemini-cli" _blank
    
    click E1 "https://cursor.com/" _blank
    click E2 "https://windsurf.com/editor" _blank
    click E3 "https://github.com/microsoft/vscode-copilot-chat" _blank
    click E4 "https://github.com/zed-industries/zed" _blank
    
    style Products fill:#f9f,stroke:#333,stroke-width:2px
    style Agents fill:#bbf,stroke:#333,stroke-width:2px
    style Editors fill:#bfb,stroke:#333,stroke-width:2px
```

</div>

<div class="mt-4 text-center text-sm text-gray-400">
The ecosystem is interconnected - Products generate code for Editors, Editors integrate with Agents
</div>

---

# But usually with good products

---

# Ideas to try with Bolt.new

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div>

<div v-click>
<strong>💀 DeathClock.lol</strong><br/>
Lifestyle → death countdown with sass
</div>

<div v-click>
<strong>🤡 RoastMyStartup.ai</strong><br/>
Get your startup idea demolished
</div>

<div v-click>
<strong>🔥 BurnItDown.club</strong><br/>
Watch things you hate burn virtually
</div>

<div v-click>
<strong>👻 GhostYourself.io</strong><br/>
Generate elaborate excuses instantly
</div>

</div>

<div>

<div v-click>
<strong>🎭 UnhingedLinkedIn.com</strong><br/>
LinkedIn but brutally honest
</div>

<div v-click>
<strong>🌶️ ToxicOrFlirting.game</strong><br/>
AI judges your text screenshots
</div>

<div v-click>
<strong>🎪 ExistentialCrisis.chat</strong><br/>
Simple questions → reality crisis
</div>

<div v-click>
<strong>🔮 FortuneCookie.wtf</strong><br/>
Gen Z chaos fortune cookies
</div>

</div>

</div>

<div v-click class="mt-6 text-center text-lg">
<span class="text-yellow-400">🚀</span> Build any of these in an afternoon!
</div>

---
layout: section
---

# Mind the GAP

What is the gap between real product & vibe coded solutions

---

# How wide is the gap?

---

# Cost of software

---

# Vibe coding - depends on taste

Taste comes with practice

---

# Better abstractions

---

# Accelerate for AI coding

---

# Rule of thumb

---
layout: section
---

# AXL way

How do we use it and how should we use it at AXL

---

# Our setup

---

# Cursor stats

---

# Team opinion

---

# Pre-requisites

PR, CI/CD, deployment

---

# Option 1: Slack

---

# Option 2: Dashboard

---

# Option 3: Mobile
