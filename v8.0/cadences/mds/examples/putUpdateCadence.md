# Examples: putUpdateCadence

**PUT /settings/automation/cadences/{id}**

## Request examples

### `application/json` — SamplePutRequest

Sample Cadence update request body

```json
{
  "cadences": [
    {
      "id": "111112000000069836",
      "name": "cadence",
      "description": "description",
      "execution_details": {
        "unenroll_properties": [
          {
            "type": "end_date",
            "details": {}
          },
          {
            "type": "automatic_unenroll"
          },
          {
            "type": "end_date",
            "details": {
              "unenroll_date": "2025-11-30"
            }
          },
          {
            "type": "criteria",
            "details": {
              "criteria": {
                "field": {
                  "api_name": "Annual_Revenue"
                },
                "comparator": "equal",
                "value": 123
              }
            }
          },
          {
            "type": "followup_criteria",
            "details": {
              "type": "Tasks",
              "details": {
                "criteria": {
                  "field": {
                    "api_name": "Subject",
                    "id": "111112000000004066"
                  },
                  "comparator": "equal",
                  "value": "teste"
                },
                "specific": false,
                "state": null
              }
            }
          }
        ]
      },
      "follow_ups": [
        {
          "parent_follow_up": {
            "id": "111112000000106722"
          },
          "id": "111112000000106723",
          "triggers": [
            "Completed"
          ],
          "execute_after": {
            "unit": 10,
            "period": "minutes"
          },
          "action": {
            "type": "schedule_call",
            "id": "111112000000003660",
            "details": {
              "layout": {
                "id": "111112000000003660",
                "name": "Standard"
              },
              "module": {
                "id": "111112000000002654",
                "api_name": "Calls"
              },
              "field_mappings": [
                {
                  "field": {
                    "id": "111112000000004208",
                    "api_name": "Call_Type"
                  },
                  "type": "static",
                  "value": "Outbound"
                }
              ]
            }
          }
        },
        {
          "parent_follow_up": {
            "id": "111112000000106723"
          },
          "reference_id": "{{Followup_3}}",
          "triggers": [
            "Completed"
          ],
          "execute_after": {
            "unit": 1,
            "period": "days"
          },
          "action": {
            "type": "email_notifications",
            "id": "111112000000003661"
          }
        }
      ]
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Successful Cadence update response

```json
{
  "cadences": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111112000000092007"
      },
      "message": "Cadences updated successfully",
      "status": "success"
    }
  ]
}
```

### Status `200` — `application/json` — DraftCadenceSuccess

Successful Cadence draft save response

```json
{
  "cadences": [
    {
      "code": "SUCCESS",
      "details": {
        "draft_cadence": {
          "id": "111111000000070063"
        },
        "id": "111111000000070062"
      },
      "message": "Cadences updated successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse0

Invalid field data value error

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 3
  },
  "message": "the given id seems to be invalid",
  "status": "error"
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

Invalid field data value error

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

Invalid field data value error

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

Invalid field data value error

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

### Status `400` — `application/json` — MandatoryNotFoundResponse4

Missing required field error

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

Invalid field data value error

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

Invalid field data value error

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

### Status `400` — `application/json` — InvalidDataResponse7

Invalid field data value error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "type",
        "json_path": "$.cadences[0].execution_details.unenroll_properties[0].type",
        "supported_values": [
          "automatic_unenroll",
          "end_date",
          "criteria",
          "followup_criteria"
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LimitExceededResponse3

Follow-up steps limit exceeded error

```json
{
  "cadences": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "api_name": "type",
        "limit": 1,
        "json_path": "$.cadences[0].execution_details.unenroll_properties[2].type"
      },
      "message": "Given unenroll type limit is exceeded",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse2

Missing required dependent field error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.cadences[0].execution_details.unenroll_properties[0].type"
        },
        "api_name": "details",
        "json_path": "$.cadences[0].execution_details.unenroll_properties[0].details"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse3

Missing required dependent field error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.cadences[0].execution_details.unenroll_properties[0].type"
        },
        "api_name": "unenroll_date",
        "json_path": "$.cadences[0].execution_details.unenroll_properties[0].details.unenroll_date"
      },
      "message": "dependent field is missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse8

Invalid field data value error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "unenroll_date",
        "json_path": "$.cadences[0].execution_details.unenroll_properties.unenroll_date"
      },
      "message": "the given format is invalid please provide the value as MM/DD/YYYY",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse4

Missing required dependent field error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "id",
          "json_path": "$.cadences[0].execution_details.unenroll_properties[2].id"
        },
        "api_name": "criteria",
        "json_path": "$.cadences[0].execution_details.unenroll_properties[2].details.criteria"
      },
      "message": "dependent field is missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse5

Missing required dependent field error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.cadences[0].execution_details.unenroll_properties[3].type"
        },
        "api_name": "details",
        "json_path": "$.cadences[0].execution_details.unenroll_properties[3].details.details"
      },
      "message": "dependent field is missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse1

Dependent field value mismatch error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.cadences[0].execution_details.unenroll_properties[3].type"
        },
        "api_name": "type",
        "json_path": "$.cadences[0].execution_details.unenroll_properties[3].details.type",
        "supported_values": [
          "tasks",
          "schedule_call",
          "email_notifications",
          "whatsapp_message_notification"
        ]
      },
      "message": "Dependent Field is not matching",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse6

Missing required dependent field error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.cadences[0].execution_details.unenroll_properties[3].type"
        },
        "api_name": "specific",
        "json_path": "$.cadences[0].execution_details.unenroll_properties[3].details.specific"
      },
      "message": "dependent field is missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse7

Missing required dependent field error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.cadences[0].execution_details.unenroll_properties[3].type"
        },
        "api_name": "state",
        "json_path": "$.cadences[0].execution_details.unenroll_properties[3].details.state"
      },
      "message": "dependent field is missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AmbiguityDuringProcessingResponse1

Ambiguity during processing error

```json
{
  "cadences": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "specific",
            "json_path": "$.cadences[0].execution_details.unenroll_properties[3].details.specific"
          },
          {
            "api_name": "state",
            "json_path": "$.cadences[0].execution_details.unenroll_properties[3].details.state"
          }
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse8

Missing required dependent field error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.cadences[0].execution_details.unenroll_properties[3].details.type"
        },
        "api_name": "criteria",
        "json_path": "$.cadences[0].execution_details.unenroll_properties[3].details.details.criteria"
      },
      "message": "dependent field is missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse5

Missing required field error

```json
{
  "cadences": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "reference_id",
        "json_path": "$.cadences[0].follow_ups[0].reference_id"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse6

Missing required field error

```json
{
  "cadences": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "parent_follow_up",
        "json_path": "$.cadences[0].follow_ups[1].parent_follow_up"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse7

Missing required field error

```json
{
  "cadences": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "action",
        "json_path": "$.cadences[0].follow_ups[0].action"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse8

Missing required field error

```json
{
  "cadences": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "type",
        "json_path": "$.cadences[0].follow_ups[0].action.type"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ExpectedFieldMissingResponse1

Missing expected field error

```json
{
  "cadences": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "reference_id",
            "json_path": "$.cadences[0].follow_ups[1].parent_follow_up.reference_id"
          },
          {
            "api_name": "id",
            "json_path": "$.cadences[0].follow_ups[1].parent_follow_up.id"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse9

Invalid field data value error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "reference_id",
        "json_path": "$.cadences[0].follow_ups[1].parent_follow_up.reference_id"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse10

Invalid field data value error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "reference_id",
        "json_path": "$.cadences[0].follow_ups[0].reference_id"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse11

Invalid field data value error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "type",
        "json_path": "$.cadences[0].follow_ups[0].action.type",
        "supported_values": [
          "tasks",
          "email_notifications",
          "schedule_call",
          "whatsapp_message_notification"
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse9

Missing required dependent field error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.cadences[0].follow_ups[0].action.type"
        },
        "api_name": "id",
        "json_path": "$.cadences[0].follow_ups[0].action.id"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse10

Missing required dependent field error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.cadences[0].follow_ups[1].action.type"
        },
        "api_name": "details",
        "json_path": "$.cadences[0].follow_ups[1].action.details"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse12

Invalid field data value error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.cadences[0].FollowUp[0].action.id"
      },
      "message": "the given actionid seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse13

Invalid field data value error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.cadences[0].FollowUp[0].action.id"
      },
      "message": "Action is already associated with another rule",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse9

Missing required field error

```json
{
  "cadences": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "module",
        "json_path": "$.cadences[0].follow_ups[1].action.details.module"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse10

Missing required field error

```json
{
  "cadences": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "layout",
        "json_path": "$.cadences[0].follow_ups[1].action.details.layout"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse11

Missing required field error

```json
{
  "cadences": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "field_mappings",
        "json_path": "$.cadences[0].follow_ups[1].action.details.field_mappings"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse12

Missing required field error

```json
{
  "cadences": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "field",
        "json_path": "$.cadences[0].follow_ups[1].action.details.field_mappings[0].field"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ExpectedFieldMissingResponse2

Second expected field missing error

```json
{
  "cadences": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "api_name",
            "json_path": "$.cadences[0].follow_ups[1].action.details.field_mappings[0].field.api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.cadences[0].follow_ups[1].action.details.field_mappings[0].field.id"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse13

Missing required field error

```json
{
  "cadences": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "type",
        "json_path": "$.cadences[0].follow_ups[1].action.details.field_mappings[0].type"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse14

Invalid field data value error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "type",
        "json_path": "$.cadences[0].follow_ups[1].action.details.field_mappings[0].type",
        "supported_values": [
          "static",
          "reference",
          "time_computed",
          "execution_time",
          "merge_field"
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse2

Inconsistent dependent field values error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "reference_id",
          "json_path": "$.cadences[0].follow_ups[1].parent_follow_up.reference_id"
        },
        "api_name": "triggers",
        "json_path": "$.cadences[0].follow_ups[1].triggers[0]",
        "supported_values": []
      },
      "message": "dependent mismatch",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AlreadyUsedResponse1

Field value already in use error

```json
{
  "cadences": [
    {
      "code": "ALREADY_USED",
      "details": {
        "api_name": "triggers",
        "exists_in": {
          "api_name": "triggers",
          "json_path": "$.cadences[0].follow_ups[1].triggers[0]"
        },
        "json_path": "$.cadences[0].follow_ups[1].triggers[1]"
      },
      "message": "trigger type is already given in the same request under different key",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AmbiguityDuringProcessingResponse2

Conflicting values ambiguity error

```json
{
  "cadences": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "triggers",
            "json_path": "$.cadences[0].follow_ups[1].triggers[0]"
          },
          {
            "api_name": "triggers",
            "json_path": "$.cadences[0].follow_ups[1].triggers[1]"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse14

Missing required field error

```json
{
  "cadences": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "unit",
        "json_path": "$.cadences[0].follow_ups[1].execute_after.unit"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse15

Missing required field error

```json
{
  "cadences": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "period",
        "json_path": "$.cadences[0].follow_ups[1].execute_after.period"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse16

Invalid field data value error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "period",
        "json_path": "$.cadences[0].follow_ups[1].execute_after.period",
        "supported_values": [
          "minutes",
          "hours",
          "business_hours",
          "days",
          "business_days",
          "months"
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse17

Invalid field data value error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "unit",
        "json_path": "$.cadences[0].follow_ups[1].execute_after.unit"
      },
      "message": "the value given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse11

Missing required dependent field error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "triggers",
          "json_path": "$.cadences[0].follow_ups[1].triggers[0]"
        },
        "api_name": "execute_after",
        "json_path": "$.cadences[0].follow_ups[1].execute_after"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse12

Missing required dependent field error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "period",
          "json_path": "$.cadences[0].execution_details.execute_every.period"
        },
        "api_name": "unit",
        "json_path": "$.cadences[0].execution_details.execute_every.unit"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse18

Invalid field data type error

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

Invalid field data type error

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

Invalid field data type error

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

Invalid field data type error

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

Invalid field data type error

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

Invalid field data type error

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

Invalid field data type error

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

Invalid field data type error

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

Invalid field data type error

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

Invalid field data type error

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

Invalid field data type error

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

Invalid field data type error

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

### Status `400` — `application/json` — InvalidDataTypeResponse36

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "unenroll_properties",
        "expected_data_type": "jsonarray",
        "json_path": "$.cadences[*].cadences.execution_details.unenroll_properties"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse37

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.cadences[*].cadences.execution_details.unenroll_properties[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse39

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "details",
        "expected_data_type": "jsonobject",
        "json_path": "$.cadences[*].cadences.execution_details.unenroll_properties[*].details"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse40

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "follow_ups",
        "expected_data_type": "jsonarray",
        "json_path": "$.cadences[*].cadences.follow_ups"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse41

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "parent_follow_up",
        "expected_data_type": "jsonobject",
        "json_path": "$.cadences[*].cadences.follow_ups[*].parent_follow_up"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse42

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "reference_id",
        "expected_data_type": "text",
        "json_path": "$.cadences[*].cadences.follow_ups[*].parent_follow_up.reference_id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse43

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "reference_id",
        "expected_data_type": "text",
        "json_path": "$.cadences[*].cadences.follow_ups[*].reference_id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse44

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "triggers",
        "expected_data_type": "jsonarray",
        "json_path": "$.cadences[*].cadences.follow_ups[*].triggers"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse46

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "execute_after",
        "expected_data_type": "jsonobject",
        "json_path": "$.cadences[*].cadences.follow_ups[*].execute_after"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse47

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "unit",
        "expected_data_type": "integer",
        "json_path": "$.cadences[*].cadences.follow_ups[*].execute_after.unit"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse48

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "period",
        "expected_data_type": "text",
        "json_path": "$.cadences[*].cadences.follow_ups[*].execute_after.period"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse52

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "action",
        "expected_data_type": "jsonobject",
        "json_path": "$.cadences[*].cadences.follow_ups[*].action"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse53

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.cadences[*].cadences.follow_ups[*].action.type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse55

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.cadences[*].cadences.follow_ups[*].action.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse56

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "details",
        "expected_data_type": "jsonobject",
        "json_path": "$.cadences[*].cadences.follow_ups[*].action.details"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse57

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "layout",
        "expected_data_type": "jsonobject",
        "json_path": "$.cadences[*].cadences.follow_ups[*].action.details.layout"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse58

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.cadences[*].cadences.follow_ups[*].action.details.layout.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse59

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.cadences[*].cadences.follow_ups[*].action.details.layout.name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse60

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "module",
        "expected_data_type": "jsonobject",
        "json_path": "$.cadences[*].cadences.follow_ups[*].action.details.module"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse61

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.cadences[*].cadences.follow_ups[*].action.details.module.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse62

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.cadences[*].cadences.follow_ups[*].action.details.module.api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse63

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field_mappings",
        "expected_data_type": "jsonarray",
        "json_path": "$.cadences[*].cadences.follow_ups[*].action.details.field_mappings"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse64

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field",
        "expected_data_type": "jsonobject",
        "json_path": "$.cadences[*].cadences.follow_ups[*].action.details.field_mappings[*].field"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse65

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.cadences[*].cadences.follow_ups[*].action.details.field_mappings[*].field.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse66

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.cadences[*].cadences.follow_ups[*].action.details.field_mappings[*].field.api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse67

Invalid field data type error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.cadences[*].cadences.follow_ups[*].action.details.field_mappings[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionResponse1

No permission to update Cadence error

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
