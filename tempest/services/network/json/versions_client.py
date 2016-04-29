#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from tempest.lib.services.network import base
from six.moves import urllib
from oslo_serialization import jsonutils as json


class VersionsClient(base.BaseNetworkClient):

    def list_versions(self):
        """Do a GET / to fetch available API version information."""

        endpoint = self.base_url
        url = urllib.parse.urlparse(endpoint)
        version_url = '%s://%s/' % (url.scheme, url.netloc)

        # Note: we do a raw_request here because we want to use
        # an unversioned URL, not "v2/$project_id/".
        response, body = self.raw_request(version_url, 'GET')
        body = json.loads(body)
        return body
