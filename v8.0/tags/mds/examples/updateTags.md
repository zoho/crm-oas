# Examples: updateTags

**PUT /settings/tags**

## Parameter examples

### `module` (query) — Example

```json
"Leads"
```

## Request examples

### `application/json` — SamplePutRequest

Sample update tags request body

```json
{
  "tags": [
    {
      "name": "NewTag",
      "color_code": "#AAFE62",
      "id": "123456789012345678"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Successful response for tag update

```json
{
  "tags": [
    {
      "code": "SUCCESS",
      "details": {
        "created_time": "2025-12-29T10:43:05+05:30",
        "modified_time": "2025-12-29T18:56:59+05:30",
        "name": "NewTagupdate",
        "modified_by": {
          "name": "Roobini Devi",
          "id": "111111000000059475"
        },
        "id": "111111000000071739",
        "created_by": {
          "name": "Roobini Devi",
          "id": "111111000000059475"
        },
        "color_code": "#AAFE62"
      },
      "message": "tags updated successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidModuleResponse1

Error response for invalid module name

```json
{
  "code": "INVALID_MODULE",
  "details": {},
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModuleResponse2

Error response for unsupported module

```json
{
  "code": "INVALID_MODULE",
  "details": {},
  "message": "the given module is not supported for this api",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response for invalid color code value

```json
{
  "tags": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 7,
        "api_name": "color_code",
        "json_path": "$.tags[0].color_code"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponseAPI

Error response for invalid color code data

```json
{
  "tags": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "color_code",
        "json_path": "$.tags[0].color_code"
      },
      "message": "special characters found in the given name",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

Error response for missing required field name (case 1)

```json
{
  "tags": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "name",
        "json_path": "$.tags[0].name"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — RequiredParamMissingResponse1

Error response for missing required parameter (case 1)

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param": "module"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — DuplicateDataResponse1

Error response for duplicate tag name

```json
{
  "tags": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.tags[0].name",
        "id": "111111000000116258"
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidRequestMethodResponse1

Error response for invalid HTTP method

```json
{
  "code": "INVALID_REQUEST_METHOD",
  "details": {},
  "message": "The http request method type is not a valid one",
  "status": "error"
}
```

### Status `400` — `application/json` — RequiredParamMissingResponse2

Error response for missing required parameter (case 2)

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "module"
  },
  "message": "One of the expected param is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

Error response for missing required field name (case 2)

```json
{
  "tags": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "name",
        "json_path": "$.tags[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Error response for invalid tag name data type

```json
{
  "tags": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.tags[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Error response for invalid tag name

```json
{
  "tags": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 26,
        "json_path": "$.tags[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

Error response for invalid color code data type

```json
{
  "tags": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "color_code",
        "expected_data_type": "text",
        "json_path": "$.tags[*].color_code"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

Error response for invalid color code

```json
{
  "tags": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "color_code",
        "maximum_length": 7,
        "json_path": "$.tags[*].color_code"
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
      "Crm_Implied_Tags_Leads",
      "Crm_Implied_Edit_Leads"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```

### Status `404` — `application/json` — InvalidUrlPatternResponse1

Error response for invalid URL pattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error"
}
```
