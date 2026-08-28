# Examples: deleteUser

**DELETE /users/{user}**

## Response examples

### Status `200` — `application/json` — SuccessfulUserDeletion

User deleted successfully from the organization

```json
{
  "users": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111113000000071587"
      },
      "message": "User deleted",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InValidUserIdResponse

Delete request with an invalid user ID

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 1
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — UserDeletionInSandBox

Delete attempt within a sandbox organization

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {},
      "message": "You cannot delete user in a sandbox org",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SupportUserDeletionResponse

Delete attempt on a support user

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "resource_path_index": 1
      },
      "message": "Support user cannot be deleted",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SystemUserDeletionResponse

Delete attempt on a system user

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "resource_path_index": 1
      },
      "message": "System user cannot be deleted",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DeletingWithoutSufficientPrivileges

Delete attempt by a user without sufficient privileges

```json
{
  "users": [
    {
      "code": "AUTHORIZATION_FAILED",
      "details": {},
      "message": "User does not have sufficient previlege to delete users",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DeletingAlreadyDeletedUser

Delete request targeting a previously deleted user

```json
{
  "users": [
    {
      "code": "ID_ALREADY_DELETED",
      "details": {
        "json_path": "$.users[0].id",
        "id": "2922942000003738152"
      },
      "message": "User is already deleted",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DigitalUserDeletion

Delete attempt on a Digital Employee user

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "resource_path_index": 1
      },
      "message": "Digital Employee cannot be deleted/deactivated/activated",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — PermissionDeniedResponse

Delete request denied due to insufficient profile permissions

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Users"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```

### Status `403` — `application/json` — DeletingClosedOrDeletedUser

Delete attempt targeting a closed or deleted organization

```json
{
  "code": "PERMISSION_DENIED",
  "details": {},
  "message": "You can't perform this action over a closed/deleted user",
  "status": "error"
}
```

### Status `403` — `application/json` — DeletionLimitExceededForOrg

Delete request rejected because the organization deletion limit is exceeded

```json
{
  "code": "PERMISSION_DENIED",
  "details": {},
  "message": "User deletion is not allowed for the org because of CrmKeyValue entry RESTRICT_USER_DELETION_FOR_THE_ORG & deleted users count exceeded 10",
  "status": "error"
}
```
