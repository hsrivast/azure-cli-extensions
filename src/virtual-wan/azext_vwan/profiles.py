# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.profiles import CustomResourceType

CUSTOM_VWAN = CustomResourceType('azext_vwan.vendored_sdks.v2020_05_01', 'NetworkManagementClient')
CUSTOM_VWAN_2021_03_01 = CustomResourceType('azext_vwan.vendored_sdks.v2021_03_01', 'NetworkManagementClient')
