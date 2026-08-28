# Examples: getWorkflowRuleUsage

**GET /settings/automation/workflow_rules/{workflowRuleId}/actions/usage**

## Response examples

### Status `200` — `application/json` — Success200

Successful retrieval of workflow rule action usage metrics

```json
{
  "workflow_rules": [
    {
      "trigger_count": 3,
      "name": "High Value Lead Rule",
      "id": "4876876000013248001",
      "conditions": [
        {
          "instant_actions": {
            "actions": [
              {
                "queue_count": 0,
                "related_details": {
                  "bulk_mail": false,
                  "unopened": 0,
                  "sent_percentage": 100,
                  "opened": 1,
                  "delivered": 1,
                  "unsent": 0,
                  "bounced": 0,
                  "clicked": 0,
                  "sent": 1
                },
                "name": "High revenue Lead added",
                "success_count": 1,
                "failure_count": 0,
                "id": "4876876000016390103",
                "type": "email_notifications",
                "associated_time": "2025-10-16T16:19:58+05:30"
              },
              {
                "name": "To users : Patricia Boyle",
                "success_count": 2,
                "failure_count": 0,
                "id": "4876876000013248016",
                "type": "assign_owner",
                "associated_time": "2025-08-08T22:40:00+05:30"
              }
            ]
          },
          "scheduled_actions": [
            {
              "id": "4876876000016390118",
              "actions": [
                {
                  "queue_count": 0,
                  "related_details": {
                    "bulk_mail": false,
                    "unopened": 0,
                    "sent_percentage": 100,
                    "opened": 1,
                    "delivered": 1,
                    "unsent": 0,
                    "bounced": 0,
                    "clicked": 0,
                    "sent": 1
                  },
                  "name": "High revenue Lead added",
                  "success_count": 1,
                  "failure_count": 0,
                  "id": "4876876000016390103",
                  "type": "email_notifications",
                  "associated_time": "2025-10-16T16:19:58+05:30"
                }
              ]
            }
          ],
          "usage_count": 2,
          "id": "4876876000013248002"
        },
        {
          "instant_actions": {
            "actions": [
              {
                "name": "P1",
                "success_count": 0,
                "tag_id": "4876876000011037076",
                "failure_count": 0,
                "id": "4876876000013248015",
                "type": "add_tags",
                "associated_time": "2025-08-08T22:40:00+05:30"
              }
            ]
          },
          "scheduled_actions": [],
          "usage_count": 0,
          "id": "4876876000013248004"
        }
      ],
      "reset_time": "2025-10-16T16:23:04+05:30"
    }
  ]
}
```

### Status `400` — `application/json` — RequiredParamMissingResponse

Required query parameter missing from the request

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "executed_from"
  },
  "message": "required param not found",
  "status": "error"
}
```

### Status `400` — `application/json` — DateRangeExceedsResponse

400 error when the queried date range exceeds the allowed limit

```json
{
  "code": "INVALID_REQUEST",
  "details": {},
  "message": "DATE_RANGE_EXCEEDS",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataTypeResponse

400 error when a date or time parameter is not in ISO 8601 format

```json
{
  "code": "INVALID_DATA",
  "details": {
    "expected_data_type": "datetime",
    "param_name": "executed_from"
  },
  "message": "Please provide  ISO Time format to the param",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidRequestMethodResponse

Invalid HTTP request method used for this endpoint

```json
{
  "code": "INVALID_REQUEST_METHOD",
  "details": {},
  "message": "The http request method type is not a valid one",
  "status": "error"
}
```

### Status `401` — `application/json` — AuthenticationFailureResponse

Authentication failed for the request

```json
{
  "code": "AUTHENTICATION_FAILURE",
  "details": {},
  "message": "Authentication failed",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse

Workflow rules feature not available in the current Zoho CRM edition

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
