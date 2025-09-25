import argparse
from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient


def main():
    parser = argparse.ArgumentParser(description="Verify Azure VNet and Subnet")
    parser.add_argument("--subscription-id", required=True)
    parser.add_argument("--resource-group-name", required=True)
    parser.add_argument("--vnet-name", required=True)
    parser.add_argument("--subnet-name", default="subnet1")
    args = parser.parse_args()

    cred = DefaultAzureCredential(exclude_interactive_browser_credential=False)
    net = NetworkManagementClient(cred, args.subscription_id)
    vnet = net.virtual_networks.get(args.resource_group_name, args.vnet_name)
    subnet = net.subnets.get(args.resource_group_name, args.vnet_name, args.subnet_name)
    print(f"Found VNet: {vnet.name} address spaces: {vnet.address_space.address_prefixes}")
    print(f"Found Subnet: {subnet.name} address prefix: {subnet.address_prefix}")


if __name__ == "__main__":
    main()

