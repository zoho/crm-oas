# Examples: singleInviteUser

**POST /{module}/{recordId}/actions/portal_invite**

## Response examples

### Status `200` — `application/json` — Success

Successful single portal user invitation

```json
{
  "portal_invite": [
    {
      "code": "SUCCESS",
      "details": {
        "record_id": "5020928000002338037"
      },
      "message": "An Invite has been sent to the personality.",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — CannotProcess

Error when the invitation type is invalid

```json
{
  "code": "CANNOT_PROCESS",
  "details": {},
  "message": "Invalid type for the portal invite",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidData

Error when the record does not have an email address

```json
{
  "code": "INVALID_DATA",
  "details": {},
  "message": "Invitation sent has failed as provided personality record does not have email id.",
  "status": "error"
}
```

### Status `400` — `application/json` — NotReviewed

Error when the record is pending review approval

```json
{
  "code": "NOT_REVIEWED",
  "details": {
    "record_id": "67890"
  },
  "message": "You cannot sent portal invitation since the record is waiting for approval under review process.",
  "status": "error"
}
```

### Status `400` — `application/json` — NotApproved

Error when the record has not been approved

```json
{
  "code": "NOT_APPROVED",
  "details": {
    "record_id": "67890"
  },
  "message": "Entity has not approved to invite yet.",
  "status": "error"
}
```

### Status `400` — `application/json` — DuplicateData

Error when a portal user with the same email already exists

```json
{
  "code": "DUPLICATE_DATA",
  "details": {
    "record_id": "67890"
  },
  "message": "Invitation sent has failed as a portal user exists with same email id",
  "status": "error"
}
```

### Status `400` — `application/json` — ApiNotSupported

Error when the API runs in a sandbox environment

```json
{
  "code": "API_NOT_SUPPORTED",
  "details": {
    "unsupported_environment": "sandbox"
  },
  "message": "api not supported in sandbox",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissions

Error when the user lacks required permissions

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_ClientPortal_Users"
    ]
  },
  "message": "NO_PERMISSION",
  "status": "error"
}
```
