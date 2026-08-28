# Examples: updateNotesModule

**PUT /Notes**

## Request examples

### `application/json` — UpdateMultipleNotes

Update multiple notes

```json
{
  "data": [
    {
      "id": "4876876000006021002",
      "Note_Title": "Follow-up Completed",
      "Note_Content": "Customer requested additional information"
    },
    {
      "id": "4876876000006021003",
      "Note_Title": "Meeting Notes",
      "Note_Content": "Discussed project requirements"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — SuccessfulUpdate

Notes successfully updated

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2023-12-19T17:30:15+05:30",
        "Modified_By": {
          "name": "Patricia Boyle",
          "id": "4876876000000327001"
        },
        "Created_Time": "2023-12-19T16:45:07+05:30",
        "id": "4876876000006021002",
        "Created_By": {
          "name": "Patricia Boyle",
          "id": "4876876000000327001"
        }
      },
      "message": "record updated",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2023-12-19T17:30:16+05:30",
        "Modified_By": {
          "name": "Patricia Boyle",
          "id": "4876876000000327001"
        },
        "Created_Time": "2023-12-19T16:45:08+05:30",
        "id": "4876876000006021003",
        "Created_By": {
          "name": "Patricia Boyle",
          "id": "4876876000000327001"
        }
      },
      "message": "record updated",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — PartialSuccess

Partial success - some notes updated, some failed

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2026-01-05T14:27:48+05:30",
        "Modified_By": {
          "name": "Prasanna CEO",
          "id": "111111000000059489"
        },
        "Created_Time": "2026-01-05T14:27:48+05:30",
        "id": "111111000000116018",
        "Created_By": {
          "name": "Prasanna CEO",
          "id": "111111000000059489"
        }
      },
      "message": "record updated",
      "status": "success"
    },
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "Note_Content",
            "json_path": "$.data[1].Note_Content"
          },
          {
            "api_name": "Note_Title",
            "json_path": "$.data[1].Note_Title"
          }
        ]
      },
      "message": "should contain either content or title",
      "status": "error"
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
