### `application/json` — CreateGlobalPicklistExample

Example request to create a global picklist

```json
{
  "global_picklists": [
    {
      "display_label": "Priority Level",
      "api_name": "priority_level__s",
      "description": "Priority levels for tasks and activities",
      "pick_list_values_sorted_lexically": false,
      "pick_list_values": [
        {
          "display_value": "High",
          "type": "used"
        },
        {
          "display_value": "Medium",
          "type": "used"
        },
        {
          "display_value": "Low",
          "type": "unused"
        }
      ]
    }
  ]
}
```
