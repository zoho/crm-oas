# Examples: getHolidays

**GET /settings/holidays**

## Parameter examples

### `year` (query) — Current

Current year

```json
2024
```

### `year` (query) — Next

Next year

```json
2025
```

### `type` (query) — Business

Business holidays

```json
"business_holiday"
```

### `type` (query) — Shift

Shift holidays

```json
"shift_holiday"
```

### `shift_id` (query) — Default

Example shift ID

```json
"5725767000000296005"
```

## Response examples

### Status `200` — `application/json` — Default

Default response with empty holidays list

```json
{
  "holidays": []
}
```

### Status `400` — `application/json` — PatternNotMatched

Invalid query parameter value

```json
{
  "code": "PATTERN_NOT_MATCHED",
  "details": {
    "param_name": "type"
  },
  "message": "Please check whether the input values are correct",
  "status": "error"
}
```
