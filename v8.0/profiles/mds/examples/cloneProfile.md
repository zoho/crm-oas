# Examples: cloneProfile

**POST /settings/profiles/{id}/actions/clone**

## Request examples

### `application/json` — Sample

Clone profile payload

```json
{
  "profiles": [
    {
      "name": "Cloned Standard",
      "description": "Cloned from Standard profile"
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — Created

Clone result

```json
{
  "profiles": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "1697753000033202019"
      },
      "message": "profile created successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidCreateRequest

Validation failed

```json
{
  "profiles": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "name",
        "json_path": "$.profiles[0].name"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateProfileName

Duplicate profile name

```json
{
  "profiles": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.profiles[0].name"
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LimitExceeded

License limit exceeded

```json
{
  "profiles": [
    {
      "code": "LICENSE_LIMIT_EXCEEDED",
      "details": {
        "limit": 2
      },
      "message": "Request exceeds your license limit.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidProfileNameSpecialChars

Invalid profile name

```json
{
  "profiles": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.profiles[0].name"
      },
      "message": "Profile name should not contain the following special character(s) : #, %, &, (, ), *, ^",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — CannotBeCloned

Profile cannot be cloned

```json
{
  "profiles": [
    {
      "code": "INVALID_DATA",
      "details": {},
      "message": "Profile cannot be Cloned",
      "status": "error"
    }
  ]
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
