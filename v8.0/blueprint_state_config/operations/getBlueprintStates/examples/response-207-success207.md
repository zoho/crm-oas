Successful Retrieval of Blueprint States With Escalation Details

```json
{
  "states": [
    {
      "process_id": "111111000000205815",
      "state_escalation": {
        "period": "days",
        "value": 2,
        "trigger_details": [
          {
            "period": "days",
            "execute_type": "after",
            "id": "111111000000205823",
            "value": 2,
            "actions": [
              {
                "name": "Default SLA Alert",
                "details": {
                  "escalate_to": [
                    {
                      "id": "111111000000059900",
                      "type": "user"
                    }
                  ]
                },
                "id": "111111000000205827",
                "type": "sla"
              }
            ]
          }
        ]
      },
      "module": {
        "api_name": "Leads",
        "id": "111111000000002830"
      },
      "pick_list_value": {
        "actual_value": "-None-",
        "id": "111111000000007736"
      }
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "param_name": "ids",
        "id": "1234"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    }
  ]
}
```
