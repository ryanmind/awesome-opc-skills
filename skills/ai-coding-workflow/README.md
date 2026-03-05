# AI Coding Workflow

Transform your development process with AI-powered tools to achieve 10x productivity as a solo developer.

## 🎯 Overview

This skill teaches you how to leverage AI tools (Claude Code, Cursor, GitHub Copilot) to build features 5-10x faster while maintaining high code quality.

**Key Benefits:**
- Build features in hours instead of days
- AI-generated tests and documentation
- Automated code reviews
- Focus on architecture, not boilerplate

## 🚀 Quick Start

### 1. Install Core Tools

```bash
# Claude Code (you already have this!)

# Cursor - AI-native code editor
# Download from cursor.sh

# GitHub Copilot
# Enable in your IDE settings
```

### 2. Configure Your Project

Create `.cursorrules` in your project root:

```
# AI Coding Guidelines
- Use TypeScript for type safety
- Write tests for all features
- Follow Airbnb style guide
- Prefer functional programming
- Add JSDoc comments for complex functions
```

### 3. Create Prompt Templates

Save reusable prompts in `prompts/` directory:

```markdown
# prompts/feature-template.md
Build [FEATURE] with:
- Tech: [Your stack]
- Requirements:
  1. [Requirement 1]
  2. [Requirement 2]

Include:
- Implementation
- Tests
- Documentation
```

## 💡 AI Development Workflow

### Daily Workflow

```
Morning (15 min)
├── Review AI-generated code from overnight
├── Check automated test results
└── Plan today's features

Development (4-6 hours)
├── Use Claude Code for feature development
├── Cursor for inline coding
├── Copilot for boilerplate
└── AI generates tests

Review (30 min)
├── AI code review
├── Run automated tests
└── Deploy with monitoring
```

### Feature Development Process

1. **Describe** - Tell AI what you want in plain English
2. **Review** - Check generated architecture
3. **Iterate** - Refine implementation with AI
4. **Test** - AI generates comprehensive tests
5. **Deploy** - Automated deployment pipeline

## 🛠️ Recommended Stack

### Development
- **Claude Code** - Primary AI pair programmer ($20/mo)
- **Cursor** - AI-native editor ($20/mo)
- **GitHub Copilot** - Inline completion ($10/mo)

### UI/UX
- **v0.dev** - AI component generation (Free/Pro)
- **Figma AI** - Design assistance
- **Midjourney** - Asset generation

### Backend
- **Supabase** - Backend as a service
- **Vercel** - Deployment and hosting
- **Cloudflare** - CDN and edge functions

## 📈 Productivity Gains

| Task | Without AI | With AI | Speedup |
|------|-----------|---------|---------|
| Feature Development | 2-5 days | 4-8 hours | **5x** |
| Bug Fixing | 2-4 hours | 15-30 min | **8x** |
| Writing Tests | 4-8 hours | 30 min | **10x** |
| Documentation | 2-4 hours | 10 min | **15x** |
| Code Review | 1-2 hours | 10 min | **6x** |

**Overall: 5-10x productivity increase**

## 🎓 Examples

### Example 1: Building Authentication

**Prompt to Claude Code:**
```
Build a complete authentication system with:
- Email/password login
- JWT tokens
- Password reset flow
- Email verification
- Protected routes

Tech: Next.js 14, Supabase, TypeScript
Include tests and error handling.
```

**Result:** Complete auth system in 1 hour (vs 8 hours manually)

### Example 2: Adding Stripe Payments

**Prompt:**
```
Integrate Stripe payments with:
- Checkout page
- Webhook handling
- Subscription management
- Invoice generation

Include error handling and tests.
```

**Result:** Payment system in 2 hours (vs 2 days manually)

### Example 3: Automated Testing

**Prompt:**
```
Generate comprehensive tests for [component]:
- Unit tests for all functions
- Integration tests for API calls
- E2E tests for user flows
- Edge cases and error scenarios
```

**Result:** Full test suite in 15 minutes (vs 4 hours manually)

## 🎯 Best Practices

### 1. Trust but Verify
- Review all AI-generated code
- Understand the implementation
- Test thoroughly before deploying

### 2. Build a Prompt Library
- Save successful prompts
- Create templates for common tasks
- Iterate and improve prompts

### 3. Iterate with AI
- Start with rough requirements
- Refine based on output
- Build incrementally

### 4. Automate Everything
- Testing → AI-generated
- Documentation → AI-generated
- Code review → AI-assisted
- Deployment → Fully automated

### 5. Focus on Architecture
- Let AI handle implementation details
- You focus on system design
- Review and guide AI output

## 📊 Success Metrics

**Track these to measure AI impact:**
- Time to ship features (should decrease 5x)
- Test coverage (should increase to 90%+)
- Bug rate (should decrease 50%+)
- Documentation completeness (should reach 100%)
- Code review time (should decrease 80%+)

## 🔗 Resources

- [Claude Code Documentation](https://claude.ai/code)
- [Cursor Documentation](https://cursor.sh/docs)
- [GitHub Copilot Guide](https://github.com/features/copilot)
- [v0.dev](https://v0.dev)

## 📖 Usage with Claude Code

Reference this skill in your conversations:

```
"Use ai-coding-workflow to help me set up my development environment"
"Help me build [feature] using AI tools"
"Generate tests for my code using AI"
"Review my code with AI assistance"
```

---

**Remember**: AI doesn't replace developers—it makes them 10x more productive.

---

[中文版本 / Chinese Version](./README.zh-CN.md)
