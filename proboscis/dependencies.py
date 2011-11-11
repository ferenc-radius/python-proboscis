# Copyright (c) 2011 Rackspace
# All Rights Reserved.
#
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

try:
    global use_nose
    use_nose = True

    from nose.plugins.skip import SkipTest
    from nose.core import TestProgram
    from nose.core import TextTestResult
    from nose.core import TextTestRunner

    def skip_test(test_self, message):
        raise SkipTest(message)

except ImportError:
    global use_nose
    use_nose = False

    import unittest
    from unittest import TextTestRunner

    # In 2.7 unittest.TestCase has a skipTest method.
    def skip_test(test_self, message):
        try:
            test_self.skipTest(message)
        except AttributeError:
            raise AssertionError("SKIPPED:%s" % message)

    class TestProgram(unittest.TestProgram):
        def __init__(self, suite, config=None, *args, **kwargs):
            self.suite_arg = suite
            self.test = suite
            super(TestProgram, self).__init__(*args, **kwargs)

        def createTests(self):
            self.test = self.suite_arg

    class TextTestResult(unittest._TextTestResult):
        def __init__(self, stream, descriptions, verbosity, config=None,
                     errorClasses=None):
            super(TextTestResult, self).__init__(stream, descriptions,
                                                 verbosity);
            