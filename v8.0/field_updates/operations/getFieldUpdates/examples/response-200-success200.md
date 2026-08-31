Success response for status 200

```json
{
  "field_updates": [
    {
      "created_time": "2025-11-20T22:34:38-08:00",
      "update_type": "append",
      "lock_status": {
        "locked": false
      },
      "apply_assignment_threshold": false,
      "editable": true,
      "module": {
        "api_name": "Deals",
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
      "modified_time": "2025-11-20T22:34:38-08:00",
      "field": {
        "api_name": "Layout",
        "id": "3361265000000098017"
      },
      "associated": false,
      "related_records": null,
      "name": "LayoutPipeline",
      "modified_by": {
        "name": "B Indumathi",
        "id": "3361265000000535001"
      },
      "id": "3361265000006176255",
      "value": {
        "display_label": "TestLayout",
        "name": "TestLayout",
        "id": "3361265000001347001"
      }
    },
    {
      "created_time": "2025-11-20T22:34:08-08:00",
      "update_type": "overwrite",
      "lock_status": {
        "locked": false
      },
      "apply_assignment_threshold": false,
      "editable": true,
      "module": {
        "api_name": "Deals",
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
      "modified_time": "2025-11-20T22:34:08-08:00",
      "field": {
        "api_name": "Pipeline",
        "id": "3361265000000236001"
      },
      "associated": false,
      "related_records": null,
      "name": "DependentField",
      "modified_by": {
        "name": "B Indumathi",
        "id": "3361265000000535001"
      },
      "id": "3361265000006176251",
      "value": "Test"
    },
    {
      "created_time": "2025-11-20T22:33:36-08:00",
      "update_type": "append",
      "lock_status": {
        "locked": false
      },
      "apply_assignment_threshold": true,
      "editable": true,
      "module": {
        "api_name": "Deals",
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
      "notify": true,
      "feature_type": "workflow",
      "modified_time": "2025-11-20T22:33:36-08:00",
      "field": {
        "api_name": "Owner",
        "id": "3361265000000000515"
      },
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
      "name": "OwnerField",
      "modified_by": {
        "name": "B Indumathi",
        "id": "3361265000000535001"
      },
      "id": "3361265000006176247",
      "value": {
        "name": "testUser user2",
        "id": "3361265000002134004"
      }
    },
    {
      "created_time": "2025-11-20T22:33:19-08:00",
      "update_type": "append",
      "lock_status": {
        "locked": false
      },
      "apply_assignment_threshold": false,
      "editable": true,
      "module": {
        "api_name": "Deals",
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
      "modified_time": "2025-11-20T22:33:19-08:00",
      "field": {
        "api_name": "Multi_Select_1",
        "id": "3361265000006103385"
      },
      "associated": false,
      "related_records": null,
      "name": "MultiSelect",
      "modified_by": {
        "name": "B Indumathi",
        "id": "3361265000000535001"
      },
      "id": "3361265000006176243",
      "value": [
        "Option 2"
      ]
    },
    {
      "created_time": "2025-11-20T22:32:58-08:00",
      "update_type": "overwrite",
      "lock_status": {
        "locked": false
      },
      "apply_assignment_threshold": false,
      "editable": true,
      "module": {
        "api_name": "Deals",
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
      "modified_time": "2025-11-20T22:32:58-08:00",
      "field": {
        "api_name": "Deal_Name",
        "id": "3361265000000000519"
      },
      "associated": false,
      "related_records": null,
      "name": "FUP_POST",
      "modified_by": {
        "name": "B Indumathi",
        "id": "3361265000000535001"
      },
      "id": "3361265000006176239",
      "value": "PostTest"
    }
  ],
  "info": {
    "per_page": 200,
    "count": 5,
    "page": 1,
    "more_records": false
  }
}
```
