# Examples: postGenerateApiName

**POST /settings/variables/actions/generate_api_name**

## Request examples

### `application/json` — SamplePostRequest

Sample request body

```json
{
  "variables": [
    {
      "name": "nothingGenerate2",
      "variable_group": {
        "id": "400000000470050090988",
        "name": "General",
        "api_name": "General"
      }
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
        "api_name": "nothingGenerate2"
      },
      "message": "the api name is generated successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

Error response with code MANDATORY_NOT_FOUND: required field not found (Field: variable_group)

```json
{
  "variables": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "variable_group",
        "json_path": "$.variables[0].variable_group"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: name)

```json
{
  "variables": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "name",
        "json_path": "$.variables[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response with code INVALID_DATA: Invalid data type (Field: name)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.variables[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Error response with code INVALID_DATA: Invalid data (Field: name)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 16,
        "json_path": "$.variables[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Error response with code INVALID_DATA: Invalid data type (Field: variable_group)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "variable_group",
        "expected_data_type": "jsonobject",
        "json_path": "$.variables[*].variable_group"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

Error response with code INVALID_DATA: Invalid data (Field: id)

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 21,
        "json_path": "$.variables[*].variable_group.id"
      },
      "status": "error"
    }
  ]
}
```
