Successful retrieval of a Blueprint transition by ID

```json
{
  "transitions": [
    {
      "id": "111112000000000856",
      "trigger_type": "manual",
      "transition_type": "standalone_transition",
      "process_id": "11111200000000876",
      "name": "Renamed Transition",
      "criteria": null,
      "color_code": "#F27E22",
      "owners": [
        {
          "type": "users",
          "resources": [
            {
              "id": "111111000000000039"
            }
          ]
        }
      ],
      "module": {
        "api_name": "Leads",
        "id": "111112000000000030"
      },
      "during_inputs": [
        {
          "id": "111112000000007172",
          "type": "field",
          "optional": false,
          "sequence_number": 4,
          "validation_filter": null,
          "module": "Deals",
          "field": {
            "api_name": "Subject",
            "id": "111111000000059420"
          }
        },
        {
          "id": "111112000000000091",
          "type": "checklist",
          "sequence_number": 4,
          "checklist_info": {
            "title": "checklist items",
            "items": [
              "checklist1",
              "checklist2"
            ]
          }
        }
      ],
      "actions": [
        {
          "type": "tasks",
          "name": "Reminder Task",
          "id": "111111000000059424",
          "details": null
        }
      ]
    }
  ]
}
```
