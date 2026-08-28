# Examples: reorderWorkflowRules

**PUT /settings/automation/workflow_rules/actions/reorder**

## Request examples

### `application/json` — SamplePutRequest

Sample request body

```json
{
  "reorder": {
    "workflow_rules": [
      {
        "id": "3361265000006559113",
        "module_specific_sequence": 3
      },
      {
        "id": "3361265000006559076",
        "module_specific_sequence": 1
      }
    ]
  }
}
```

## Response examples

### Status `200` — `application/json` — ReorderWorkflowSuccess

Success response for status 200

```json
{
  "reorder": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "3361265000006559076"
      },
      "message": "rules reordered successfully",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "3361265000006559113"
      },
      "message": "rules reordered successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — RequiredParamMissingResponse1

Error response with code REQUIRED_PARAM_MISSING: required param not found

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "module"
  },
  "message": "required param not found",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModuleResponse

Error response with code INVALID_MODULE: Invalid Module

```json
{
  "code": "INVALID_MODULE",
  "details": {
    "param_name": "module"
  },
  "message": "Invalid Module",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response with code INVALID_DATA: duplicate data (Field: module_specific_sequence)

```json
{
  "reorder": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "module_specific_sequence",
        "json_path": "$.reorder.workflow_rules[1].module_specific_sequence"
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Error response with code INVALID_DATA: duplicate data (Field: id)

```json
{
  "reorder": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.reorder.workflow_rules[1].id"
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Error response with code INVALID_DATA: Invalid process id (Field: id)

```json
{
  "reorder": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.reorder.workflow_rules[0].id"
      },
      "message": "Invalid process id",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

Error response with code INVALID_DATA: Invalid sequence number is given (Field: module_specific_sequence)

```json
{
  "reorder": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "module_specific_sequence",
        "json_path": "$.reorder.workflow_rules[1].module_specific_sequence"
      },
      "message": "Invalid sequence number is given",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

Error response with code MANDATORY_NOT_FOUND: The required data missing (Field: module_specific_sequence)

```json
{
  "reorder": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "module_specific_sequence",
        "json_path": "$.reorder.workflow_rules[1].module_specific_sequence"
      },
      "message": "The required data missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response2

Error response

```json
{
  "reorder": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "workflow_rules",
        "expected_data_type": "jsonarray",
        "json_path": "$.reorder.workflow_rules"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response3

Error response

```json
{
  "reorder": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "workflow_rules",
        "maximum_length": 2,
        "json_path": "$.reorder.workflow_rules"
      },
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionResponse

Error response for status 403

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Workflow"
    ]
  },
  "message": "feature not available in this edition",
  "status": "error"
}
```
