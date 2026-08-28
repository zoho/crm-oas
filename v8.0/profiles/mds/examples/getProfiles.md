# Examples: getProfiles

**GET /settings/profiles**

## Parameter examples

### `include_types` (query) — LiteOnly

Include lite profiles

```json
"Lite"
```

### `include_types` (query) — SupportOnly

Include support profiles

```json
"Support"
```

### `include_types` (query) — LiteAndSupport

Include both lite and support profiles

```json
"Lite,Support"
```

### `filters` (query) — `application/json` — ProfileNameEqualsAdministrator

Filter by profile name equals Administrator

```json
{
  "group_operator": "or",
  "group": [
    {
      "field": {
        "api_name": "name",
        "field_label": "Profile Name",
        "data_type": "text"
      },
      "comparator": "equal",
      "value": "Administrator",
      "type": "value"
    },
    {
      "field": {
        "api_name": "name",
        "field_label": "Profile Name",
        "data_type": "text"
      },
      "comparator": "equal",
      "value": "Administrator",
      "type": "value"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Sample

Profiles list

```json
{
  "profiles": [
    {
      "display_label": "Administrator",
      "created_time": null,
      "modified_time": "2025-09-26T18:53:34+05:30",
      "api_name": "Administrator",
      "custom": false,
      "name": "Administrator",
      "modified_by": {
        "name": "Mohan Sai Mohan Sai",
        "id": "1697753000000424001"
      },
      "description": "This profile will have all the permissions. Users with Administrator profile will be able to view and manage all the data within the organization account by default.",
      "id": "1697753000000015972",
      "type": "normal_profile",
      "created_by": null
    },
    {
      "display_label": "Standard",
      "created_time": null,
      "modified_time": "2025-05-28T15:10:51+05:30",
      "api_name": "Standard",
      "custom": false,
      "name": "Standard",
      "modified_by": {
        "name": "Mohan Sai Mohan Sai",
        "id": "1697753000000424001"
      },
      "description": "This profile will have all the permissions except administrative privileges.",
      "id": "1697753000000015975",
      "type": "normal_profile",
      "created_by": null
    },
    {
      "display_label": "Team User",
      "created_time": null,
      "modified_time": "2025-07-24T18:42:58+05:30",
      "api_name": "Team_User",
      "custom": false,
      "name": "Team User",
      "modified_by": {
        "name": "Mohan Sai Mohan Sai",
        "id": "1697753000000424001"
      },
      "description": "This profile will be auto-assigned only for Team users who can access  Team modules and have limited permissions for Organisation modules.",
      "id": "1697753000010415055",
      "type": "lite_profile",
      "created_by": null
    },
    {
      "display_label": "34r8ynjke",
      "created_time": "2025-01-28T14:03:56+05:30",
      "modified_time": "2025-11-20T19:03:43+05:30",
      "api_name": "r8ynjk",
      "custom": true,
      "name": "34r8ynjke",
      "modified_by": {
        "name": "Mohan Sai Mohan Sai",
        "id": "1697753000000424001"
      },
      "description": null,
      "id": "1697753000021778019",
      "type": "normal_profile",
      "created_by": {
        "name": "Mohan Sai Mohan Sai",
        "id": "1697753000000424001"
      }
    }
  ],
  "info": {
    "page": 1,
    "per_page": 200,
    "count": 4,
    "more_records": false,
    "license_limit": 200
  }
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

### Status `400` — `application/json` — InvalidTypeParam

Invalid value for `type` query parameter

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "type"
  },
  "message": "invalid data",
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
