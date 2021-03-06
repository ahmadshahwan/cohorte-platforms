# *****************************************************************************
# Copyright 2004-2008 Steve Menard
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# *****************************************************************************

# Reuse the Linux code
from ._linux import LinuxJVMFinder


class DarwinJVMFinder(LinuxJVMFinder):
    """
    Mac OS X JVM library finder class
    """
    def __init__(self):
        """
        Sets up members
        """
        # Call the parent constructor
        LinuxJVMFinder.__init__(self)

        # Library file name
        self._libfile = "libjvm.dylib"

        self._methods = list(self._methods)
        self._methods.append(self._pre_vm7_path)

        # Predefined locations
        self._locations = ('/Library/Java/JavaVirtualMachines',)

    def _pre_vm7_path(self):
        """
        Returns the previous constant JVM library path:
        '/System/Library/Frameworks/JavaVM.framework/JavaVM'
        """
        return '/System/Library/Frameworks/JavaVM.framework/JavaVM'
