# Examples: updateVariableGroups

**PUT /settings/variable_groups**

## Request examples

### `application/json` — SamplePutRequest

Sample bulk update variable groups request body

```json
{
  "variable_groups": [
    {
      "id": "111111000000117081",
      "name": "VarGroup",
      "api_name": "VarGroup",
      "description": "description"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Successful bulk update variable groups response

```json
{
  "variable_groups": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000117081"
      },
      "message": "variable group updated successfully",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — Success207

Multi-status bulk update variable groups response

```json
{
  "variable_groups": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000117081"
      },
      "message": "variable group updated successfully",
      "status": "success"
    },
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.variable_groups[1].name"
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response for invalid variable groups field data

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 10,
    "api_name": "variable_groups",
    "json_path": "$.variable_groups"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — DuplicateDataResponse1

Error response for duplicate variable group data

```json
{
  "variable_groups": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.variable_groups[0].name"
      },
      "message": "duplicate data",
      "status": "error"
    },
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.variable_groups[1].name"
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — CannotPerformActionResponse1

Error response for system variable group action not allowed

```json
{
  "variable_groups": [
    {
      "code": "CANNOT_PERFORM_ACTION",
      "details": {
        "api_name": "id",
        "json_path": "$.variable_groups[0].id"
      },
      "message": "the given operation is not supported for system defined variable group",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

Error response for missing required ID field

```json
{
  "variable_groups": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "id",
        "json_path": "$.variable_groups[0].id"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDataResponse2

Error response for duplicate field value

```json
{
  "variable_groups": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.variable_groups[0].name"
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDataResponse3

Error response for multiple duplicate entries

```json
{
  "variable_groups": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.variable_groups[0].api_name"
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — PatternNotMatchedResponse1

Error response for API name pattern mismatch

```json
{
  "variable_groups": [
    {
      "code": "PATTERN_NOT_MATCHED",
      "details": {
        "api_name": "variable_group.api_name",
        "json_path": "$.variable_groups[0].variable_group.api_name"
      },
      "message": "Please check whether the input values are correct",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Error response for data exceeding maximum length

```json
{
  "variable_groups": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.variable_groups[0].id"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

Error response for missing required field in update request

```json
{
  "variable_groups": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "id",
        "json_path": "$.variable_groups[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Error response for API name pattern mismatch

```json
{
  "variable_groups": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.variable_groups[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

Error response for ambiguity during processing

```json
{
  "variable_groups": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 18,
        "json_path": "$.variable_groups[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

Error response for missing required field

```json
{
  "variable_groups": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "rid",
        "expected_data_type": "text",
        "json_path": "$.variable_groups[*].rid"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse6

Error response for missing required field ID

```json
{
  "variable_groups": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "rid",
        "maximum_length": 36,
        "json_path": "$.variable_groups[*].rid"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse7

Error response for invalid variable group ID in item

```json
{
  "variable_groups": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.variable_groups[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse8

Error response for invalid request data

```json
{
  "variable_groups": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 50,
        "json_path": "$.variable_groups[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse9

Error response for invalid variable groups field type

```json
{
  "variable_groups": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.variable_groups[*].api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse10

Error response for invalid field data type

```json
{
  "variable_groups": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 100,
        "json_path": "$.variable_groups[*].api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse11

Error response for invalid field data

```json
{
  "variable_groups": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "description",
        "expected_data_type": "text",
        "json_path": "$.variable_groups[*].description"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse12

Error response for invalid variable group ID

```json
{
  "variable_groups": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "description",
        "maximum_length": 3000,
        "json_path": "$.variable_groups[*].description"
      },
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionResponse1

Error response for insufficient permissions

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Variables_Access"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
