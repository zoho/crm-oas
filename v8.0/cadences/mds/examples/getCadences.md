# Examples: getCadences

**GET /settings/automation/cadences**

## Response examples

### Status `200` — `application/json` — SuccessfulList

Successful Cadence list response

```json
{
  "cadences": [
    {
      "summary": {
        "task_follow_up_count": 2,
        "call_follow_up_count": 1,
        "email_follow_up_count": 3
      },
      "description": "Cadence for leads",
      "created_time": "2025-10-30T08:46:14+00:00",
      "module": {
        "api_name": "Leads",
        "id": "111111000000002648"
      },
      "active": true,
      "execution_details": {
        "unenroll_properties": {
          "end_date": "2025-12-31",
          "type": "date"
        },
        "end_date": "2025-12-31",
        "automatic_unenroll": false,
        "type": "automatic_unenroll",
        "execute_every": {
          "unit": 1,
          "period": "days"
        }
      },
      "published": true,
      "type": "Custom view",
      "created_by": {
        "name": "Nish test",
        "id": "111111000000057812"
      },
      "modified_time": "2025-01-01T16:43:11+05:30",
      "name": "Onboard Leads",
      "modified_by": {
        "name": "Nish test",
        "id": "111111000000057812"
      },
      "id": "2001",
      "custom_view": {
        "name": "All Contacts",
        "id": "111111000000051423"
      },
      "status": "active"
    }
  ],
  "info": {
    "per_page": 20,
    "count": 1,
    "page": 1,
    "more_records": false
  }
}
```

### Status `400` — `application/json` — ErrorResponse1

Invalid module name error

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "module"
  },
  "message": "the given module doesn't exist",
  "status": "error"
}
```

### Status `400` — `application/json` — ErrorResponse3

Invalid data type error

```json
{
  "code": "UNABLE_TO_PARSE_DATA_TYPE",
  "details": {},
  "message": "either the request body or parameters is in wrong format",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse1

No permission to retrieve Cadences error

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_View_Cadences"
    ]
  },
  "message": "No permission",
  "status": "error"
}
```
