# Examples: getWebhookFailures

**GET /settings/automation/webhook_failures**

## Response examples

### Status `200` — `application/json` — Success200

Successful retrieval of webhook execution failure records


```json
{
  "webhook_failures": [
    {
      "webhook": {
        "name": "Premium Lead Alert",
        "id": "4876876000016390771"
      },
      "entity_details": {
        "module": {
          "api_name": "Leads",
          "id": "4876876000000002175"
        },
        "name": "Freelancer.com",
        "id": "4876876000016474049"
      },
      "failure_time": "2025-10-21T17:08:07+05:30",
      "failure_reason": "page_notfound",
      "id": "4876876000016474075",
      "workflow_rule": {
        "name": "WF-C",
        "id": "4876876000016390881"
      }
    }
  ],
  "info": {
    "per_page": 200,
    "count": 1,
    "page": 1,
    "more_records": false
  }
}
```

### Status `400` — `application/json` — InvalidModuleResponse1

Error for unrecognized module API name in module parameter


```json
{
  "code": "INVALID_MODULE",
  "details": {
    "param_name": "module"
  },
  "message": "The value provided to the param is Invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error for invalid action ID in webhook_id parameter


```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "webhook_id"
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Error for malformed date format in from or to parameter


```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "from",
    "expected_data_type": "datetime"
  },
  "message": "The value provided to the param is Invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Error for future date in from or to parameter


```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "to",
    "expected_data_type": "datetime"
  },
  "message": "The value provided to the param is Invalid",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse1

Error for missing Manage Workflow permission


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
