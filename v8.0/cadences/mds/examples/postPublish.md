# Examples: postPublish

**POST /settings/automation/cadences/{id}/actions/publish**

## Request examples

### `application/json` — SamplePutRequestManualType

Sample minimal publish request

```json
{
  "cadences": []
}
```

### `application/json` — SamplePutRequestCustomView

Sample publish request with process existing records

```json
{
  "cadences": [
    {
      "process_existing_records": true
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Successful Cadence publish response

```json
{
  "cadences": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111112000000092007"
      },
      "message": "Cadences published successfully",
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

### Status `400` — `application/json` — NotAllowedResponse1

Cannot merge published Cadences error

```json
{
  "code": "NOT_ALLOWED",
  "details": {},
  "message": "Cannot merge published Cadences / Only Cadences in draft can be merged with its parent",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowedResponse2

No follow-up actions in Cadence error

```json
{
  "code": "NOT_ALLOWED",
  "details": {},
  "message": "Cadence must contain at least one follow-up to publish",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowedResponse3

Task action not supported error

```json
{
  "code": "NOT_ALLOWED",
  "details": {},
  "message": "Task Action Not Supported in this Edition",
  "status": "error"
}
```

### Status `400` — `application/json` — NotSupportedResponse1

Custom view unsupported fields error

```json
{
  "code": "NOT_SUPPORTED",
  "details": {},
  "message": "The custom_view contains unsupported fields in the criteria",
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

### Status `400` — `application/json` — InvalidKeyInRequestBody

Invalid key in request body error

```json
{
  "cadences": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "process_existing_records",
        "json_path": "$.cadences[0].process_existing_records"
      },
      "message": "For manual Enrollment we wont add process_existing_records key not allowed",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionResponse1

No permission to publish Cadence error

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
