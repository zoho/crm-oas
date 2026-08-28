# Examples: updateVariableById

**PUT /settings/variables/{id}**

## Request examples

### `application/json` — SamplePutRequest

Sample request body

```json
{
  "variables": [
    {
      "id": "40000000047003",
      "value": "This is a new value"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Success response for status 200

```json
{
  "variables": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "40000000047003"
      },
      "message": "variable updated",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response with code INVALID_DATA: invalid data

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Error response with code INVALID_DATA: invalid data (Field: variables)

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 1,
    "api_name": "variables",
    "json_path": "$.variables"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — DuplicateDataResponse1

Error response with code DUPLICATE_DATA: duplicate data (Field: name)

```json
{
  "variables": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.variables[0].name"
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDataResponse2

Error response with code DUPLICATE_DATA: duplicate data (Field: name)

```json
{
  "variables": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.variables[0].api_name"
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Error response with code INVALID_DATA: invalid data (Field: value)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "integer",
        "api_name": "value",
        "json_path": "$.variables[0].value"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

Error response with code INVALID_DATA: Invalid data type (Field: id)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.variables[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

Error response with code INVALID_DATA: Invalid data (Field: id)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 14,
        "json_path": "$.variables[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse6

Error response with code INVALID_DATA: Invalid data type (Field: value)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "value",
        "expected_data_type": "text",
        "json_path": "$.variables[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse7

Error response with code INVALID_DATA: Invalid data (Field: value)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "value",
        "maximum_length": 19,
        "json_path": "$.variables[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDataResponse3

Error response with code DUPLICATE_DATA: duplicate data (Field: name)

```json
{
  "variables": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.variables[0].name"
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDataResponse4

Error response with code DUPLICATE_DATA: duplicate data (Field: name)

```json
{
  "variables": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.variables[0].api_name"
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse8

Error response with code INVALID_DATA: invalid data (Field: value)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "integer",
        "api_name": "value",
        "json_path": "$.variables[0].value"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
