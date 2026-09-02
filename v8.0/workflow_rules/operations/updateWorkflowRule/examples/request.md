### `application/json` — SamplePutRequest

Sample request body

```json
{
  "workflow_rules": [
    {
      "execute_when": {
        "type": "create_or_edit",
        "details": {
          "repeat": true,
          "trigger_module": {
            "api_name": "Contacts",
            "id": "3361265000000000129"
          }
        }
      },
      "conditions": [
        {
          "criteria_details": {
            "criteria": {
              "field": {
                "api_name": "Department",
                "id": "3361265000000000455"
              },
              "comparator": "equal",
              "value": "${EMPTY}"
            }
          },
          "instant_actions": {
            "actions": [
              {
                "id": "3361265000006492245",
                "name": "To users : user2 testUser, testUser1",
                "type": "assign_owner",
                "details": {
                  "module": {
                    "api_name": "Vendors"
                  },
                  "assign_to": [
                    {
                      "resource": {
                        "id": "3361265000002134004",
                        "name": "user2 testUser"
                      },
                      "type": "user"
                    },
                    {
                      "resource": {
                        "id": "3361265000002134024",
                        "name": "testUser1"
                      },
                      "type": "user"
                    }
                  ],
                  "related_records": null,
                  "notify": false,
                  "apply_assignment_threshold": false,
                  "user_availability_based_on": null
                }
              },
              {
                "id": "3361265000006458562",
                "type": "email_notifications",
                "name": "EmailNotification"
              }
            ]
          },
          "scheduled_actions": [
            {
              "id": "3361265000006526070",
              "actions": [
                {
                  "type": "remove_tags",
                  "name": "criteria",
                  "details": {
                    "tags": [
                      {
                        "id": "3361265000001715141",
                        "name": "criteria",
                        "color_code": "#879BFC"
                      }
                    ],
                    "module": {
                      "api_name": "Contacts",
                      "id": "3361265000000000129"
                    }
                  }
                }
              ]
            }
          ],
          "id": "3361265000006492242",
          "sequence_number": 1
        }
      ],
      "id": "3361265000006492241"
    }
  ]
}
```
