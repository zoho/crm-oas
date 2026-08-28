# Examples: putScoringRuleById

**PUT /settings/automation/scoring_rules/{ruleId}**

## Request examples

### `application/json` — SamplePutRequest

Sample update Scoring Rule by ID request body

```json
{
  "scoring_rules": [
    {
      "id": "111114000000072349",
      "name": "Altered scoring",
      "field_rules": [
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
        },
        {
          "id": "111114000000004892",
          "score": 45
        }
      ],
      "signal_rules": [
        {
          "id": "111114000000012345",
          "_delete": null
        },
        {
          "score": -100,
          "signal": {
            "namespace": "zoho.emailinsight.bounce",
            "id": "111114000000034755"
          }
        }
      ],
      "custom_fields": [
        {
          "field_label": "Contact Total Score",
          "reference_field": {
            "api_name": "Score"
          }
        },
        {
          "id": "111114000000012345",
          "field_label": "Total score"
        }
      ]
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Successful update Scoring Rule by ID response

```json
{
  "scoring_rules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111114000000313122"
      },
      "message": "scoring rule updated successfully",
      "status": "success"
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

### Status `400` — `application/json` — DuplicateDataResponse1

Error response with code DUPLICATE_DATA: The data is already given in the name (Field: name)

```json
{
  "scoring_rules": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.scoring_rules[0].name"
      },
      "message": "The data is already given in the name",
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

### Status `400` — `application/json` — AlreadyUsedResponse1

Error response with code ALREADY_USED: The custom field has already used in other places (Field: id)

```json
{
  "scoring_rules": [
    {
      "code": "ALREADY_USED",
      "status": "error",
      "details": {
        "api_name": "id",
        "id": "1000000000047",
        "json_path": "$.scoring_rules[0].custom_fields[2].id",
        "associated_places": [
          {
            "name": "L WFR",
            "id": "111111000000067060",
            "type": "workflow"
          }
        ]
      },
      "message": "The custom field has already used in other places"
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

### Status `400` — `application/json` — DuplicateDataResponse2

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

### Status `400` — `application/json` — InvalidDataResponse4

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

### Status `400` — `application/json` — InvalidDataResponse5

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

### Status `400` — `application/json` — InvalidDataResponse6

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

### Status `400` — `application/json` — InvalidDataResponse7

Error response with code INVALID_DATA: The id given seems to be invalid (Field: id)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "status": "error",
      "details": {
        "api_name": "id",
        "json_path": "$.scoring_rules[0].custom_fields[1].id"
      },
      "message": "The id given seems to be invalid"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse8

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

### Status `400` — `application/json` — MandatoryNotFoundResponse1

Error response with code MANDATORY_NOT_FOUND: required field not found (Field: reference_field | field_label)

```json
{
  "scoring_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "status": "error",
      "details": {
        "api_name": "reference_field | field_label",
        "json_path": "$.scoring_rules[0].custom_fields[0].reference_field | $.scoring_rules[0].custom_fields[0].field_label"
      },
      "message": "required field not found"
    }
  ]
}
```

### Status `400` — `application/json` — AmbiguityDuringProcessingResponse1

Error response with code AMBIGUITY_DURING_PROCESSING: Ambiguity while processing the request

```json
{
  "scoring_rules": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "status": "error",
      "details": {
        "ambiguity_due_to": [
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
      "message": "Ambiguity while processing the request"
    }
  ]
}
```

### Status `400` — `application/json` — ExpectedFieldMissingResponse1

Error response with code EXPECTED_FIELD_MISSING: Specify atleast one field

```json
{
  "scoring_rules": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "status": "error",
      "details": {
        "expected_fields": [
          {
            "api_name": "api_name",
            "json_path": "$.scoring_rules[0].custom_fields[0].reference_field.api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.scoring_rules[0].custom_fields[0].reference_field.id"
          }
        ]
      },
      "message": "Specify atleast one field"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDataResponse3

Error response with code DUPLICATE_DATA: Field label duplicate (Field: field_label)

```json
{
  "scoring_rules": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "field_label",
        "json_path": "$.scoring_rules[0].custom_fields[0].field_label"
      },
      "message": "Field label duplicate",
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

### Status `400` — `application/json` — DuplicateDataResponse4

Error response with code DUPLICATE_DATA: The criteria is already available in the rule (Field: criteria)

```json
{
  "scoring_rules": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "criteria",
        "json_path": "$.scoring_rules[0].field_rules[0].criteria"
      },
      "message": "The criteria is already available in the rule",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse9

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
        "json_path": "$.scoring_rules[0].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse10

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
        "json_path": "$.scoring_rules[0].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse11

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

### Status `400` — `application/json` — InvalidDataResponse12

Error response with code INVALID_DATA: Invalid data (Field: name)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 15,
        "json_path": "$.scoring_rules[0].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse13

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

### Status `400` — `application/json` — InvalidDataResponse14

Error response with code INVALID_DATA: Invalid data (Field: field_rules)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "field_rules",
        "maximum_length": 2,
        "json_path": "$.scoring_rules[0].field_rules"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse15

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

### Status `400` — `application/json` — InvalidDataResponse16

Error response with code INVALID_DATA: Invalid data (Field: criteria)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "criteria",
        "maximum_length": 4,
        "json_path": "$.scoring_rules[0].field_rules[0].criteria"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse33

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

### Status `400` — `application/json` — InvalidDataResponse34

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

### Status `400` — `application/json` — InvalidDataResponse35

Error response with code INVALID_DATA: Invalid data (Field: signal_rules)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "signal_rules",
        "maximum_length": 2,
        "json_path": "$.scoring_rules[0].signal_rules"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse36

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
        "json_path": "$.scoring_rules[0].signal_rules[0].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse37

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
        "json_path": "$.scoring_rules[0].signal_rules[0].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse39

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

### Status `400` — `application/json` — InvalidDataResponse40

Error response with code INVALID_DATA: Invalid data (Field: custom_fields)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "custom_fields",
        "maximum_length": 2,
        "json_path": "$.scoring_rules[0].custom_fields"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse41

Error response with code INVALID_DATA: Invalid data type (Field: field_label)

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

### Status `400` — `application/json` — InvalidDataResponse43

Error response with code INVALID_DATA: Invalid data type (Field: reference_field)

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

### Status `400` — `application/json` — InvalidDataResponse45

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
