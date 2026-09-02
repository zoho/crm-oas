Successful get Scoring Rule by ID response

```json
{
  "scoring_rules": [
    {
      "created_time": "2025-11-19T19:56:51+05:30",
      "has_signal_rules": false,
      "custom_fields": [
        {
          "api_name": "Lead_Scoring_Score",
          "id": "111114000000314018"
        },
        {
          "api_name": "Lead_Scoring_Touch_point_Score",
          "id": "111114000000314035"
        }
      ],
      "module": {
        "api_name": "Leads",
        "id": "111114000000002628"
      },
      "active": false,
      "description": null,
      "created_by": {
        "name": "Vignesh SR",
        "id": "111114000000057344",
        "zuid": "43249796"
      },
      "layout": {
        "display_label": "Standard",
        "api_name": "Standard",
        "id": "111114000000003626"
      },
      "modified_time": "2025-11-21T11:26:40+05:30",
      "field_rules": [
        {
          "score": 10,
          "criteria": {
            "group_operator": "AND",
            "group": [
              {
                "comparator": "equal",
                "field": {
                  "api_name": "CF_Date",
                  "id": "111114000000081970"
                },
                "type": "value",
                "value": "2025-11-19"
              },
              {
                "comparator": "equal",
                "field": {
                  "api_name": "Company",
                  "id": "111114000000004780"
                },
                "type": "value",
                "value": "Zohho"
              }
            ]
          },
          "id": "111114000000314010"
        },
        {
          "score": -10,
          "criteria": {
            "comparator": "not_equal",
            "field": {
              "api_name": "Country",
              "id": "111114000000004892"
            },
            "type": "value",
            "value": "${EMPTY}"
          },
          "id": "111114000000314012"
        }
      ],
      "name": "Lead - Scoring",
      "modified_by": {
        "name": "Vignesh SR",
        "id": "111114000000057344",
        "zuid": "43249796"
      },
      "id": "111114000000314009",
      "signal_rules": [
        {
          "score": -100,
          "id": "111114000000316001",
          "signal": {
            "namespace": "zoho.emailinsight.bounce",
            "id": "111114000000034755"
          }
        },
        {
          "score": 10,
          "id": "111114000000316002",
          "signal": {
            "namespace": "zoho.emailinsight.open",
            "id": "111114000000034749"
          }
        }
      ]
    }
  ]
}
```
