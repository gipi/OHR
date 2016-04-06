#!/usr/bin/env python
import os
import sys
import environ


ROOT_DIR = environ.Path(__file__) - 2  # (/a/b/myfile.py - 3 = /)

env = environ.Env()
env.read_env(ROOT_DIR('.env'))


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
