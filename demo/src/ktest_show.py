import subprocess
import os
import argparse


# check .ktest file
def ktest_write(bc_base_name='symbolic', root_pth='/home/klee/demo_ivan/bc', output_pth='/home/klee/demo_ivan/output'):

    program_name = 'klee_' + bc_base_name
    program_pth = root_pth + '/' + program_name
    os.chdir(root_pth)

    ktest_dir = os.listdir(program_pth)
    outs = []
    for ktest in (ktest_dir):
        if ktest.endswith('.ktest'):
            try:
                # run ktest-tool
                ktest_pth = program_pth + '/' + ktest
                p1 = subprocess.Popen(['ktest-tool', ktest_pth], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                print('ktest-tool ' + ktest)
                out, stderr = p1.communicate()
                outs.append((ktest ,out))
                # print('ktest-tool Output:', stdout)
                # print('ktest-tool Error:', stderr)
            except OSError as e:
                print('OSError:', e)
            except subprocess.CalledProcessError as e:
                print('CalledProcessError:', e)

    # write stdout to file
    file_pth = output_pth + '/' + bc_base_name + '_ktest_o.txt'
    with open(file_pth, 'w') as f:
        for ktest, out in outs:
            f.write(bc_base_name +': '+ ktest + '\n')
            f.write(out + '\n')


if __name__ == '__main__':  

    parser = argparse.ArgumentParser(description='Run KLEE and process .ktest files.')
    parser.add_argument('-bc-name', type=str, help='The name of the .bc file to process')
    parser.add_argument('-generate', type=str, default='False' , help='generate ktest files or not')
    args = parser.parse_args()
    
    output_pth = '/home/klee/demo_ivan/output'
    if not os.path.exists(output_pth):
        os.makedirs(output_pth)
    root_pth='/home/klee/demo_ivan/bc'
    os.chdir(root_pth)
    # bc_name = 'symbolic.bc'
    bc_name = args.bc_name
    bc_base_name = bc_name.split('.')[0]
    program_name = 'klee_' + bc_base_name
    # run klee
    if args.generate == 'True':
        p0 = subprocess.Popen(['klee', '--output-dir=' + program_name, bc_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        out = p0.communicate()  # wait for the process to finish
        print('klee Output:', out)
    ktest_write(bc_base_name=bc_base_name, output_pth=output_pth)