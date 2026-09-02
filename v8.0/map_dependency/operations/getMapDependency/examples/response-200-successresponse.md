Example of a successful response with field dependencies.

```json
{
  "map_dependency": [
    {
      "parent": {
        "api_name": "Lead_Source",
        "id": "1043386000000002609"
      },
      "internal": false,
      "sub_module": null,
      "active": true,
      "id": "1043386000020283001",
      "source": 1,
      "category": 0,
      "child": {
        "api_name": "Lead_Status",
        "id": "1043386000000002611"
      }
    },
    {
      "parent": {
        "api_name": "Pick_List_1",
        "id": "1043386000019791055"
      },
      "internal": false,
      "sub_module": {
        "api_name": "Subform_3",
        "id": "1043386000016645081"
      },
      "active": true,
      "id": "1043386000020283005",
      "source": 1,
      "category": 0,
      "child": {
        "api_name": "Pick_List_2",
        "id": "1043386000019791245"
      }
    }
  ],
  "info": {
    "per_page": 200,
    "count": 2,
    "page": 1,
    "more_records": false
  }
}
```
