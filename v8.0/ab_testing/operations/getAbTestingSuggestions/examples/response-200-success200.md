Split suggestion for an AB test with an underperforming variant

```json
{
  "AB_testing_suggestions": [
    {
      "suggestion_details": {
        "variant_form": [
          {
            "underperforming_variant": true,
            "name": "variant1",
            "id": "111111000000093204",
            "no_of_submission": 5,
            "conversion_rate": 10,
            "no_of_visits": 23,
            "traffic": 20
          },
          {
            "underperforming_variant": false,
            "name": "variant2",
            "id": "111111000000093205",
            "no_of_submission": 5,
            "conversion_rate": 5,
            "no_of_visits": 23,
            "traffic": 30
          }
        ],
        "base_form": {
          "underperforming_variant": false,
          "id": "111111000000093194",
          "no_of_submission": 5,
          "no_of_visits": 23,
          "traffic": 50
        }
      },
      "type": "split_suggestion"
    }
  ]
}
```
