# Examples: lockRecord

**POST /{moduleName}/{recordId}/Locking_Information__s**

## Request examples

### `application/json` — LockRecord

Lock record request with reason

```json
{
  "data": [
    {
      "Locked_Reason__s": "Locking the record for review"
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — SuccessCase

Successful record lock

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2021-07-13T18:54:49+05:30",
        "Modified_By": {
          "name": "priya",
          "id": "111111000000047241"
        },
        "Created_Time": "2021-07-13T18:54:49+05:30",
        "id": "111111000000054029",
        "Created_By": {
          "name": "priya",
          "id": "111111000000047241"
        }
      },
      "message": "record added",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidRequestMethod

Invalid HTTP method error

```json
{
  "code": "INVALID_REQUEST_METHOD",
  "details": {},
  "message": "The http request method type is not a valid one",
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryNotFound

Missing mandatory field error

```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "Locked_Reason__s",
        "json_path": "$.data[0].Locked_Reason__s"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataRelationNotFound

Relation not found error

```json
{
  "code": "INVALID_DATA",
  "details": {},
  "message": "relation not found",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModule

Invalid module name error

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

### Status `400` — `application/json` — InvalidDataRelationId

Relation not found error

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 1
  },
  "message": "the related id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowed

Locking configuration missing error

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 2
  },
  "message": "Required Record Locking Configuration is not present",
  "status": "error"
}
```

### Status `403` — `application/json` — NotAllowedCase1

Record already locked error

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 1
  },
  "message": "record is already locked",
  "status": "error"
}
```

### Status `403` — `application/json` — NotAllowedCase2

Automatic locking only configured error

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 1
  },
  "message": "record cannot be locked, only automatic locking is configured",
  "status": "error"
}
```
