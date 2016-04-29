# Copyright 2016 VMware, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from tempest.api.network import base
from tempest import test


class NetworksApiDiscovery(base.BaseNetworkTest):

    @test.attr(type='n00b')
    @test.idempotent_id('bdf8183d-5dbf-4633-98b8-e892f987a79b')
    def test_list_api_versions(self):
        """Test that a GET request to / returns proper API versions.

        Clients that want to use OpenStack services need to know
        what versions of the API are available to them.  They can
        discover the versions available by sending an unauthenticated
        GET request for the unversioned root URL.  This simple
        capability is important for interoperability in that
        clients must have a way to discover how to interact with
        a given cloud.
        """

        result = self.network_versions_client.list_versions()
        versions = result['versions']

        # There is currently only one version of the API...
        self.assertEqual(len(versions), 1)

        # ...and it is v2.0
        self.assertEqual(versions[0]['id'], 'v2.0',
                         "The first listed version should be v2.0")

    @test.attr(type='n00b')
    @test.idempotent_id('cac8a836-c2e0-4304-b556-cd299c7281d1')
    def test_api_version_resources(self):
        """Test that GET / returns expected resources.

        The versions document returned by Neutron returns a few other
        resources other than just available API versions: it also
        states the status of each API version and provides links to
        schema.
        """

        result = self.network_versions_client.list_versions()
        expected_versions = ('v2.0')
        expected_resources = ('id', 'links', 'status')
        received_list = result.values()

        for item in received_list:
            for version in item:
                for resource in expected_resources:
                    self.assertIn(resource, version)
                self.assertIn(version['id'], expected_versions)
