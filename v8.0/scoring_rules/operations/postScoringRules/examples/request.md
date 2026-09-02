### `application/json` — SamplePostRequest

Sample create Scoring Rules request body

```json
{
  "scoring_rules": [
    {
      "description": "",
      "active": true,
      "custom_fields": [
        {
          "field_label": "Lead - Scoring Score",
          "reference_field": {
            "api_name": "Score"
          }
        },
        {
          "field_label": "Lead - Scoring Touch point Score",
          "reference_field": {
            "api_name": "Touch_Point_Score"
          }
        }
      ],
      "field_rules": [
        {
          "criteria": {
            "group_operator": "and",
            "group": [
              {
                "field": {
                  "api_name": "CF_Date",
                  "id": "111114000000081970",
                  "field_label": "CF Date",
                  "data_type": "date"
                },
                "comparator": "equal",
                "value": "2025-11-19",
                "type": "value"
              },
              {
                "field": {
                  "api_name": "Company",
                  "id": "111114000000004780",
                  "field_label": "Company",
                  "data_type": "text"
                },
                "comparator": "equal",
                "value": "Zohho",
                "type": "value"
              }
            ]
          },
          "score": 10
        },
        {
          "criteria": {
            "field": {
              "api_name": "Country",
              "id": "111114000000004892",
              "field_label": "Country",
              "data_type": "text"
            },
            "comparator": "not_equal",
            "value": "${EMPTY}",
            "type": "value"
          },
          "score": -10
        }
      ],
      "signal_rules": [
        {
          "signal": {
            "namespace": "zoho.emailinsight.bounce",
            "id": "111114000000034755"
          },
          "score": -99
        },
        {
          "signal": {
            "namespace": "zoho.emailinsight.open",
            "id": "111114000000034749"
          },
          "score": 10
        },
        {
          "signal": {
            "namespace": "zoho.emailinsight.click",
            "id": "111114000000034752"
          },
          "score": 100
        }
      ],
      "layout": {
        "id": "111114000000003626",
        "api_name": "Standard",
        "display_label": "Standard"
      },
      "module": {
        "api_name": "Leads",
        "id": "111114000000002628"
      },
      "name": "Lead - Scoring"
    }
  ]
}
```
