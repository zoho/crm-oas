### `application/json` — CreateDependency

Example of creating a field dependency.

```json
{
  "map_dependency": [
    {
      "parent": {
        "api_name": "Lead_Source",
        "id": "111111000000004107"
      },
      "pick_list_values": [
        {
          "display_value": "-None-",
          "maps": [
            {
              "display_value": "Contacted",
              "actual_value": "Contacted",
              "id": "111111000000016330"
            },
            {
              "display_value": "Contact in Future",
              "actual_value": "Contact in Future",
              "id": "111111000000016333"
            }
          ],
          "actual_value": "-None-",
          "id": "111111000000016273"
        },
        {
          "display_value": "Advertisement",
          "maps": [
            {
              "display_value": "Pre-Qualified",
              "actual_value": "Pre-Qualified",
              "id": "111111000000016327"
            },
            {
              "display_value": "Not Qualified",
              "actual_value": "Not Qualified",
              "id": "111111000000016351"
            }
          ],
          "actual_value": "Advertisement",
          "id": "111111000000016276"
        }
      ],
      "child": {
        "api_name": "Lead_Status",
        "id": "111111000000004109"
      }
    }
  ]
}
```
