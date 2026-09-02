Partial deletion where one record deleted, one failed with INVALID_DATA.


```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111115000000147279"
      },
      "message": "record deleted",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "23132423"
      },
      "message": "record not deleted",
      "status": "error"
    }
  ]
}
```
