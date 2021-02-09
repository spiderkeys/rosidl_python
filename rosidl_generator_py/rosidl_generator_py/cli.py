# Copyright 2021 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ament_index_python import get_package_share_directory
from ament_index_python import get_resources

from rosidl_cli.command.generate.extensions import GenerateCommandExtension
from rosidl_cli.command.generate.helpers import legacy_generator_arguments_file

from rosidl_generator_py import generate_py


class GeneratePython(GenerateCommandExtension):

    def generate(
        self,
        package_name,
        interface_files,
        include_paths,
        output_path
    ):
        package_share_path = \
            get_package_share_directory(
                'rosidl_generator_py'
            )
        templates_path = os.path.join(
            package_share_path, 'resource'
        )
        typesupport_implementations = ['rosidl_typesupport_c']
        typesupport_implementations.extend(get_resources('rosidl_typesupport_c'))
        with legacy_generator_arguments_file(
            package_name, interface_files,
            include_paths, templates_path,
            output_path
        ) as path_to_arguments_file:
            generate_py(path_to_arguments_file, typesupport_implementations)
