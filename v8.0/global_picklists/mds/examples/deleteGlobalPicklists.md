# Examples: deleteGlobalPicklists

**DELETE /settings/global_picklists**

## Parameter examples

### `ids` (query) — Example

```json
"111111000000055938"
```

## Response examples

### Status `202` — `application/json` — AcceptedExample

```json
{
  "global_picklists": [
    {
      "code": "SCHEDULED",
      "message": "Deletion scheduled",
      "details": {
        "job_id": "job_01Fxxxxxx"
      },
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidId

```json
{
  "global_picklists": [
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "111111000000055935"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AlreadyScheduled

```json
{
  "global_picklists": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "id": "111111000000075039"
      },
      "message": "global picklist deletion in progress.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ConversionInProgress

```json
{
  "global_picklists": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "id": "111111000000075039"
      },
      "message": "global picklist conversion in progress",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AssociatedTooMany

```json
{
  "global_picklists": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "id": "111111000000068005"
      },
      "message": "global set can't be deleted as it is associated to more than 15 fields",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SystemDefined

```json
{
  "global_picklists": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "id": "11111100000005593"
      },
      "message": "Deletion of system defined global set is not allowed",
      "status": "error"
    }
  ]
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
