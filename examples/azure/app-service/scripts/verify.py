import argparse
from azure.identity import DefaultAzureCredential
from azure.mgmt.web import WebSiteManagementClient


def main():
    parser = argparse.ArgumentParser(description="Verify Azure Web App")
    parser.add_argument("--subscription-id", required=True)
    parser.add_argument("--resource-group-name", required=True)
    parser.add_argument("--webapp-name", required=True)
    args = parser.parse_args()

    cred = DefaultAzureCredential(exclude_interactive_browser_credential=False)
    web = WebSiteManagementClient(cred, args.subscription_id)
    app = web.web_apps.get(args.resource_group_name, args.webapp_name)
    print(f"Found Web App: {app.name}, default hostname: {app.default_host_name}")


if __name__ == "__main__":
    main()

