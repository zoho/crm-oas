# Examples: deleteHoliday

**DELETE /settings/holidays/{holidayId}**

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

## Response examples

### Status `200` — `application/json` — Default

Default response confirming holiday deletion

```json
{
  "holidays": []
}
```

### Status `400` — `application/json` — InvalidId

Invalid holiday ID in request path

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "Invalid ID",
  "status": "error"
}
```
