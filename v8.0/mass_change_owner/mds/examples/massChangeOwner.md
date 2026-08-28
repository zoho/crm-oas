# Examples: massChangeOwner

**POST /{module}/actions/mass_change_owner**

## Request examples

### `application/json` — MassChangeOwnerExample

An example of mass change owner request with territory and criteria filter.

```json
{
  "cvid": "2423488000000091545",
  "owner": {
    "id": "2423488000000483001"
  },
  "territory": {
    "id": "2423488000000780003",
    "include_child": true
  },
  "criteria": {
    "field": {
      "api_name": "Stage",
      "id": "2423488000000000525"
    },
    "comparator": "equal",
    "value": "Qualification"
  }
}
```

## Response examples

### Status `202` — `application/json` — SuccessResponse

Example of a successful mass change owner job scheduling.

```json
{
  "data": [
    {
      "status": "success",
      "code": "SCHEDULED",
      "message": "change owner is successfully scheduled",
      "details": {
        "job_id": "2423488000001234567"
      }
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFound

An example of missing required cvid parameter.

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "message": "Required field is missing",
  "status": "error",
  "details": {
    "api_name": "cvid",
    "json_path": "$.cvid"
  }
}
```

### Status `400` — `application/json` — InvalidDataOwnerStatus

An example of a specified owner not being a CRM user.

```json
{
  "code": "INVALID_DATA",
  "message": "Invalid data provided",
  "status": "error",
  "details": {
    "api_name": "owner",
    "json_path": "$.owner.id",
    "owner_status": "not_crm_user"
  }
}
```

### Status `400` — `application/json` — InvalidDataExpectedField

Example of criteria field value provided as wrong data type.

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "field",
    "json_path": "$.criteria.field",
    "expected_data_type": "jsonobject"
  },
  "message": "the value given is invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — RecordLimitExceeded

Example of custom view record count exceeding the 50,000 limit.

```json
{
  "status": "error",
  "code": "RECORD_LIMIT_EXCEEDED",
  "message": "The number of records exceeds the limit",
  "details": {
    "limit": 50000
  }
}
```

### Status `400` — `application/json` — CombinedCriteriaLimitExceeded

Example of combined criteria count exceeding the limit of 25.

```json
{
  "status": "error",
  "code": "COMBINED_CRITERIA_LIMIT_EXCEEDED",
  "message": "Given CVID has more than 25 criteria, so change owner not done.",
  "details": {
    "limit": 25
  }
}
```

### Status `400` — `application/json` — ExpectedFieldMissing

Example of missing required field or group in criteria object.

```json
{
  "code": "EXPECTED_FIELD_MISSING",
  "details": {
    "expected_fields": [
      {
        "api_name": "group",
        "json_path": "$.criteria.group"
      },
      {
        "api_name": "field",
        "json_path": "$.criteria.field"
      }
    ]
  },
  "message": "Specify atleast one field",
  "status": "error"
}
```

### Status `400` — `application/json` — AmbiguityDuringProcessing

Example of ambiguous criteria field with both id and api_name provided.

```json
{
  "code": "AMBIGUITY_DURING_PROCESSING",
  "details": {
    "ambiguity_due_to": [
      {
        "api_name": "id",
        "json_path": "$.criteria.field.id"
      },
      {
        "api_name": "api_name",
        "json_path": "$.criteria.field.api_name"
      }
    ]
  },
  "message": "required field not found",
  "status": "error"
}
```

### Status `400` — `application/json` — DependentFieldMissing

Example of missing dependent comparator or value in criteria.

```json
{
  "code": "DEPENDENT_FIELD_MISSING",
  "details": {
    "dependee": {
      "api_name": "field",
      "json_path": "$.criteria.field"
    },
    "api_name": "field|comparator|value",
    "json_path": "$.<field|comparator|value>"
  },
  "message": "Dependent Field missing",
  "status": "error"
}
```

### Status `400` — `application/json` — NonSubordinateUser

Example of a non-subordinate user assigned as new owner.

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "owner_id"
  },
  "message": "The user to whom you are trying to transfer the records is  not a subordinate user.",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowedServiceProviderOwner

Example of assigning ownership to a Service Provider user outside allowed modules.

```json
{
  "code": "NOT_ALLOWED",
  "message": "Service Provider User can only be assigned to tasks, meetings, calls, and appointments",
  "status": "error",
  "details": {
    "api_name": "id",
    "json_path": "$.owner.id"
  }
}
```

### Status `403` — `application/json` — NoPermission

Example of missing mass-transfer permission for the module.

```json
{
  "code": "NO_PERMISSION",
  "message": "permission denied",
  "status": "error",
  "details": {
    "permissions": [
      "MASSTRANSFER_Leads"
    ]
  }
}
```
