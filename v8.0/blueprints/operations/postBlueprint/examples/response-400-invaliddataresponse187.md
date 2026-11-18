Error response with code INVALID_DATA: Invalid data (Field: type)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "field",
          "related_list",
          "info",
          "attachment",
          "tags",
          "notes",
          "checklist",
          "widget",
          "kiosk"
        ],
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].type"
      },
      "status": "error"
    }
  ]
}
```
