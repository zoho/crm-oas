Success response containing get records with different criteria types

```json
{
  "get_records": [
    {
      "selection_details": {
        "selection_type": null,
        "result_type": "single",
        "limit": 1,
        "range": 1
      },
      "criteria": {
        "comparator": "not_equal",
        "field": {
          "api_name": "Annual_Revenue",
          "id": "4676645000000000581"
        },
        "type": "value",
        "value": "${EMPTY}"
      },
      "module": {
        "api_name": "Leads",
        "id": "4676645000000000125"
      },
      "name": "GetRecords 4",
      "id": "4676645000000914086",
      "type": "parent",
      "selected_fields": null,
      "sort_order": {
        "order_by_name": "descending",
        "order_by_field": {
          "api_name": "Modified_Time",
          "id": "4676645000000000595"
        }
      }
    },
    {
      "selection_details": {
        "selection_type": "mandate",
        "result_type": "multiple",
        "limit": 10,
        "range": 100
      },
      "criteria": {
        "group_operator": "AND",
        "group": [
          {
            "comparator": "equal",
            "field": {
              "api_name": "Annual_Revenue",
              "id": "4676645000000000581"
            },
            "type": "value",
            "value": "250"
          },
          {
            "comparator": "not_equal",
            "field": {
              "api_name": "City",
              "id": "4676645000000000605"
            },
            "type": "value",
            "value": "${EMPTY}"
          }
        ]
      },
      "module": {
        "api_name": "Leads",
        "id": "4676645000000000125"
      },
      "name": "GetRecords 3",
      "id": "4676645000000901064",
      "type": "parent",
      "selected_fields": null,
      "sort_order": {
        "order_by_name": "descending",
        "order_by_field": {
          "api_name": "Modified_Time",
          "id": "4676645000000000595"
        }
      }
    }
  ]
}
```
