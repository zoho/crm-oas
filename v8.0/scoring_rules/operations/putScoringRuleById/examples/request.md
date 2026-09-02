### `application/json` — SamplePutRequest

Sample update Scoring Rule by ID request body

```json
{
  "scoring_rules": [
    {
      "id": "111114000000072349",
      "name": "Altered scoring",
      "field_rules": [
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
        },
        {
          "id": "111114000000004892",
          "score": 45
        }
      ],
      "signal_rules": [
        {
          "id": "111114000000012345",
          "_delete": null
        },
        {
          "score": -100,
          "signal": {
            "namespace": "zoho.emailinsight.bounce",
            "id": "111114000000034755"
          }
        }
      ],
      "custom_fields": [
        {
          "field_label": "Contact Total Score",
          "reference_field": {
            "api_name": "Score"
          }
        },
        {
          "id": "111114000000012345",
          "field_label": "Total score"
        }
      ]
    }
  ]
}
```
