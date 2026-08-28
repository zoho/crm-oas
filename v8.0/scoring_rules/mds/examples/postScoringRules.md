# Examples: postScoringRules

**POST /settings/automation/scoring_rules**

## Request examples

### `application/json` — SamplePostRequest

Sample create Scoring Rules request body

```json
{
  "scoring_rules": [
    {
      "description": "",
      "active": true,
      "custom_fields": [
        {
          "field_label": "Lead - Scoring Score",
          "reference_field": {
            "api_name": "Score"
          }
        },
        {
          "field_label": "Lead - Scoring Touch point Score",
          "reference_field": {
            "api_name": "Touch_Point_Score"
          }
        }
      ],
      "field_rules": [
        {
          "criteria": {
            "group_operator": "and",
            "group": [
              {
                "field": {
                  "api_name": "CF_Date",
                  "id": "111114000000081970",
                  "field_label": "CF Date",
                  "data_type": "date"
                },
                "comparator": "equal",
                "value": "2025-11-19",
                "type": "value"
              },
              {
                "field": {
                  "api_name": "Company",
                  "id": "111114000000004780",
                  "field_label": "Company",
                  "data_type": "text"
                },
                "comparator": "equal",
                "value": "Zohho",
                "type": "value"
              }
            ]
          },
          "score": 10
        },
        {
          "criteria": {
            "field": {
              "api_name": "Country",
              "id": "111114000000004892",
              "field_label": "Country",
              "data_type": "text"
            },
            "comparator": "not_equal",
            "value": "${EMPTY}",
            "type": "value"
          },
          "score": -10
        }
      ],
      "signal_rules": [
        {
          "signal": {
            "namespace": "zoho.emailinsight.bounce",
            "id": "111114000000034755"
          },
          "score": -99
        },
        {
          "signal": {
            "namespace": "zoho.emailinsight.open",
            "id": "111114000000034749"
          },
          "score": 10
        },
        {
          "signal": {
            "namespace": "zoho.emailinsight.click",
            "id": "111114000000034752"
          },
          "score": 100
        }
      ],
      "layout": {
        "id": "111114000000003626",
        "api_name": "Standard",
        "display_label": "Standard"
      },
      "module": {
        "api_name": "Leads",
        "id": "111114000000002628"
      },
      "name": "Lead - Scoring"
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — Success201

Successful create Scoring Rules response

```json
{
  "scoring_rules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "2995635000023340017"
      },
      "message": "scoring rule created successfully",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — Success207

Partial success create Scoring Rules response

```json
{
  "scoring_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "name",
        "json_path": "$.scoring_rules[0].name"
      },
      "message": "required field not found",
      "status": "error"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "2995635000023340019"
      },
      "message": "scoring rule created successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

Error response with code MANDATORY_NOT_FOUND: required field not found (Field: name)

```json
{
  "scoring_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "name",
        "json_path": "$.scoring_rules[0].name"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response with code INVALID_DATA: invalid data (Field: name)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 25,
        "api_name": "name",
        "json_path": "$.scoring_rules[0].name"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Error response with code INVALID_DATA: invalid data (Field: name)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "regex": "[^`~#%^&*()+=\";<>\\[\\]{}|\\\\]+$",
        "api_name": "name",
        "json_path": "$.scoring_rules[0].name"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Error response with code INVALID_DATA: invalid data (Field: description)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 500,
        "api_name": "description",
        "json_path": "$.scoring_rules[0].description"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

Error response with code INVALID_DATA: invalid data (Field: description)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 500,
        "api_name": "description",
        "json_path": "$.scoring_rules[0].description"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

Error response with code INVALID_DATA: Layout id seems to be invalid (Field: id)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.scoring_rules[0].layout.id"
      },
      "message": "Layout id seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ActiveStateLimitExceededResponse1

Error response with code ACTIVE_STATE_LIMIT_EXCEEDED: More than 5 active scoring rules cannot be created for a layout (Field: id)

```json
{
  "scoring_rules": [
    {
      "code": "ACTIVE_STATE_LIMIT_EXCEEDED",
      "details": {
        "api_name": "id",
        "limit": 5,
        "json_path": "$.scoring_rules[0].layout.id"
      },
      "message": "More than 5 active scoring rules cannot be created for a layout",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

Error response with code MANDATORY_NOT_FOUND: required field not found (Field: module)

```json
{
  "scoring_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "module",
        "json_path": "$.scoring_rules[0].module"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse6

Error response with code INVALID_DATA: Module specified seems to be invalid (Field: id)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.scoring_rules[0].module.id"
      },
      "message": "Module specified seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse7

Error response with code INVALID_DATA: Module specified seems to be invalid (Field: api_name)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.scoring_rules[0].module.api_name"
      },
      "message": "Module specified seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ExpectedFieldMissingResponse1

Error response with code EXPECTED_FIELD_MISSING: field_rules or signal_rules is expected(For leads and contacts)

```json
{
  "scoring_rules": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "field_rules",
            "json_path": "$.scoring_rules[0].field_rules"
          },
          {
            "api_name": "signal_rules",
            "json_path": "$.scoring_rules[0].signal_rules"
          }
        ]
      },
      "message": "field_rules or signal_rules is expected",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ExpectedFieldMissingResponse2

Error response with code EXPECTED_FIELD_MISSING: Field_Rules is expected (Except Leads and Contacts)

```json
{
  "scoring_rules": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "field_rules",
            "json_path": "$.scoring_rules[0].field_rules"
          }
        ]
      },
      "message": "Field_Rules is expected",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse3

Error response with code MANDATORY_NOT_FOUND: required field not found (Field: criteria)

```json
{
  "scoring_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "criteria",
        "json_path": "$.scoring_rules[0].field_rules[0].criteria"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AlreadyUsedResponse1

Error response with code ALREADY_USED: The criteria is already given in the same rule under different index (Field: criteria)

```json
{
  "scoring_rules": [
    {
      "code": "ALREADY_USED",
      "details": {
        "api_name": "criteria",
        "exists_in": {
          "api_name": "criteria",
          "json_path": "$.scoring_rules[0].field_rules[0].criteria"
        },
        "json_path": "$.scoring_rules[0].field_rules[1].criteria"
      },
      "message": "The criteria is already given in the same rule under different index",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse4

Error response with code MANDATORY_NOT_FOUND: required field not found (Field: signal)

```json
{
  "scoring_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "signal",
        "json_path": "$.scoring_rules[0].signal_rules[0].signal"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse8

Error response with code INVALID_DATA: Invalid or Unsupported signal id (Field: id)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.scoring_rules[0].signal_rules[0].signal.id"
      },
      "message": "Invalid or Unsupported signal id",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse5

Error response with code MANDATORY_NOT_FOUND: required field not found (Field: field_label)

```json
{
  "scoring_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "field_label",
        "json_path": "$.scoring_rules[0].custom_fields[0].field_label"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse6

Error response with code MANDATORY_NOT_FOUND: required field not found (Field: reference_field)

```json
{
  "scoring_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "reference_field",
        "json_path": "$.scoring_rules[0].custom_fields[0].reference_field"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ExpectedFieldMissingResponse3

Error response with code EXPECTED_FIELD_MISSING: Specify atleast one field

```json
{
  "scoring_rules": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.scoring_rules[0].custom_fields[0].reference_field.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.scoring_rules[0].custom_fields[0].reference_field.api_name"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AlreadyUsedResponse2

Error response with code ALREADY_USED: Duplicate reference field (Field: reference_field)

```json
{
  "scoring_rules": [
    {
      "code": "ALREADY_USED",
      "details": {
        "api_name": "reference_field",
        "json_path": "$.scoring_rules[0].custom_fields[1].reference_field"
      },
      "message": "Duplicate reference field",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FieldLimitExceededResponse1

Error response with code FIELD_LIMIT_EXCEEDED: Field limit reached for the given field type in the given module

```json
{
  "scoring_rules": [
    {
      "code": "FIELD_LIMIT_EXCEEDED",
      "status": "error",
      "details": {
        "limit": 40
      },
      "message": "Field limit reached for the given field type in the given module"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDataResponse1

Error response with code DUPLICATE_DATA: Field label duplicate (Field: field_label)

```json
{
  "scoring_rules": [
    {
      "code": "DUPLICATE_DATA",
      "status": "error",
      "details": {
        "api_name": "field_label",
        "json_path": "$.scoring_rules[0].custom_fields[0].field_label"
      },
      "message": "Field label duplicate"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse9

Error response with code INVALID_DATA: Special characters in field label (Field: field_label)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "field_label",
        "json_path": "$.scoring_rules[0].custom_fields[0].field_label"
      },
      "message": "Special characters in field label",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse10

Error response with code INVALID_DATA: invalid data (Field: field_label)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 50,
        "api_name": "field_label",
        "json_path": "$.scoring_rules[0].custom_fields[0].field_label"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse11

Error response with code INVALID_DATA: Reference field api_name given seems to be invalid (Field: api_name)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "status": "error",
      "details": {
        "api_name": "api_name",
        "json_path": "$.scoring_rules[0].custom_fields[0].reference_field.api_name",
        "supported_values": [
          "Positive_Score",
          "Negative_score",
          "Touch_Point_score",
          "Touch_Point_Positive_Score",
          "Touch_Point_Negative_Score",
          "Score"
        ]
      },
      "message": "Reference field api_name given seems to be invalid"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse12

Error response with code INVALID_DATA: The id given seems to be invalid (Field: id)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "status": "error",
      "details": {
        "api_name": "id",
        "json_path": "$.scoring_rules[0].custom_fields[0].reference_field.id"
      },
      "message": "The id given seems to be invalid"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse1

Error response with code NOT_ALLOWED: System keyword not allowed in field label (Field: field_label)

```json
{
  "scoring_rules": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "field_label",
        "json_path": "$.scoring_rules[0].custom_fields[0].field_label"
      },
      "message": "System keyword not allowed in field label",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LimitExceededResponse1

Error response with code LIMIT_EXCEEDED: More than 50 criteria cannot be configured with field_rules (Field: field_rules)

```json
{
  "scoring_rules": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "api_name": "field_rules",
        "limit": 50,
        "json_path": "$.scoring_rules[0].field_rules"
      },
      "message": "More than 50 criteria cannot be configured with field_rules",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LimitExceededResponse2

Error response with code LIMIT_EXCEEDED: More than 10 scoring rules cannot be created for a layout (Field: id)

```json
{
  "scoring_rules": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "api_name": "id",
        "limit": 10,
        "json_path": "$.scoring_rules[0].layout.id"
      },
      "message": "More than 10 scoring rules cannot be created for a layout",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse13

Error response with code INVALID_DATA: Invalid data type (Field: description)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "description",
        "expected_data_type": "text",
        "json_path": "$.scoring_rules[0].description"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse14

Error response with code INVALID_DATA: Invalid data (Field: description)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "description",
        "maximum_length": 500,
        "json_path": "$.scoring_rules[0].description"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse15

Error response with code INVALID_DATA: Invalid data type (Field: active)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "active",
        "expected_data_type": "boolean",
        "json_path": "$.scoring_rules[0].active"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse16

Error response with code INVALID_DATA: Invalid data type (Field: custom_fields)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "custom_fields",
        "expected_data_type": "jsonarray",
        "json_path": "$.scoring_rules[0].custom_fields"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse17

Error response with code INVALID_DATA: Invalid data (Field: custom_fields)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "custom_fields",
        "maximum_length": 6,
        "json_path": "$.scoring_rules[0].custom_fields"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse7

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: field_label)

```json
{
  "scoring_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "field_label",
        "json_path": "$.scoring_rules[0].custom_fields[0].field_label"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse18

Error response: INVALID_DATA for invalid field_label type

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field_label",
        "expected_data_type": "text",
        "json_path": "$.scoring_rules[0].custom_fields[0].field_label"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse19

Error response: INVALID_DATA for invalid field_label value

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "field_label",
        "maximum_length": 100,
        "json_path": "$.scoring_rules[0].custom_fields[0].field_label"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse8

Error response: MANDATORY_NOT_FOUND for missing reference_field

```json
{
  "scoring_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "reference_field",
        "json_path": "$.scoring_rules[0].custom_fields[0].reference_field"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse20

Error response: INVALID_DATA for invalid reference_field type

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "reference_field",
        "expected_data_type": "jsonobject",
        "json_path": "$.scoring_rules[0].custom_fields[0].reference_field"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse21

Error response: INVALID_DATA for invalid reference_field data

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "reference_field",
        "maximum_length": 1,
        "json_path": "$.scoring_rules[0].custom_fields[0].reference_field"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse22

Error response with code INVALID_DATA: Invalid data type (Field: api_name)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.scoring_rules[0].custom_fields[0].reference_field.api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse23

Error response with code INVALID_DATA: Invalid data (Field: api_name)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 5,
        "json_path": "$.scoring_rules[0].custom_fields[0].reference_field.api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse24

Error response with code INVALID_DATA: Invalid data (Field: api_name)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "supported_values": [
          "Positive_Score",
          "Negative_Score",
          "Touch_Point_Positive_Score",
          "Touch_Point_Negative_Score",
          "Touch_Point_Score",
          "Score"
        ],
        "json_path": "$.scoring_rules[0].custom_fields[0].reference_field.api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse25

Error response with code INVALID_DATA: Invalid data type (Field: field_rules)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field_rules",
        "expected_data_type": "jsonarray",
        "json_path": "$.scoring_rules[0].field_rules"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse26

Error response with code INVALID_DATA: Invalid data (Field: field_rules)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "field_rules",
        "maximum_length": 50,
        "json_path": "$.scoring_rules[0].field_rules"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse9

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: criteria)

```json
{
  "scoring_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "criteria",
        "json_path": "$.scoring_rules[0].field_rules[0].criteria"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse27

Error response with code INVALID_DATA: Invalid data type (Field: criteria)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "criteria",
        "expected_data_type": "jsonobject",
        "json_path": "$.scoring_rules[0].field_rules[0].criteria"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse10

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: score)

```json
{
  "scoring_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "score",
        "json_path": "$.scoring_rules[0].field_rules[0].score"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse28

Error response with code INVALID_DATA: Invalid data type (Field: score)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "score",
        "expected_data_type": "integer",
        "json_path": "$.scoring_rules[0].field_rules[0].score"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse29

Error response with code INVALID_DATA: Invalid data type (Field: signal_rules)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "signal_rules",
        "expected_data_type": "jsonarray",
        "json_path": "$.scoring_rules[0].signal_rules"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse11

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: signal)

```json
{
  "scoring_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "signal",
        "json_path": "$.scoring_rules[0].signal_rules[0].signal"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse30

Error response with code INVALID_DATA: Invalid data type (Field: signal)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "signal",
        "expected_data_type": "jsonobject",
        "json_path": "$.scoring_rules[0].signal_rules[0].signal"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse31

Error response with code INVALID_DATA: Invalid data type (Field: namespace)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "namespace",
        "expected_data_type": "text",
        "json_path": "$.scoring_rules[0].signal_rules[0].signal.namespace"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse32

Error response with code INVALID_DATA: Invalid data (Field: namespace)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "namespace",
        "maximum_length": 100,
        "json_path": "$.scoring_rules[0].signal_rules[0].signal.namespace"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse33

Error response with code INVALID_DATA: Invalid data type (Field: id)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.scoring_rules[0].signal_rules[0].signal.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse34

Error response with code INVALID_DATA: Invalid data (Field: id)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 20,
        "json_path": "$.scoring_rules[0].signal_rules[0].signal.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse12

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: score)

```json
{
  "scoring_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "score",
        "json_path": "$.scoring_rules[0].signal_rules[0].score"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse35

Error response with code INVALID_DATA: Invalid data type (Field: score)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "score",
        "expected_data_type": "integer",
        "json_path": "$.scoring_rules[0].signal_rules[0].score"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse36

Error response with code INVALID_DATA: Invalid data type (Field: layout)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "layout",
        "expected_data_type": "jsonobject",
        "json_path": "$.scoring_rules[0].layout"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse37

Error response with code INVALID_DATA: Invalid data type (Field: id)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.scoring_rules[0].layout.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse38

Error response with code INVALID_DATA: Invalid data type (Field: api_name)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.scoring_rules[0].layout.api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse39

Error response with code INVALID_DATA: Invalid data (Field: api_name)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 8,
        "json_path": "$.scoring_rules[0].layout.api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse13

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: module)

```json
{
  "scoring_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "module",
        "json_path": "$.scoring_rules[0].module"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse40

Error response with code INVALID_DATA: Invalid data type (Field: module)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "module",
        "expected_data_type": "jsonobject",
        "json_path": "$.scoring_rules[0].module"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse41

Error response with code INVALID_DATA: Invalid data type (Field: api_name)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.scoring_rules[0].module.api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse42

Error response with code INVALID_DATA: Invalid data type (Field: id)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.scoring_rules[0].module.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse43

Error response with code INVALID_DATA: Invalid data (Field: id)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 18,
        "json_path": "$.scoring_rules[0].module.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse14

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: name)

```json
{
  "scoring_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "name",
        "json_path": "$.scoring_rules[0].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse44

Error response with code INVALID_DATA: Invalid data type (Field: name)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.scoring_rules[0].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse45

Error response with code INVALID_DATA: Invalid data (Field: name)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 50,
        "json_path": "$.scoring_rules[0].name"
      },
      "status": "error"
    }
  ]
}
```
