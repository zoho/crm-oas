# Examples: deleteServiceById

**DELETE /Services__s/{id}**

## Response examples

### Status `200` — `application/json` — Success200

Successful deletion of a single service record

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111115000000128210"
      },
      "message": "record deleted",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Invalid data error for a service record that could not be deleted

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

Invalid module name error for a service DELETE request

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

Missing service ID parameter error for a DELETE request

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

Internal server error during a service DELETE request

```json
{
  "code": "INTERNAL_ERROR",
  "details": {},
  "message": "Internal Server Error",
  "status": "error"
}
```
