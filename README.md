# eBay item details API — examples

Full detail per eBay item id — price, condition, seller, item specifics, photos.

**Live page, full schema & pricing → [quanticdata.io/collectors/ebay-product-api/](https://quanticdata.io/collectors/ebay-product-api/)**

One row per eBay item: title, price with parsed value and currency, condition, seller with positive-feedback percent, availability line, photos, the item-specifics grid (brand, model, size… as label → value pairs) and the category breadcrumb. Pair with ebay_search to discover item ids. Ended or removed listings are reported under failed, never billed.

## Quick start (curl)

```bash
curl -X POST https://api.quanticdata.io/v1/scraper/collectors/ebay_product/run \
  -H "Authorization: Bearer $QD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"items": ["158070397228"], "max_results": 1}'
```

## Python

See [`example.py`](example.py):

```bash
export QD_API_KEY=qd_live_...   # https://quanticdata.io/
python3 example.py
```

## Inputs

- `items` (array, required) — eBay item ids or /itm/ URLs (ebay_search returns both).
- `country` (string) — ISO 3166-1 alpha-2 code — proxy exit geo and Google locale (gl). Omit for the default pool.
- `max_results` (integer) — How many products to deliver at most (1–20). You pay only for delivered products.

## Output — one row per product

| field | type | description |
|---|---|---|
| `item_id` | string | eBay item id. |
| `url` | string | Item URL. |
| `title` | string | Item title. |
| `subtitle` | string | Subtitle when present. |
| `price` | string | Price as shown ("US $98.00"). |
| `price_value` | number | Parsed price. |
| `currency` | string | Price currency (best-effort). |
| `condition` | string | Item condition. |
| `seller` | string | Seller name. |
| `seller_feedback_pct` | number | Seller positive feedback %. |
| `availability` | string | Quantity/availability line. |
| `images` | string[] | Item photos (up to 6). |
…and 2 more fields — full schema on the [live page](https://quanticdata.io/collectors/ebay-product-api/).

## Pricing

**$0.003 per delivered product** ($3 per 1,000). A run that delivers nothing costs nothing, and failed rows are never billed. The $2/month free allowance covers roughly 666 products — no card required.

## Links

- This collector: https://quanticdata.io/collectors/ebay-product-api/
- All collectors: https://quanticdata.io/collectors/
- Docs: https://quanticdata.io/docs/
