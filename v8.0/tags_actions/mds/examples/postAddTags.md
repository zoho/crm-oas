# Examples: postAddTags

**POST /{module}/actions/add_tags**

## Parameter examples

### `module` (path) — Example

```json
"Leads"
```

## Request examples

### `application/json` — SamplePostRequest

Sample request body

```json
{
  "tags": [
    {
      "name": "test",
      "color_code": "#F17574"
    },
    {
      "name": "new",
      "color_code": "#63C57E"
    },
    {
      "name": "34ytwerfdgjhfwgerfs",
      "color_code": "#E7A826"
    }
  ],
  "ids": "[\"3060320000002538026\"]",
  "over_write": true
}
```

## Response examples

### Status `200` — `application/json` — Success200

Success response for status 200

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "3060320000002538026",
        "affected_data": null,
        "tags": [
          {
            "name": "test",
            "id": "3060320000000666862",
            "color_code": "#F17574"
          },
          {
            "name": "new",
            "id": "3060320000000669006",
            "color_code": "#63C57E"
          },
          {
            "name": "34ytwerfdgjhfwgerfs",
            "id": "3060320000000666022",
            "color_code": "#E7A826"
          }
        ]
      },
      "message": "tags updated successfully",
      "status": "success"
    }
  ],
  "locked_count": "0"
}
```

### Status `400` — `application/json` — RecordLockedResponse1

Error response with code RECORD_LOCKED: Sorry, you cannot perform this operation as the record is locked.

```json
{
  "code": "RECORD_LOCKED",
  "details": {
    "action": "record_locking",
    "id": "3060320000002538026"
  },
  "message": "Sorry, you cannot perform this operation as the record is locked.",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response with code INVALID_DATA: invalid data (Field: tags)

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 3,
    "api_name": "tags",
    "json_path": "$.tags"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModuleResponse1

Error response with code INVALID_MODULE: the module name given seems to be invalid

```json
{
  "code": "INVALID_MODULE",
  "details": {},
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModuleResponse2

Error response with code INVALID_MODULE: the given module is not supported for this api

```json
{
  "code": "INVALID_MODULE",
  "details": {},
  "message": "the given module is not supported for this api",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidRequestMethodResponse1

Error response with code INVALID_REQUEST_METHOD: The http request method type is not a valid one

```json
{
  "code": "INVALID_REQUEST_METHOD",
  "details": {},
  "message": "The http request method type is not a valid one",
  "status": "error"
}
```

### Status `400` — `application/json` — RequiredParamMissingResponse1

Error response with code REQUIRED_PARAM_MISSING: One of the expected param is missing

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

### Status `400` — `application/json` — InvalidDataResponse2

Error response with code INVALID_DATA: Invalid data type (Field: name)

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

Error response with code INVALID_DATA: Invalid data (Field: name)

```json
{
  "tags": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 25,
        "json_path": "$.tags[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

Error response with code INVALID_DATA: Invalid data type (Field: color_code)

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

Error response with code INVALID_DATA: Invalid data (Field: color_code)

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

Error response with code NO_PERMISSION: permission denied

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Edit_Leads",
      "Crm_Implied_Tags_Leads"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
