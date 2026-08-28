# Examples: userTransferWithoutId

**POST /users/actions/transfer_and_delete**

## Request examples

### `application/json` — TransferAndDeleteExample

An example response for transfer and delete request with user ID in body.

```json
{
  "transfer_and_delete": [
    {
      "id": "5725767000000411001",
      "move_subordinate": {
        "id": "5725767000000411003"
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

An example success response for transfer and delete request. 

```json
{
  "transfer_and_delete": [
    {
      "status": "success",
      "code": "SUCCESS",
      "message": "User is deleted successfully",
      "details": {
        "job_id": "5725767000000498001",
        "id": "5725767000000411001"
      }
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataError1

An example error response for a maximum length exceeded request.

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 1,
    "api_name": "transfer_and_delete",
    "json_path": "$.transfer_and_delete"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataError2

An example error response for deleted transfer target user request.

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

An example error response for missing required fields.

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

### Status `400` — `application/json` — NotAllowedSelfDeleteError

An example error response for attempting to delete your own account.

```json
{
  "transfer_and_delete": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.transfer_and_delete.id"
      },
      "message": "Super Admin cannot be Deleted.",
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

An example of no permission to transfer issue.

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
