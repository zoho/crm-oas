# Examples: updateRecord

**PUT /{module}/{recordId}**

## Parameter examples

### `module` (path) — Example

```json
"Leads"
```

## Request examples

### `application/json` — Leads

Records retrieved from the Leads module

```json
{
  "data": [
    {
      "Layout": {
        "id": "554023000002734009"
      },
      "Lead_Source": "Employee Referral",
      "Company": "ABC",
      "Last_Name": "Daly",
      "First_Name": "Paul",
      "Email": "p.daly@zylker.com",
      "State": "Texas",
      "id": "111112000000142001"
    }
  ],
  "apply_feature_execution": [
    {
      "name": "layout_rules"
    }
  ],
  "skip_feature_execution": [
    {
      "name": "cadences"
    }
  ],
  "trigger": [
    "approval",
    "workflow",
    "blueprint",
    "pathfinder",
    "orchestration"
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success

Successfully completed operation

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2023-05-10T01:10:47-07:00",
        "Modified_By": {
          "name": "Patricia Boyle",
          "id": "5725767000000411001"
        },
        "Created_Time": "2023-05-10T01:10:47-07:00",
        "id": "5725767000000524157",
        "Created_By": {
          "name": "Patricia Boyle",
          "id": "5725767000000411001"
        },
        "$approval_state": "approved"
      },
      "message": "record updated",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidData

Invalid field value in the request

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "message": "The field value given for Company is invalid",
      "status": "error",
      "details": {
        "api_name": "Company",
        "json_path": "$.data[0].Company"
      }
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataType

Field value with an incorrect data type

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "integer",
        "api_name": "Number_1",
        "json_path": "$.data[0].Number_1"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidSupportedValue

Unsupported value for a fixed-value field

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.apply_feature_execution[0].name",
        "supported_values": [
          "layout_rules",
          "range_validation",
          "assignment_rules",
          "function_validation_rule",
          "criteria_validation_rule",
          "global_map_dependency",
          "territory_subordinates"
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataLength

Field value exceeds the maximum allowed length

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 2,
        "api_name": "Number_1",
        "json_path": "$.data[0].Number_1"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidModule

Invalid module API name in the request

```json
{
  "data": [
    {
      "code": "INVALID_MODULE",
      "details": {
        "resource_path_index": 0
      },
      "message": "the module name given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MultipleErrors

Multiple validation errors in a single record

```json
{
  "data": [
    {
      "code": "MULTIPLE_OR_MULTI_ERRORS",
      "details": {
        "errors": [
          {
            "code": "DUPLICATE_DATA",
            "details": {
              "api_name": "Email",
              "duplicate_record": {
                "Owner": {
                  "name": "Prajesh Kumar S",
                  "id": "4881139000000307001",
                  "zuid": "736078909"
                },
                "module": {
                  "api_name": "Leads",
                  "id": "4881139000000002175"
                },
                "id": "4881139000000428295"
              },
              "json_path": "$.data[0].Email",
              "more_records": true
            },
            "message": "duplicate data",
            "status": "error"
          },
          {
            "code": "DUPLICATE_DATA",
            "details": {
              "api_name": "Mobile",
              "duplicate_record": {
                "Owner": {
                  "name": "Prajesh Kumar S",
                  "id": "4881139000000307001",
                  "zuid": "736078909"
                },
                "module": {
                  "api_name": "Leads",
                  "id": "4881139000000002175"
                },
                "id": "4881139000002432007"
              },
              "json_path": "$.data[0].Mobile",
              "more_records": true
            },
            "message": "duplicate data",
            "status": "error"
          }
        ]
      },
      "message": "Multiple errors in the request",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissing

Required dependent field missing from the request

```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "Product_Category",
          "json_path": "$.data[0].Product_Category"
        },
        "api_name": "Product_Subcategory",
        "json_path": "$.data[0].Product_Subcategory"
      },
      "message": "The field 'Product_Subcategory' is required when 'Product_Category' is provided",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFound

Required field missing from the request

```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "id",
        "json_path": "$.data.service.id"
      },
      "message": "Service Id Not Found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundLayoutRule

Layout rule mandatory field absent from the request

```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "layout_rule": {
          "name": "Layout Rule",
          "id": "5410702000000761547"
        },
        "api_name": "Phone",
        "json_path": "$.data[0].Phone"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatch

Dependent field value conflicts with controlling field

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Status",
          "json_path": "$.data[0].Status"
        },
        "api_name": "Unavailable_Till",
        "json_path": "$.data[0].Unavailable_Till"
      },
      "message": "Unavailable Till must be greater than current Time.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidRequestMethod

Unsupported HTTP method for this endpoint

```json
{
  "data": [
    {
      "status": "error",
      "message": "The HTTP request method type is not a valid one.",
      "code": "INVALID_REQUEST_METHOD",
      "details": {
        "resource_path_index": 0
      }
    }
  ]
}
```

### Status `400` — `application/json` — AuthorizationFailed

Insufficient privileges for the operation

```json
{
  "data": [
    {
      "code": "AUTHORIZATION_FAILED",
      "details": {
        "resource_path_index": 0
      },
      "message": "User does not have sufficient privilege to perform this action",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDataError

Duplicate unique field value matches an existing record

```json
{
  "data": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "Unique_1",
        "duplicate_record": {
          "Owner": {
            "name": "Pranav",
            "id": "2008662000000454001",
            "zuid": "75092197"
          },
          "id": "2008662000006256222"
        },
        "json_path": "$.data[0].Unique_1",
        "id": "2008662000006256222",
        "more_records": false
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — RecordLockedError

Record is locked and cannot be modified

```json
{
  "data": [
    {
      "code": "RECORD_LOCKED",
      "details": {
        "api_name": "id",
        "json_path": "$.data[0].id",
        "action": "record_locking"
      },
      "message": "Sorry, you cannot perform this operation as the record is locked.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotApprovedError

Record is not approved and cannot be modified

```json
{
  "code": "NOT_APPROVED",
  "details": {
    "resource_path_index": 1
  },
  "message": "Cannot update record that is not approved yet",
  "status": "error"
}
```

### Status `400` — `application/json` — NotReviewedError

Record is under review and cannot be modified

```json
{
  "data": [
    {
      "code": "NOT_REVIEWED",
      "details": {},
      "message": "record in review",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LimitExceededError

Record count exceeds the allowed limit per request

```json
{
  "data": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "maximum_length": 100,
        "api_name": "data"
      },
      "message": "count of records in your request exceeds the limit",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ResourcePathIndexError

Invalid resource path index reference

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "message": "record not deleted",
      "details": {
        "resource_path_index": 1
      },
      "status": "error"
    }
  ]
}
```

### Status `401` — `application/json` — OauthScopeMismatch

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
  "message": "Permission denied",
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

### Status `412` — `application/json` — AlreadyModified

Record already modified after the specified timestamp

```json
{
  "data": [
    {
      "code": "ALREADY_MODIFIED",
      "message": "record updated time has already passed if-unmodified-since time",
      "status": "error",
      "details": {
        "Modified_Time": "2023-06-04T12:00:24+05:30",
        "Created_Time": "2023-04-17T16:23:25+05:30",
        "id": "492070000199308229",
        "Modified_By": {
          "name": "Senthilkumar",
          "id": "492070000000209017"
        },
        "Created_By": {
          "name": "Senthilkumar",
          "id": "492070000000209017"
        }
      }
    }
  ]
}
```

### Status `500` — `application/json` — InternalError

Unexpected internal server error during processing

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error",
  "status": "error",
  "details": {}
}
```
