# Examples: updateWorkflowRule

**PUT /settings/automation/workflow_rules**

## Request examples

### `application/json` — SamplePutRequest

Sample request body

```json
{
  "workflow_rules": [
    {
      "execute_when": {
        "type": "create_or_edit",
        "details": {
          "repeat": true,
          "trigger_module": {
            "api_name": "Contacts",
            "id": "3361265000000000129"
          }
        }
      },
      "conditions": [
        {
          "criteria_details": {
            "criteria": {
              "field": {
                "api_name": "Department",
                "id": "3361265000000000455"
              },
              "comparator": "equal",
              "value": "${EMPTY}"
            }
          },
          "instant_actions": {
            "actions": [
              {
                "id": "3361265000006492245",
                "name": "To users : user2 testUser, testUser1",
                "type": "assign_owner",
                "details": {
                  "module": {
                    "api_name": "Vendors"
                  },
                  "assign_to": [
                    {
                      "resource": {
                        "id": "3361265000002134004",
                        "name": "user2 testUser"
                      },
                      "type": "user"
                    },
                    {
                      "resource": {
                        "id": "3361265000002134024",
                        "name": "testUser1"
                      },
                      "type": "user"
                    }
                  ],
                  "related_records": null,
                  "notify": false,
                  "apply_assignment_threshold": false,
                  "user_availability_based_on": null
                }
              },
              {
                "id": "3361265000006458562",
                "type": "email_notifications",
                "name": "EmailNotification"
              }
            ]
          },
          "scheduled_actions": [
            {
              "id": "3361265000006526070",
              "actions": [
                {
                  "type": "remove_tags",
                  "name": "criteria",
                  "details": {
                    "tags": [
                      {
                        "id": "3361265000001715141",
                        "name": "criteria",
                        "color_code": "#879BFC"
                      }
                    ],
                    "module": {
                      "api_name": "Contacts",
                      "id": "3361265000000000129"
                    }
                  }
                }
              ]
            }
          ],
          "id": "3361265000006492242",
          "sequence_number": 1
        }
      ],
      "id": "3361265000006492241"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — SuccessResponse

PUT- Success response for status 200

```json
{
  "workflow_rules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "3361265000006294001"
      },
      "message": "workflow updated",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidConditionId

Error response with code INVALID_DATA: This given conditionid seems to be invalid

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.workflow_rules[0].conditions[0].id"
      },
      "message": "This given conditionid seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse1

Error response with code DEPENDENT_FIELD_MISSING: Dependent Field missing (Field: details)

```json
{
  "workflow_rules": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[1].type"
        },
        "api_name": "id",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[1].id"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateActionNotAllowedResponse

Error response with code INVALID_DATA: Duplicate action not allowed

```json
{
  "workflow_rules": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "actions",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0]"
      },
      "message": "Duplicate action not allowed",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AlreadyUsedResponse

Error response with code ALREADY_USED: The condition is already used in the mentioned workflow

```json
{
  "workflow_rules": [
    {
      "code": "ALREADY_USED",
      "details": {
        "api_name": "criteria_details",
        "exists_in": {
          "api_name": "criteria_details",
          "json_path": "$.workflow_rules[0].conditions[0].criteria_details"
        },
        "json_path": "$.workflow_rules[0].conditions[1].criteria_details"
      },
      "message": "duplicate criteria details.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — CannotRemoveLastActionResponse

Error response with code CANNOT_REMOVE: cannot delete the last remaining action from a condition

```json
{
  "workflow_rules": [
    {
      "code": "CANNOT_REMOVE",
      "details": {},
      "message": "Actions cannot be empty",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NoUrlIdResponse

Error response with code INVALID_DATA: Workflow Rule Id is missing in the request body

```json
{
  "workflow_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "id",
        "json_path": "$.workflow_rules[0].id"
      },
      "message": "The workflow processid is mandatory",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidRuleIdResponse

Error response with code INVALID_DATA: the id given seems to be invalid

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.workflow_rules[0].id"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionResponse

Error response for status 403

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Workflow"
    ]
  },
  "message": "feature not available in this edition",
  "status": "error"
}
```
