# Examples: getNoteById

**GET /Notes/{id}**

## Response examples

### Status `200` — `application/json` — SuccessResponse

Successful note retrieval

```json
{
  "data": [
    {
      "id": "1043386000020244003",
      "Note_Title": null,
      "Note_Content": "sdf",
      "$attachments": [
        {
          "$file_id": "2rsp48b6960fb9f4d444dada8740791775f35",
          "File_Name": "20251117_194524.jpg",
          "Size": "1623514",
          "id": "1043386000020248003"
        }
      ],
      "Parent_Id": {
        "module": {
          "api_name": "Leads",
          "id": "1043386000000002175"
        },
        "name": "a",
        "id": "1043386000019763257"
      },
      "Owner": {
        "name": "Prasanna",
        "id": "1043386000000322001",
        "email": "prasanna.saravanan@zohocorp.com"
      },
      "Modified_Time": "2025-11-19T19:27:53+05:30",
      "Created_Time": "2025-11-14T11:54:12+05:30"
    }
  ]
}
```

### Status `401` — `application/json` — AuthenticationFailure

Authentication failed

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

### Status `404` — `application/json` — InvalidUrlPattern

Invalid URL pattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error"
}
```

### Status `500` — `application/json` — InternalError

Internal server error

```json
{
  "code": "INTERNAL_ERROR",
  "details": {},
  "message": "Internal Server Error",
  "status": "error"
}
```
