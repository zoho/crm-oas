Screen state — data-hub element with one primary button and right-to-left alignment

```json
{
  "states": [
    {
      "associated_fields": [
        {
          "api_name": "Query_1",
          "id": "4676645000000885198"
        }
      ],
      "configured_properties": null,
      "from_transition": {
        "name": "Done",
        "id": "4676645000000888001"
      },
      "name": "Screen 1011",
      "details": {
        "screen_details": {
          "buttons": [
            {
              "prop_name": "primary",
              "name": "Done",
              "id": "4676645000000887109"
            }
          ],
          "elements": [
            {
              "data_hub": {
                "selection_details": {
                  "selection_type": null,
                  "result_type": "single",
                  "limit": 1,
                  "range": null
                },
                "module": {
                  "api_name": "DataHub1",
                  "id": "4676645000000883025"
                },
                "name": "Query 1",
                "id": "4676645000000885198",
                "selected_fields": [
                  {
                    "api_name": "First_Name",
                    "id": "4676645000000885151"
                  },
                  {
                    "api_name": "Company",
                    "id": "4676645000000885166"
                  },
                  {
                    "api_name": "Last_Name",
                    "id": "4676645000000885181"
                  }
                ]
              },
              "type": "data_hubs",
              "value": null
            }
          ],
          "width": "670px",
          "title": "Screen 10",
          "button_align": "right_to_left"
        }
      },
      "id": "4676645000000887111",
      "type": "screen",
      "transitions": [
        {
          "name": "Done",
          "id": "4676645000000887109"
        }
      ]
    }
  ]
}
```
