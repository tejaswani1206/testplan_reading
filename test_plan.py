import sys

from testplan import test_plan
from testplan.testing.multitest import MultiTest, testsuite, testcase
from testplan.testing.multitest.result import Result

@testsuite
class TestingSuite(object):

    @testcase(summarize=True)
    def testcase_summarization(self, env, result):
        # Result data will contain a subset of failing / passing assertions
        for i in range(5000):
            result.equal(i, i)
            result.equal(i, i + 1)


    @testcase
    def block_summarization(self, env, result):

        result.equal('foo', 'bar', 'Assertion outside summary context')

        with result.group(
            summarize=True,
            num_passing=1,
            num_failing=2,
            description='Block level summary description',
        ) as group:
            for i in range(5000):
                result.equal(i, i)
                result.less(i, i + 1)

@test_plan(name='Basic Test Case')
def main(plan):
    plan.add(
        MultiTest(
            name='Example MultiTest',
            suites=[TestingSuite()]
        )
    )

if __name__ == '__main__':
    sys.exit(main().exit_code)