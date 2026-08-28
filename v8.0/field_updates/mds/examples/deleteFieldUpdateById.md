# Examples: deleteFieldUpdateById

**DELETE /settings/automation/field_updates/{id}**

## Response examples

### Status `200` — `application/json` — Success200

Success response for status 200

```json
{
  "field_updates": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "3361265000006131027"
      },
      "message": "field update deleted successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — FieldUpdatesInvalidData

Error response with code INVALID_DATA: the id given seems to be invalid

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 3
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — RequiredParamMissingResponse1

Error response with code REQUIRED_PARAM_MISSING: One of the expected parameter is missing

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "id"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — ReadOnlyActionNotAllowed1

Error response with code NOT_ALLOWED: field update can not be deleted

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 3
  },
  "message": "field update can not be deleted",
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
