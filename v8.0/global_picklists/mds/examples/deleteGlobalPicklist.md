# Examples: deleteGlobalPicklist

**DELETE /settings/global_picklists/{id}**

## Parameter examples

### `id` (path) — Example

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

### Status `400` — `application/json` — InvalidIdURL

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — AlreadyScheduled

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

### Status `400` — `application/json` — ConversionInProgress

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 2
  },
  "message": "global picklist conversion in progress",
  "status": "error"
}
```

### Status `400` — `application/json` — AssociatedTooMany

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 2
  },
  "message": "global set can't be deleted as it is associated to more than 15 fields",
  "status": "error"
}
```

### Status `400` — `application/json` — SystemDefined

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 2
  },
  "message": "Deletion of system defined global set is not allowed",
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
