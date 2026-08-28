# Examples: generateAPIName

**POST /settings/variable_groups/actions/generate_api_name**

## Request examples

### `application/json` — SamplePostRequest

Sample generate API name request body

```json
{
  "variable_groups": [
    {
      "name": "asdasd"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Successful generate API name response

```json
{
  "variable_groups": [
    {
      "code": "SUCCESS",
      "details": {
        "api_name": "variable"
      },
      "message": "the api name is generated successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response for invalid data

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 1,
    "api_name": "variable_groups",
    "json_path": "$.variable_groups"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

Error response for missing required field ID

```json
{
  "variable_groups": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "name",
        "json_path": "$.variable_groups[0].name"
      },
      "message": "required field not found",
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
        "maximum_length": 50,
        "api_name": "name",
        "json_path": "$.variable_groups[0].name"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

Error response for missing required field

```json
{
  "variable_groups": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "name",
        "json_path": "$.variable_groups[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Error response for invalid field data type

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

### Status `400` — `application/json` — InvalidDataResponse4

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
