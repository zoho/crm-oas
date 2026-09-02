# Mass Delete Tags APIs

- [OpenAPI specification](mass_delete_tags.yaml)
- [Mass delete tags](operations/massDeleteTags/operation.md)
  - To schedule a background job that deletes multiple tags in bulk from a single module in your Zoho CRM organization. You can delete tags in bulk from one module per API call. The response returns a job identifier that can be used with the Mass Delete Tags Status GET operation to track the progress of the deletion.
  - [Examples](operations/massDeleteTags/examples/)
- [Mass Delete Tags Status](operations/getMassDeleteTagsStatus/operation.md)
  - To retrieve the current status, the scheduled time, and the success and failure counts for a previously scheduled mass delete tag job in your Zoho CRM organization, using the job ID returned by the Mass Delete Tags POST operation.
  - [Examples](operations/getMassDeleteTagsStatus/examples/)
