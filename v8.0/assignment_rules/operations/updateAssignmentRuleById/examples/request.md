### `application/json` — SamplePutRequest

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
          "api_name": "${CURRENTUSER}"
        }
      },
      "rule_entries": [
        {
          "id": "526435000000001111",
          "_delete": null
        },
        {
          "id": "526435000000001112",
          "criteria": null,
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
          ]
        },
        {
          "assign_to": {
            "type": "criteria",
            "criteria": {
              "field": {
                "api_name": "City"
              },
              "comparator": "equal",
              "value": "Chennai"
            }
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
