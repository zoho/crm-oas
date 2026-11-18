### `application/json` — SamplePutRequest

Sample request to update a Blueprint transition

```json
{
  "blueprint": [
    {
      "transition_id": "4554588000001189006",
      "data": {
        "CheckLists": [
          {
            "questionone": true
          },
          {
            "questiontwo": false
          }
        ],
        "Subform_1": [
          {
            "Name": "Row 1",
            "Amount": 100
          },
          {
            "Name": "Row 2",
            "Amount": 200
          }
        ]
      },
      "state": "draft"
    }
  ]
}
```

### `application/json` — SamplePutRequestWithAssociatedModule

Request with a tag, an associated module subform, and a link attachment

```json
{
  "blueprint": [
    {
      "transition_id": "4554588000001189006",
      "data": {
        "Tag": [
          {
            "name": "Important",
            "id": "4554588000000123001",
            "color_code": "#FFB300"
          }
        ],
        "Sales_Order": {
          "Subject": "Test",
          "Ordered_Items": [
            {
              "Product_Name": "Item A",
              "Quantity": 2,
              "List_Price": 150
            }
          ]
        }
      },
      "state": "completed"
    }
  ]
}
```
