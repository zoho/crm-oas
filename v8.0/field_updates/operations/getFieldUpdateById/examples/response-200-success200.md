Success response for status 200

```json
{
  "field_updates": [
    {
      "created_time": "2025-11-19T03:12:20-08:00",
      "update_type": "append",
      "lock_status": {
        "locked": false
      },
      "apply_assignment_threshold": false,
      "editable": true,
      "module": {
        "singular_label": "Deal",
        "plural_label": "Deals WF",
        "api_name": "Deals",
        "moduleName": "Potentials",
        "id": "3361265000000000131"
      },
      "related_module": null,
      "deletable": true,
      "source": "crm",
      "type": "static",
      "created_by": {
        "name": "B Indumathi",
        "id": "3361265000000535001"
      },
      "notify": false,
      "feature_type": "workflow",
      "modified_time": "2025-11-19T03:12:20-08:00",
      "field": {
        "ui_type": 2,
        "api_name": "Pipeline",
        "id": "3361265000000236001"
      },
      "dependent_fields": [
        {
          "field": {
            "ui_type": 26,
            "api_name": "Stage",
            "id": "3361265000000000525"
          },
          "value": "Qualification"
        }
      ],
      "associated": false,
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
      "name": "FieldUpdateGET",
      "modified_by": {
        "name": "B Indumathi",
        "id": "3361265000000535001"
      },
      "id": "3361265000006103364",
      "value": "Test"
    }
  ]
}
```
