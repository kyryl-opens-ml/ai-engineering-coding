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

# What is Vibe Coding?

<div class="text-2xl mt-8">
Writing code through <span class="text-blue-400">natural language</span> and <span class="text-green-400">high-level intent</span>
</div>

<div class="mt-8 text-lg opacity-80">
Instead of syntax, focus on <span class="font-bold">what you want to build</span>
</div>

---

# The Vibe Coding Revolution

<div class="grid grid-cols-2 gap-8 mt-8">

<div v-click>

## Traditional Coding
- Learn syntax first
- Debug line by line
- Stack Overflow diving
- Years to proficiency
- Implementation focused

</div>

<div v-click>

## Vibe Coding
- Describe your intent
- AI handles syntax
- Instant prototypes
- Minutes to start
- Outcome focused

</div>

</div>

<div v-click class="mt-12 text-center text-xl">
<span class="text-yellow-400">⚡</span> The barrier to entry has never been lower
</div>

---
layout: section
---

# The Vibe Coding Ecosystem

Products, Agents, and Editors

---

# Products: Full-Stack in Minutes

<div class="grid grid-cols-2 gap-4 mt-8">

<div v-click>

### [Lovable.dev](https://lovable.dev/)
- Full-stack web apps
- Beautiful UI out of the box
- Deploy instantly
- Great for MVPs

</div>

<div v-click>

### [Bolt.new](https://bolt.new/)
- Browser-based development
- Full-stack applications
- No setup required
- Instant preview

</div>

<div v-click>

### [V0.dev](https://v0.dev/)
- UI component generation
- React/Next.js focused
- Copy-paste ready
- Design system aware

</div>

<div v-click>

### Gemini Canvas
- Google's take on AI coding
- Integrated with Google services
- Collaborative features
- Multi-modal input

</div>

</div>

---

# Agents: Your AI Pair Programmers

<div class="space-y-6 mt-8">

<div v-click>

### [Cursor Agents](https://cursor.com/agents)
- Deep codebase understanding
- Multi-file edits
- Test generation
- Refactoring assistance

</div>

<div v-click>

### [OpenAI Codex](https://openai.com/index/introducing-codex/)
- Powers GitHub Copilot
- Code completion
- Natural language to code
- Multiple language support

</div>

<div v-click>

### [Jules by Google](https://jules.google/)
- Autonomous coding agent
- Bug fixing
- Code reviews
- Integration with Google Cloud

</div>

</div>

---

# More Agents

<div class="space-y-6 mt-8">

<div v-click>

### [Claude Code](https://www.anthropic.com/claude-code)
- Anthropic's coding assistant
- Strong reasoning capabilities
- Code explanation
- Security-focused

</div>

<div v-click>

### [Gemini CLI](https://github.com/google-gemini/gemini-cli)
- Command-line interface
- Script generation
- System administration
- DevOps automation

</div>

</div>

---

# Code Editors: Where the Magic Happens

<div class="grid grid-cols-2 gap-8 mt-8">

<div v-click>

## [Cursor](https://cursor.com/)
- Fork of VS Code
- AI-first design
- Multi-file awareness
- Chat + inline edits
- Codebase indexing

</div>

<div v-click>

## [Windsurf](https://windsurf.com/editor)
- Next-gen AI editor
- Flow-based coding
- Visual programming
- Real-time collaboration
- Cloud-native

</div>

</div>

<div v-click class="mt-8 text-center">
<span class="text-2xl">🎯</span> Both understand your entire codebase context
</div>

---
layout: center
---

# Demo Time! 

Let's see vibe coding in action

<div class="mt-8 text-lg opacity-80">
Building something real in < 5 minutes
</div>

---
layout: section
---

# The Reality Check

POC vs Production Systems

---

# From Prototype to Production

<div class="mt-8">

<v-clicks>

### ✅ What Vibe Coding Excels At
- Rapid prototyping
- UI/UX iterations
- Boilerplate generation
- Learning new frameworks
- POCs and demos

### ⚠️ Where You Still Need Expertise
- System architecture
- Performance optimization
- Security considerations
- Complex business logic
- Integration challenges

</v-clicks>

</div>

---

# Bridging the Gap

<div class="grid grid-cols-3 gap-4 mt-8">

<div v-click class="text-center">

### Phase 1: Vibe
<div class="mt-4 text-6xl">💡</div>
<div class="mt-2">Ideation & Prototype</div>
<div class="text-sm opacity-80 mt-2">0-2 weeks</div>

</div>

<div v-click class="text-center">

### Phase 2: Hybrid
<div class="mt-4 text-6xl">🔧</div>
<div class="mt-2">Refine & Optimize</div>
<div class="text-sm opacity-80 mt-2">2-8 weeks</div>

</div>

<div v-click class="text-center">

### Phase 3: Production
<div class="mt-4 text-6xl">🚀</div>
<div class="mt-2">Scale & Maintain</div>
<div class="text-sm opacity-80 mt-2">Ongoing</div>

</div>

</div>

<div v-click class="mt-12 text-center text-lg">
The gap is shrinking every month 📉
</div>

---
layout: section
---

# Vibe Coding at AXL

Our Process & How to Join

---

# How We Use Vibe Coding

<div class="space-y-6 mt-8">

<v-clicks>

### 🎯 Use Cases
- Rapid prototyping for client demos
- Internal tool development
- Hackathon projects
- Learning new technologies
- Automating repetitive tasks

### 🛠️ Our Stack
- **Primary Editor**: Cursor
- **Prototyping**: Lovable.dev, V0
- **Agents**: Claude, GPT-4
- **Deployment**: Vercel, Netlify

</v-clicks>

</div>

---

# Getting Involved at AXL

<div class="text-center mt-12">

<div class="text-6xl mb-8">💬</div>

<h2 class="text-3xl mb-8">It's as easy as using Slack!</h2>

<v-clicks>

<div class="text-xl mb-4">1. Join #vibe-coding channel</div>
<div class="text-xl mb-4">2. Share your idea or problem</div>
<div class="text-xl mb-4">3. Get paired with a vibe coder</div>
<div class="text-xl mb-8">4. Ship something amazing</div>

<div class="text-lg opacity-80">No coding experience required!</div>

</v-clicks>

</div>

---
layout: section
---

# Let's Get You Started

Haven't coded in 20 years? No problem!

---

# Your First Vibe Coding Session

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

<v-clicks>

### Step 1: Pick Your Tool
- **No setup?** → Bolt.new
- **Want an app?** → Lovable.dev
- **Need components?** → V0.dev
- **Ready to dive deeper?** → Cursor

### Step 2: Start Simple
- "Make a todo list app"
- "Create a landing page for..."
- "Build a calculator that..."

</v-clicks>

</div>

<div v-click>

### Step 3: Iterate
```
You: "Add a dark mode toggle"
AI: *generates code*

You: "Make the buttons bigger"
AI: *updates code*

You: "Save todos to browser"
AI: *adds localStorage*
```

<div class="mt-4 text-sm opacity-80">
It's just a conversation!
</div>

</div>

</div>

---

# Pro Tips for Beginners

<div class="space-y-4 mt-8">

<v-clicks>

### 🎯 Be Specific
"Create a blue button" → "Create a rounded blue button with white text that says 'Get Started'"

### 🔄 Iterate Freely
Don't worry about getting it right the first time

### 📋 Copy Everything
Save prompts that work well for reuse

### 🤝 Pair with AI
Think of it as pair programming, not code generation

### 🎨 Start with UI
Visual feedback is motivating and easier to understand

</v-clicks>

</div>

---
layout: center
---

# Live Coding Challenge!

<div class="text-2xl mt-8">
Let's build something together from the audience
</div>

<div class="mt-8 text-lg opacity-80">
What should we create?
</div>

---
layout: two-cols
---

# Key Takeaways

<v-clicks>

- 🚀 **Anyone can code now** - the tools have democratized development

- ⚡ **Start today** - pick any tool and try building something

- 🤝 **It's collaborative** - you're pairing with AI, not being replaced

- 📈 **The gap is closing** - POCs are getting closer to production quality

- 💬 **Join us** - hop into Slack and start vibing!

</v-clicks>

::right::

<div class="flex items-center justify-center h-full">
<div class="text-center">
<div class="text-8xl mb-4">🎉</div>
<div class="text-2xl">You're ready to vibe!</div>
</div>
</div>

---
layout: center
class: text-center
---

# Thank You!

<div class="text-2xl mt-8 mb-12">
Questions?
</div>

<div class="text-lg opacity-80">
Join **#vibe-coding** on Slack to get started
</div>

<div class="mt-8">
<span class="text-sm opacity-60">Slides available at: [your-url-here]</span>
</div>
