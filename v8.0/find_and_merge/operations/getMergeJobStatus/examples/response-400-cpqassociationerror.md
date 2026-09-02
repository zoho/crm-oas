Example of child record has CPQ rule associations. 

```json
{
  "merge": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "data": [
          {
            "_associated_places": [
              {
                "resources": [
                  {
                    "name": "asdfsdf",
                    "id": "111111000000071837"
                  }
                ],
                "type": "product_configurators"
              },
              {
                "resources": [
                  {
                    "name": "PR -sample",
                    "id": "111111000000072007"
                  }
                ],
                "type": "pricing_rules"
              }
            ],
            "id": "111111000000071814"
          }
        ],
        "api_name": "data",
        "json_path": "$.merge[0].data"
      },
      "message": "unable to merge records since there are association in child records",
      "status": "error"
    }
  ]
}
```
