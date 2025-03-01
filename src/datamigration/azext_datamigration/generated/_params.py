# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import (
    get_default_location_from_resource_group,
    validate_file_or_dict
)
from azext_datamigration.action import (
    AddSourceSqlConnection,
    AddOfflineConfiguration,
    AddTargetLocation
)


def load_arguments(self, _):

    with self.argument_context('datamigration sql-managed-instance show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_instance_name', type=str, help='Name of the target SQL Managed Instance.', id_part='name')
        c.argument('target_db_name', type=str, help='The name of the target database.', id_part='child_name_1')
        c.argument('migration_operation_id', help='Optional migration operation ID. If this is provided, then details '
                   'of migration operation for that ID are retrieved. If not provided (default), then details related '
                   'to most recent or current operation are retrieved.')
        c.argument('expand', type=str, help='The child resources to include in the response.')

    with self.argument_context('datamigration sql-managed-instance create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_instance_name', type=str, help='Name of the target SQL Managed Instance.')
        c.argument('target_db_name', type=str, help='The name of the target database.')
        c.argument('scope', type=str, help='Resource Id of the target resource (SQL VM or SQL Managed Instance)')
        c.argument('source_sql_connection', action=AddSourceSqlConnection, nargs='+', help='Source SQL Server '
                   'connection details.')
        c.argument('source_database_name', type=str, help='Name of the source database.')
        c.argument('migration_service', type=str, help='Resource Id of the Migration Service.')
        c.argument('migration_operation_id', type=str, help='ID tracking current migration operation.')
        c.argument('target_db_collation', type=str, help='Database collation to be used for the target database.')
        c.argument('provisioning_error', type=str, help='Error message for migration provisioning failure, if any.')
        c.argument('offline_configuration', action=AddOfflineConfiguration, nargs='+', help='Offline configuration.')
        c.argument('source_location', type=validate_file_or_dict, help='Source location of backups. Expected value: '
                   'json-string/json-file/@json-file.', arg_group='Backup Configuration')
        c.argument('target_location', action=AddTargetLocation, nargs='+', help='Target location for copying backups.',
                   arg_group='Backup Configuration')

    with self.argument_context('datamigration sql-managed-instance cancel') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_instance_name', type=str, help='Name of the target SQL Managed Instance.', id_part='name')
        c.argument('target_db_name', type=str, help='The name of the target database.', id_part='child_name_1')
        c.argument('migration_operation_id', help='ID tracking migration operation.')

    with self.argument_context('datamigration sql-managed-instance cutover') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_instance_name', type=str, help='Name of the target SQL Managed Instance.', id_part='name')
        c.argument('target_db_name', type=str, help='The name of the target database.', id_part='child_name_1')
        c.argument('migration_operation_id', help='ID tracking migration operation.')

    with self.argument_context('datamigration sql-managed-instance wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('managed_instance_name', type=str, help='Name of the target SQL Managed Instance.', id_part='name')
        c.argument('target_db_name', type=str, help='The name of the target database.', id_part='child_name_1')
        c.argument('migration_operation_id', help='Optional migration operation ID. If this is provided, then details '
                   'of migration operation for that ID are retrieved. If not provided (default), then details related '
                   'to most recent or current operation are retrieved.')
        c.argument('expand', type=str, help='The child resources to include in the response.')

    with self.argument_context('datamigration sql-vm show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('sql_vm_name', type=str, help='Name of the target SQL Virtual Machine.', id_part='name')
        c.argument('target_db_name', type=str, help='The name of the target database.', id_part='child_name_1')
        c.argument('migration_operation_id', help='Optional migration operation ID. If this is provided, then details '
                   'of migration operation for that ID are retrieved. If not provided (default), then details related '
                   'to most recent or current operation are retrieved.')
        c.argument('expand', type=str, help='The child resources to include in the response.')

    with self.argument_context('datamigration sql-vm create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('sql_vm_name', type=str, help='Name of the target SQL Virtual Machine.')
        c.argument('target_db_name', type=str, help='The name of the target database.')
        c.argument('scope', type=str, help='Resource Id of the target resource (SQL VM or SQL Managed Instance)')
        c.argument('source_sql_connection', action=AddSourceSqlConnection, nargs='+', help='Source SQL Server '
                   'connection details.')
        c.argument('source_database_name', type=str, help='Name of the source database.')
        c.argument('migration_service', type=str, help='Resource Id of the Migration Service.')
        c.argument('migration_operation_id', type=str, help='ID tracking current migration operation.')
        c.argument('target_db_collation', type=str, help='Database collation to be used for the target database.')
        c.argument('provisioning_error', type=str, help='Error message for migration provisioning failure, if any.')
        c.argument('offline_configuration', action=AddOfflineConfiguration, nargs='+', help='Offline configuration.')
        c.argument('source_location', type=validate_file_or_dict, help='Source location of backups. Expected value: '
                   'json-string/json-file/@json-file.', arg_group='Backup Configuration')
        c.argument('target_location', action=AddTargetLocation, nargs='+', help='Target location for copying backups.',
                   arg_group='Backup Configuration')

    with self.argument_context('datamigration sql-vm cancel') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('sql_vm_name', type=str, help='Name of the target SQL Virtual Machine.', id_part='name')
        c.argument('target_db_name', type=str, help='The name of the target database.', id_part='child_name_1')
        c.argument('migration_operation_id', help='ID tracking migration operation.')

    with self.argument_context('datamigration sql-vm cutover') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('sql_vm_name', type=str, help='Name of the target SQL Virtual Machine.', id_part='name')
        c.argument('target_db_name', type=str, help='The name of the target database.', id_part='child_name_1')
        c.argument('migration_operation_id', help='ID tracking migration operation.')

    with self.argument_context('datamigration sql-vm wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('sql_vm_name', type=str, help='Name of the target SQL Virtual Machine.', id_part='name')
        c.argument('target_db_name', type=str, help='The name of the target database.', id_part='child_name_1')
        c.argument('migration_operation_id', help='Optional migration operation ID. If this is provided, then details '
                   'of migration operation for that ID are retrieved. If not provided (default), then details related '
                   'to most recent or current operation are retrieved.')
        c.argument('expand', type=str, help='The child resources to include in the response.')

    with self.argument_context('datamigration sql-service list') as c:
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('datamigration sql-service show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('sql_migration_service_name', options_list=['--name', '-n', '--sql-migration-service-name'],
                   type=str, help='Name of the SQL Migration Service.', id_part='name')

    with self.argument_context('datamigration sql-service create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('sql_migration_service_name', options_list=['--name', '-n', '--sql-migration-service-name'],
                   type=str, help='Name of the SQL Migration Service.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)

    with self.argument_context('datamigration sql-service update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('sql_migration_service_name', options_list=['--name', '-n', '--sql-migration-service-name'],
                   type=str, help='Name of the SQL Migration Service.', id_part='name')
        c.argument('tags', tags_type)

    with self.argument_context('datamigration sql-service delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('sql_migration_service_name', options_list=['--name', '-n', '--sql-migration-service-name'],
                   type=str, help='Name of the SQL Migration Service.', id_part='name')

    with self.argument_context('datamigration sql-service delete-node') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('sql_migration_service_name', options_list=['--name', '-n', '--sql-migration-service-name'],
                   type=str, help='Name of the SQL Migration Service.', id_part='name')
        c.argument('node_name', type=str, help='The name of node to delete.')
        c.argument('integration_runtime_name', options_list=['--ir-name'], type=str, help='The name of integration '
                   'runtime.')

    with self.argument_context('datamigration sql-service list-auth-key') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('sql_migration_service_name', options_list=['--name', '-n', '--sql-migration-service-name'],
                   type=str, help='Name of the SQL Migration Service.')

    with self.argument_context('datamigration sql-service list-integration-runtime-metric') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('sql_migration_service_name', options_list=['--name', '-n', '--sql-migration-service-name'],
                   type=str, help='Name of the SQL Migration Service.')

    with self.argument_context('datamigration sql-service list-migration') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('sql_migration_service_name', options_list=['--name', '-n', '--sql-migration-service-name'],
                   type=str, help='Name of the SQL Migration Service.')

    with self.argument_context('datamigration sql-service regenerate-auth-key') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('sql_migration_service_name', options_list=['--name', '-n', '--sql-migration-service-name'],
                   type=str, help='Name of the SQL Migration Service.', id_part='name')
        c.argument('key_name', type=str, help='The name of authentication key to generate.')
        c.argument('auth_key1', type=str, help='The first authentication key.')
        c.argument('auth_key2', type=str, help='The second authentication key.')

    with self.argument_context('datamigration sql-service wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('sql_migration_service_name', options_list=['--name', '-n', '--sql-migration-service-name'],
                   type=str, help='Name of the SQL Migration Service.', id_part='name')
