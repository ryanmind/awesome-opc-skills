---
name: ai-coding-workflow
description: |
  AI-powered development workflow for 10x productivity. Activate when user needs:
  (1) Set up AI coding environment (Claude Code, Cursor, Copilot)
  (2) Optimize development workflow with AI tools
  (3) Build features faster using AI assistance
  (4) Automate repetitive coding tasks
  (5) Implement AI-first development practices

  Core principle: One developer + AI agents = 10x output
---

# AI Coding Workflow

Transform your development process with AI-powered tools and workflows. This skill helps you leverage Claude Code, Cursor, GitHub Copilot, and other AI tools to achieve 10x productivity.

## Instructions

### When to Activate

Activate this skill when the user asks:
- "How do I set up an AI coding workflow?"
- "What's the best AI stack for development?"
- "How can I code faster with AI?"
- "Help me build [feature] using AI"
- "Set up automated testing with AI"

**Core Philosophy**: AI is not just an assistant—it's your development team.

---

### 1. Assess Current Setup

**Questions to ask:**
- What's your primary language/framework?
- What editor do you use?
- What type of project are you building?
- What's your biggest time sink in development?

### 2. Recommend AI Stack

**Tier 1: Essential (Start Here)**
- **Claude Code** - Primary AI pair programmer
- **Cursor** - AI-native code editor
- **GitHub Copilot** - Inline code completion

**Tier 2: Advanced**
- **v0.dev** - AI UI component generation
- **Supabase** - Backend with AI-friendly APIs
- **Vercel** - Deploy with AI optimization

**Tier 3: Automation**
- **GitHub Actions** - CI/CD automation
- **Dependabot** - Automated dependency updates
- **AI Code Review** - Automated PR reviews

### 3. Set Up Workflow

**Step 1: Development Environment**
```bash
# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Set up Cursor
# Download from cursor.sh

# Configure GitHub Copilot
# Install in your IDE
```

**Step 2: Project Structure**
```
project/
├── .cursorrules          # AI coding guidelines
├── .github/
│   └── copilot-instructions.md
├── prompts/              # Reusable AI prompts
│   ├── feature-template.md
│   ├── bug-fix-template.md
│   └── refactor-template.md
└── docs/
    └── ai-workflow.md    # Team AI guidelines
```

**Step 3: AI Prompts Library**
Create reusable prompts for common tasks:

```markdown
# Feature Development Prompt
I need to build [FEATURE]. Requirements:
- [Requirement 1]
- [Requirement 2]

Tech stack: [Stack]
Code style: [Style guide]

Please:
1. Design the architecture
2. Write the implementation
3. Add tests
4. Update documentation
```

### 4. Development Workflow

**Daily Workflow:**
1. **Morning**: Review AI-generated code from overnight automation
2. **Development**: Use Claude Code for feature development
3. **Testing**: AI-generated test cases
4. **Review**: AI code review before merge
5. **Deploy**: Automated with AI monitoring

**Feature Development:**
```
1. Describe feature to Claude Code
2. Review generated architecture
3. Iterate on implementation
4. AI generates tests
5. AI reviews code quality
6. Deploy with AI monitoring
```

### 5. Productivity Multipliers

**10x Techniques:**

1. **AI Pair Programming**
   - Describe what you want in plain English
   - Let AI write the boilerplate
   - Focus on business logic and architecture

2. **Automated Testing**
   - AI generates unit tests
   - AI generates integration tests
   - AI suggests edge cases

3. **Code Review Automation**
   - AI reviews PRs for bugs
   - AI checks code style
   - AI suggests optimizations

4. **Documentation Automation**
   - AI generates API docs
   - AI writes README files
   - AI creates code comments

5. **Refactoring at Scale**
   - AI identifies code smells
   - AI suggests refactoring
   - AI implements changes

### 6. Common Patterns

**Pattern 1: Rapid Prototyping**
```
User: "Build a user authentication system"
AI: Generates complete auth flow with:
- Login/signup pages
- JWT token handling
- Password reset
- Email verification
- Tests
```

**Pattern 2: Bug Fixing**
```
User: "Fix this bug: [error message]"
AI:
1. Analyzes error
2. Identifies root cause
3. Suggests fix
4. Implements solution
5. Adds test to prevent regression
```

**Pattern 3: Feature Addition**
```
User: "Add payment processing with Stripe"
AI:
1. Sets up Stripe integration
2. Creates payment UI
3. Handles webhooks
4. Adds error handling
5. Writes tests
```

## Examples

### Example 1: Setting Up AI Workflow

**User**: "I want to build a SaaS app faster. How do I set up an AI coding workflow?"

**Assistant**:
Let's set up a 10x AI development workflow:

**Step 1: Install Core Tools**
```bash
# Claude Code (you already have this!)
# Install Cursor
brew install --cask cursor

# Enable GitHub Copilot
# Go to GitHub settings → Copilot
```

**Step 2: Configure Your Workspace**
Create `.cursorrules` in your project:
```
# AI Coding Guidelines
- Use TypeScript for type safety
- Write tests for all features
- Follow Airbnb style guide
- Prefer functional programming
- Add JSDoc comments
```

**Step 3: Create Prompt Templates**
Save in `prompts/feature.md`:
```markdown
Build [FEATURE] with:
- Tech: Next.js 14, TypeScript, Tailwind
- Database: Supabase
- Auth: Clerk
- Payments: Stripe

Requirements:
1. [Requirement]
2. [Requirement]

Include tests and documentation.
```

**Step 4: Daily Workflow**
1. Morning: `claude code review yesterday's changes`
2. Development: Use Cursor with Copilot
3. Testing: `claude code generate tests for [file]`
4. Deploy: Automated via Vercel

**Expected Results:**
- 5x faster feature development
- 90% test coverage (AI-generated)
- Zero boilerplate writing
- Focus on business logic only

---

### Example 2: Building a Feature with AI

**User**: "Help me build a user dashboard with analytics"

**Assistant**:
Let's build this with AI assistance:

**Phase 1: Architecture (5 minutes)**
```
Claude: Design a user dashboard with:
- User profile section
- Analytics charts (revenue, users, activity)
- Recent activity feed
- Quick actions panel

Tech: Next.js 14, Recharts, Tailwind
```

**Phase 2: Implementation (30 minutes)**
```typescript
// AI generates complete dashboard
// You review and customize business logic
```

**Phase 3: Testing (10 minutes)**
```
Claude: Generate tests for dashboard component
- Unit tests for each section
- Integration tests for data fetching
- E2E tests for user interactions
```

**Phase 4: Polish (15 minutes)**
```
Claude: Add loading states, error handling, and animations
```

**Total Time: 1 hour** (vs 8 hours manually)

---

### Example 3: Automated Code Review

**User**: "Review my PR before merging"

**Assistant**:
Running AI code review:

**Security Check:**
- ✅ No hardcoded secrets
- ✅ Input validation present
- ⚠️ SQL query needs parameterization (line 45)

**Performance:**
- ✅ Efficient database queries
- ⚠️ Consider caching API response (line 78)
- ✅ Proper error handling

**Code Quality:**
- ✅ TypeScript types complete
- ✅ Tests cover main paths
- ⚠️ Missing edge case test for empty state

**Suggestions:**
1. Fix SQL injection risk on line 45
2. Add Redis caching for API calls
3. Add test for empty user list

**Estimated fix time: 15 minutes**

## AI Tools Comparison

| Tool | Best For | Cost | Learning Curve |
|------|----------|------|----------------|
| Claude Code | Full features, architecture | $20/mo | Low |
| Cursor | Daily coding, refactoring | $20/mo | Low |
| GitHub Copilot | Inline completion | $10/mo | Very Low |
| v0.dev | UI components | Free/Pro | Very Low |
| Replit AI | Quick prototypes | $20/mo | Very Low |

## Productivity Metrics

**Before AI:**
- Feature development: 2-5 days
- Bug fixing: 2-4 hours
- Testing: 4-8 hours
- Documentation: 2-4 hours
- Code review: 1-2 hours

**After AI:**
- Feature development: 4-8 hours (5x faster)
- Bug fixing: 15-30 minutes (8x faster)
- Testing: 30 minutes (10x faster)
- Documentation: 10 minutes (15x faster)
- Code review: 10 minutes (6x faster)

**Overall: 5-10x productivity increase**

## Best Practices

1. **Trust but Verify**
   - AI generates code fast, but review carefully
   - Test AI-generated code thoroughly
   - Understand what the AI wrote

2. **Iterate with AI**
   - Start with rough prompt
   - Refine based on output
   - Build incrementally

3. **Build Prompt Library**
   - Save successful prompts
   - Create templates for common tasks
   - Share with team

4. **Automate Everything**
   - Testing → AI-generated
   - Documentation → AI-generated
   - Code review → AI-assisted
   - Deployment → Automated

5. **Focus on Architecture**
   - Let AI handle implementation
   - You focus on design decisions
   - Review and guide AI output

## Resources

- [Claude Code Documentation](https://claude.ai/code)
- [Cursor Documentation](https://cursor.sh/docs)
- [GitHub Copilot Guide](https://github.com/features/copilot)
- [AI Coding Best Practices](https://github.com/ai-coding-best-practices)

---

**Remember**: AI doesn't replace developers—it makes them 10x more productive.
