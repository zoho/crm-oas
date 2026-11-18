### `application/json` — SamplePutRequest

Update Blueprint States With Escalation Details

```json
{
  "states": [
    {
      "id": "111111000000101033",
      "state_escalation": {
        "period": "days",
        "value": 10,
        "trigger_details": [
          {
            "period": "days",
            "execute_type": "on",
            "value": 14,
            "actions": [
              {
                "details": {
                  "escalate_to": [
                    {
                      "id": "111111000000057619",
                      "type": "user"
                    }
                  ],
                  "name": "SLA"
                },
                "name": "SLA",
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

Sample SLA Action With Role Recipient

```json
{
  "states": [
    {
      "id": "111111000000101033",
      "state_escalation": {
        "period": "days",
        "value": 10,
        "trigger_details": [
          {
            "period": "days",
            "execute_type": "on",
            "value": 14,
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
      "id": "111111000000101033",
      "state_escalation": {
        "period": "days",
        "value": 10,
        "trigger_details": [
          {
            "period": "days",
            "execute_type": "on",
            "value": 14,
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
