# Mintlify broken-link reconciliation

Date: 2026-08-11

## Result

- Total reported link occurrences: **254**
- Unique reported targets: **76**
- Proven valid: **76 unique targets / 254 occurrences**
- Genuinely broken: **0**
- Ambiguous: **0**
- Exact fixes required: **none**

The Mintlify CLI reports these root-relative links as broken because its local checker attempts filesystem resolution from the command context. Each target below was normalized to the expected Mintlify route and verified against an existing .mdx file in this docs project. The table preserves every unique reported target and its occurrence count; repeated occurrences are grouped by target.

| Reported route | Occurrences | Verified source file route | Classification |
|---|---:|---|---|
| /product/accounting/bank/reconcile-bank | 5 | /product/accounting/bank/reconcile-bank.mdx | proven valid |
| /product/accounting/cash/cash-disbursements | 3 | /product/accounting/cash/cash-disbursements.mdx | proven valid |
| /product/accounting/cash/cash-receipts | 3 | /product/accounting/cash/cash-receipts.mdx | proven valid |
| /product/accounting/chart-of-accounts | 3 | /product/accounting/chart-of-accounts.mdx | proven valid |
| /product/accounting/credit-notes | 1 | /product/accounting/credit-notes.mdx | proven valid |
| /product/accounting/financial-reports | 14 | /product/accounting/financial-reports.mdx | proven valid |
| /product/accounting/journals/create-journal-entry | 4 | /product/accounting/journals/create-journal-entry.mdx | proven valid |
| /product/accounting/journals/post-reverse | 4 | /product/accounting/journals/post-reverse.mdx | proven valid |
| /product/accounting/overview | 3 | /product/accounting/overview.mdx | proven valid |
| /product/accounting/payables/approve-pay-bill | 4 | /product/accounting/payables/approve-pay-bill.mdx | proven valid |
| /product/accounting/payables/create-supplier-bill | 3 | /product/accounting/payables/create-supplier-bill.mdx | proven valid |
| /product/accounting/periods/close-period | 5 | /product/accounting/periods/close-period.mdx | proven valid |
| /product/accounting/periods/reopen-period | 3 | /product/accounting/periods/reopen-period.mdx | proven valid |
| /product/accounting/reports/ap-aging | 1 | /product/accounting/reports/ap-aging.mdx | proven valid |
| /product/accounting/reports/ar-aging | 1 | /product/accounting/reports/ar-aging.mdx | proven valid |
| /product/accounting/reports/balance-sheet | 1 | /product/accounting/reports/balance-sheet.mdx | proven valid |
| /product/accounting/reports/bank-reconciliation-readiness | 1 | /product/accounting/reports/bank-reconciliation-readiness.mdx | proven valid |
| /product/accounting/reports/cash-flow | 1 | /product/accounting/reports/cash-flow.mdx | proven valid |
| /product/accounting/reports/chart-balances | 1 | /product/accounting/reports/chart-balances.mdx | proven valid |
| /product/accounting/reports/general-ledger | 4 | /product/accounting/reports/general-ledger.mdx | proven valid |
| /product/accounting/reports/profit-loss | 1 | /product/accounting/reports/profit-loss.mdx | proven valid |
| /product/accounting/reports/trial-balance | 1 | /product/accounting/reports/trial-balance.mdx | proven valid |
| /product/accounting/tax/tax-center | 1 | /product/accounting/tax/tax-center.mdx | proven valid |
| /product/agreements/invoices/create-invoice | 3 | /product/agreements/invoices/create-invoice.mdx | proven valid |
| /product/agreements/invoices/fulfillment | 2 | /product/agreements/invoices/fulfillment.mdx | proven valid |
| /product/agreements/invoices/post-invoice | 9 | /product/agreements/invoices/post-invoice.mdx | proven valid |
| /product/agreements/invoices/record-payment | 10 | /product/agreements/invoices/record-payment.mdx | proven valid |
| /product/agreements/invoices/void-refund | 3 | /product/agreements/invoices/void-refund.mdx | proven valid |
| /product/agreements/overview | 2 | /product/agreements/overview.mdx | proven valid |
| /product/agreements/quotes/create-quote | 4 | /product/agreements/quotes/create-quote.mdx | proven valid |
| /product/agreements/quotes/revisions | 1 | /product/agreements/quotes/revisions.mdx | proven valid |
| /product/agreements/quotes/send-follow-up | 2 | /product/agreements/quotes/send-follow-up.mdx | proven valid |
| /product/agreements/quotes/status-expiry | 4 | /product/agreements/quotes/status-expiry.mdx | proven valid |
| /product/dashboard/customize-dashboard | 1 | /product/dashboard/customize-dashboard.mdx | proven valid |
| /product/inventory/goods-receipts/create-goods-receipt | 4 | /product/inventory/goods-receipts/create-goods-receipt.mdx | proven valid |
| /product/inventory/goods-receipts/damaged-on-hold | 3 | /product/inventory/goods-receipts/damaged-on-hold.mdx | proven valid |
| /product/inventory/goods-receipts/post-goods-receipt | 5 | /product/inventory/goods-receipts/post-goods-receipt.mdx | proven valid |
| /product/inventory/overview | 1 | /product/inventory/overview.mdx | proven valid |
| /product/inventory/products/create-product | 2 | /product/inventory/products/create-product.mdx | proven valid |
| /product/inventory/products/product-margin | 2 | /product/inventory/products/product-margin.mdx | proven valid |
| /product/inventory/products/stock-levels | 5 | /product/inventory/products/stock-levels.mdx | proven valid |
| /product/inventory/purchase-orders/create-purchase-order | 7 | /product/inventory/purchase-orders/create-purchase-order.mdx | proven valid |
| /product/inventory/purchase-orders/receive-purchase-order | 5 | /product/inventory/purchase-orders/receive-purchase-order.mdx | proven valid |
| /product/inventory/purchase-orders/statuses | 3 | /product/inventory/purchase-orders/statuses.mdx | proven valid |
| /product/inventory/suppliers/create-supplier | 4 | /product/inventory/suppliers/create-supplier.mdx | proven valid |
| /product/marketing/campaigns/create-campaign | 2 | /product/marketing/campaigns/create-campaign.mdx | proven valid |
| /product/marketing/overview | 1 | /product/marketing/overview.mdx | proven valid |
| /product/reports/build-report | 4 | /product/reports/build-report.mdx | proven valid |
| /product/reports/catalog | 2 | /product/reports/catalog.mdx | proven valid |
| /product/reports/overview | 3 | /product/reports/overview.mdx | proven valid |
| /product/reports/schedule-report | 4 | /product/reports/schedule-report.mdx | proven valid |
| /product/reports/use-report-catalog | 4 | /product/reports/use-report-catalog.mdx | proven valid |
| /product/sales/activities/log-activity | 2 | /product/sales/activities/log-activity.mdx | proven valid |
| /product/sales/companies/manage-company | 2 | /product/sales/companies/manage-company.mdx | proven valid |
| /product/sales/deals/close-deal | 8 | /product/sales/deals/close-deal.mdx | proven valid |
| /product/sales/deals/create-deal | 1 | /product/sales/deals/create-deal.mdx | proven valid |
| /product/sales/deals/deal-value | 2 | /product/sales/deals/deal-value.mdx | proven valid |
| /product/sales/deals/manage-pipeline | 5 | /product/sales/deals/manage-pipeline.mdx | proven valid |
| /product/sales/deals/reopen-deal | 1 | /product/sales/deals/reopen-deal.mdx | proven valid |
| /product/sales/leads/assign-lead | 2 | /product/sales/leads/assign-lead.mdx | proven valid |
| /product/sales/leads/create-lead | 3 | /product/sales/leads/create-lead.mdx | proven valid |
| /product/sales/leads/filter-leads | 1 | /product/sales/leads/filter-leads.mdx | proven valid |
| /product/sales/leads/qualify-lead | 7 | /product/sales/leads/qualify-lead.mdx | proven valid |
| /product/sales/overview | 1 | /product/sales/overview.mdx | proven valid |
| /product/support/overview | 2 | /product/support/overview.mdx | proven valid |
| /product/support/sla/understand-sla | 5 | /product/support/sla/understand-sla.mdx | proven valid |
| /product/support/sla-automation | 2 | /product/support/sla-automation.mdx | proven valid |
| /product/support/tickets/assign-manage | 5 | /product/support/tickets/assign-manage.mdx | proven valid |
| /product/support/tickets/create-ticket | 6 | /product/support/tickets/create-ticket.mdx | proven valid |
| /reference/calculations/accounting-metrics | 3 | /reference/calculations/accounting-metrics.mdx | proven valid |
| /reference/calculations/inventory-metrics | 2 | /reference/calculations/inventory-metrics.mdx | proven valid |
| /reference/calculations/sales-metrics | 8 | /reference/calculations/sales-metrics.mdx | proven valid |
| /teams/access/action-permissions | 3 | /teams/access/action-permissions.mdx | proven valid |
| /teams/access/product-areas | 9 | /teams/access/product-areas.mdx | proven valid |
| /teams/approvals/using-approvals | 1 | /teams/approvals/using-approvals.mdx | proven valid |
| /teams/members/invite-member | 3 | /teams/members/invite-member.mdx | proven valid |

## Verification method

For every CLI-reported route, the leading slash was removed and the following candidates were checked in order: .mdx, .md, /index.mdx, /index.md. A target was proven valid only when exactly one file-backed route existed. No target had zero matches or multiple matches.

Navigation and route integrity were also checked with npx mintlify validate; it passed. The existing navigation remains unchanged because no genuinely broken target was found.

