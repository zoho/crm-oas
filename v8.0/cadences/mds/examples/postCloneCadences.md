# Examples: postCloneCadences

**POST /settings/automation/cadences/{id}/actions/clone**

## Request examples

### `application/json` — SamplePostRequest

Sample clone Cadence request body

```json
{
  "cadences": [
    {
      "name": "cadence",
      "description": "description",
      "module": {
        "api_name": "Leads",
        "id": "111112000000002628"
      },
      "type": "custom_view",
      "custom_view": {
        "id": "111112000000051112"
      },
      "execution_details": {
        "execute_every": {
          "period": "hours",
          "unit": 1
        }
      }
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — Success201

Successful Cadence clone response

```json
{
  "cadences": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111112000000092007"
      },
      "message": "Cadences cloned successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — LimitExceededResponse1

Cadences per module limit exceeded error

```json
{
  "code": "LIMIT_EXCEEDED",
  "details": {
    "api_name": "id",
    "limit": 60
  },
  "message": "More than 60 Cadences cannot be created for module",
  "status": "error"
}
```

### Status `400` — `application/json` — LimitExceededResponse2

Total Cadences limit exceeded error

```json
{
  "code": "LIMIT_EXCEEDED",
  "details": {
    "api_name": "id",
    "limit": 150
  },
  "message": "More than 150 Cadences cannot be created",
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

Missing required name field error

```json
{
  "cadences": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "name",
        "json_path": "$.cadences[0].name"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

Missing required module field error

```json
{
  "cadences": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "module",
        "json_path": "$.cadences[0].module"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse3

Missing required type field error

```json
{
  "cadences": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "type",
        "json_path": "$.cadences[0].type"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDataResponse1

Duplicate Cadence name error

```json
{
  "cadences": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.cadences[0].name"
      },
      "message": "A Cadences with the same name already exists",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Invalid Cadence name error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.cadences[0].name"
      },
      "message": "Name should not contain the following special character : #%^",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Cadence name too long error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 100,
        "api_name": "name",
        "json_path": "$.cadences[0].name"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Cadence description too long error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 500,
        "api_name": "description",
        "json_path": "$.cadences[0].description"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

Invalid Cadence type value error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "type",
        "json_path": "$.cadences[0].type",
        "supported_values": [
          "custom_view",
          "manual_enrollment"
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse1

Missing required dependent field error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.cadences[0].type"
        },
        "api_name": "custom_view",
        "json_path": "$.cadences[0].custom_view"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse4

Missing required period field error

```json
{
  "cadences": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "period",
        "json_path": "$.cadences[0].execution_details.execute_every.period"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

Invalid execution period value error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "period",
        "json_path": "$.cadences[0].execution_details.execute_every.period",
        "supported_values": [
          "immediately",
          "hours",
          "days",
          "weeks"
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse6

Invalid execution unit value error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "unit",
        "json_path": "$.cadences[0].execution_details.execute_every.unit"
      },
      "message": "unit value must be between 1 to 99",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse18

Invalid name field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.cadences[*].cadences.name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse20

Invalid description field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "description",
        "expected_data_type": "text",
        "json_path": "$.cadences[*].cadences.description"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse22

Invalid module field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "module",
        "expected_data_type": "jsonobject",
        "json_path": "$.cadences[*].cadences.module"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse23

Invalid api_name field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.cadences[*].cadences.module.api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse24

Invalid module ID field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.cadences[*].cadences.module.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse25

Invalid type field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.cadences[*].cadences.type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse27

Invalid custom_view field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "custom_view",
        "expected_data_type": "jsonobject",
        "json_path": "$.cadences[*].cadences.custom_view"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse28

Invalid Custom View ID data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.cadences[*].cadences.custom_view.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse30

Invalid execute_every field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "execution_details",
        "expected_data_type": "jsonobject",
        "json_path": "$.cadences[*].cadences.execution_details"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse32

Invalid execute_every period data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "execute_every",
        "expected_data_type": "jsonobject",
        "json_path": "$.cadences[*].cadences.execution_details.execute_every"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse33

Invalid execute_every period value error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "period",
        "expected_data_type": "text",
        "json_path": "$.cadences[*].cadences.execution_details.execute_every.period"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse35

Invalid execute_every unit data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "unit",
        "expected_data_type": "integer",
        "json_path": "$.cadences[*].cadences.execution_details.execute_every.unit"
      },
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionResponse1

No permission to clone Cadence error

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Cadences"
    ]
  },
  "message": "No permission",
  "status": "error"
}
```
