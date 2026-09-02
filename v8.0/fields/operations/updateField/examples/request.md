### `application/json` — FullExample

Bulk update of multiple field configurations

```json
{
  "fields": [
    {
      "history_tracking_enabled": true,
      "history_tracking": {
        "related_list_name": "Region Tracker",
        "duration_configuration": "time",
        "followed_fields": [
          {
            "api_name": "Owner",
            "_delete": null
          },
          {
            "api_name": "Company",
            "id": "5725767000000002591"
          }
        ]
      }
    },
    {
      "id": "2276164000002053013",
      "pick_list_values": [
        {
          "id": "2276164000002053012",
          "_global_picklist_value": {
            "id": "2276164000002053039"
          }
        },
        {
          "id": "2276164000002053014",
          "_global_picklist_value": {
            "id": "2276164000002053041"
          }
        }
      ],
      "global_picklist": {
        "api_name": "Market",
        "id": "2276164000002053035"
      }
    },
    {
      "id": "2276164000002053013",
      "field_label": "Updated Field Label",
      "length": 255,
      "association_details": {
        "related_field": {
          "id": "4832675000000710341",
          "api_name": "City"
        },
        "lookup_field": {
          "id": "4832675000000710334",
          "api_name": "Lookup_Field"
        }
      }
    }
  ]
}
```
