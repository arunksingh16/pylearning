import sys
from kubernetes import client, config
import requests
from prettytable import PrettyTable
# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import warnings

warnings.filterwarnings('ignore', message='Unverified HTTPS request')


class OCApiCall:
    def __init__(self, key, url, namespace="party-data-hub-prd-axa-xl"):
        self._key = key
        self._url = url
        self._namespace = namespace

    def kubecall(self):
        """ Fetch POD Details
            Args:
                :namespace
                :key Oauth API Token
                :url OpenShift URL to connect
            Returns:
                :returns

        """
        key = self._key.replace("'", "")
        url = self._url.replace("'", "")
        configuration = client.Configuration()
        configuration.api_key["authorization"] = key
        configuration.api_key_prefix['authorization'] = 'Bearer'
        configuration.host = url
        configuration.ssl_ca_cert = None
        configuration.verify_ssl = False
        v1 = client.CoreV1Api(client.ApiClient(configuration))
        print("Listing pods with their IPs:")
        ns = ['party-data-hub-ppd-axa-xl', 'party-data-hub-prd-axa-xl']

        for ns_v in ns:
            print('Namespace: ' + ns_v)
            ret = v1.list_namespaced_pod(ns_v)
            # dir(ret) see methods/vars
            t = PrettyTable(['POD Name', 'POD status', 'POD IP', 'Status Reason', 'Namespace', 'Node'])
            for pod in ret.items:
                t.add_row(
                    [pod.metadata.name, pod.status.phase, pod.status.pod_ip, pod.status.reason, pod.metadata.namespace,
                     pod.spec.node_name])

            print(t)
