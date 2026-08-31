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
