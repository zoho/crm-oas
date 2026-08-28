# Examples: deleteBulkNotes

**DELETE /{parentRecordModule}/{parentRecordId}/Notes**

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

### `ids` (query) — SingleId

Single note ID

```json
"1043386000020244003"
```

### `ids` (query) — MultipleIds

Multiple note IDs

```json
"1043386000020244003,1043386000020244004,1043386000020244005"
```

## Response examples

### Status `200` — `application/json` — SuccessfulDeletion

Single note successfully deleted

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4876876000006021002"
      },
      "message": "record deleted",
      "status": "success"
    }
  ]
}
```

### Status `200` — `application/json` — BulkDeletion

Multiple notes successfully deleted

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4876876000006021002"
      },
      "message": "record deleted",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "4876876000006021003"
      },
      "message": "record deleted",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — PartialSuccess

Partial success - some notes deleted, some failed

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000116001"
      },
      "message": "record deleted",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "111111000000116002"
      },
      "message": "record not deleted",
      "status": "error"
    }
  ]
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
