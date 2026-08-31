### `application/json` — SamplePutRequest

Sample request body

```json
{
  "assignment_rules": [
    {
      "rule_entries": [
        {
          "id": "526435000000001111",
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
