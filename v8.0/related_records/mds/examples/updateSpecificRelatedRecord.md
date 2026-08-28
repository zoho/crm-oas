# Examples: updateSpecificRelatedRecord

**PUT /{parentRecordModule}/{parentRecord}/{relatedList}/{record}**

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

## Request examples

### `application/json` — UpdateSingleProduct

Update price for a single product

```json
{
  "data": [
    {
      "id": "3652397000001234001",
      "Unit_Price": 109.99,
      "Discount": 10
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — SuccessfulUpdate

Record updated successfully

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "3652397000001234001"
      },
      "message": "record updated",
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
  "message": "The given module is not supported",
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
  "code": "INVALID_MODULE",
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

Insufficient privilege to update related records data

```json
{
  "code": "AUTHORIZATION_FAILED",
  "message": "User does not have sufficient privilege to update related records data",
  "status": "error",
  "details": {}
}
```

### Status `400` — `application/json` — MandatoryNotFound

Required field not found

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "message": "Required field not found",
  "status": "error",
  "details": {
    "api_name": "list_price",
    "json_path": "$.data[0].list_price"
  }
}
```

### Status `400` — `application/json` — MandatoryNotFoundBulk

Required field not found in bulk operation

```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "list_price",
        "json_path": "$.data[0].list_price"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `401` — `application/json` — InvalidToken

Invalid authentication token

```json
{
  "code": "INVALID_TOKEN",
  "details": {},
  "message": "Invalid OAuth token",
  "status": "error"
}
```

### Status `401` — `application/json` — OAuthScopeMismatch

Missing READ scope

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "message": "The access token you have used to make this API call does not have the required scope.",
  "status": "error",
  "details": {}
}
```

### Status `403` — `application/json` — NoPermission

No permission to read related records

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_View_Leads"
    ]
  },
  "message": "Permission denied to read related records",
  "status": "error"
}
```

### Status `404` — `application/json` — RecordNotFound

Related record not found

```json
{
  "code": "INVALID_DATA",
  "details": {},
  "message": "The record does not exist",
  "status": "error"
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
