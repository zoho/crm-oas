### `application/json` — SamplePutRequest

Update two services with mixed availability types and date range constraints.


```json
{
  "data": [
    {
      "Job_Sheet_Required": "No",
      "Owner": {
        "name": "Madeshwaran G",
        "id": "4671651000000635001",
        "email": "madeshwaran.g@zohocorp.com"
      },
      "Description": null,
      "Available_Days": [
        "Monday",
        "Tuesday",
        "Wednesday"
      ],
      "Tax": [],
      "Unavailable_From": "2026-01-13T15:40:03+05:30",
      "Record_Image": null,
      "id": "4671651000000862030",
      "Available_Dates": [],
      "Status": "Not in Use",
      "Available_Timings": null,
      "Service_Name": "service99",
      "Available_From": "2026-01-13",
      "Available_Till": "2026-01-13",
      "Duration": 30,
      "Job_Sheet_Section__s": null,
      "Price": 3993,
      "Tag": [],
      "Availability_Type": "Specific Day(s)",
      "Members": [
        {
          "id": "4671651000000862031",
          "Members": {
            "module": "Users",
            "name": "Madeshwaran G",
            "id": "4671651000000635001"
          }
        }
      ],
      "Location": "Business Address",
      "Unavailable_Till": null
    },
    {
      "Job_Sheet_Required": "No",
      "Owner": {
        "name": "Madeshwaran G",
        "id": "4671651000000635001",
        "email": "madeshwaran.g@zohocorp.com"
      },
      "Description": null,
      "Available_Days": [],
      "Tax": [],
      "Unavailable_From": "2026-01-14T12:20:35+05:30",
      "Record_Image": null,
      "id": "4671651000000867004",
      "Available_Dates": [],
      "Status": "Not in Use",
      "Available_Timings": null,
      "Service_Name": "dd",
      "Available_From": "2026-01-01",
      "Available_Till": "2026-01-29",
      "Duration": 120,
      "Job_Sheet_Section__s": null,
      "Price": 44,
      "Tag": [],
      "Availability_Type": "Specific Date Range",
      "Members": [
        {
          "id": "4671651000000867005",
          "Members": {
            "module": "Users",
            "name": "Madeshwaran G",
            "id": "4671651000000635001"
          }
        }
      ],
      "Location": "Business Address",
      "Unavailable_Till": null
    }
  ]
}
```
