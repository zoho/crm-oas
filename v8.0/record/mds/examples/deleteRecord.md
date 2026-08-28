# Examples: deleteRecord

**DELETE /{module}/{recordId}**

## Parameter examples

### `module` (path) — Example

```json
"Leads"
```

## Response examples

### Status `200` — `application/json` — SuccessfulDeletion

Successfully deleted records

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "message": "record deleted",
      "status": "success",
      "details": {
        "id": "5843104000000624046"
      }
    }
  ]
}
```

### Status `400` — `application/json` — InvalidRecordId

Invalid record ID in the request URL

```json
{
  "code": "INVALID_DATA",
  "message": "invalid record id",
  "details": {
    "resource_path_index": 0
  },
  "status": "error"
}
```

### Status `400` — `application/json` — RecordNotDeleted

Record could not be deleted due to invalid data

```json
{
  "code": "INVALID_DATA",
  "message": "record not deleted",
  "details": {
    "resource_path_index": 1
  },
  "status": "error"
}
```

### Status `400` — `application/json` — UnableToParseDataType

Request body or parameters in incorrect format

```json
{
  "code": "INVALID_DATA",
  "message": "either the request body or parameters is in wrong format",
  "details": {
    "resource_path_index": 1
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModule

Invalid module API name in the request

```json
{
  "code": "INVALID_MODULE",
  "message": "the module name given seems to be invalid",
  "details": {
    "resource_path_index": 0
  },
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidRequestMethod

Unsupported HTTP method for this endpoint

```json
{
  "code": "INVALID_REQUEST_METHOD",
  "message": "The http request method type is not a valid one",
  "details": {},
  "status": "error"
}
```

### Status `400` — `application/json` — AuthorizationFailed

Insufficient privileges for the operation

```json
{
  "code": "AUTHORIZATION_FAILED",
  "message": "User does not have sufficient privilege to delete records",
  "details": {},
  "status": "error"
}
```

### Status `400` — `application/json` — RecordLocked

Record is locked and cannot be modified

```json
{
  "data": [
    {
      "code": "RECORD_LOCKED",
      "details": {
        "action": "record_locking",
        "id": "5040565000001052497"
      },
      "message": "You cannot perform this operation as the record is locked.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotApproved

Record is not approved and cannot be deleted

```json
{
  "data": [
    {
      "code": "NOT_APPROVED",
      "details": {
        "id": "5040565000001052497"
      },
      "message": "cannot delete record that is not approved yet",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MissingParam

Required parameter missing from the request

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "message": "Required parameter is missing",
  "details": {
    "param_name": "ids"
  },
  "status": "error"
}
```

### Status `401` — `application/json` — ScopeMismatch

OAuth access token missing the required scope

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "message": "Unauthorized",
  "status": "error",
  "details": {}
}
```

### Status `403` — `application/json` — NoPermission

User profile lacks the required module permission

```json
{
  "code": "NO_PERMISSION",
  "message": "Permission denied to delete",
  "status": "error",
  "details": {
    "permissions": [
      "Crm_Implied_View_Leads"
    ]
  }
}
```

### Status `404` — `application/json` — InvalidUrlPattern

Invalid or unrecognized API endpoint URL pattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error",
  "details": {}
}
```

### Status `500` — `application/json` — InternalError

Unexpected internal server error during processing

```json
{
  "data": [
    {
      "code": "INTERNAL_ERROR",
      "message": "Internal Server Error",
      "status": "error",
      "details": {}
    }
  ]
}
```
