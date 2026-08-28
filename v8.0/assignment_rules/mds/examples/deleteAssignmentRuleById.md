# Examples: deleteAssignmentRuleById

**DELETE /settings/automation/assignment_rules/{id}**

## Parameter examples

### `id` (path) — Typical

sample value 1

```json
"123456789"
```

### `id` (path) — LargeId

Maximum long value example

```json
"9223372036854775807"
```

## Response examples

### Status `200` — `application/json` — Success200

Successful Assignment Rule operation

```json
{
  "assignment_rules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "1234567890098765432"
      },
      "message": "{proper success message}",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — ErrorResponseInvalidModuleExample

INVALID_MODULE error for module parameter

```json
{
  "code": "INVALID_MODULE",
  "details": {
    "param_name": "module"
  },
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — ErrorResponseFeatureNotSupportedExample

FEATURE_NOT_SUPPORTED error for Assignment Rules

```json
{
  "code": "FEATURE_NOT_SUPPORTED",
  "details": {},
  "message": "Assignment rules not supported for current edition",
  "status": "error"
}
```

### Status `400` — `application/json` — ErrorResponseModuleNotSupportedExample

NOT_SUPPORTED error for Assignment Rules module

```json
{
  "code": "NOT_SUPPORTED",
  "details": {
    "param_name": "module"
  },
  "message": "Module not supported in assignment rules",
  "status": "error"
}
```

### Status `400` — `application/json` — ErrorResponseInvalidRequestPathParamIdExample

INVALID_DATA error for Assignment Rule ID

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 3
  },
  "message": "Invalid assignment rule id",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionToManageARErrorResponseExample

NO_PERMISSION error for Assignment Rule access

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_AR_{moduleName}"
    ]
  },
  "message": "User does not have sufficient permission to manage assignment rules of given module",
  "status": "error"
}
```
