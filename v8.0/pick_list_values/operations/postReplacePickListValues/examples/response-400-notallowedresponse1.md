Error response with code NOT_ALLOWED: The picklist option is used in features (Field: id)

```json
{
  "replace_pick_list_values": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.replace_pick_list_values[0].old_value.id",
        "_associations": [
          {
            "resources": [
              {
                "name": "Lead Nurturing blueprint",
                "id": "1560451000004719301",
                "_details": null
              }
            ],
            "type": "blueprint"
          },
          {
            "resources": [
              {
                "name": "CadenceTest1",
                "id": "1560451000004719986",
                "_details": null
              }
            ],
            "type": "cadences"
          }
        ]
      },
      "message": "The picklist option is used in features",
      "status": "error"
    }
  ]
}
```
