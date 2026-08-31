### `application/json` — LeadRecordOperations

Create and update Leads using chained sub-requests

```json
{
  "rollback_on_fail": false,
  "parallel_execution": false,
  "__composite_requests": [
    {
      "sub_request_id": "1",
      "method": "POST",
      "uri": "/crm/v3/Leads",
      "headers": {},
      "body": {
        "data": [
          {
            "Last_Name": "Boyle"
          }
        ]
      }
    },
    {
      "sub_request_id": "2",
      "method": "PUT",
      "uri": "/crm/v3/Leads/@{1:$.data[0].details.id}",
      "headers": {},
      "body": {
        "data": [
          {
            "Company": "Zylker"
          }
        ]
      }
    }
  ]
}
```
