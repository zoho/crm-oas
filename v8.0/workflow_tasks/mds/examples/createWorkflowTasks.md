# Examples: createWorkflowTasks

**POST /settings/automation/tasks**

## Request examples

### `application/json` — SamplePostRequest

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
          "value": "SampleTask"
        },
        {
          "field": {
            "id": "6660682000000000223",
            "api_name": "Due_Date"
          },
          "type": "execution_time",
          "value": {
            "period": "business_days",
            "unit": "3",
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
          "value": "Not Started"
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
      "name": "NewTask",
      "feature_type": "workflow"
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — CreateTaskSuccess

Task created successfully

```json
{
  "tasks": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "6660682000001550002"
      },
      "message": "task created successfully",
      "status": "success"
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

### Status `400` — `application/json` — DependentMismatchResponse3

Error response with code DEPENDENT_MISMATCH: Dependent Field is not matching

```json
{
  "tasks": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "id",
          "json_path": "$.tasks[0].field_mappings[2].field.id"
        },
        "api_name": "type",
        "json_path": "$.tasks[0].field_mappings[2].type"
      },
      "message": "Dependent Field is not matching",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse4

Error response with code DEPENDENT_MISMATCH: Type and value is mismatched

```json
{
  "tasks": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.tasks[0].field_mappings[0].type"
        },
        "api_name": "value",
        "json_path": "$.tasks[0].field_mappings[0].value"
      },
      "message": "Type and value is mismatched",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

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

### Status `400` — `application/json` — InvalidDataResponse4

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

### Status `400` — `application/json` — InvalidDataResponse5

Error response with code INVALID_DATA: Invalid data (Field: module)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "The field given seems to be invalid",
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

### Status `400` — `application/json` — MandatoryModuleApiNameResponse

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

### Status `400` — `application/json` — InvalidModuleApiNameTypeResponse

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

### Status `400` — `application/json` — InvalidModuleApiNameLengthResponse

Error response

```json
{
  "tasks": {
    "code": "INVALID_DATA",
    "message": "The field given seems to be invalid",
    "details": {
      "api_name": "api_name",
      "maximum_length": 5,
      "json_path": "$.tasks[*].module.api_name"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — InvalidModuleIdTypeResponse

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

### Status `400` — `application/json` — InvalidModuleIdLengthResponse

Error response

```json
{
  "tasks": {
    "code": "INVALID_DATA",
    "message": "The field given seems to be invalid",
    "details": {
      "api_name": "id",
      "maximum_length": 19,
      "json_path": "$.tasks[*].module.id"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — InvalidDataResponse6

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

### Status `400` — `application/json` — MandatoryNotFoundResponse3

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

### Status `400` — `application/json` — InvalidDataResponse7

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

### Status `400` — `application/json` — InvalidDataResponse8

Error response with code INVALID_DATA: Invalid data (Field: field_mappings)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "The field given seems to be invalid",
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

### Status `400` — `application/json` — InvalidDataResponse9

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

### Status `400` — `application/json` — InvalidDataResponse10

Error response with code INVALID_DATA: Invalid data (Field: field)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "The field given seems to be invalid",
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

### Status `400` — `application/json` — MandatoryFieldApiNameResponse

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

### Status `400` — `application/json` — InvalidFieldApiNameTypeResponse

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

### Status `400` — `application/json` — InvalidFieldApiNameLengthResponse

Error response

```json
{
  "tasks": {
    "code": "INVALID_DATA",
    "message": "The field given seems to be invalid",
    "details": {
      "api_name": "api_name",
      "maximum_length": 9,
      "json_path": "$.tasks[*].field_mappings[*].field.api_name"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — MandatoryFieldIdResponse

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

### Status `400` — `application/json` — InvalidFieldIdTypeResponse

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

### Status `400` — `application/json` — InvalidFieldIdLengthResponse

Error response

```json
{
  "tasks": {
    "code": "INVALID_DATA",
    "message": "The field given seems to be invalid",
    "details": {
      "api_name": "id",
      "maximum_length": 19,
      "json_path": "$.tasks[*].field_mappings[*].field.id"
    },
    "status": "error"
  }
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse4

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

### Status `400` — `application/json` — InvalidDataResponse11

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

### Status `400` — `application/json` — InvalidDataResponse12

Error response with code INVALID_DATA: Invalid data (Field: type)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "The field given seems to be invalid",
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

### Status `400` — `application/json` — MandatoryNotFoundResponse5

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

### Status `400` — `application/json` — InvalidDataResponse14

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

### Status `400` — `application/json` — InvalidDataResponse15

Error response with code INVALID_DATA: Invalid data (Field: value)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "The field given seems to be invalid",
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

### Status `400` — `application/json` — MandatoryNotFoundResponse6

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

### Status `400` — `application/json` — InvalidDataResponse16

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

### Status `400` — `application/json` — InvalidDataResponse17

Error response with code INVALID_DATA: Invalid data (Field: name)

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "The field given seems to be invalid",
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

### Status `400` — `application/json` — ExpectedFieldMissingResponse

Error response with code EXPECTED_FIELD_MISSING: Specify Atleast one field

```json
{
  "tasks": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.tasks[0].field_mapping[0].field.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.tasks[0].field_mapping[0].field.api_name"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AmbiguityDuringProcessingResponse

Error response with code AMBIGUITY_DURING_PROCESSING: Ambiguity while processing the request

```json
{
  "tasks": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.tasks[0].field_mapping[0].field.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.tasks[0].field_mapping[0].field.api_name"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse

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

### Status `400` — `application/json` — MandatoryNotFoundResponse

Error response with code MANDATORY_NOT_FOUND: mandatory field is not given (Field: value)

```json
{
  "tasks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "value",
        "json_path": "$.tasks[0].field_mapping[0].value"
      },
      "message": "mandatory field is not given",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse

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

### Status `400` — `application/json` — InvalidModuleResponse

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

### Status `400` — `application/json` — InvalidDataDatePeriodResponse

Error response with code INVALID_DATA: Invalid date Period

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "period",
        "json_path": "$.tasks[0].field_mappings[6].value.period"
      },
      "message": "Invalid date Period",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeGivenInvalidResponse

Error response with code INVALID_DATA: The type given is invalid

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "type",
        "json_path": "$.tasks[0].field_mappings[0].type"
      },
      "message": "The type given is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataGivenValueInvalidResponse

Error response with code INVALID_DATA: The given value seems to be invalid

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "time",
        "json_path": "$.tasks[0].field_mappings[4].value.time"
      },
      "message": "The given value seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataFieldIdInvalidResponse

Error response with code INVALID_DATA: the fieldId given seems to be invalid

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.tasks[0].field_mappings[0].field.id"
      },
      "message": "the fieldId given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTabIdInvalidResponse

Error response with code INVALID_DATA: the tabId given seems to be invalid

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.tasks[0].module.id"
      },
      "message": "the tabId given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse

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

### Status `400` — `application/json` — RequiredDataNotFoundResponse

Error response with code REQUIRED_DATA_NOT_FOUND: The required data missing

```json
{
  "tasks": [
    {
      "code": "REQUIRED_DATA_NOT_FOUND",
      "message": "The required data missing",
      "details": {
        "sub_json_path": "field.api_name",
        "api_name": "api_name",
        "json_path": "$.tasks[0].field_mappings",
        "value": "Subject"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryDataMissingResponse

Error response with code MANDATORY_NOT_FOUND: The required data missing

```json
{
  "tasks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "The required data missing",
      "details": {
        "api_name": "value",
        "json_path": "$.tasks[0].field_mappings[0].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataNotifyValueResponse

Error response with code INVALID_DATA: please specify notify value

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "please specify notify value",
      "details": {
        "expected_data_type": "boolean",
        "api_name": "notify",
        "json_path": "$.tasks[0].notify"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeNotSupportedResponse

Error response with code INVALID_DATA: data type not supported

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "data type not supported",
      "details": {
        "expected_data_type": "jsonobject",
        "api_name": "value",
        "json_path": "$.tasks[0].field_mappings[9].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataLengthExceededResponse

Error response with code INVALID_DATA: The length of the value exceeded the max limit

```json
{
  "tasks": [
    {
      "code": "INVALID_DATA",
      "message": "The length of the value exceeded the max limit",
      "details": {
        "maximum_length": 16,
        "api_name": "value",
        "json_path": "$.tasks[0].field_mappings[2].value"
      },
      "status": "error"
    }
  ]
}
```

### Status `401` — `application/json` — OauthScopeMismatchResponse

OAUTH_SCOPE_MISMATCH: Unauthorized

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "details": {},
  "message": "Unauthorized",
  "status": "error"
}
```

### Status `401` — `application/json` — AuthenticationFailureResponse

AUTHENTICATION_FAILURE: Authentication failed

```json
{
  "code": "AUTHENTICATION_FAILURE",
  "details": {},
  "message": "Authentication failed",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse

Feature not available in this edition / insufficient permission

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

### Status `404` — `application/json` — InvalidUrlPatternResponse

INVALID_URL_PATTERN: Please check if the URL trying to access is a correct one

```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "Please check if the URL trying to access is a correct one",
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
