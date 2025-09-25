import argparse
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient


def main():
    parser = argparse.ArgumentParser(description="Verify Azure Resource Group exists")
    parser.add_argument("--subscription-id", required=True)
    parser.add_argument("--resource-group-name", required=True)
    args = parser.parse_args()

    cred = DefaultAzureCredential(exclude_interactive_browser_credential=False)
    client = ResourceManagementClient(cred, args.subscription_id)
    rg = client.resource_groups.get(args.resource_group_name)
    print(f"Found resource group: {rg.name} in {rg.location}")


if __name__ == "__main__":
    main()

