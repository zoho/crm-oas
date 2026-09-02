### `application/json` — CustomHours

Custom Business Hours

```json
{
  "business_hours": {
    "week_starts_on": "Monday",
    "type": "custom",
    "business_days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday"
    ],
    "same_as_everyday": false,
    "daily_timing": [
      "09:00",
      "18:00"
    ],
    "custom_timing": [
      {
        "days": "Monday",
        "business_timing": [
          "09:00",
          "18:00"
        ]
      }
    ]
  }
}
```
