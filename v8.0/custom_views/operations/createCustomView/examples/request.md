### `application/json` — PostRequestBody

Create Custom View request body

```json
{
  "custom_views": [
    {
      "name": "crossfilter1",
      "access_type": "shared",
      "shared_to": [
        {
          "name": "Jess Moana",
          "id": "2411194000000478001",
          "type": "users",
          "subordinates": null
        }
      ],
      "wrap_text": true,
      "sort_by": {
        "api_name": "Created_Time",
        "id": "2411194000000000129"
      },
      "sort_order": "desc",
      "locked": false,
      "fields": [
        {
          "api_name": "First_Name",
          "id": "2411194000000000557",
          "_pin": false
        },
        {
          "api_name": "Last_Name",
          "id": "2411194000000000559",
          "_pin": false
        },
        {
          "api_name": "Company",
          "id": "2411194000000000555",
          "_pin": false
        },
        {
          "api_name": "Email",
          "id": "2411194000000000563",
          "_pin": false
        }
      ],
      "criteria": {
        "field": {
          "id": "2411194000000000605",
          "api_name": "City"
        },
        "comparator": "contains",
        "value": "e",
        "type": "value"
      },
      "cross_filters": [
        {
          "include_objects": true,
          "relation": {
            "id": "2411194000000282522",
            "api_name": "Notes__r"
          },
          "criteria": {
            "group": [
              {
                "field": {
                  "id": "2411194000000000285",
                  "api_name": "Created_By"
                },
                "comparator": "equal",
                "value": {
                  "id": "2411194000000478001",
                  "name": "Jess Moana"
                },
                "type": "value"
              },
              {
                "comparator": "equal",
                "field": {
                  "api_name": "Parent_Id",
                  "id": "2411194000000000283"
                },
                "value": "${NOTEMPTY}"
              }
            ],
            "group_operator": "and"
          }
        }
      ]
    }
  ]
}
```
