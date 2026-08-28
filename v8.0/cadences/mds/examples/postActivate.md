# Examples: postActivate

**POST /settings/automation/cadences/{id}/actions/activate**

## Request examples

### `application/json` — SamplePutRequest

Sample activate request body

```json
{}
```

## Response examples

### Status `200` — `application/json` — Success200

Successful Cadence activation response

```json
{
  "cadences": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111112000000092007"
      },
      "message": "Cadences activated successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Invalid Cadence ID error

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 3
  },
  "message": "the given id seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — AlreadyActivatedResponse1

Cadence already activated error

```json
{
  "code": "ALREADY_ACTIVATED",
  "details": {
    "resource_path_index": 3
  },
  "message": "The cadences is already activated",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowedResponse1

Task action not supported error

```json
{
  "code": "NOT_ALLOWED",
  "details": {},
  "message": "Task Action Not Supported in this Edition",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowedResponse2

Custom view not available error

```json
{
  "code": "NOT_ALLOWED",
  "details": {},
  "message": "Associated Custom View is not available",
  "status": "error"
}
```

### Status `400` — `application/json` — LimitExceededResponse1

Action count limit exceeded error

```json
{
  "code": "LIMIT_EXCEEDED",
  "details": {
    "limit": 70
  },
  "message": " action Configured more than allowed limit",
  "status": "error"
}
```

### Status `400` — `application/json` — LimitExceededResponse2

Cadences per module activation limit exceeded error

```json
{
  "code": "LIMIT_EXCEEDED",
  "details": {
    "limit": 30
  },
  "message": "More than 30 Cadences cannot be activated for module",
  "status": "error"
}
```

### Status `400` — `application/json` — LimitExceededResponse3

Total Cadence activation limit exceeded error

```json
{
  "code": "LIMIT_EXCEEDED",
  "details": {
    "limit": 150
  },
  "message": "More than 150 Cadences cannot be activated",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse1

No permission to activate Cadence error

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Cadences"
    ]
  },
  "message": "No permission",
  "status": "error"
}
```
