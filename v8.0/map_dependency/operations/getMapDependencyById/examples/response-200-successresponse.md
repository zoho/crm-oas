Example of single field dependency with picklist mappings.

```json
{
  "map_dependency": [
    {
      "parent": {
        "api_name": "Lead_Source",
        "id": "1043386000000002609"
      },
      "internal": false,
      "active": true,
      "id": "1043386000020283001",
      "source": 1,
      "category": 0,
      "pick_list_values": [
        {
          "display_value": "-None-",
          "maps": [
            {
              "display_value": "Contacted",
              "actual_value": "Contacted",
              "id": "1043386000000016330"
            },
            {
              "display_value": "Contact in Future",
              "actual_value": "Contact in Future",
              "id": "1043386000000016333"
            }
          ],
          "actual_value": "-None-",
          "id": "1043386000000016273"
        }
      ],
      "child": {
        "api_name": "Lead_Status",
        "id": "1043386000000002611"
      }
    }
  ]
}
```
