Related list of type multiselectlookup with full config

```json
{
  "related_lists": [
    {
      "id": "4150868000000091080",
      "sequence_number": "5",
      "display_label": "Products",
      "api_name": "Products",
      "module": {
        "api_name": "Products",
        "id": "4150868000000002200",
        "plural_label": "Products"
      },
      "name": "Products",
      "action": null,
      "href": null,
      "type": "multiselectlookup",
      "connectedlookupApiName": "Product_Name",
      "customize_sort": true,
      "customize_fields": true,
      "customize_display_label": true,
      "status": "visible",
      "connectedmodule": "Products",
      "linkingmodule": "Deals_X_Products",
      "parent_related_lists": null,
      "multiselectlookup": {
        "field": {
          "api_name": "Product_Name",
          "field_label": "Product Name",
          "id": "4150868000000002300"
        },
        "linking_details": {
          "visibility": 1,
          "module": {
            "plural_label": "Deals_X_Products",
            "api_name": "Deals_X_Products",
            "id": "4150868000000002400"
          },
          "lookup_field": {
            "api_name": "Deal_Name",
            "id": "4150868000000002500"
          },
          "connected_lookup_field": {
            "api_name": "Product_Name",
            "id": "4150868000000002600"
          }
        },
        "connected_details": {
          "field": {
            "api_name": "Deal_Name",
            "field_label": "Deal Name",
            "id": "4150868000000002700"
          },
          "module": {
            "plural_label": "Deals",
            "api_name": "Deals",
            "id": "4150868000000002800"
          },
          "related_list": {
            "display_label": "Deals",
            "api_name": "Deals",
            "id": "4150868000000002900"
          }
        },
        "field_enabled": true
      }
    }
  ]
}
```
