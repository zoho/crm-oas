# Examples: deleteProfile

**DELETE /settings/profiles/{id}**

## Response examples

### Status `200` — `application/json` — Deleted

Delete result

```json
{
  "code": "SUCCESS",
  "details": {
    "id": "1697753000032967150"
  },
  "message": "Profile deleted",
  "status": "success"
}
```

### Status `400` — `application/json` — TransferToIdNotFound

Missing transfer_to parameter

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "details": {
    "param": "transfer_to"
  },
  "message": "Users in the profile need to be transferred. transfer_to param is mandatory.",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidTransferToId

Invalid transfer_to profile ID

```json
{
  "code": "INVALID_DATA",
  "details": {
    "id": "169775300002369603"
  },
  "message": "the id given seems to be invalid or already deleted",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDeleteRequest

Profile deletion failed

```json
{
  "code": "CANNOT_DELETE",
  "details": {},
  "message": "Profile cannot be deleted",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidRequestMethod

Invalid HTTP method used

```json
{
  "code": "INVALID_REQUEST_METHOD",
  "details": {},
  "message": "The http request method type is not a valid one",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidId

Invalid profile ID

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "the id given seems to be invalid or already deleted",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidAction

Invalid action

```json
{
  "code": "INVALID_DATA",
  "details": {},
  "message": "The action given is invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — SystemProfileNotAllowed

System profile cannot be deleted

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 2
  },
  "message": "System profile cannot be deleted",
  "status": "error"
}
```

### Status `401` — `application/json` — AuthenticationFailure

Authentication failure

```json
{
  "code": "AUTHENTICATION_FAILURE",
  "details": {},
  "message": "Authentication failed",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermission

No permission to manage profiles

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Profiles"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```

### Status `500` — `application/json` — InternalError

Unexpected server-side error

```json
{
  "code": "INTERNAL_ERROR",
  "details": {},
  "message": "Problem occurred internally",
  "status": "error"
}
```
