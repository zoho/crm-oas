# Examples: massConvert

**POST /Leads/actions/mass_convert**

## Request examples

### `application/json` — Success

Example of mass convert request with two leads, Deal creation, tag carry-over, and related module transfer.

```json
{
  "ids": [
    "3652397000009850001",
    "3652397000009851001"
  ],
  "Deals": {
    "Deal_Name": "test7000"
  },
  "carry_over_tags": [
    {
      "id": "3652397000000002179",
      "api_name": "Contacts"
    },
    {
      "id": "3652397000000002180",
      "api_name": "Accounts"
    },
    {
      "id": "3652397000000002172",
      "api_name": "Deals"
    }
  ],
  "related_modules": [
    {
      "api_name": "Tasks",
      "id": "3652397000000002193"
    },
    {
      "api_name": "Events",
      "id": "3652397000000002195"
    },
    {
      "api_name": "Calls",
      "id": "3652397000000002197"
    }
  ],
  "assign_to": {
    "id": "3652397000000281001"
  },
  "move_attachments_to": {
    "api_name": "Contacts",
    "id": "3652397000000002179"
  }
}
```

## Response examples

### Status `202` — `application/json` — Success

Example of a successful mass convert job scheduling response.

```json
{
  "code": "SCHEDULED",
  "message": "Mass Convert scheduled successfully",
  "status": "success",
  "details": {
    "job_id": "1234567890"
  }
}
```

### Status `400` — `application/json` — InvalidDataBoolean

Example of invalid apply_assignment_threshold value in the request.

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "status": "error",
  "details": {
    "api_name": "apply_assignment_threshold",
    "json_path": "$.apply_assignment_threshold"
  }
}
```

### Status `400` — `application/json` — MandatoryIdsMissing

Example of missing mandatory ids field in the request body.

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "message": "required field not found",
  "status": "error",
  "details": {
    "api_name": "ids",
    "json_path": "$.ids"
  }
}
```

### Status `400` — `application/json` — MandatoryDealFieldMissing

Example of missing mandatory Deal_Name field in the Deals object.

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "message": "required field missing",
  "status": "error",
  "details": {
    "api_name": "Deal_Name",
    "json_path": "$.Deals.Deal_Name"
  }
}
```

### Status `400` — `application/json` — InvalidAssigneeData

Example of mismatched or invalid assign_to user data.

```json
{
  "code": "INVALID_DATA",
  "message": "Given assignee param does not match",
  "status": "error",
  "details": {
    "api_name": "id",
    "json_path": "$.assignee.id"
  }
}
```

### Status `400` — `application/json` — InvalidPortalUserType

Example of invalid portal_user_type ID in the request.

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "status": "error",
  "details": {
    "api_name": "id",
    "json_path": "$.portal_user_type.id"
  }
}
```

### Status `400` — `application/json` — InvalidRecordIds

Example of invalid lead record ID in the ids array.

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "status": "error",
  "details": {
    "api_name": "ids",
    "json_path": "$.ids[0]"
  }
}
```

### Status `400` — `application/json` — AmbiguityDuringProcessing

Example of conflicting api_name and ID in a related_modules entry.

```json
{
  "code": "AMBIGUITY_DURING_PROCESSING",
  "message": "two modules are different",
  "status": "error",
  "details": {
    "ambiguity_due_to": [
      {
        "api_name": "id",
        "json_path": "$.related_modules[0].id"
      },
      {
        "api_name": "api_name",
        "json_path": "$.related_modules[0].api_name"
      }
    ]
  }
}
```

### Status `400` — `application/json` — LimitExceeded

Example of ids array exceeds the maximum limit of 50 entries.

```json
{
  "code": "LIMIT_EXCEEDED",
  "message": "Limit exceeded for mass convert",
  "status": "error",
  "details": {
    "limit": 50,
    "limit_due_to": [
      {
        "api_name": "ids",
        "json_path": "$.ids"
      }
    ]
  }
}
```

### Status `400` — `application/json` — ExpectedFieldMissing

Example of missing expected field in a related_modules entry.

```json
{
  "code": "EXPECTED_FIELD_MISSING",
  "message": "Specify Atleast one field",
  "status": "error",
  "details": {
    "expected_fields": [
      {
        "api_name": "id",
        "json_path": "$.related_modules[0].id"
      },
      {
        "api_name": "api_name",
        "json_path": "$.related_modules[0].api_name"
      }
    ]
  }
}
```

### Status `400` — `application/json` — InvalidDataType

Example of non-integer value in the ids array.

```json
{
  "code": "INVALID_DATA",
  "message": "invalid data",
  "status": "error",
  "details": {
    "expected_data_type": "long",
    "api_name": "ids",
    "json_path": "$.ids[0]"
  }
}
```

### Status `400` — `application/json` — NonSubordinateUser

Example of non-subordinate user specified in the assign_to field.

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "assign_to",
    "json_path": "$.assign_to.id"
  },
  "message": "Non Subordinate User Found",
  "status": "error"
}
```

### Status `403` — `application/json` — Failure

Example of forbidden response when the user lacks mass conversion permission.

```json
{
  "code": "NO_PERMISSION",
  "message": "permission denied",
  "details": {
    "permissions": [
      "Crm_Implied_Mass_Convert_Leads"
    ]
  },
  "status": "error"
}
```

### Status `500` — `application/json` — Failure

Example of internal server error during mass convert request.

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error",
  "details": {},
  "status": "error"
}
```
