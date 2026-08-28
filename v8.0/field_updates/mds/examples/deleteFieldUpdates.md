# Examples: deleteFieldUpdates

**DELETE /settings/automation/field_updates**

## Response examples

### Status `200` — `application/json` — BulkDeleteAllSuccess

All requested field updates deleted successfully

```json
{
  "field_updates": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000090003"
      },
      "message": "field update deleted successfully",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000090007"
      },
      "message": "field update deleted successfully",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — BulkDeleteMixedResult

Mixed response  - one invalid ID, one success, one associated field update

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "111111000000090003"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000081106"
      },
      "message": "field update deleted successfully",
      "status": "success"
    },
    {
      "code": "NOT_ALLOWED",
      "details": {
        "id": "111111000000064003"
      },
      "message": "This field update is associated with at least one of Approval Process/Workflow Rules/Blueprint",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — IdsMissingResponse

Error when the required ids query parameter is not provided

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "ids"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — BulkDeleteAllFailed

All provided IDs failed  - mix of invalid IDs and associated field updates

```json
{
  "field_updates": [
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "111111000000199637"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "111111000000227042"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "111111000000129018"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — IdsLimitExceededResponse

Error when more than 10 IDs are provided in the ids parameter

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 10,
    "param_name": "ids"
  },
  "message": "Ids maximum length exceeded",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse1

Error response with code NO_PERMISSION: feature not available in this edition

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Workflow",
      "Crm_Implied_Customize_Zoho_CRM",
      "Crm_Implied_Manage_ConnectedWorkflow"
    ]
  },
  "message": "feature not available in this edition",
  "status": "error"
}
```
