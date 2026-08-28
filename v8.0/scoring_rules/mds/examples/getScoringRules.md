# Examples: getScoringRules

**GET /settings/automation/scoring_rules**

## Response examples

### Status `200` — `application/json` — Success200

Successful list Scoring Rules response

```json
{
  "scoring_rules": [
    {
      "created_time": "2025-10-14T09:42:53+05:30",
      "has_signal_rules": false,
      "module": {
        "api_name": "Contacts",
        "id": "111114000000002630"
      },
      "active": true,
      "description": "",
      "created_by": {
        "name": "Vignesh SR",
        "id": "111114000000057344",
        "zuid": "43249796"
      },
      "layout": null,
      "modified_time": "2025-11-21T10:37:50+05:30",
      "field_rules": [
        {
          "score": 10,
          "criteria": {
            "comparator": "equal",
            "field": {
              "api_name": "Assistant",
              "id": "111114000000004570"
            },
            "type": "value",
            "value": "asst"
          },
          "id": "111114000000310446"
        },
        {
          "score": 1,
          "criteria": {
            "comparator": "contains",
            "field": {
              "api_name": "Assistant",
              "id": "111114000000004570"
            },
            "type": "value",
            "value": "awsst"
          },
          "id": "111114000000310448"
        }
      ],
      "name": "Contact scoring",
      "modified_by": {
        "name": "Vignesh SR",
        "id": "111114000000057344",
        "zuid": "43249796"
      },
      "id": "111114000000180006",
      "signal_rules": null
    },
    {
      "created_time": "2025-11-05T14:29:04+05:30",
      "has_signal_rules": false,
      "module": {
        "api_name": "Accounts",
        "id": "111114000000002632"
      },
      "active": true,
      "description": "",
      "created_by": {
        "name": "Vignesh SR",
        "id": "111114000000057344",
        "zuid": "43249796"
      },
      "layout": {
        "display_label": "Standard",
        "api_name": "Standard",
        "id": "111114000000003628"
      },
      "modified_time": null,
      "field_rules": [
        {
          "score": 10,
          "criteria": {
            "comparator": "contains",
            "field": {
              "api_name": "Account_Site",
              "id": "111114000000004480"
            },
            "type": "value",
            "value": "zoho"
          },
          "id": "111114000000265029"
        },
        {
          "score": 10,
          "criteria": {
            "comparator": "greater_equal",
            "field": {
              "api_name": "Annual_Revenue",
              "id": "111114000000004456"
            },
            "type": "value",
            "value": "100000"
          },
          "id": "111114000000265031"
        }
      ],
      "name": "ASR 1",
      "modified_by": null,
      "id": "111114000000265003",
      "signal_rules": null
    },
    {
      "created_time": "2025-11-18T10:44:53+05:30",
      "has_signal_rules": false,
      "module": {
        "api_name": "Accounts",
        "id": "111114000000002632"
      },
      "active": true,
      "description": "",
      "created_by": {
        "name": "Vignesh SR",
        "id": "111114000000057344",
        "zuid": "43249796"
      },
      "layout": {
        "display_label": "Standard",
        "api_name": "Standard",
        "id": "111114000000003628"
      },
      "modified_time": "2025-11-21T12:13:04+05:30",
      "field_rules": [
        {
          "score": 10,
          "criteria": {
            "comparator": "contains",
            "field": {
              "api_name": "Account_Site",
              "id": "111114000000004480"
            },
            "type": "value",
            "value": "zohho"
          },
          "id": "111114000000313070"
        }
      ],
      "name": "ASR",
      "modified_by": {
        "name": "Vignesh SR",
        "id": "111114000000057344",
        "zuid": "43249796"
      },
      "id": "111114000000313069",
      "signal_rules": null
    },
    {
      "created_time": "2025-11-18T14:05:11+05:30",
      "has_signal_rules": false,
      "module": {
        "api_name": "Leads",
        "id": "111114000000002628"
      },
      "active": false,
      "description": "",
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
      "modified_time": "2025-11-20T18:26:01+05:30",
      "field_rules": [
        {
          "score": 10,
          "criteria": {
            "comparator": "greater_than",
            "field": {
              "api_name": "Modified_Time",
              "id": "111114000000004830"
            },
            "type": "value",
            "value": "${DUEINDAYS}+12"
          },
          "id": "111114000000313123"
        }
      ],
      "name": "LSR",
      "modified_by": {
        "name": "Vignesh SR",
        "id": "111114000000057344",
        "zuid": "43249796"
      },
      "id": "111114000000313122",
      "signal_rules": null
    },
    {
      "created_time": "2025-11-19T19:56:51+05:30",
      "has_signal_rules": false,
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
  ],
  "info": {
    "per_page": 50,
    "count": 5,
    "page": 1,
    "more_records": false
  }
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response with code INVALID_DATA: Please check whether the input values are correct

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "module"
  },
  "message": "Please check whether the input values are correct",
  "status": "error"
}
```
