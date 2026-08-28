# Examples: getReplacedValues

**GET /settings/global_picklists/{id}/actions/replaced_values**

## Parameter examples

### `id` (path) — Example

```json
"111111000000055938"
```

## Response examples

### Status `200` — `application/json` — ReplacedValuesExample

Example response with replaced values

```json
{
  "replaced_values": [
    {
      "display_value": "Cold",
      "reference_value": "Colder"
    },
    {
      "display_value": "Warm",
      "reference_value": "Warmer"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidaId

Invalid ID example

```json
{
  "code": "INVALID_DATA",
  "message": "the id given seems to be invalid",
  "details": {
    "resource_path_index": 2
  },
  "status": "error"
}
```

### Status `400` — `application/json` — DeletionInProgress

Deletion in progress example

```json
{
  "code": "NOT_ALLOWED",
  "message": "global picklist deletion in progress.",
  "details": {
    "resource_path_index": 2
  },
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
