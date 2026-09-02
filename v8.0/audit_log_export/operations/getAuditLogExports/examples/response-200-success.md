Successful retrieval of audit log export jobs

```json
{
  "audit_log_export": [
    {
      "criteria": {
        "group_operator": "and",
        "group": [
          {
            "field": {
              "api_name": "module"
            },
            "comparator": "in",
            "value": [
              {
                "api_name": "Leads"
              },
              {
                "api_name": "Contacts"
              }
            ]
          },
          {
            "field": {
              "api_name": "action"
            },
            "comparator": "in",
            "value": [
              "added",
              "updated"
            ]
          }
        ]
      },
      "id": "1234567890",
      "status": "finished",
      "created_by": {
        "name": "John Doe",
        "id": "123456"
      },
      "download_links": [
        "https://example.com/download/1234567890"
      ],
      "job_start_time": "2023-01-01T00:00:00Z",
      "job_end_time": "2023-01-01T01:00:00Z",
      "expiry_date": "2023-01-08T00:00:00Z"
    }
  ]
}
```
