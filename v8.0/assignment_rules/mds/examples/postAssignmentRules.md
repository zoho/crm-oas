# Examples: postAssignmentRules

**POST /settings/automation/assignment_rules**

## Request examples

### `application/json` — SamplePostRequest

Sample request body

```json
{
  "assignment_rules": [
    {
      "api_name": "Lead_Assignment_Rule_US",
      "name": "Lead owner assignment rule - US",
      "description": "Rule to assign owners for US leads",
      "default_assignee": {
        "type": "user",
        "resource": {
          "id": "32425678"
        }
      },
      "rule_entries": [
        {
          "criteria": {
            "field": {
              "api_name": "Annual_Revenue"
            },
            "comparator": "equal",
            "value": "123"
          },
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

### Status `201` — `application/json` — Success201

Successful Assignment Rule operation

```json
{
  "assignment_rules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "123456789",
        "rule_entries": [
          {
            "id": "123456789"
          }
        ]
      },
      "message": "created successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

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

### Status `400` — `application/json` — LimitExceededResponse1

LIMIT_EXCEEDED error for Assignment Rules

```json
{
  "assignment_rules": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit": 10
      },
      "message": "limit exceeded",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDataResponse1

DUPLICATE_DATA error for Assignment Rule name

```json
{
  "assignment_rules": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.assignment_rules[0].api_name"
      },
      "message": "The data is already given in the api_name",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse2

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 10,
        "api_name": "rule_entries",
        "json_path": "$.assignment_rules[0].rule_entries"
      },
      "message": "{error_message}",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — RequiredParamMissingResponse1

Error response with code REQUIRED_PARAM_MISSING: One of the expected param is missing

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "module"
  },
  "message": "One of the expected param is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — DependentMismatchResponse1

Error response with code DEPENDENT_MISMATCH: Invalid data (Field: ID)

```json
{
  "assignment_rules": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "param_name": "module"
        },
        "api_name": "id",
        "json_path": "$.assignment_rules[0].default_assignee.id"
      },
      "message": "dependent mismatch",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 10,
        "api_name": "rule_entries",
        "json_path": "$.assignment_rules[0].rule_entries"
      },
      "message": "{error_message}",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse2

Error response with code DEPENDENT_MISMATCH: Invalid data (Field: type)

```json
{
  "assignment_rules": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "param_name": "module"
        },
        "api_name": "type",
        "json_path": "$.assignment_rules[0].rule_entries[*].assign_to.resources[*].type"
      },
      "message": "dependent mismatch",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse3

Error response with code DEPENDENT_MISMATCH: Invalid data (Field: type)

```json
{
  "assignment_rules": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "param_name": "module"
        },
        "api_name": "type",
        "json_path": "$.assignment_rules[0].rule_entries[*].assign_to.resources[*].type"
      },
      "message": "dependent mismatch",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse4

Error response with code DEPENDENT_MISMATCH: Invalid data (Field: ID)

```json
{
  "assignment_rules": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "param_name": "module"
        },
        "api_name": "id",
        "json_path": "$.assignment_rules[0].rule_entries[*].assign_to.resources[*].id"
      },
      "message": "dependent mismatch",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse5

Error response with code DEPENDENT_MISMATCH: A Requester profile user is not allowed to be the owner of a record. (Field: ID)

```json
{
  "assignment_rules": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "param_name": "module"
        },
        "api_name": "id",
        "json_path": "$.assignment_rules[0].rule_entries[*].assign_to.resources[*].id"
      },
      "message": "dependent mismatch",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse6

Error response with code DEPENDENT_MISMATCH: A Requester profile users are not allowed to be the owner of a record. (Field: ID)

```json
{
  "assignment_rules": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "param_name": "module"
        },
        "api_name": "id",
        "json_path": "$.assignment_rules[0].rule_entries[i].assign_to.resources[i].id"
      },
      "message": "dependent mismatch",
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
      "details": {
        "api_name": "id",
        "json_path": "$.assignment_rules[0].rule_entries[*].id"
      },
      "message": "",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDataResponse2

DUPLICATE_DATA error for Assignment Rule name

```json
{
  "assignment_rules": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.assignment_rules[0].name"
      },
      "message": "The data is already given in the name",
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
      "details": {
        "api_name": "id",
        "json_path": "$.assignment_rules[0].rule_entries[*].assign_to.resource.id"
      },
      "message": "",
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
      "details": {
        "api_name": "id",
        "json_path": "$.assignment_rules[0].rule_entries[*].assign_to.resources[*].id"
      },
      "message": "",
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
      "details": {
        "api_name": "id",
        "json_path": "$.assignment_rules[0].rule_entries[*].followup_actions[*].resources[*].id"
      },
      "message": "",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDataResponse3

DUPLICATE_DATA error for Assignment Rule name

```json
{
  "assignment_rules": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.assignment_rules[0].name"
      },
      "message": "The data is already given in the name",
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
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.assignment_rules[*].api_name"
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
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 100,
        "json_path": "$.assignment_rules[*].api_name"
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
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "minimum_length": 1,
        "json_path": "$.assignment_rules[*].api_name"
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
        "api_name": "name",
        "json_path": "$.assignment_rules[*].name"
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
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.assignment_rules[*].name"
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
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 100,
        "json_path": "$.assignment_rules[*].name"
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
        "api_name": "name",
        "minimum_length": 1,
        "json_path": "$.assignment_rules[*].name"
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
      "message": "Invalid data type",
      "details": {
        "api_name": "description",
        "expected_data_type": "text",
        "json_path": "$.assignment_rules[*].description"
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
      "message": "Invalid data",
      "details": {
        "api_name": "description",
        "maximum_length": 250,
        "json_path": "$.assignment_rules[*].description"
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
        "api_name": "default_assignee",
        "json_path": "$.assignment_rules[*].default_assignee"
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
      "message": "Invalid data type",
      "details": {
        "api_name": "default_assignee",
        "expected_data_type": "jsonobject",
        "json_path": "$.assignment_rules[*].default_assignee"
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
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.assignment_rules[*].default_assignee.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ExpectedFieldMissingResponse1

Error response with code EXPECTED_FIELD_MISSING: One of the required fields is missing

```json
{
  "assignment_rules": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "message": "One of the required fields is missing",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.assignment_rules[*].default_assignee.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.assignment_rules[*].default_assignee.assignment_rules.default_assignee.api_name"
          }
        ]
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
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.assignment_rules[*].default_assignee.api_name"
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
        "api_name": "api_name",
        "supported_values": [
          "${CURRENTUSER}"
        ],
        "json_path": "$.assignment_rules[*].default_assignee.api_name"
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

### Status `400` — `application/json` — InvalidDataResponse21

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

### Status `400` — `application/json` — InvalidDataResponse22

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

### Status `400` — `application/json` — InvalidDataResponse23

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

### Status `400` — `application/json` — MandatoryNotFoundResponse3

MANDATORY_NOT_FOUND error for Assignment Rule name

```json
{
  "assignment_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "assign_to",
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse24

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

### Status `400` — `application/json` — MandatoryNotFoundResponse4

MANDATORY_NOT_FOUND error for Assignment Rule name

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

### Status `400` — `application/json` — InvalidDataResponse25

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
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse26

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "minimum_length": -2,
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse27

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

### Status `400` — `application/json` — DependentFieldMissingResponse1

Error response with code DEPENDENT_FIELD_MISSING: Dependent field is missing (Field: criteria)

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

### Status `400` — `application/json` — DependentFieldMissingResponse2

Error response with code DEPENDENT_FIELD_MISSING: Dependent field is missing (Field: resource)

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

### Status `400` — `application/json` — DependentFieldMissingResponse3

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

### Status `400` — `application/json` — InvalidDataResponse28

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
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.criteria"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse29

INVALID_DATA error for Assignment Rule data

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

### Status `400` — `application/json` — MandatoryNotFoundResponse5

MANDATORY_NOT_FOUND error for Assignment Rule name

```json
{
  "assignment_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "id",
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.resource.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse30

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
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.resource.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse31

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
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.resources"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse32

INVALID_DATA error for Assignment Rule data

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

### Status `400` — `application/json` — InvalidDataResponse33

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
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.resources"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse6

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

### Status `400` — `application/json` — InvalidDataResponse34

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

### Status `400` — `application/json` — InvalidDataResponse35

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

### Status `400` — `application/json` — InvalidDataResponse36

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "user_availability_based_on",
        "maximum_length": 2,
        "json_path": "$.assignment_rules[*].rule_entries[*].user_availability_based_on"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse37

INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "user_availability_based_on",
        "supported_values": [
          "online_status",
          "shift_timing"
        ],
        "json_path": "$.assignment_rules[*].rule_entries[*].user_availability_based_on"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse38

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

### Status `400` — `application/json` — InvalidDataResponse39

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

### Status `400` — `application/json` — InvalidDataResponse40

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

### Status `400` — `application/json` — MandatoryNotFoundResponse7

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

### Status `400` — `application/json` — InvalidDataResponse41

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

### Status `400` — `application/json` — InvalidDataResponse42

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

### Status `400` — `application/json` — DependentFieldMissingResponse4

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

### Status `400` — `application/json` — InvalidDataResponse43

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

### Status `400` — `application/json` — InvalidDataResponse44

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

### Status `400` — `application/json` — InvalidDataResponse45

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

### Status `400` — `application/json` — MandatoryNotFoundResponse8

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

### Status `400` — `application/json` — InvalidDataResponse46

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
