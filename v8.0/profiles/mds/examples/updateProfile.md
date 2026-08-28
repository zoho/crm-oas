# Examples: updateProfile

**PUT /settings/profiles/{id}**

## Request examples

### `application/json` — UpdatePermissions

Update permission enablement for a profile

```json
{
  "profiles": [
    {
      "name": "Updated Profile Name",
      "description": "Updated description for the profile.",
      "permissions_details": [
        {
          "id": "1408246000000063001",
          "enabled": false
        },
        {
          "id": "1408246000000057001",
          "enabled": true
        }
      ]
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Updated

Update result

```json
{
  "profiles": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4670092000001127685"
      },
      "message": "profile updated successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateData

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

### Status `400` — `application/json` — InvalidProfileNameSpecialChars

Invalid profile name (special characters)

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

### Status `400` — `application/json` — InvalidAction

Invalid action

```json
{
  "profiles": [
    {
      "code": "INVALID_DATA",
      "details": {},
      "message": "The action given is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidPermissionId

Invalid permission ID

```json
{
  "profiles": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.profiles[0].permissions_details[0].id"
      },
      "message": "Invalid permission ID",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidPermissionsDetailsDatatype

Invalid data type for `permissions_details`

```json
{
  "profiles": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "jsonarray",
        "api_name": "permissions_details",
        "json_path": "$.profiles[0].permissions_details"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ChildPermissionParentDisabled

Child permission cannot be enabled because parent is disabled

```json
{
  "profiles": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.profiles[0].permissions_details[0].id"
      },
      "message": "Child permission can not be enabled, since its parent permission is disabled",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — PermissionNotAllowed

Permission ID cannot be updated

```json
{
  "profiles": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.profiles[0].permissions_details[0].id"
      },
      "message": "This Permissionid cannot be updated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SystemProfileNotAllowed

System profile cannot be updated

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 2
  },
  "message": "System profile cannot be updated",
  "status": "error"
}
```

### Status `400` — `application/json` — PrivateProfileNotAllowed

Team Module profile cannot be updated

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 2
  },
  "message": "Team Module profile cannot be updated",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidProfileId

Invalid or deleted profile ID

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
