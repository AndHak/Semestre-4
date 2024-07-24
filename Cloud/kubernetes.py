from kubernetes import client, config

# Load the Kubernetes configuration from the default location
config.load_kube_config()

# Alternatively, you can load configuration from a specific file
# config.load_kube_config(config_file="path/to/config")

# Initialize the Kubernetes client
v1 = client.CoreV1Api()

# Define the Pod details
pod_name = "example-pod"
container_name = "example-container"
image_name = "nginx:latest"
port = 80

# Create a Pod
def create_pod(namespace, name, container_name, image, port):
	container = client.V1Container(
    	name=container_name,
    	image=image,
    	ports=[client.V1ContainerPort(container_port=port)],
	)

	pod_spec = client.V1PodSpec(containers=[container])
	pod_template = client.V1PodTemplateSpec(
    	metadata=client.V1ObjectMeta(labels={"app": name}), spec=pod_spec
	)

	pod = client.V1Pod(
    	api_version="v1",
    	kind="Pod",
    	metadata=client.V1ObjectMeta(name=name),
    	spec=pod_spec,
	)

	try:
		response = v1.create_namespaced_pod(namespace, pod)
		print("Pod created successfully.")
		return response
	except Exception as e:
		print("Error creating Pod:", e)


# Read a Pod
def get_pod(namespace, name):
	try:
		response = v1.read_namespaced_pod(name, namespace)
		print("Pod details:", response)
	except Exception as e:
		print("Error getting Pod:", e)


# Update a Pod (e.g., change the container image)
def update_pod(namespace, name, image):
	try:
		response = v1.read_namespaced_pod(name, namespace)
		response.spec.containers[0].image = image

		updated_pod = v1.replace_namespaced_pod(name, namespace, response)
		print("Pod updated successfully.")
		return updated_pod
	except Exception as e:
		print("Error updating Pod:", e)


# Delete a Pod
def delete_pod(namespace, name):
	try:
		response = v1.delete_namespaced_pod(name, namespace)
		print("Pod deleted successfully.")
	except Exception as e:
		print("Error deleting Pod:", e)


if __name__ == "__main__":
	namespace = "default"

	# Create a Pod
	create_pod(namespace, pod_name, container_name, image_name, port)

	# Read a Pod
	get_pod(namespace, pod_name)

	# Update a Pod
	new_image_name = "nginx:1.19"
	update_pod(namespace, pod_name, new_image_name)

	# Read the updated Pod
	get_pod(namespace, pod_name)

	# Delete the Pod
	delete_pod(namespace, pod_name)