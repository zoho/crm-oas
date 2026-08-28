# Examples: getCustomViewById

**GET /settings/custom_views/{id}**

## Response examples

### Status `200` — `application/json` — SuccessResponse

Get Custom View by ID success response

```json
{
  "custom_views": [
    {
      "display_value": "crossfilter",
      "access_type": "shared",
      "criteria": {
        "comparator": "contains",
        "field": {
          "ui_type": 27,
          "api_name": "Full_Name",
          "id": "2411194000000000597"
        },
        "$disrupted": false,
        "type": "value",
        "value": "1"
      },
      "sort_by": null,
      "$modified_criteria": false,
      "default": true,
      "modified_time": "2025-11-27T07:39:34-02:00",
      "id": "2411194000004030016",
      "last_accessed_time": "2025-11-27T09:12:18-02:00",
      "locked": false,
      "sort_order": null,
      "created_time": "2025-11-27T07:37:52-02:00",
      "system_name": null,
      "created_by": {
        "name": "Jess Moana",
        "id": "2411194000000478001"
      },
      "shared_to": [
        {
          "name": "Jess Moana",
          "id": "2411194000000478001",
          "type": "users",
          "subordinates": null
        }
      ],
      "cross_filters": [
        {
          "criteria": {
            "group_operator": "AND",
            "group": [
              {
                "$disrupted": false,
                "comparator": "contains",
                "field": {
                  "ui_type": 20,
                  "api_name": "Note_Title",
                  "id": "2411194000000000279"
                },
                "type": "value",
                "value": "e"
              },
              {
                "$disrupted": false,
                "comparator": "equal",
                "field": {
                  "ui_type": 4,
                  "api_name": "Parent_Id",
                  "id": "2411194000000000283"
                },
                "type": "value",
                "value": "${NOTEMPTY}"
              }
            ]
          },
          "include_objects": true,
          "relation": {
            "$disrupted": false,
            "api_name": "Notes__r",
            "id": "2411194000000282522"
          }
        }
      ],
      "name": "crossfilter",
      "system_defined": false,
      "modified_by": {
        "name": "Jess Moana",
        "id": "2411194000000478001"
      },
      "fields": [
        {
          "api_name": "First_Name",
          "_pin": false,
          "id": "2411194000000000557"
        },
        {
          "api_name": "Last_Name",
          "_pin": false,
          "id": "2411194000000000559"
        },
        {
          "api_name": "Company",
          "_pin": false,
          "id": "2411194000000000555"
        },
        {
          "api_name": "Email",
          "_pin": false,
          "id": "2411194000000000563"
        }
      ],
      "category": "created_by_me",
      "favorite": 7
    }
  ],
  "info": {
    "translation": {
      "public_views": "Public Views",
      "other_users_views": "Other User's Views",
      "shared_with_me": "Shared With Me",
      "created_by_me": "Created By Me"
    }
  }
}
```

### Status `400` — `application/json` — FailureResponse

Invalid request error

```json
{
  "code": "INVALID_MODULE",
  "details": {},
  "message": "the module name given seems to be invalid",
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

### Status `401` — `application/json` — OAuthScopeMismatch

OAuth scope mismatch

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "details": {},
  "message": "invalid oauth scope to access this URL",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionError

Permission denied

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": []
  },
  "message": "permission denied",
  "status": "error"
}
```
