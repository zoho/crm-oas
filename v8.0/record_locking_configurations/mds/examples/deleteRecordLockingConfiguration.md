# Examples: deleteRecordLockingConfiguration

**DELETE /settings/record_locking_configurations**

## Response examples

### Status `200` — `application/json` — SuccessCase

Successful response for deleting a record locking configuration

```json
{
  "record_locking_configurations": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "431525000001114019"
      },
      "message": "record locking configuration deleted",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidModule

Invalid module name provided

```json
{
  "code": "INVALID_MODULE",
  "details": {},
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — RequiredParamMissing

Missing required `module` parameter

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "module"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidData

Invalid configuration ID provided

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — FeatureNotSupported

Record locking not supported in the user's edition

```json
{
  "code": "FEATURE_NOT_SUPPORTED",
  "details": {},
  "message": "Record Locking Configuration is not supported in your edition",
  "status": "error"
}
```

### Status `400` — `application/json` — NoPermission

User lacks customization permission

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Customize_Zoho_CRM"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowed

Attempting to delete a system-created configuration

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 1
  },
  "message": "Configuration created by system cannot be deleted",
  "status": "error"
}
```
