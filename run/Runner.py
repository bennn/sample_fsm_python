import glob
import itertools
import subprocess
from math import log2
from Reader import get_name
from shutil import copyfile

def run_all(benchmark, test, output):
    """
    :param benchmark: Full path
    :param test: Full path
    :param output: path
    :return: None
    """
    directories = glob.glob('%s/*' % benchmark)
    names = [get_name(d) for d in directories]

    all_files = [glob.glob('%s/*' % d) for d in directories]
    lengths = [len(files) for files in all_files]
    with open(output, 'r') as out:
        for files in itertools.product(*all_files):
            for name, file in zip(names, files):
                copyfile(file, '%s/%s.py' % (test, name))
                t = run_1(test)
                nums = [get_name(f) for f in files]
                tag = '-'.join(nums)
                print('%s   %s   %s' % (tag, count_types(nums, lengths), t), file=out)


def count_types(nums, lengths):
    """
    Number of typed functions across all the files
    :param nums: List of int
    :param lengths: lengths[i] is upper bound for nums[i]
    :return: Int, representing number of annotated functions in the file
    """
    total = 0
    for num, length in zip(nums, lengths):
        b = bin(int(num))[2:]
        l = log2(length)
        c = ("0" * (l - len(b))) + b
        total+=sum([1 for bit in c if c == '0'])

    return total

def run_1(test):
    output = str(subprocess.check_output('retic %s/Fsm0.py' % test, shell=True),
                 encoding="utf-8")

    return output

run_all('/Users/zeinamigeed/sample_fsm_python/Benchmark',
        '/Users/zeinamigeed/sample_fsm_python/Test',
        '/Users/zeinamigeed/sample_fsm_python/output.py')