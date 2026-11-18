### `application/json` — SamplePutRequest

Update a Blueprint State With Escalation and Action Details

```json
{
  "states": [
    {
      "process_id": "111111000000084134",
      "state_escalation": {
        "period": "days",
        "value": 5,
        "trigger_details": [
          {
            "period": "days",
            "execute_type": "on",
            "value": 1,
            "actions": [
              {
                "details": {
                  "name": "Test",
                  "id": "111111000000092017"
                },
                "type": "email_notifications"
              },
              {
                "details": {
                  "name": "Task to re-attempt - ${Leads.Last Name}",
                  "id": "111111000000058728"
                },
                "type": "tasks"
              },
              {
                "details": {
                  "name": "Test City Update",
                  "details": {
                    "module": {
                      "api_name": "Leads",
                      "id": "111111000000002628"
                    }
                  },
                  "id": "111111000000081799"
                },
                "type": "field_updates"
              },
              {
                "details": {
                  "escalate_to": [
                    {
                      "id": "111111000000057662",
                      "type": "user"
                    }
                  ],
                  "name": "SLA"
                },
                "type": "sla"
              }
            ]
          }
        ]
      }
    }
  ]
}
```

### `application/json` — SampleSLARolePutRequest

Update Blueprint State SLA Escalation With Role Recipient

```json
{
  "states": [
    {
      "process_id": "111111000000084134",
      "state_escalation": {
        "period": "days",
        "value": 5,
        "trigger_details": [
          {
            "period": "days",
            "execute_type": "on",
            "value": 1,
            "actions": [
              {
                "details": {
                  "escalate_to": [
                    {
                      "id": "111111000000057620",
                      "type": "role"
                    }
                  ],
                  "name": "SLA Role"
                },
                "type": "sla"
              }
            ]
          }
        ]
      }
    }
  ]
}
```

### `application/json` — SampleSLAGroupPutRequest

Update Blueprint State SLA Escalation With Group Recipient

```json
{
  "states": [
    {
      "process_id": "111111000000084134",
      "state_escalation": {
        "period": "days",
        "value": 5,
        "trigger_details": [
          {
            "period": "days",
            "execute_type": "on",
            "value": 1,
            "actions": [
              {
                "details": {
                  "escalate_to": [
                    {
                      "id": "111111000000057621",
                      "type": "group"
                    }
                  ],
                  "name": "SLA Group"
                },
                "type": "sla"
              }
            ]
          }
        ]
      }
    }
  ]
}
```
