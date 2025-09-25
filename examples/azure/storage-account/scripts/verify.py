import argparse
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient


def main():
    parser = argparse.ArgumentParser(description="Verify Azure Storage Account")
    parser.add_argument("--subscription-id", required=True)
    parser.add_argument("--resource-group-name", required=True)
    parser.add_argument("--account-name", required=True)
    args = parser.parse_args()

    cred = DefaultAzureCredential(exclude_interactive_browser_credential=False)
    res_client = ResourceManagementClient(cred, args.subscription_id)
    _ = res_client.resource_groups.get(args.resource_group_name)

    stor_client = StorageManagementClient(cred, args.subscription_id)
    acct = stor_client.storage_accounts.get_properties(args.resource_group_name, args.account_name)
    print(f"Found storage account: {acct.name} in {acct.location}. TLS min version: {acct.minimum_tls_version}")


if __name__ == "__main__":
    main()

