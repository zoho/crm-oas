### `application/json` — Default

An example of create shift hour request.

```json
{
  "shift_hours": [
    {
      "name": "New Shift",
      "timezone": "Asia/Kolkata",
      "same_as_everyday": true,
      "daily_timing": [
        "09:00",
        "18:00"
      ],
      "shift_days": [
        "Monday",
        "Tuesday"
      ],
      "users": [],
      "break_hours": [],
      "holidays": []
    }
  ]
}
```
