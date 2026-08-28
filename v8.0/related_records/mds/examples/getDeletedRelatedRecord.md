# Examples: getDeletedRelatedRecord

**GET /{parentRecordModule}/deleted/{parentRecord}/{relatedList}**

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

### `fields` (query) — BasicFields

Basic contact fields

```json
"First_Name,Last_Name,Email"
```

### `fields` (query) — ExtendedFields

Extended fields including custom field

```json
"Account_Name,Phone,Lead_Source,Custom_Field__c"
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

## Response examples

### Status `200` — `application/json` — DeletedProducts

List of deleted product records

```json
{
  "data": [
    {
      "id": "2423488000000552158",
      "Owner": {
        "name": "Patricia",
        "id": "2423488000000483001",
        "email": "patricia@zoho.com"
      },
      "$member_info": {
        "Created_Time": "2023-10-31T18:10:23+05:30",
        "Modified_Time": "2023-10-31T18:10:23+05:30",
        "id": "2423488000000558116"
      }
    }
  ],
  "info": {
    "page": 1,
    "per_page": 200,
    "count": 1,
    "more_records": false,
    "next_page_token": null,
    "page_token_expiry": null,
    "previous_page_token": null
  }
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
    "resource_path_index": 2
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

Insufficient privilege to read related records data

```json
{
  "code": "AUTHORIZATION_FAILED",
  "message": "User does not have sufficient privilege to read related records data",
  "status": "error",
  "details": {}
}
```

### Status `400` — `application/json` — RequiredParamMissing

A required parameter is missing

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "message": "One of the expected parameter is missing",
  "status": "error",
  "details": {
    "param_name": "fields"
  }
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

No permission to read related records

```json
{
  "code": "NO_PERMISSION",
  "message": "Permission denied to read related records",
  "status": "error",
  "details": {
    "permissions": [
      "Crm_Implied_View_Leads"
    ]
  }
}
```

### Status `404` — `application/json` — RecordNotFound

Parent record not found

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
