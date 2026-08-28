# Examples: postEnrolInCadences

**POST /{module}/actions/enrol_in_cadences**

## Parameter examples

### `module` (path) — Example

```json
"Leads"
```

## Request examples

### `application/json` — SamplePostRequest

Sample enroll records request

```json
{
  "cadences_ids": [
    "534412000002201155",
    "534412000002201156"
  ],
  "ids": [
    "1234567890234567",
    "1234567890456789",
    "2345678902345678"
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Successful enrollment result

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "534412000002201155",
        "cadences": [
          {
            "name": "Cadence 1",
            "id": "1234567890456789"
          },
          {
            "name": "Cadence 2",
            "id": "1234567890456789"
          }
        ]
      },
      "message": "records manually enrolled",
      "status": "success"
    }
  ]
}
```

### Status `202` — `application/json` — Success202

Enrollment request accepted for background processing

```json
{
  "data": [
    {
      "code": "SCHEDULED",
      "details": {},
      "message": "Cadence manual enrolment is in progress.",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — Success207

Multi-status response with partial enrollment success

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "534412000002201155",
        "cadences": [
          {
            "name": "Cadence 1",
            "id": "1234567890456789"
          },
          {
            "name": "Cadence 2",
            "id": "1234567890456789"
          }
        ]
      },
      "message": "records manually enrolled",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "ids",
        "json_path": "$.ids[1]"
      },
      "message": "given id seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ApiNotSupportedResponse1

API_NOT_SUPPORTED error for client portal users

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

API_NOT_SUPPORTED error for unsupported domain

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

### Status `400` — `application/json` — LimitExceededResponse1

LIMIT_EXCEEDED error - Cadence ID array exceeds the limit

```json
{
  "code": "LIMIT_EXCEEDED",
  "details": {
    "limit": 5,
    "limit_due_to": [
      {
        "api_name": "cadences_ids",
        "json_path": "$.cadences_ids"
      }
    ]
  },
  "message": "Limit Exceeded, You cannot give more than 5 cadences ids",
  "status": "error"
}
```

### Status `400` — `application/json` — LimitExceededResponse2

LIMIT_EXCEEDED error for ids exceeding 100

```json
{
  "code": "LIMIT_EXCEEDED",
  "details": {
    "limit": 100,
    "limit_due_to": [
      {
        "api_name": "ids",
        "json_path": "$.ids"
      }
    ]
  },
  "message": "Limit Exceeded, You cannot give more than 100 record ids",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowedResponse1

NOT_ALLOWED error for non-manual Cadence ID

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "api_name": "cadences_id",
    "json_path": "$.cadences_id[0]"
  },
  "message": "id given is not manual enrollment cadence",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse1

INVALID_DATA error - invalid entry in Cadence ID array

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 5,
    "api_name": "cadences_ids",
    "json_path": "$.cadences_ids"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

Error response - record IDs not provided

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "details": {
    "api_name": "ids",
    "json_path": "$.ids"
  },
  "message": "Record ids not found",
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

Error response - Cadence IDs not provided

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "details": {
    "api_name": "cadences_ids",
    "json_path": "$.cadences_ids"
  },
  "message": "Cadences ids not found",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Error response - record IDs expected as an array

```json
{
  "code": "INVALID_DATA",
  "details": {
    "expected_data_type": "jsonarray",
    "api_name": "ids",
    "json_path": "$.ids"
  },
  "message": "Record ids not found",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Error response - Cadence IDs expected as an array

```json
{
  "code": "INVALID_DATA",
  "details": {
    "expected_data_type": "jsonarray",
    "api_name": "cadences_ids",
    "json_path": "$.cadences_ids"
  },
  "message": "Cadences ids not found",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse4

Error response - invalid Cadence ID provided

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "cadences_ids",
    "json_path": "$.cadences_ids"
  },
  "message": "the given id seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse5

Error response - invalid record ID provided

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "ids",
    "json_path": "$.ids"
  },
  "message": "the given id seems to be invalid",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse1

NO_PERMISSION error for missing profile permission

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_UnEnroll_Series"
    ]
  },
  "message": "No permission",
  "status": "error"
}
```
