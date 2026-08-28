# Examples: userTransferAPI

**POST /users/{userId}/actions/transfer**

## Request examples

### `application/json` — TransferExample

An example of transfer records and assignments.

```json
{
  "transfer": [
    {
      "move_subordinate": {
        "id": "5725767000000411001"
      },
      "transfer": {
        "records": true,
        "assignment": true,
        "criteria": false,
        "id": "5725767000000411002"
      }
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — SuccessResponse

An example success response for the scheduled transfer job.

```json
{
  "transfer": [
    {
      "code": "SCHEDULED",
      "details": {
        "job_id": "4243020004133788"
      },
      "message": "transfer of data is successfully scheduled",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse1

An example of error response where Transfer is allowed only for subordinate users of current user.

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 2
  },
  "message": "Transfer is allowed only for subordinate users of current user.",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataError1

An example error response for a deleted user in path.

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 1,
    "owner_status": "deleted"
  },
  "message": "the user id provided is already deleted.",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataError2

An example error response of a deleted transfer target user.

```json
{
  "transfer": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.transfer.transfer.id",
        "owner_status": "deleted"
      },
      "message": "The user to whom you are trying to transfer is deleted.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ExpectedFieldMissingError

An example error response of a missing required fields.

```json
{
  "transfer": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_data": [
          {
            "api_name": "transfer",
            "json_path": "$.transfer.transfer"
          },
          {
            "api_name": "move_subordinate",
            "json_path": "$.transfer.move_subordinate"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryFieldMissingError

An example of a missing id field inside the transfer object.

```json
{
  "transfer": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "id",
        "json_path": "$.transfer.transfer.id",
        "parent_api_name": "transfer"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SchedulerLimitExceededError

An example error response for exceeding the concurrent scheduler job limit.

```json
{
  "status": "error",
  "code": "CONCURRENT_JOB_LIMIT_EXCEEDED",
  "message": "Transfer and delete user scheduler limit reached",
  "details": {
    "limit": "10"
  }
}
```

### Status `403` — `application/json` — NoPermissionError

An example error response for no permission to transfer.

```json
{
  "status": "error",
  "code": "NO_PERMISSION",
  "message": "You do not have permission to perform this operation",
  "details": {
    "permissions": [
      "Crm_Implied_Change_Owner_Leads"
    ]
  }
}
```
