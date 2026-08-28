# Examples: changeOwnerBulk

**POST /{module}/actions/change_owner**

## Request examples

### `application/json` — BulkChangeOwnerExample

```json
{
  "ids": [
    "5725767000000291001",
    "5725767000000291002"
  ],
  "owner": {
    "id": "5725767000000291003"
  },
  "notify": true,
  "related_modules": [
    {
      "api_name": "Tasks",
      "id": "5725767000000293001"
    },
    {
      "api_name": "Calls",
      "id": "5725767000000294001"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — SuccessResponse

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "475418000007459055"
      },
      "message": "owner is successfully updated",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "475418000007459060"
      },
      "message": "owner is successfully updated",
      "status": "success"
    }
  ]
}
```

### Status `202` — `application/json` — PartialSuccessResponse

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4987786000003224001"
      },
      "message": "owner is successfully updated",
      "status": "success"
    },
    {
      "code": "CANNOT_PROCESS",
      "details": {
        "id": "4987786000003224629",
        "index": 1
      },
      "message": "The record is in stop-processing state.",
      "status": "error"
    }
  ]
}
```

### Status `207` — `application/json` — PartialSuccessResponse

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4987786000003224001"
      },
      "message": "owner is successfully updated",
      "status": "success"
    },
    {
      "code": "CANNOT_PROCESS",
      "details": {
        "id": "4987786000003224629",
        "index": 1
      },
      "message": "The record is in stop-processing state.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotSupportedError

```json
{
  "code": "NOT_SUPPORTED",
  "details": {
    "resource_path_index": 0
  },
  "message": "The requested operation is not supported",
  "status": "error"
}
```

### Status `400` — `application/json` — ApiNotSupportedError

```json
{
  "code": "API_NOT_SUPPORTED",
  "details": {
    "supported_version": 3
  },
  "message": "Change Owner is not supported in this API version",
  "status": "error"
}
```

### Status `400` — `application/json` — CannotProcessError

```json
{
  "code": "CANNOT_PROCESS",
  "details": {
    "id": "4987786000003224629",
    "index": 0
  },
  "message": "The record is in stop-processing state.",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataError

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "owner",
    "json_path": "$.owner.id"
  },
  "message": "Invalid data provided",
  "status": "error"
}
```

### Status `400` — `application/json` — NonSubordinateUser

Owner is not a subordinate of the current user.

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "id",
    "json_path": "$.owner.id",
    "owner_status": "include_subordinate_owners"
  },
  "message": "The user to whom you are trying to transfer the records is not a subordinate.",
  "status": "error"
}
```

### Status `400` — `application/json` — InactiveOwnerError

New owner's user account is not active

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "id",
    "json_path": "$.owner.id",
    "owner_status": "inactive"
  },
  "message": "The user to whom you are trying to transfer the records is not active.",
  "status": "error"
}
```

### Status `400` — `application/json` — LiteUserOwnerError

New owner is a Lite user

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "id",
    "json_path": "$.owner.id"
  },
  "message": "The user to whom you are trying to transfer the records is a Lite User.",
  "status": "error"
}
```

### Status `400` — `application/json` — ServiceProviderOwnerError

New owner is a Service Provider user not allowed for this module

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "api_name": "id",
    "json_path": "$.owner.id"
  },
  "message": "Service Provider User can only be assigned to tasks, meetings, calls, and appointments",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataTypeError

```json
{
  "data": {
    "code": "INVALID_DATA",
    "details": {
      "expected_data_type": "long",
      "api_name": "ids",
      "json_path": "$.ids[1]"
    },
    "message": "invalid data",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — RecordLockingConflictError

```json
{
  "data": [
    {
      "code": "RECORD_LOCKED",
      "details": {
        "action": "record_locking",
        "id": "4987786000003224629"
      },
      "message": "Sorry, you cannot perform this operation as the record is locked.",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionError

```json
{
  "code": "NO_PERMISSION",
  "message": "You do not have permission to perform this operation",
  "status": "error",
  "details": {
    "permissions": [
      "Crm_Implied_Change_Owner_Leads"
    ]
  }
}
```

### Status `403` — `application/json` — CannotAssignError

```json
{
  "code": "CANNOT_ASSIGN",
  "details": {
    "permissions": [
      "Crm_Implied_Role_View_Leads"
    ]
  },
  "message": "The user you are trying to assign does not have permission for this module.",
  "status": "error"
}
```

### Status `403` — `application/json` — CannotPerformActionError

```json
{
  "code": "CANNOT_PERFORM_ACTION",
  "details": {
    "id": "4987786000003224629",
    "index": 0
  },
  "message": "You do not have permission to change the owner of this record.",
  "status": "error"
}
```

### Status `403` — `application/json` — ClosedOrDeletedUserError

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "id",
    "json_path": "$.owner.id",
    "owner_status": "deleted"
  },
  "message": "The user to whom you are trying to transfer the records has closed their account.",
  "status": "error"
}
```
