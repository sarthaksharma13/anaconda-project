# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2016, Continuum Analytics, Inc. All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
# ----------------------------------------------------------------------------
"""Commands related to setting and unsetting variables."""
from __future__ import absolute_import, print_function

from anaconda_project.project import Project
from anaconda_project import project_ops
from anaconda_project.commands.console_utils import print_project_problems


def set_variables(project_dir, conda_environment, vars_to_set):
    """Change default env variables for local project and change project file.

    Returns:
        Success result (can be treated as True on success).
    """
    fixed_vars = []
    for var in vars_to_set:
        if '=' not in var:
            print("Error: {} doesn't define a name=value pair".format(var))
            return 1
        fixed_vars.append(tuple(var.split('=', maxsplit=1)))
    project = Project(project_dir, default_conda_environment=conda_environment)
    if print_project_problems(project):
        return 1
    project_ops.add_variables(project, fixed_vars)
    return 0


def unset_variables(*args):
    """Unset the variables for local project and changes project file.

    Returns:
        Success result
    """
    raise NotImplementedError("Not yet.")


def main(args):
    """Start the prepare command and return exit status code."""
    if args.action == 'set':
        return set_variables(args.project, args.environment, args.vars_to_set)
    else:
        return unset_variables(args.project, args.environment, args.vars_to_unset)
