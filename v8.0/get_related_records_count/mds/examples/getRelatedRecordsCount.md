# Examples: getRelatedRecordsCount

**POST /{moduleApiName}/{recordId}/actions/get_related_records_count**

## Parameter examples

### `moduleApiName` (path) — Contacts

Contacts module

```json
"Contacts"
```

### `moduleApiName` (path) — Deals

Deals module

```json
"Deals"
```

### `moduleApiName` (path) — Accounts

Accounts module

```json
"Accounts"
```

### `moduleApiName` (path) — CustomModule

Custom module example

```json
"Services__s"
```

### `recordId` (path) — Numeric

Numeric record ID

```json
"4150868000004381002"
```

### `recordId` (path) — Uuid

UUID format record ID

```json
"550e8400-e29b-41d4-a716-446655440000"
```

## Request examples

### `application/json` — BasicCount

Basic related list count without filters

```json
{
  "get_related_records_count": [
    {
      "related_list": {
        "api_name": "Contacts",
        "id": "4150868000001038001"
      }
    }
  ]
}
```

### `application/json` — FilteredCount

Count request with field filter and approval status

```json
{
  "get_related_records_count": [
    {
      "related_list": {
        "api_name": "Deals",
        "id": "4150868000001038002"
      },
      "params": {
        "approved": true,
        "filters": {
          "comparator": "equal",
          "field": {
            "api_name": "Stage"
          },
          "value": "Closed Won"
        }
      }
    }
  ]
}
```

### `application/json` — MultipleRelatedLists

Count multiple related lists in one request

```json
{
  "get_related_records_count": [
    {
      "related_list": {
        "api_name": "Contacts",
        "id": "4150868000001038001"
      }
    },
    {
      "related_list": {
        "api_name": "Deals",
        "id": "4150868000001038002"
      }
    },
    {
      "related_list": {
        "api_name": "Tasks",
        "id": "4150868000001038003"
      }
    }
  ]
}
```

### `application/json` — ConvertedFilter

Count only converted leads in a related list

```json
{
  "get_related_records_count": [
    {
      "related_list": {
        "api_name": "Leads",
        "id": "4150868000001038004"
      },
      "params": {
        "converted": true,
        "filters": {
          "comparator": "equal",
          "field": {
            "api_name": "Status"
          },
          "value": "Qualified"
        }
      }
    }
  ]
}
```

### `application/json` — CategoryFilter

Count related records filtered by category type

```json
{
  "get_related_records_count": [
    {
      "related_list": {
        "api_name": "Attachments",
        "id": "4150868000001038005"
      },
      "params": {
        "category": "files",
        "filters": {
          "comparator": "equal",
          "field": {
            "api_name": "File_Type"
          },
          "value": "PDF"
        }
      }
    }
  ]
}
```

### `application/json` — ApprovalStateFilter

Count records filtered by approval state

```json
{
  "get_related_records_count": [
    {
      "related_list": {
        "api_name": "Quotes",
        "id": "4150868000001038006"
      },
      "params": {
        "approval_state": "approved",
        "filters": {
          "comparator": "equal",
          "field": {
            "api_name": "Quote_Stage"
          },
          "value": "Accepted"
        }
      }
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — SuccessfulCount

Successful count response for a single related list

```json
{
  "get_related_records_count": [
    {
      "count": 15,
      "related_list": {
        "api_name": "Contacts",
        "id": "4150868000001038001"
      }
    }
  ]
}
```

### Status `200` — `application/json` — MultipleRelatedLists

Successful count response for multiple related lists

```json
{
  "get_related_records_count": [
    {
      "count": 15,
      "related_list": {
        "api_name": "Contacts",
        "id": "4150868000001038001"
      }
    },
    {
      "count": 8,
      "related_list": {
        "api_name": "Deals",
        "id": "4150868000001038002"
      }
    }
  ]
}
```

### Status `200` — `application/json` — EmptyCount

Count response with zero matching records

```json
{
  "get_related_records_count": [
    {
      "count": 0,
      "related_list": {
        "api_name": "Tasks",
        "id": "4150868000001038003"
      }
    }
  ]
}
```

### Status `200` — `application/json` — FilteredCountResult

Count response after applying filter criteria

```json
{
  "get_related_records_count": [
    {
      "count": 3,
      "related_list": {
        "api_name": "Deals",
        "id": "4150868000001038002"
      }
    }
  ]
}
```

### Status `207` — `application/json` — PartialSuccessInvalidData

Partial success with INVALID_DATA error

```json
{
  "get_related_records_count": [
    {
      "count": 0,
      "related_list": {
        "api_name": "Notes",
        "id": "4987786000000002730"
      }
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.get_related_records_count[1].related_list.id"
      },
      "message": "Given related_list is invalid",
      "status": "error"
    }
  ]
}
```

### Status `207` — `application/json` — PartialSuccessMandatoryNotFound

Partial success with MANDATORY_NOT_FOUND error

```json
{
  "get_related_records_count": [
    {
      "count": 0,
      "related_list": {
        "api_name": "Notes",
        "id": "4987786000000002730"
      }
    },
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "related_list",
        "json_path": "$.get_related_records_count[1].related_list"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidRecordId

Invalid record ID in URL path

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 1
  },
  "message": "the related id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — IdAlreadyConverted

Record ID already converted

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 1
  },
  "message": "id already converted",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataRelatedList

Invalid related list ID or API name

```json
{
  "get_related_records_count": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.get_related_records_count[0].related_list.id"
      },
      "message": "Given related_list is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFound

MANDATORY_NOT_FOUND error for a missing required field

```json
{
  "get_related_records_count": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "related_list",
        "json_path": "$.get_related_records_count[0].related_list"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidModule

Invalid module API name

```json
{
  "code": "INVALID_MODULE",
  "details": {
    "resource_path_index": 0
  },
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — ExpectedFieldMissing

Missing ID or API name

```json
{
  "get_related_records_count": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "api_name",
            "json_path": "$.get_related_records_count[0].related_list.api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.get_related_records_count[0].related_list.id"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AmbiguityDuringProcessing

ID and API name mismatch

```json
{
  "get_related_records_count": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.get_related_records_count[0].related_list.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.get_related_records_count[0].related_list.api_name"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotSupportedFilters

Filters not supported for module

```json
{
  "get_related_records_count": [
    {
      "code": "NOT_SUPPORTED",
      "details": {
        "expected_data_type": "json_type",
        "api_name": "filters",
        "json_path": "$.get_related_records_count[0].params.filters"
      },
      "message": "Filters are not supported for this modules",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotSupportedRelatedList

Related list not supported in API

```json
{
  "get_related_records_count": [
    {
      "code": "NOT_SUPPORTED",
      "details": {},
      "message": "The given related list id is not supported in api",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AuthorizationFailed

Insufficient permissions

```json
{
  "code": "AUTHORIZATION_FAILED",
  "details": {},
  "message": "You do not have sufficient permission to read the module records",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidRequestMethod

Invalid HTTP request method

```json
{
  "code": "INVALID_REQUEST_METHOD",
  "details": {},
  "message": "The http request method type is not a valid one",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidRequest

Invalid request

```json
{
  "code": "INVALID_REQUEST",
  "details": {},
  "message": "unable to process your request. please verify whether you have entered proper method name, parameter and parameter values.",
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

### Status `401` — `application/json` — InvalidToken

Invalid or expired token

```json
{
  "code": "INVALID_TOKEN",
  "details": {},
  "message": "Invalid API token",
  "status": "error"
}
```

### Status `401` — `application/json` — OAuthScopeMismatch

OAuth scope mismatch

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "details": {},
  "message": "The access token does not have the required scope",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermission

No permission to read records

```json
{
  "code": "NO_PERMISSION",
  "details": {},
  "message": "You do not have permission to read records from the module",
  "status": "error"
}
```

### Status `403` — `application/json` — NotAllowed

Not allowed to read related records

```json
{
  "code": "NOT_ALLOWED",
  "details": {},
  "message": "You do not have permission to read related records from the module",
  "status": "error"
}
```

### Status `404` — `application/json` — InvalidUrlPattern

Invalid URL pattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "The request URL is incorrect. Please check the URL",
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
