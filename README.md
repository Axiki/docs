# Lynka documentation

This repository contains the customer-facing Lynka documentation.

## Editorial model

Write for entrepreneurs and small teams who want to finish real business work. Explain the business meaning before the UI when the concept matters.

The core product story is:

1. Find prospects with LeadGen.
2. Work and qualify them in Sales.
3. Turn opportunities into Quotes, Invoices, and Payments.
4. Manage products, purchasing, receiving, and stock.
5. Keep financial records and reports in Accounting.
6. Support customers after the sale.
7. Let a small team share the same workspace with controlled access.
8. Use automation and reporting to surface what needs attention.

Do not present Lynka as a set of disconnected product areas. Product areas are navigation. Business workflows are the explanation.

## Audience

Primary audience: entrepreneurs, owner-led small businesses, and small teams, including teams of around five people where one person may wear several hats.

Regional writing should work across Africa, Europe, and the Middle East. Do not assume one tax regime, one currency, or one country's terminology.

## Claims

Use frontend source and live backend contracts for behavioral claims. Do not infer a provider, filter, permission, plan entitlement, tax rule, or automated outcome because a neighboring feature exists.

LeadGen is a first-class product story. Current verified backend behavior includes targeting payload support for search terms, geography, industries, and enrichment, metered run capacity, plan and credit-grant charge sources, and refunds for runs finalized as failed, no results, or canceled.

Current prices, included users, LeadGen allowance numbers, promotions, and billing terms belong at https://lynkacrm.com/pricing.

## Style

Use plain English. Explain terms at first use. Prefer task titles and questions people actually search for. Avoid filler, fake excitement, repeated template headings, and unsupported superlatives.

Do not use em dash or en dash characters.

## Local preview

Use the current Mintlify CLI:

```bash
mint dev
```

Before publishing, run:

```bash
python scripts/validate_docs.py
python scripts/content_audit.py
mint validate
mint broken-links
mint a11y
```

## Search and AI discovery after deployment

Mintlify generates the sitemap, robots.txt, semantic page markup, llms.txt, and llms-full.txt from the published documentation. Keep the documentation public if you want search engines and AI search tools to read it.

After deployment:

1. Open `/robots.txt` on the real docs host and verify it does not block Googlebot, Bingbot, or OAI-SearchBot.
2. Open `/llms.txt` and `/llms-full.txt` and verify the new LeadGen, Teams, workflow, Accounting, and regional pages are present with useful descriptions.
3. Submit the sitemap to Google Search Console and Bing Webmaster Tools.
4. Use `scripts/submit_indexnow.py` only for new, changed, or deleted routes after IndexNow is configured. Do not repeatedly submit the whole site after every small edit.
5. Check search results and ChatGPT referrals for the actual questions people use, then improve the page that answers that question instead of creating thin keyword variants.
6. Keep titles descriptive and distinct. Do not stuff the same keywords into every title.

The documentation is written for people first. Search metadata should help a search engine or LLM locate the right complete answer, not turn the article into SEO copy.
