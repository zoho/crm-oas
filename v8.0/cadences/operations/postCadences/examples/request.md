### `application/json` — SamplePostRequest

Sample create Cadence request body

```json
{
  "cadences": [
    {
      "name": "cadence",
      "description": "description",
      "module": {
        "api_name": "Leads",
        "id": "111112000000002628"
      },
      "type": "custom_view",
      "custom_view": {
        "id": "111112000000051112"
      },
      "execution_details": {
        "execute_every": {
          "period": "hours",
          "unit": 1
        },
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
            "reference_id": "{{Followup_1}}"
          },
          "reference_id": "{{Followup_2}}",
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
            "reference_id": "{{Followup_2}}"
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
