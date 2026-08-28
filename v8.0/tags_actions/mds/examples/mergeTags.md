# Examples: mergeTags

**POST /settings/tags/{id}/actions/merge**

## Request examples

### `application/json` — SamplePostRequest

Sample request body

```json
{
  "tags": [
    {
      "conflict_id": "3060320000001987032",
      "modified_time": "2025-09-25T12:00:04+05:30"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Success response for status 200

```json
{
  "tags": [
    {
      "code": "SUCCESS",
      "details": {
        "created_time": "2025-09-25T12:00:04+05:30",
        "modified_time": "2025-12-30T17:35:44+05:30",
        "modified_by": {
          "name": "Amelia Burrows",
          "id": "3060320000000520001"
        },
        "id": "3060320000001987032",
        "created_by": {
          "name": "Amelia Burrows",
          "id": "3060320000000520001"
        },
        "color_code": "#1DB9B4"
      },
      "message": "tags merged successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response with code INVALID_DATA: invalid data (Field: tags)

```json
{
  "code": "INVALID_DATA",
  "details": {
    "expected_data_type": "jsonarray",
    "api_name": "tags",
    "json_path": "$.tags"
  },
  "message": "invalid data",
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

### Status `400` — `application/json` — InvalidDataResponse2

Error response with code INVALID_DATA: invalid data (Field: id)

```json
{
  "tags": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.tags[0].id"
      },
      "message": "Invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Error response with code INVALID_DATA: Invalid data type (Field: conflict_id)

```json
{
  "tags": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "conflict_id",
        "expected_data_type": "bigint",
        "json_path": "$.tags[*].conflict_id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

Error response with code INVALID_DATA: Invalid data (Field: conflict_id)

```json
{
  "tags": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "conflict_id",
        "maximum_length": 19,
        "json_path": "$.tags[*].conflict_id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

Error response with code INVALID_DATA: Invalid data type (Field: modified_time)

```json
{
  "tags": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "modified_time",
        "expected_data_type": "datetime",
        "json_path": "$.tags[*].modified_time"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse6

Error response with code INVALID_DATA: Invalid data (Field: modified_time)

```json
{
  "tags": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "modified_time",
        "maximum_length": 25,
        "json_path": "$.tags[*].modified_time"
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
  "tags": [
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
  ]
}
```
