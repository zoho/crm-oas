# Examples: convertInventory

**POST /{moduleApiName}/{id}/actions/convert**

## Request examples

### `application/json` — Success

Convert a Quotes record to a Sales Order

```json
{
  "data": [
    {
      "convert_to": [
        {
          "module": {
            "id": "111111000000002469",
            "api_name": "Sales_Orders"
          }
        }
      ]
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success

Successful conversion of a Quotes record to a Sales Order

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Sales_Orders": {
          "name": "TestQ4",
          "id": "111111000000072039"
        }
      },
      "message": "The record has been converted successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryIdsMissing

Missing mandatory convert_to field

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "message": "required field not found",
  "status": "error",
  "details": {
    "api_name": "convert_to",
    "json_path": "$.data[0].convert_to"
  }
}
```

### Status `400` — `application/json` — NoPermission

Permission denied to access the source module

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "resource_path_index": 0
  },
  "message": "permission denied to access the module",
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

### Status `400` — `application/json` — InvalidParentId

Invalid or mismatched source record ID

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "status": "error",
  "details": {
    "resource_path_index": 1
  }
}
```

### Status `400` — `application/json` — AmbiguityDuringProcessing

API name and ID do not match

```json
{
  "data": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "api_name",
            "json_path": "$.data[0].convert_to[0].module.api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.data[0].convert_to[0].module.id"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ExpectedFieldMissing

Required field missing from convert_to array

```json
{
  "data": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "api_name",
            "json_path": "$.data[0].convert_to[0].module.api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.data[0].convert_to[0].module.id"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — IdAlreadyConverted

Source record has already been converted

```json
{
  "code": "ID_ALREADY_CONVERTED",
  "details": {
    "resource_path_index": 1
  },
  "message": "id already converted",
  "status": "error"
}
```

### Status `400` — `application/json` — NotApproved

Source record is pending approval

```json
{
  "code": "NOT_APPROVED",
  "details": {
    "resource_path_index": 1
  },
  "message": "record not approved",
  "status": "error"
}
```

### Status `400` — `application/json` — NotReviewed

Source record is pending review

```json
{
  "code": "NOT_REVIEWED",
  "details": {
    "resource_path_index": 1
  },
  "message": "record in review",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowed

carry_over_tags must be set to true

```json
{
  "data": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "reason": "Carry over tags will be automatically converted",
        "api_name": "carry_over_tags",
        "json_path": "$.data[0].convert_to[0].carry_over_tags"
      },
      "message": "carry over tags must be given as true",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateData

Duplicate unique field value in the target module

```json
{
  "data": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "Billing_Street",
        "duplicate_record": {
          "Owner": {
            "name": "Poovi MBUser2",
            "id": "111111000000058229",
            "zuid": "44653171"
          },
          "module": {
            "api_name": "Sales_Orders",
            "id": "111111000000002766"
          },
          "id": "111111000000536282"
        },
        "json_path": "$.data[0].Billing_Street",
        "more_records": false
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — PermissionDeniedForTargetModule

Permission denied for target module

```json
{
  "data": [
    {
      "code": "NO_PERMISSION",
      "details": {
        "api_name": "module",
        "permissions": [
          "Crm_Implied_Create_Invoices",
          "Crm_Implied_View_Invoices"
        ],
        "json_path": "$.data[0].convert_to[0].module"
      },
      "message": "permission denied",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionForSourceModule

Permission denied for source module

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_View_Quotes",
      "Crm_Implied_Convert_Quotes"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
