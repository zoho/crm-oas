An example of two records updated successfully and one record failing.

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2026-08-12T19:02:29+05:30",
        "Modified_By": {
          "name": "Dharun Kumar Dharun Kumar 95",
          "id": "1990117000000450001"
        },
        "Created_Time": "2026-08-04T17:55:37+05:30",
        "id": "1990117000045575047",
        "Created_By": {
          "name": "Dharun Kumar Dharun Kumar 95",
          "id": "1990117000000450001"
        }
      },
      "message": "record updated",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2026-08-12T19:02:29+05:30",
        "Modified_By": {
          "name": "Dharun Kumar Dharun Kumar 95",
          "id": "1990117000000450001"
        },
        "Created_Time": "2026-08-04T17:55:54+05:30",
        "id": "1990117000045575059",
        "Created_By": {
          "name": "Dharun Kumar Dharun Kumar 95",
          "id": "1990117000000450001"
        }
      },
      "message": "record updated",
      "status": "success"
    },
    {
      "code": "RECORD_LOCKED",
      "details": {
        "action": "record_locking",
        "id": "1990117000045639003"
      },
      "message": "Sorry, you cannot perform this operation as the record is locked.",
      "status": "error"
    }
  ]
}
```
