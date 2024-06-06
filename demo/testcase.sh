#!/bin/bash

# Array of test file names
# test_files=("test000143.ktest" "test000210.ktest" "test000256.ktest" "test000300.ktest")

# Output file
# output_file="output/maze_solution.txt"
#!/bin/bash

# output_file="/dev/stdout"
program="bst_sym"
output_file="output/$program.log"
# touch $output_file
exe_file="exe/$program"

# Clear
> $output_file

# iterate .ktest files
for test_file in bc/klee_$program/*.ktest; do
    echo "Running $test_file" >> $output_file
    export KTEST_FILE="$test_file"
    ./$exe_file >> $output_file
    echo "----------------------------" >> $output_file
done


# test_files=("test000143.ktest" "test000210.ktest" "test000256.ktest" "test000300.ktest")
# test_file=${test_files[0]}
# export KTEST_FILE="bc/klee_maze_symbolic/$test_file"
# ./exe/maze_symbolic