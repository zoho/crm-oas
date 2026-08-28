# Examples: updateReasonofLockedRecord

**PUT /{moduleName}/{recordId}/Locking_Information__s/{lockId}**

## Request examples

### `application/json` — UpdateLockReason

Update lock reason request

```json
{
  "data": [
    {
      "Locked_Reason__s": "Updating the lock reason for review"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — SuccessCase

Successful lock reason update

```json
{
  "data": [
    {
      "status": "success",
      "code": "SUCCESS",
      "message": "relation updated",
      "details": {
        "id": "111111000000053293"
      }
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

### Status `400` — `application/json` — InvalidDataConfigurationNotCreated

Relation not found error

```json
{
  "code": "INVALID_DATA",
  "details": {},
  "message": "relation not found",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowedConfigurationNotCreated

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

### Status `400` — `application/json` — InvalidModuleData

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

### Status `400` — `application/json` — InvalidDataRelation

Invalid relation ID error

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

### Status `400` — `application/json` — InvalidDataChildId

Invalid lock ID error

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 3
  },
  "message": "the id given seems to be invalid",
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
