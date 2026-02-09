# Contributing to Awesome Agent APIs

Thanks for your interest in contributing! 🎉

## How to Contribute

1. **Fork** this repository
2. **Add your API** to the appropriate category in `README.md`
3. **Follow the format**:
   ```markdown
   | [API Name](https://example.com) | Brief description | Auth type | ✅/❌ HTTPS | ✅/⚠️/❌ |
   ```
4. **Submit a Pull Request**

## Inclusion Criteria

Your API should meet these requirements:

### ✅ Required
- Publicly accessible (not internal/private)
- Returns JSON (or easily parseable format)
- Stable and actively maintained
- Has documentation
- No human verification (CAPTCHA, phone verification, etc.)

### ⭐ Preferred
- No authentication required, or simple API key
- Rate limits: 100+ requests/day minimum
- HTTPS enabled
- CORS enabled
- Predictable response structure
- Agent-friendly documentation

### ❌ Not Accepted
- OAuth flows requiring browser interaction
- APIs with frequent breaking changes
- APIs requiring human verification steps
- APIs with rate limits under 100 req/day
- APIs that explicitly block automation
- Paid-only APIs (freemium is OK)

## Categories

If your API doesn't fit existing categories, propose a new one!

Current categories:
- Betting & Prediction Markets
- Blockchain & Crypto
- Data & Information
- Weather
- Finance
- Search & Knowledge
- Communication
- No Auth Required (cross-reference section)

## Pull Request Guidelines

- Keep descriptions concise (1 line)
- Maintain alphabetical order within categories
- Test the API before submitting
- Include HTTPS status and agent-friendliness rating
- Add to "No Auth Required" section if applicable

## Agent-Friendly Rating Guide

- ✅ = Excellent for agents (no auth, stable, good docs)
- ⚠️ = Usable but has limitations (rate limits, auth required)
- ❌ = Not recommended (unstable, poor docs, blocks automation)
- ⭐ = Exceptional (built specifically for agents)

## Questions?

Open an issue or reach out to [@hoony_han](https://t.me/hoony_han) on Telegram.

---

**Note**: This is a curated list. Not all submissions will be accepted. Priority is given to APIs that provide genuine value to AI agents and automation use cases.
