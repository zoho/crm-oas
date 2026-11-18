### `application/json` — SamplePutRequest

Sample request body for updating a single Blueprint via PUT /settings/blueprints/{blueprintId}

```json
{
  "blueprints": [
    {
      "id": "123456789012345678",
      "owners": [
        {
          "resources": [
            {
              "id": "1231231231"
            }
          ],
          "type": "users"
        }
      ],
      "criteria": {
        "comparator": "greater_than",
        "field": {
          "api_name": "Annual_Revenue",
          "id": "111111000000004782"
        },
        "type": "value",
        "value": "100"
      },
      "chart_data": {
        "nodes": [
          {
            "position_x": 330,
            "position_y": 340,
            "state": {
              "api_name": "State_1"
            }
          },
          {
            "position_x": 880,
            "position_y": 320,
            "state": {
              "api_name": "State_2"
            }
          }
        ],
        "connections": [
          {
            "from": {
              "end_point": {
                "position_x": 0.5,
                "position_y": 1,
                "direction_x": 0,
                "direction_y": 1
              },
              "state": {
                "api_name": "State_1"
              }
            },
            "api_name": "Transition_1",
            "to": {
              "end_point": {
                "position_x": 0,
                "position_y": 0.5,
                "direction_x": 0,
                "direction_y": 0
              },
              "state": {
                "api_name": "State_2"
              }
            },
            "transition": {
              "api_name": "Transition_1",
              "name": "Transition 1"
            }
          }
        ]
      },
      "continuous": false,
      "name": "Lead Bp 1",
      "description": "Test description",
      "connections": [
        {
          "id": "32123123123123",
          "_delete": null,
          "to_state": {
            "name": "Contacted",
            "api_name": "State_2"
          },
          "api_name": "Transition_1",
          "transitions": {
            "api_name": "Transition_1",
            "name": "Transition 1",
            "precedence": 1
          },
          "from_state": {
            "name": "-None-",
            "api_name": "State_1"
          }
        }
      ]
    }
  ]
}
```
