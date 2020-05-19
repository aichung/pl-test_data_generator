#!/usr/bin/env python                                            
#
# test_data_generator fs ChRIS plugin app
#
# (c) 2016-2019 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#


import os
import sys
sys.path.append(os.path.dirname(__file__))

# import the Chris app superclass
from chrisapp.base import ChrisApp

from os import listdir, sep
from os.path import abspath, basename, isdir
from distutils.dir_util import copy_tree
import shutil
import time
import glob


Gstr_title = """

 _            _        _       _                                           _             
| |          | |      | |     | |                                         | |            
| |_ ___  ___| |_   __| | __ _| |_ __ _     __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| __/ _ \/ __| __| / _` |/ _` | __/ _` |   / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| ||  __/\__ \ |_ | (_| | (_| | || (_| |  | (_| |  __/ | | |  __/ | | (_| | || (_) | |   
 \__\___||___/\__| \__,_|\__,_|\__\__,_|   \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
               ______                ______ __/ |                                        
              |______|              |______|___/                                         

"""

Gstr_synopsis = """

(Edit this in-line help for app specifics. At a minimum, the 
flags below are supported -- in the case of DS apps, both
positional arguments <inputDir> and <outputDir>; for FS apps
only <outputDir> -- and similarly for <in> <out> directories
where necessary.)

    NAME

       test_data_generator.py 

    SYNOPSIS

        python test_data_generator.py                                         \\
            [-h] [--help]                                               \\
            [--json]                                                    \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--savejson <DIR>]                                          \\
            [-v <level>] [--verbosity <level>]                          \\
            [--version]                                                 \\
            <inputDir>                                                  \\
            <outputDir> 

    BRIEF EXAMPLE

        * Copy the (container) internal data to the output directory:

            mkdir in out && chmod 777 out
            python test_data_generator.py out

    DESCRIPTION

        `test_data_generator.py` copies internal 'test' data to the
        <outputDir>.

    ARGS

        [-h] [--help]
        If specified, show help message and exit.
        
        [--json]
        If specified, show json representation of app and exit.
        
        [--man]
        If specified, print (this) man page and exit.

        [--meta]
        If specified, print plugin meta data and exit.
        
        [--savejson <DIR>] 
        If specified, save json representation file to DIR and exit. 
        
        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.
        
        [--version]
        If specified, print version number and exit. 

"""


class Test_data_generator(ChrisApp):
    """
    Outputs test data for classification module (CNI).
    """
    AUTHORS                 = 'AWC (aiwern.chung@childrens.harvard.edu)'
    SELFPATH                = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC                = os.path.basename(__file__)
    EXECSHELL               = 'python3'
    TITLE                   = 'Outputs test data for classification module (CNI)'
    CATEGORY                = ''
    TYPE                    = 'fs'
    DESCRIPTION             = 'Outputs test data for classification module (CNI)'
    DOCUMENTATION           = 'http://wiki'
    VERSION                 = '0.1'
    ICON                    = '' # url of an icon image
    LICENSE                 = 'Opensource (MIT)'
    MAX_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MAX_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT           = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT           = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % self.get_version())

        str_srcDir  = '../data'
        print('\nCopying files from:\n\t%s\n to:\n\t%s.....\n' % (str_srcDir, options.outputdir))
        copy_tree(str_srcDir, options.outputdir)


    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)


# ENTRYPOINT
if __name__ == "__main__":
    chris_app = Test_data_generator()
    chris_app.launch()
