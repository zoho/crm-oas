# Examples: replacePicklistValues

**POST /settings/global_picklists/{id}/actions/replace_picklist_values**

## Parameter examples

### `id` (path) — Example

```json
"111111000000055938"
```

## Request examples

### `application/json` — ReplacedValuesExample

```json
{
  "replace_picklist_values": [
    {
      "old_value": {
        "id": "111111000000055938",
        "display_value": "abc"
      },
      "new_value": {
        "id": "111111000000055948",
        "display_value": "def"
      }
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — ImmediateCompletionExample

```json
{
  "replace_picklist_values": [
    {
      "code": "SUCCESS",
      "details": {},
      "message": "success",
      "status": "success"
    }
  ]
}
```

### Status `202` — `application/json` — ScheduledReplacementExample

```json
{
  "replace_picklist_values": [
    {
      "code": "SCHEDULED",
      "details": {
        "job_id": "111111000000084605"
      },
      "message": "success",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataExample

Invalid data error

```json
{
  "replace_picklist_values": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.replace_picklist_values[0].old_value.id"
      },
      "message": "The given value seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — TopLevelErrorExample

Top-level error

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 2
  },
  "message": "global picklist deletion in progress.",
  "status": "error"
}
```

### Status `403` — `application/json` — ErrorExample

```json
{
  "code": "NO_PERMISSION",
  "message": "permission denied",
  "details": {
    "permissions": [
      "Crm_Implied_Customize_Zoho_CRM"
    ]
  },
  "status": "error"
}
```

### Status `500` — `application/json` — ErrorExample

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error",
  "details": {},
  "status": "error"
}
```
