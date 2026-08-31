# Mass Change Owner

- [OpenAPI specification](mass_change_owner.yaml)
- [Submit mass change owner job](operations/massChangeOwner/operation.md)
  - To bulk update the ownership of records in a specified module based on a Custom View, territory, or field-based criteria in your Zoho CRM organization. You cannot change the owner of related records using this API. You can change the owner of up to 50,000 records in a custom view. This API schedules the operation as a job and returns a job ID, which you can use to check the job status. Job statuses are available for up to 60 days. The Mass Change Owner API is available only in the Enterprise and Ultimate editions. The OAuth scope enforced is specific to the target module (for example, **ZohoCRM.change_owner.leads.CREATE** for Leads); modules without a dedicated scope fall back to a generic custom-module scope.
  - [Examples](operations/massChangeOwner/examples/)
- [Get mass change owner job status](operations/getMassChangeOwnerStatus/operation.md)
  - To retrieve the status of a previously scheduled mass change owner job in your Zoho CRM organization. The OAuth scope enforced is specific to the target module (for example, **ZohoCRM.change_owner.leads.READ** for Leads); modules without a dedicated scope fall back to a generic custom-module scope.
  - [Examples](operations/getMassChangeOwnerStatus/examples/)
