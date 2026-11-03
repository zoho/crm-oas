Decision state — two paths with kiosk-field and get-record criteria groupings

```json
{
  "states": [
    {
      "associated_fields": [
        {
          "api_name": "GetRecords_3",
          "id": "4676645000000888388"
        }
      ],
      "configured_properties": [
        {
          "details": {
            "name": "${!ProcessFlow1.GetRecords_3}"
          },
          "type": "_merge_field"
        },
        {
          "details": {
            "name": "${!ProcessFlow1.Single_Line_1}"
          },
          "type": "_merge_field"
        }
      ],
      "from_transition": {
        "name": "Done",
        "id": "4676645000000887091"
      },
      "name": "Decision 3111",
      "details": {
        "path_details": [
          {
            "default": false,
            "name": "Path 1",
            "id": "4676645000000888503",
            "filter_conditions": {
              "criteria_groupings": [
                {
                  "sequence_number": 1,
                  "resource": null,
                  "criteria": {
                    "comparator": "not_equal",
                    "field": {
                      "api_name": "Single_Line_1",
                      "id": "4676645000000885268"
                    },
                    "type": "value",
                    "value": "${EMPTY}"
                  },
                  "type": "kiosk_fields",
                  "value": null
                },
                {
                  "sequence_number": 2,
                  "resource": {
                    "name": "GetRecords 3",
                    "id": "4676645000000888388"
                  },
                  "type": "get_record",
                  "value": "${NOTEMPTY}"
                }
              ],
              "pattern": "(1and2)"
            }
          },
          {
            "default": true,
            "name": "Default",
            "id": "4676645000000888505",
            "filter_conditions": null
          }
        ]
      },
      "id": "4676645000000888508",
      "type": "decision",
      "transitions": [
        {
          "name": "Path 1",
          "id": "4676645000000888503",
          "default": false
        },
        {
          "name": "Default",
          "id": "4676645000000888505",
          "default": true
        }
      ]
    }
  ]
}
```
