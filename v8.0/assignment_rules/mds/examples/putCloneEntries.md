# Examples: putCloneEntries

**PUT /settings/automation/assignment_rules/{id}/actions/clone_entries**

## Parameter examples

### `id` (path) — Typical

sample value 1

```json
"123456789"
```

### `id` (path) — LargeId

Maximum long value example

```json
"9223372036854775807"
```

## Request examples

### `application/json` — SamplePutRequest

Sample request body

```json
{
  "assignment_rules": [
    {
      "rule_entries": [
        {
          "id": "526435000000001111",
          "criteria": null,
          "assign_to": {
            "type": "users",
            "resources": [
              {
                "id": "526435000000670072"
              },
              {
                "id": "526435000000227013"
              }
            ]
          },
          "user_availability_based_on": [
            "online_status",
            "shift_timing"
          ],
          "followup_actions": [
            {
              "type": "tasks",
              "resources": [
                {
                  "id": "526435000014344004"
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Successful Assignment Rule operation

```json
{
  "assignment_rules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "123456",
        "rule_entries": [
          {
            "id": "1234567890098765432"
          }
        ]
      },
      "message": "",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse2

INVALID_DATA error for Assignment Rule data

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 1,
    "api_name": "assignment_rules",
    "json_path": "$.assignment_rules"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse3

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "rule_entries",
        "expected_data_type": "jsonarray",
        "json_path": "$.assignment_rules[*].rule_entries"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "rule_entries",
        "maximum_length": 200,
        "json_path": "$.assignment_rules[*].rule_entries"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "rule_entries",
        "minimum_length": 1,
        "json_path": "$.assignment_rules[*].rule_entries"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse6

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.assignment_rules[*].rule_entries[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse7

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "criteria",
        "expected_data_type": "jsonobject",
        "json_path": "$.assignment_rules[*].rule_entries[*].criteria"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse8

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "assign_to",
        "expected_data_type": "jsonobject",
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to"
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
  "assignment_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "type",
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response2

Error response

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response3

Error response

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "users",
          "role",
          "group",
          "profile",
          "criteria",
          "zia_suggested_users"
        ],
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response4

Error response

```json
{
  "assignment_rules": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.type"
        },
        "api_name": "criteria",
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.assignment_rules.rule_entries.assign_to.criteria"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response5

Error response

```json
{
  "assignment_rules": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.type"
        },
        "api_name": "resource",
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.assignment_rules.rule_entries.assign_to.resource"
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
  "assignment_rules": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.type"
        },
        "api_name": "resources",
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.assignment_rules.rule_entries.assign_to.resources"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response7

Error response

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "criteria",
        "expected_data_type": "jsonobject",
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.criteria"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response8

Error response

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "resource",
        "expected_data_type": "jsonobject",
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.resource"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response9

Error response

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.resource.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response10

Error response

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "resources",
        "expected_data_type": "jsonarray",
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.resources"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response11

Error response

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "resources",
        "maximum_length": 50,
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.resources"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error400Response12

Error response

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "resources",
        "minimum_length": 1,
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.resources"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

MANDATORY_NOT_FOUND error for Assignment Rule name

```json
{
  "assignment_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "id",
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.resources[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse9

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.resources[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse10

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "user_availability_based_on",
        "expected_data_type": "jsonarray",
        "json_path": "$.assignment_rules[*].rule_entries[*].user_availability_based_on"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse11

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "user_availability_based_on",
        "maximum_length": 8,
        "json_path": "$.assignment_rules[*].rule_entries[*].user_availability_based_on"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse12

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "followup_actions",
        "expected_data_type": "jsonarray",
        "json_path": "$.assignment_rules[*].rule_entries[*].followup_actions"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse13

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "followup_actions",
        "maximum_length": 1,
        "json_path": "$.assignment_rules[*].rule_entries[*].followup_actions"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse14

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "followup_actions",
        "minimum_length": 1,
        "json_path": "$.assignment_rules[*].rule_entries[*].followup_actions"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

MANDATORY_NOT_FOUND error for Assignment Rule name

```json
{
  "assignment_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "type",
        "json_path": "$.assignment_rules[*].rule_entries[*].followup_actions[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse15

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.assignment_rules[*].rule_entries[*].followup_actions[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse16

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "maximum_length": 5,
        "json_path": "$.assignment_rules[*].rule_entries[*].followup_actions[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse17

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "tasks"
        ],
        "json_path": "$.assignment_rules[*].rule_entries[*].followup_actions[*].type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse1

Error response with code DEPENDENT_FIELD_MISSING: Dependent field is missing (Field: resources)

```json
{
  "assignment_rules": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.assignment_rules[*].rule_entries[*].followup_actions[*].type"
        },
        "api_name": "resources",
        "json_path": "$.assignment_rules[*].rule_entries[*].followup_actions[*].assignment_rules.rule_entries.followup_actions.resources"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse18

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "resources",
        "expected_data_type": "jsonarray",
        "json_path": "$.assignment_rules[*].rule_entries[*].followup_actions[*].resources"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse19

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "resources",
        "maximum_length": 1,
        "json_path": "$.assignment_rules[*].rule_entries[*].followup_actions[*].resources"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse20

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "resources",
        "minimum_length": 1,
        "json_path": "$.assignment_rules[*].rule_entries[*].followup_actions[*].resources"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse3

MANDATORY_NOT_FOUND error for Assignment Rule name

```json
{
  "assignment_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "id",
        "json_path": "$.assignment_rules[*].rule_entries[*].followup_actions[*].resources[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse21

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.assignment_rules[*].rule_entries[*].followup_actions[*].resources[*].id"
      },
      "status": "error"
    }
  ]
}
```
