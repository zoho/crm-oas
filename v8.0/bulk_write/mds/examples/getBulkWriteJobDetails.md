# Examples: getBulkWriteJobDetails

**GET /write/{jobId}**

## Response examples

### Status `200` — `application/json` — BulkWriteJobDetailsResponse

Completed bulk write job with one resource

```json
{
  "status": "COMPLETED",
  "character_encoding": "UTF-8",
  "resource": [
    {
      "status": "COMPLETED",
      "type": "data",
      "module": {
        "api_name": "Contacts",
        "id": "3524001000000002179"
      },
      "field_mappings": [
        {
          "api_name": "Last_Name",
          "index": 0
        }
      ],
      "file": {
        "status": "COMPLETED",
        "name": "data.csv",
        "added_count": 100,
        "skipped_count": 0,
        "updated_count": 0,
        "total_count": 100
      }
    }
  ],
  "id": "3524001000005697001",
  "result": {
    "download_url": "https://download.zohocrm.com/v2/bulk/write/3524001000005697001/result"
  },
  "created_by": {
    "name": "John Doe",
    "id": "3524001000000186003"
  },
  "operation": "insert",
  "created_time": "2023-01-01T12:00:00Z",
  "callback": {
    "url": "http://requestbin.fullcontact.com/1fcimk51",
    "method": "post"
  }
}
```
