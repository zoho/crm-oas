Successful Retrieval of a Blueprint State by ID

```json
{
  "states": [
    {
      "process_id": "111111000000113045",
      "state_escalation": {
        "period": "Days",
        "value": 1,
        "trigger_details": [
          {
            "period": "Days",
            "execute_type": "on",
            "id": "111111000000118021",
            "value": 0,
            "actions": [
              {
                "details": {
                  "escalate_to": [
                    {
                      "id": "111111000000057846",
                      "type": "user"
                    }
                  ]
                },
                "name": "SLA",
                "id": "111111000000118022",
                "type": "sla"
              }
            ]
          },
          {
            "period": "Hours",
            "execute_type": "on",
            "id": "111111000000118023",
            "value": 1,
            "actions": [
              {
                "details": {
                  "escalate_to": [
                    {
                      "id": "111111000000057846",
                      "type": "user"
                    }
                  ]
                },
                "name": "SLA",
                "id": "111111000000118024",
                "type": "sla"
              }
            ]
          },
          {
            "period": "Days",
            "execute_type": "on",
            "id": "111111000000118025",
            "value": 2,
            "actions": [
              {
                "details": {
                  "escalate_to": [
                    {
                      "id": "111111000000057846",
                      "type": "user"
                    }
                  ]
                },
                "name": "SLA",
                "id": "111111000000118026",
                "type": "sla"
              }
            ]
          }
        ]
      },
      "module": {
        "api_name": "Leads",
        "id": "111111000000002624"
      },
      "pick_list_value": {
        "actual_value": "Option 1",
        "id": "111111000000085001"
      }
    }
  ]
}
```
