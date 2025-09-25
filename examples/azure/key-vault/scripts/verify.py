import argparse
from azure.identity import DefaultAzureCredential
from azure.mgmt.keyvault import KeyVaultManagementClient


def main():
    parser = argparse.ArgumentParser(description="Verify Azure Key Vault")
    parser.add_argument("--subscription-id", required=True)
    parser.add_argument("--resource-group-name", required=True)
    parser.add_argument("--vault-name", required=True)
    args = parser.parse_args()

    cred = DefaultAzureCredential(exclude_interactive_browser_credential=False)
    kv_client = KeyVaultManagementClient(cred, args.subscription_id)
    vault = kv_client.vaults.get(args.resource_group_name, args.vault_name)
    print(f"Found key vault: {vault.name} in {vault.location}. Purge protection: {vault.properties.enable_purge_protection}")


if __name__ == "__main__":
    main()

