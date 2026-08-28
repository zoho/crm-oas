# Examples: getWorkflowRulesActionsCount

**GET /settings/automation/workflow_rules/actions/actions_count**

## Response examples

### Status `200` — `application/json` — GetActionsCount

Success response for status 200

```json
{
  "workflow_rules": [
    {
      "id": "3361265000006526160",
      "conditions": [
        {
          "sequence_number": 1,
          "instant_actions": {
            "actions_count": [
              {
                "type": "field_updates",
                "value": 1
              },
              {
                "type": "assign_owner",
                "value": 1
              },
              {
                "type": "add_tags",
                "value": 1
              },
              {
                "type": "create_record",
                "value": 1
              },
              {
                "type": "webhooks",
                "value": 1
              }
            ]
          },
          "scheduled_actions": [
            {
              "actions_count": [
                {
                  "type": "remove_tags",
                  "value": 1
                },
                {
                  "type": "email_notifications",
                  "value": 1
                },
                {
                  "type": "functions",
                  "value": 1
                }
              ]
            }
          ],
          "id": "3361265000006526161"
        }
      ]
    },
    {
      "id": "3361265000006526223",
      "conditions": [
        {
          "sequence_number": 1,
          "instant_actions": {
            "actions_count": [
              {
                "type": "convert",
                "value": 1
              }
            ]
          },
          "scheduled_actions": null,
          "id": "3361265000006526224"
        }
      ]
    }
  ]
}
```

### Status `400` — `application/json` — RequiredParamMissingResponse1

Error response with code REQUIRED_PARAM_MISSING: One of the expected parameter is missing

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "ids"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
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
