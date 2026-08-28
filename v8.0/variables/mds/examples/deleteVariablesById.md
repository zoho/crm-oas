# Examples: deleteVariablesById

**DELETE /settings/variables/{id}**

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
      "message": "variable deleted",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response with code INVALID_DATA: Invalid ID

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

Error response with code INVALID_DATA: variable not deleted

```json
{
  "variables": [
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "40000000047007"
      },
      "message": "variable not deleted",
      "status": "error"
    }
  ]
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

### Status `403` — `application/json` — NoPermissionResponse1

Error response with code NO_PERMISSION: permission denied

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
