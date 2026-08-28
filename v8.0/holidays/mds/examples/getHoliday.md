# Examples: getHoliday

**GET /settings/holidays/{holidayId}**

## Parameter examples

### `holidayId` (path) — Default

Example holiday ID

```json
"5725767000000525001"
```

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

Default response with holiday details

```json
{
  "holidays": []
}
```
