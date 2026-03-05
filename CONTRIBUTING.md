# Contributing to Awesome OPC Skills

Thank you for your interest in contributing! This guide will help you add new skills or improve existing ones.

## 🎯 What We're Looking For

Skills that help solo developers and one-person companies:

- **Automation tools** - Save time on repetitive tasks
- **Development workflows** - Ship faster with better processes
- **Business methodologies** - Build profitable products
- **Productivity tools** - Do more with less
- **Marketing automation** - Grow without a team

## 📋 Contribution Process

### 1. Fork and Clone

```bash
git clone https://github.com/ryanmind/awesome-opc-skills.git
cd awesome-opc-skills
```

### 2. Create a Branch

```bash
git checkout -b feat/add-your-skill-name
```

### 3. Add Your Skill

Create a new directory under `skills/`:

```bash
mkdir -p skills/your-skill-name
cd skills/your-skill-name
```

### 4. Required Files

Every skill must include:

- **SKILL.md** - Skill definition (required by Claude Code)
- **README.md** - User-friendly documentation
- **scripts/** - Executable scripts (if applicable)
- **config/** - Configuration examples (use placeholders, no real credentials)

### 5. SKILL.md Template

```markdown
---
name: your-skill-name
description: |
  Clear description of what this skill does. When it activates,
  and what problems it solves. Be specific about triggers.
---

# Your Skill Name

Brief overview of what this skill does.

## When to Use

This skill activates when:
- User mentions X
- Context includes Y
- User asks for Z

## Instructions

Step-by-step instructions for Claude to follow...

## Examples

Example usage scenarios...
```

### 6. README.md Template

```markdown
# Your Skill Name

Brief description of the skill.

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

\`\`\`bash
# Installation steps
\`\`\`

## Usage

\`\`\`bash
# Usage examples
\`\`\`

## Configuration

Explain configuration options...

## Examples

Provide real-world examples...
```

## ✅ Quality Checklist

Before submitting your PR:

- [ ] SKILL.md follows the template
- [ ] README.md is clear and complete
- [ ] No sensitive information (API keys, passwords, company names)
- [ ] Configuration uses placeholders (e.g., `YOUR_API_KEY`)
- [ ] Scripts are tested and working
- [ ] Code follows existing style
- [ ] Documentation is in English
- [ ] Examples are practical and realistic

## 🚫 What NOT to Include

- ❌ Real API keys, passwords, or credentials
- ❌ Company-specific configurations
- ❌ Large binary files (.ipa, .apk, etc.)
- ❌ Proprietary code or trade secrets
- ❌ Overly complex solutions (keep it simple)

## 📝 Commit Message Format

Use conventional commits:

```
feat(skill-name): add new feature
fix(skill-name): fix bug
docs(skill-name): update documentation
refactor(skill-name): refactor code
```

## 🔍 Code Review

We'll review your PR for:

1. **Functionality** - Does it work as described?
2. **Security** - No sensitive information exposed?
3. **Quality** - Is the code clean and maintainable?
4. **Documentation** - Is it clear and complete?
5. **OPC Alignment** - Does it help solo developers?

## 💡 Ideas for New Skills

Not sure what to contribute? Here are some ideas:

- **rapid-mvp** - Build MVPs in 2 weeks
- **stripe-integration** - Quick payment setup
- **seo-automation** - Automate SEO tasks
- **email-marketing** - Email campaign automation
- **analytics-dashboard** - Simple analytics setup
- **landing-page-generator** - Quick landing pages
- **pricing-calculator** - Pricing strategy tool

## 🤝 Community

- Be respectful and constructive
- Help others in discussions
- Share your experience as a solo developer
- Learn from each other

## 📧 Questions?

Open an issue or start a discussion. We're here to help!

---

**Thank you for contributing to the OPC community!**
