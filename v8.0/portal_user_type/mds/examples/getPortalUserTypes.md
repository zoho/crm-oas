# Examples: getPortalUserTypes

**GET /settings/portals/{portal}/user_type**

## Response examples

### Status `200` — `application/json` — Success200

Portal user types retrieved successfully (200)

```json
{
  "user_type": [
    {
      "created_time": "2026-02-20T11:27:39+05:30",
      "default": true,
      "modified_time": "2026-02-24T18:04:01+05:30",
      "active_user_count": 1,
      "personality_module": {
        "plural_label": "Contacts",
        "api_name": "Contacts",
        "id": "111113000000002666"
      },
      "name": "Client Portal",
      "modified_by": {
        "name": "Pavithra R",
        "id": "111113000000059654"
      },
      "active": true,
      "invitation_field": {
        "api_name": "Email",
        "id": "111113000000004612"
      },
      "id": "111113000000158041",
      "deactive_user_count": 0,
      "created_by": {
        "name": "Pavithra R",
        "id": "111113000000059654"
      }
    },
    {
      "created_time": "2026-02-23T16:28:47+05:30",
      "default": false,
      "modified_time": "2026-02-23T16:32:01+05:30",
      "active_user_count": 0,
      "personality_module": {
        "plural_label": "Teachers",
        "api_name": "Teachers",
        "id": "111113000000162002"
      },
      "name": "Teachers",
      "modified_by": {
        "name": "Pavithra R",
        "id": "111113000000059654"
      },
      "active": true,
      "invitation_field": {
        "api_name": "Email",
        "id": "111113000000162061"
      },
      "id": "111113000000165506",
      "deactive_user_count": 0,
      "created_by": {
        "name": "Pavithra R",
        "id": "111113000000059654"
      }
    },
    {
      "created_time": "2026-02-25T11:39:39+05:30",
      "default": false,
      "modified_time": "2026-02-25T11:39:39+05:30",
      "active_user_count": 0,
      "personality_module": {
        "plural_label": "Contacts",
        "api_name": "Contacts",
        "id": "111113000000002666"
      },
      "name": "Client Portal V8",
      "modified_by": {
        "name": "Pavithra R",
        "id": "111113000000059654"
      },
      "active": true,
      "invitation_field": {
        "api_name": "Email",
        "id": "111113000000004612"
      },
      "id": "111113000000168122",
      "deactive_user_count": 0,
      "created_by": {
        "name": "Pavithra R",
        "id": "111113000000059654"
      }
    },
    {
      "created_time": "2026-02-25T12:25:22+05:30",
      "default": false,
      "modified_time": "2026-02-25T12:25:22+05:30",
      "active_user_count": 0,
      "personality_module": {
        "plural_label": "Contacts",
        "api_name": "Contacts",
        "id": "111113000000002666"
      },
      "name": "Client sPortal V8",
      "modified_by": {
        "name": "Pavithra R",
        "id": "111113000000059654"
      },
      "active": true,
      "invitation_field": {
        "api_name": "Email",
        "id": "111113000000004612"
      },
      "id": "111113000000168238",
      "deactive_user_count": 0,
      "created_by": {
        "name": "Pavithra R",
        "id": "111113000000059654"
      }
    }
  ]
}
```

### Status `400` — `application/json` — ApiNotSupportedResponse1

Api not supported for client portal user (API_NOT_SUPPORTED)

```json
{
  "code": "API_NOT_SUPPORTED",
  "details": {
    "unsupported_login_user_type": "Client Portal User"
  },
  "message": "api not supported for client portal user",
  "status": "error"
}
```

### Status `400` — `application/json` — ApiNotSupportedResponse2

Api not supported in sandbox (API_NOT_SUPPORTED)

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

### Status `400` — `application/json` — ApiNotSupportedResponse3

Api not supported (API_NOT_SUPPORTED)

```json
{
  "code": "API_NOT_SUPPORTED",
  "details": {
    "supported_domains": [
      "eu",
      "com",
      "in",
      "au",
      "ca",
      "cn",
      "jp"
    ]
  },
  "message": "api not supported",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse1

No portal exists with the given portal name. (INVALID_DATA)

```json
{
  "code": "INVALID_DATA",
  "details": {},
  "message": "No portal exists with the given portal name.",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse1

No permission (NO_PERMISSION)

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_ClientPortal"
    ]
  },
  "message": "No permission",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse2

NO_PERMISSION

```json
{
  "code": "NO_PERMISSION",
  "details": {},
  "message": "NO_PERMISSION",
  "status": "error"
}
```
