# Examples: getNotes

**GET /{parentRecordModule}/{parentRecordId}/Notes**

## Parameter examples

### `parentRecordModule` (path) — Contacts

Contacts module

```json
"Contacts"
```

### `parentRecordModule` (path) — Leads

Leads module

```json
"Leads"
```

### `parentRecordModule` (path) — Deals

Deals module

```json
"Deals"
```

### `parentRecordId` (path) — ContactId

Contact record ID

```json
"1043386000019763257"
```

### `parentRecordId` (path) — LeadId

Lead record ID

```json
"1043386000019763258"
```

### `fields` (query) — BasicFields

Basic note fields

```json
"Note_Title,Note_Content,Created_Time"
```

### `page` (query) — FirstPage

First page

```json
1
```

### `page` (query) — SecondPage

Second page

```json
2
```

### `perPage` (query) — DefaultPageSize

Default page size

```json
200
```

### `perPage` (query) — SmallPageSize

Smaller page size for limited data

```json
50
```

### `sort_by` (query) — SortById

Sort by note ID

```json
"id"
```

### `sort_by` (query) — SortByCreatedTime

Sort by creation time

```json
"Created_Time"
```

### `sort_by` (query) — SortByModifiedTime

Sort by modification time

```json
"Modified_Time"
```

### `sort_order` (query) — Ascending

Ascending order

```json
"asc"
```

### `sort_order` (query) — Descending

Descending order

```json
"desc"
```

## Response examples

### Status `200` — `application/json` — SuccessResponse

Success response for status 200

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
  ],
  "info": {
    "page": 1,
    "per_page": 200,
    "count": 1,
    "more_records": false,
    "next_page_token": null,
    "previous_page_token": null,
    "page_token_expiry": null
  }
}
```

### Status `401` — `application/json` — AuthenticationFailure

AUTHENTICATION_FAILURE error: authentication failed

```json
{
  "code": "AUTHENTICATION_FAILURE",
  "details": {},
  "message": "Authentication failed",
  "status": "error"
}
```

### Status `401` — `application/json` — OAuthScopeMismatch

OAUTH_SCOPE_MISMATCH error: OAuth scope mismatch

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "details": {},
  "message": "invalid oauth scope to access this URL",
  "status": "error"
}
```

### Status `404` — `application/json` — InvalidUrlPattern

INVALID_URL_PATTERN error: invalid URL pattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error"
}
```

### Status `500` — `application/json` — InternalError

INTERNAL_ERROR error: internal server error

```json
{
  "code": "INTERNAL_ERROR",
  "details": {},
  "message": "Internal Server Error",
  "status": "error"
}
```
