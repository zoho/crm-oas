Action state — open_link type with sequential processing disabled

```json
{
  "states": [
    {
      "associated_fields": null,
      "configured_properties": null,
      "from_transition": {
        "name": "Default",
        "id": "4676645000000888434"
      },
      "name": "Action 12",
      "details": {
        "sequential_action": false,
        "sequential_action_details": {
          "enable_failure_path": false
        },
        "open_link": {
          "encode": "UTF-8",
          "name": "Action 12",
          "link": "https://youtube.com"
        },
        "type": "open_link"
      },
      "id": "4676645000000888527",
      "type": "action",
      "transitions": [
        {
          "name": "Action 12",
          "id": "4676645000000888528"
        }
      ]
    }
  ]
}
```
