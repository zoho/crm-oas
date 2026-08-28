# Examples: cloneAssignmentRule

**POST /settings/automation/assignment_rules/{id}/actions/clone**

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

## Request examples

### `application/json` — SamplePostRequest

Sample request body

```json
{
  "assignment_rules": [
    {
      "name": "Clone of assignment rule"
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — Success201

Successful Assignment Rule operation

```json
{
  "assignment_rules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "123456"
      },
      "message": "",
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

### Status `400` — `application/json` — InvalidDataResponse2

INVALID_DATA error for Assignment Rule data

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 1,
    "api_name": "assignment_rules",
    "json_path": "$.assignment_rules"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — LimitExceededResponse1

LIMIT_EXCEEDED error for Assignment Rules

```json
{
  "assignment_rules": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit": 10
      },
      "message": "limit exceeded",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDataResponse1

DUPLICATE_DATA error for Assignment Rule name

```json
{
  "assignment_rules": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.assignment_rules[0].name"
      },
      "message": "The data is already given in the name",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

MANDATORY_NOT_FOUND error for Assignment Rule name

```json
{
  "assignment_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "name",
        "json_path": "$.assignment_rules[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.assignment_rules[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 100,
        "json_path": "$.assignment_rules[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "minimum_length": 1,
        "json_path": "$.assignment_rules[*].name"
      },
      "status": "error"
    }
  ]
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
