import os
import subprocess
import time
from collections import namedtuple

# Cannot run from any directory, problem?
TESTPATH = 'tests/'
UPYPATH = '../unix/'
SEPARATOR = '-----\n'
UIMPORTLIST = {'struct', 'collections'}

Output = namedtuple('output', ['name', 'clss', 'desc', 'code', 'output_cpy', 'output_upy', 'status'])

def readfiles():
    tests = os.listdir(TESTPATH)
    tests.sort()
    files = []

    for test in tests:
        f = open(TESTPATH + test, 'r')
        try:
            clss, desc, code = f.read().split(SEPARATOR)
        except ValueError:
            print('Incorrect format in file ' + TESTPATH + test)
        o = Output(test, clss, desc, code, '', '', '')
        files.append(o)

    return files

def uimports(code):
    for uimport in UIMPORTLIST:
        code = code.replace(uimport, 'u' + uimport)
    return code

def run_tests(files):
    results = []
    for f in files:
        cmd = 'python'
        p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output_cpy = [com.decode('ascii') for com in p.communicate(input=str.encode(f.code))]

        if output_cpy[1] != '':
            print('CPython failure in file ' + TESTPATH + f.name)
            print(output_cpy[1])

        cmd = UPYPATH +'./micropython'
        p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output_upy = [com.decode('ascii') for com in p.communicate(input=str.encode(uimports(f.code)))]

        if output_cpy[0] == output_upy[0] and output_cpy[1] == output_upy[1]:
            status = 'Supported'
        else:
            status = 'Unsupported'

        o = Output(f.name, f.clss, f.desc, f.code, output_cpy, output_upy, status)
        results.append(o)

    results.sort(key = lambda x: x.clss)
    return results

def markingdown(results):
    markdown = open('markdown.md', 'w')
    markdown.write('# Micropython unsupported operations\n  \n')
    markdown.write(time.strftime("Generated %a %d %b %Y %X AEDT\n", time.localtime()))
    clss = []
    for o in results:
        c = o.clss.split(',')
        for i in range(len(c)):
            c[i] = c[i].rstrip()
            if i >= len(clss) or c[i] != clss[i]:
                if i > 0:
                    markdown.write('#')
                markdown.write('## ' + ''.join(['.' for j in range(i)]) + c[i] + '\n---\n')
        clss = c
        #markdown.write('### ' + o.name + '\n')
        markdown.write(o.desc + '\n')
        markdown.write(o.status + '\n\n')

        markdown.write('Sample code:  \n\n')
        markdown.write('```python\n' + o.code + '```\n\n')
        markdown.write('CPy output:  \n\n')
        markdown.write('```python\n' + o.output_cpy[0] + o.output_cpy[1] + '```\n\n')
        markdown.write('uPy output:  \n\n')
        markdown.write('```python\n' + o.output_upy[0] + o.output_upy[1] + '```\n\n')

    markdown.close()

def main():
    files = readfiles()
    results = run_tests(files)
    markingdown(results)

main()
