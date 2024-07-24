from kubernetes import client, config

def update_deployment_strategy(deployment_name, namespace, max_unavailable):
    config.load_kube_config()
    apps_v1 = client.AppsV1Api()

    deployment = apps_v1.read_namespaced_deployment(deployment_name, namespace)
    deployment.spec.strategy.rolling_update.max_unavailable = max_unavailable
    apps_v1.patch_namespaced_deployment(deployment_name, namespace, deployment)

if __name__ == "__main__":
    update_deployment_strategy('my-deployment', 'my-namespace', '25%')