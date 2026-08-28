# Examples: deleteServicesS

**DELETE /Services__s**

## Response examples

### Status `200` — `application/json` — Success200

Single service record deleted successfully

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4671651000000867047"
      },
      "message": "record deleted",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — Success207

Mixed batch delete when one record deleted, one fails with INVALID_DATA

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "4671651000010893004"
      },
      "message": "record not deleted",
      "status": "error",
      "error_meta": "invalid_field"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "4671651000000950132"
      },
      "message": "record deleted",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Delete fails with INVALID_DATA where service ID is incorrect or already deleted

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 1
  },
  "message": "record not deleted",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModuleResponse1

Delete fails with INVALID_MODULE when module name in the request URL is invalid

```json
{
  "code": "INVALID_MODULE",
  "details": {
    "resource_path_index": 0
  },
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — RequiredParamMissingResponse1

Required parameter missing when ids query parameter absent from DELETE request

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param": "ids"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — InternalErrorResponse1

Delete request fails due to an internal server error

```json
{
  "code": "INTERNAL_ERROR",
  "details": {},
  "message": "Internal Server Error",
  "status": "error"
}
```
