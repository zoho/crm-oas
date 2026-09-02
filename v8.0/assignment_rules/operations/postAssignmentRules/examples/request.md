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
