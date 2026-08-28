# Examples: updateWorkflowTask

**PUT /settings/automation/tasks**

## Request examples

### `application/json` — SamplePutRequest

Sample request body

```json
{
  "tasks": [
    {
      "module": {
        "api_name": "Leads",
        "id": "6660682000000002175"
      },
      "notify": true,
      "field_mappings": [
        {
          "field": {
            "api_name": "Description",
            "id": "6660682000000002291"
          },
          "type": "merge_field",
          "value": "Automated task for ${!Leads.First_Name}${!Leads.Last_Name}"
        },
        {
          "field": {
            "api_name": "Subject",
            "id": "6660682000000002271"
          },
          "type": "static",
          "value": "Updated: Follow up with lead"
        },
        {
          "field": {
            "id": "6660682000000000223",
            "api_name": "Due_Date"
          },
          "type": "execution_time",
          "value": {
            "period": "business_days",
            "unit": "5",
            "trigger_field": "${CURRENTTIME}",
            "sign": "plus"
          }
        },
        {
          "field": {
            "api_name": "Status",
            "id": "6660682000000002279"
          },
          "type": "static",
          "value": "In Progress"
        },
        {
          "field": {
            "api_name": "Priority",
            "id": "6660682000000002281"
          },
          "type": "static",
          "value": "High"
        },
        {
          "field": {
            "api_name": "URL_1",
            "id": "6660682000001522480"
          },
          "type": "merge_field",
          "value": "${!Leads.Website}"
        },
        {
          "field": {
            "api_name": "Number_1",
            "id": "6660682000001522575"
          },
          "type": "merge_field",
          "value": "${!Leads.No_of_Employees}"
        },
        {
          "display_value": "100000000000000000",
          "field": {
            "api_name": "Long_Integer_1",
            "id": "6660682000001522533"
          },
          "type": "static",
          "value": "100000000000000000"
        },
        {
          "field": {
            "api_name": "Single_Line_1",
            "id": "6660682000001522561"
          },
          "type": "static",
          "value": "sample task"
        },
        {
          "field": {
            "api_name": "Pick_List_1",
            "id": "6660682000000922691"
          },
          "type": "static",
          "value": "Voter ID"
        },
        {
          "field": {
            "api_name": "Email_1",
            "id": "6660682000001465098"
          },
          "type": "static",
          "value": "john@zohotest.cim"
        },
        {
          "field": {
            "api_name": "Percent_1",
            "id": "6660682000001522617"
          },
          "type": "static",
          "value": "50"
        },
        {
          "field": {
            "api_name": "Currency_1",
            "id": "6660682000001522589"
          },
          "type": "merge_field",
          "value": "${!Leads.Annual_Revenue}"
        },
        {
          "field": {
            "api_name": "Phone_1",
            "id": "6660682000001522603"
          },
          "type": "merge_field",
          "value": "${!Leads.Phone}"
        },
        {
          "field": {
            "api_name": "Decimal_1",
            "id": "6660682000001522547"
          },
          "type": "static",
          "value": "12"
        }
      ],
      "name": "Updated: Follow up with lead",
      "feature_type": "workflow"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — UpdateTaskSuccessResponse

Task updated successfully

```json
{
  "tasks": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000190030"
      },
      "message": "task updated successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse1

Error response with code DEPENDENT_FIELD_MISSING: Dependent Field missing (Field: field_name)

```json
{
  "tasks": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "api_name",
          "json_path": "$.tasks[0].field_mapping[1].field.api_name"
        },
        "api_name": "field_name",
        "json_path": "$.tasks[0].field_mapping[1].value.field_name"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response with code INVALID_DATA: Unsupported mergefield provided (Field: value)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "value",
        "json_path": "$.tasks[0].field_mappings[4].value"
      },
      "message": "Unsupported mergefield provided",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidModuleResponse1

Error response with code INVALID_MODULE: the module name given seems to be invalid (Field: id)

```json
{
  "tasks": [
    {
      "code": "INVALID_MODULE",
      "details": {
        "api_name": "id",
        "json_path": "$.tasks[0].module.id"
      },
      "message": "the module name given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Error response with code INVALID_DATA: please specify valid due date (Field: sign)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "sign",
        "json_path": "$.tasks[0].field_mapping[2].value.sign"
      },
      "message": "please specify valid due date",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Error response with code INVALID_DATA: the id given seems to be invalid (Field: id)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.tasks[0].field_mapping[0].field.id"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

Error response with code INVALID_DATA: the id given seems to be invalid

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 3
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — DependentMismatchResponse2

Error response with code DEPENDENT_MISMATCH: the given value is invalid (Field: value)

```json
{
  "tasks": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "api_name": "value",
        "json_path": "$.tasks[0].field_mapping[1].value",
        "dependee": {
          "api_name": "api_name",
          "json_path": "$.tasks[0].field_mapping[1].field.api_name"
        },
        "maximum_length": 150
      },
      "message": "the given value is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: module)

```json
{
  "tasks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "module",
        "json_path": "$.tasks[*].module"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

Error response with code INVALID_DATA: Invalid data type (Field: module)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "module",
        "expected_data_type": "jsonobject",
        "json_path": "$.tasks[*].module"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse6

Error response with code INVALID_DATA: Invalid data (Field: module)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "module",
        "maximum_length": 2,
        "json_path": "$.tasks[*].module"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response1

Error response

```json
{
  "tasks": {
    "code": "MANDATORY_NOT_FOUND",
    "message": "Required field is missing",
    "details": {
      "api_name": "api_name",
      "json_path": "$.tasks[*].module.api_name"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response2

Error response

```json
{
  "tasks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "api_name",
      "expected_data_type": "text",
      "json_path": "$.tasks[*].module.api_name"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response3

Error response

```json
{
  "tasks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "api_name",
      "maximum_length": 5,
      "json_path": "$.tasks[*].module.api_name"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response4

Error response

```json
{
  "tasks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "id",
      "expected_data_type": "bigint",
      "json_path": "$.tasks[*].module.id"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response5

Error response

```json
{
  "tasks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "id",
      "maximum_length": 19,
      "json_path": "$.tasks[*].module.id"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — InvalidDataResponse7

Error response with code INVALID_DATA: Invalid data type (Field: notify)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "notify",
        "expected_data_type": "boolean",
        "json_path": "$.tasks[*].notify"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: field_mappings)

```json
{
  "tasks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "field_mappings",
        "json_path": "$.tasks[*].field_mappings"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse8

Error response with code INVALID_DATA: Invalid data type (Field: field_mappings)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field_mappings",
        "expected_data_type": "jsonarray",
        "json_path": "$.tasks[*].field_mappings"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse9

Error response with code INVALID_DATA: Invalid data (Field: field_mappings)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "field_mappings",
        "maximum_length": 19,
        "json_path": "$.tasks[*].field_mappings"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse10

Error response with code INVALID_DATA: Invalid data type (Field: field)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field",
        "expected_data_type": "jsonobject",
        "json_path": "$.tasks[*].field_mappings[*].field"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse11

Error response with code INVALID_DATA: Invalid data (Field: field)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "field",
        "maximum_length": 2,
        "json_path": "$.tasks[*].field_mappings[*].field"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response6

Error response

```json
{
  "tasks": {
    "code": "MANDATORY_NOT_FOUND",
    "message": "Required field is missing",
    "details": {
      "api_name": "api_name",
      "json_path": "$.tasks[*].field_mappings[*].field.api_name"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response7

Error response

```json
{
  "tasks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "api_name",
      "expected_data_type": "text",
      "json_path": "$.tasks[*].field_mappings[*].field.api_name"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response8

Error response

```json
{
  "tasks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "api_name",
      "maximum_length": 9,
      "json_path": "$.tasks[*].field_mappings[*].field.api_name"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response9

Error response

```json
{
  "tasks": {
    "code": "MANDATORY_NOT_FOUND",
    "message": "Required field is missing",
    "details": {
      "api_name": "id",
      "json_path": "$.tasks[*].field_mappings[*].field.id"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response10

Error response

```json
{
  "tasks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "id",
      "expected_data_type": "bigint",
      "json_path": "$.tasks[*].field_mappings[*].field.id"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response11

Error response

```json
{
  "tasks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "id",
      "maximum_length": 19,
      "json_path": "$.tasks[*].field_mappings[*].field.id"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse3

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: type)

```json
{
  "tasks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "type",
        "json_path": "$.tasks[*].field_mappings[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse12

Error response with code INVALID_DATA: Invalid data type (Field: type)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.tasks[*].field_mappings[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse13

Error response with code INVALID_DATA: Invalid data (Field: type)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "maximum_length": 14,
        "json_path": "$.tasks[*].field_mappings[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse14

Error response with code INVALID_DATA: Invalid data (Field: type)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "static",
          "merge_field",
          "execution_time"
        ],
        "json_path": "$.tasks[*].field_mappings[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse4

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: value)

```json
{
  "tasks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "value",
        "json_path": "$.tasks[*].field_mappings[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse15

Error response with code INVALID_DATA: Invalid data type (Field: value)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "value",
        "expected_data_type": "text",
        "json_path": "$.tasks[*].field_mappings[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse16

Error response with code INVALID_DATA: Invalid data (Field: value)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "value",
        "maximum_length": 6,
        "json_path": "$.tasks[*].field_mappings[*].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse5

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: name)

```json
{
  "tasks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "name",
        "json_path": "$.tasks[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse17

Error response with code INVALID_DATA: Invalid data type (Field: name)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.tasks[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse18

Error response with code INVALID_DATA: Invalid data (Field: name)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 7,
        "json_path": "$.tasks[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AmbiguityDuringProcessingResponse

AMBIGUITY_DURING_PROCESSING: field.id and field.api_name conflict

```json
{
  "tasks": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.tasks[0].field_mappings[0].field.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.tasks[0].field_mappings[0].field.api_name"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ReadOnlyTaskNotAllowedResponse

NOT_ALLOWED: Cannot update a read-only task

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 3
  },
  "message": "Insufficient privileges to edit Read only task",
  "status": "error"
}
```

### Status `401` — `application/json` — LockedTaskAuthorizationErrorResponse

AUTHORIZATION_ERROR: Task is locked and cannot be edited

```json
{
  "tasks": [
    {
      "code": "AUTHORIZATION_ERROR",
      "details": {},
      "message": "Insufficient privileges to perform this operation",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionResponse

NO_PERMISSION: feature not available in this edition

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Workflow",
      "WorkFlow_Tasks"
    ]
  },
  "message": "feature not available in this edition",
  "status": "error"
}
```

### Status `403` — `application/json` — ReadOnlyTaskResponse

NOT_ALLOWED: Cannot edit a read-only task

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 3
  },
  "message": "Insufficient privileges to edit Read only task",
  "status": "error"
}
```

### Status `404` — `application/json` — InvalidTaskIdResponse

INVALID_DATA: the id given seems to be invalid

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 3
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `500` — `application/json` — InternalServerErrorResponse

INTERNAL_ERROR: Internal Server Error

```json
{
  "code": "INTERNAL_ERROR",
  "details": {},
  "message": "Internal Server Error",
  "status": "error"
}
```
