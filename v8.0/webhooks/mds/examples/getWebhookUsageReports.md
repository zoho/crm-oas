# Examples: getWebhookUsageReports

**GET /settings/automation/webhooks/actions/usage_reports**

## Response examples

### Status `200` — `application/json` — Success200

Successful webhook action usage report response


```json
{
  "data_usage": [
    {
      "date": "2025-10-23",
      "resource": {
        "name": "Premium Lead Alert",
        "id": "4876876000016390771"
      },
      "count": 1,
      "type": "webhooks"
    },
    {
      "date": "2025-10-21",
      "resource": {
        "name": "Premium Lead Alert",
        "id": "4876876000016390771"
      },
      "count": 1,
      "type": "webhooks"
    },
    {
      "date": "2025-10-17",
      "resource": {
        "name": "Premium Lead Alert",
        "id": "4876876000016390771"
      },
      "count": 8,
      "type": "webhooks"
    }
  ],
  "info": {
    "max_limit": 2500,
    "per_page": 200,
    "count": 3,
    "page": 1,
    "more_records": false
  }
}
```

### Status `400` — `application/json` — RequiredParamMissingResponse1

REQUIRED_PARAM_MISSING error when group_by is absent


```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "group_by"
  },
  "message": "One of the expected param is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse1

INVALID_DATA error for a future date parameter value.


```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "type"
  },
  "message": "feature type is invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse2

INVALID_DATA error for an unsupported automation type value


```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "date"
  },
  "message": "provided time is ahead",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse1

NO_PERMISSION error for insufficient profile permissions


```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_manage_workflow"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
