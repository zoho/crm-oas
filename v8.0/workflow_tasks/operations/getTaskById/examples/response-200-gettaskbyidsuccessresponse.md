Single task retrieved successfully

```json
{
  "tasks": [
    {
      "created_time": "2023-10-20T11:17:30+05:30",
      "lock_status": {
        "locked": false
      },
      "editable": true,
      "module": {
        "api_name": "Leads",
        "id": "111111000000002393"
      },
      "related_module": null,
      "deletable": true,
      "source": "user",
      "created_by": {
        "name": "vignesh B",
        "id": "111111000000051635"
      },
      "notify": false,
      "feature_type": "workflow",
      "field_mappings": [
        {
          "display_value": "efefdeff",
          "field": {
            "api_name": "Subject",
            "id": "111111000000000221"
          },
          "type": "static",
          "value": "efefdeff"
        },
        {
          "display_value": "From Date plus 1 day(s)",
          "field": {
            "api_name": "Due_Date",
            "id": "111111000000000223"
          },
          "type": "execution_time",
          "value": {
            "period": "days",
            "unit": "1",
            "trigger_field": "${CURRENTTIME}",
            "sign": "plus"
          }
        },
        {
          "display_value": "Not Started",
          "field": {
            "api_name": "Status",
            "id": "111111000000000229"
          },
          "type": "static",
          "value": "Not Started"
        },
        {
          "display_value": "High",
          "field": {
            "api_name": "Priority",
            "id": "111111000000000231"
          },
          "type": "static",
          "value": "High"
        }
      ],
      "modified_time": "2023-10-20T11:17:30+05:30",
      "associated": true,
      "modified_by": {
        "name": "vignesh B",
        "id": "111111000000051635"
      },
      "name": "efefdeff",
      "id": "111111000000190030"
    }
  ]
}
```
