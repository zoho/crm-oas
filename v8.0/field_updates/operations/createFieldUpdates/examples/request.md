### `application/json` — SamplePostRequest

Sample request body

```json
{
  "field_updates": [
    {
      "name": "FieldUpdatePOST",
      "module": {
        "id": "3361265000000000131",
        "api_name": "Deals"
      },
      "field": {
        "id": "3361265000000236001",
        "api_name": "Pipeline"
      },
      "value": "Test",
      "dependent_fields": [
        {
          "field": {
            "api_name": "Stage",
            "id": "3361265000000000525"
          },
          "value": "Qualification"
        }
      ],
      "related_records": [
        {
          "api_name": "Events",
          "id": "3361265000000000145"
        },
        {
          "api_name": "Calls",
          "id": "3361265000000017015"
        }
      ],
      "notify": true,
      "feature_type": "workflow",
      "type": "static",
      "apply_assignment_threshold": true,
      "update_type": "append"
    }
  ]
}
```
