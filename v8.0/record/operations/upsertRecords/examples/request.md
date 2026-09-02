### `application/json` — RequestBody

Sample request body for the upsertRecords operation

```json
{
  "data": [
    {
      "Last_Name": "test",
      "Email": "a@gmail.com",
      "Phone": "987654321",
      "id": "5725767000000524001"
    }
  ],
  "duplicate_check_fields": [
    "Phone"
  ]
}
```
