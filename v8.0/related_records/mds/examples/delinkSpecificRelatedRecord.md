# Examples: delinkSpecificRelatedRecord

**DELETE /{parentRecordModule}/{parentRecord}/{relatedList}/{record}**

## Parameter examples

### `parentRecordModule` (path) — Contacts

Contacts module

```json
"Contacts"
```

### `parentRecordModule` (path) — Deals

Deals module

```json
"Deals"
```

### `parentRecordModule` (path) — CustomModule

Custom Services module

```json
"Services__s"
```

### `parentRecord` (path) — ContactId

Contact record ID

```json
"3652397000000624001"
```

### `parentRecord` (path) — DealId

Deal record ID

```json
"3652397000000789001"
```

### `relatedList` (path) — Products

Products related list

```json
"Products"
```

### `relatedList` (path) — Notes

Notes related list

```json
"Notes"
```

### `relatedList` (path) — Attachments

Attachments related list

```json
"Attachments"
```

### `record` (path) — ProductId

Product record ID

```json
"3652397000001234001"
```

### `record` (path) — NoteId

Note record ID

```json
"3652397000001567001"
```

## Response examples

### Status `200` — `application/json` — SuccessfulDelink

Record delinked successfully

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "3652397000001234001"
      },
      "message": "record deleted",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidModule

Invalid module name provided

```json
{
  "code": "INVALID_MODULE",
  "message": "The module name given seems to be invalid",
  "status": "error",
  "details": {
    "resource_path_index": 0
  }
}
```

### Status `400` — `application/json` — NotSupported

Module not supported in API

```json
{
  "code": "NOT_SUPPORTED",
  "message": "The given module is not supported in API",
  "status": "error",
  "details": {
    "resource_path_index": 0
  }
}
```

### Status `400` — `application/json` — InvalidDataError

Invalid data or related ID

```json
{
  "code": "INVALID_DATA",
  "message": "The related id given seems to be invalid",
  "status": "error",
  "details": {
    "resource_path_index": 1
  }
}
```

### Status `400` — `application/json` — InvalidDataRelationNameError

Invalid data or related name

```json
{
  "code": "INVALID_DATA",
  "message": "The related name given seems to be invalid",
  "status": "error",
  "details": {
    "resource_path_index": 2
  }
}
```

### Status `400` — `application/json` — InvalidRequestMethod

Invalid HTTP request method

```json
{
  "code": "INVALID_REQUEST_METHOD",
  "message": "The http request method type is not a valid one",
  "status": "error",
  "details": {}
}
```

### Status `400` — `application/json` — AuthorizationFailed

Insufficient privilege to delete related records data

```json
{
  "code": "AUTHORIZATION_FAILED",
  "message": "User does not have sufficient privilege to delete related records data",
  "status": "error",
  "details": {}
}
```

### Status `400` — `application/json` — MandatoryNotFound

A required parameter is missing

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "message": "One of the expected parameter is missing",
  "status": "error",
  "details": {
    "api_name": "list_price",
    "json_path": "$.data[0].list_price"
  }
}
```

### Status `400` — `application/json` — UnableToParseDataType

Request body or parameters in wrong format

```json
{
  "code": "UNABLE_TO_PARSE_DATA_TYPE",
  "message": "Either the request body or parameters is in wrong format",
  "status": "error",
  "details": {}
}
```

### Status `401` — `application/json` — InvalidToken

Invalid authentication token

```json
{
  "code": "INVALID_TOKEN",
  "message": "Invalid OAuth token",
  "status": "error",
  "details": {}
}
```

### Status `401` — `application/json` — OAuthScopeMismatch

Missing DELETE scope

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "message": "The access token you have used to make this API call does not have the required scope.",
  "status": "error",
  "details": {}
}
```

### Status `403` — `application/json` — NoPermission

No permission to delete related records

```json
{
  "code": "NO_PERMISSION",
  "message": "Permission denied to delete records",
  "status": "error",
  "details": {
    "permissions": [
      "Crm_Implied_View_Leads"
    ]
  }
}
```

### Status `404` — `application/json` — RecordNotFound

Related record not found

```json
{
  "code": "INVALID_DATA",
  "message": "The record does not exist",
  "status": "error",
  "details": {}
}
```

### Status `404` — `application/json` — InvalidURLPattern

Invalid URL pattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error",
  "details": {}
}
```

### Status `500` — `application/json` — InternalError

Unexpected server error

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Unexpected and unhandled exception in Server",
  "status": "error",
  "details": {}
}
```
