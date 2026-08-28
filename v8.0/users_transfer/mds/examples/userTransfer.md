# Examples: userTransfer

**POST /users/{userId}/actions/transfer_and_delete**

## Request examples

### `application/json` — TransferAndDeleteExample

An example response of Transfer and delete request with records and assignments.

```json
{
  "transfer_and_delete": [
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

An example of successful transfer and delete operation.

```json
{
  "transfer_and_delete": [
    {
      "status": "success",
      "code": "SUCCESS",
      "message": "User is deleted successfully",
      "details": {
        "job_id": "5725767000000498001"
      }
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedError

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 1
  },
  "message": "Super Admin cannot be Deleted.",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataError1

An example response of deleted user provided in the path.

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

An example error response of deleted transfer target user request.

```json
{
  "transfer_and_delete": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.transfer_and_delete.transfer.id",
        "owner_status": "deleted"
      },
      "message": "The user to whom you are trying to transfer is deleted.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ExpectedFieldMissingError

An example of missing required fields in the request.

```json
{
  "transfer_and_delete": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_data": [
          {
            "api_name": "transfer",
            "json_path": "$.transfer_and_delete.transfer"
          },
          {
            "api_name": "move_subordinate",
            "json_path": "$.transfer_and_delete.move_subordinate"
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
  "transfer_and_delete": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "id",
        "json_path": "$.transfer_and_delete.transfer.id",
        "parent_api_name": "transfer"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — JobLimitExceededError

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

### Status `403` — `application/json` — SuperAdminPermissionError

An example error response when the caller is not a super admin.

```json
{
  "status": "error",
  "code": "NO_PERMISSION",
  "message": "Only super admin has permission to delete users"
}
```
