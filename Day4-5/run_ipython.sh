#!/bin/bash

module="Anaconda3"

if [ "$#" -eq 1 ]; then
   module=$1
fi

#ip=$(host `uname -n` | cut -d ' ' -f 4)
ip=$(/sbin/ip route get 8.8.8.8 | awk '{print $NF;exit}')
port=$((10000+ $RANDOM % 20000))

echo "Running ipython notebook"
echo "If you need another version of Python please run sh $BASH_SOURCE python_module_name"
echo "Please wait ..."

module load $module

jupyter-notebook --no-browser --ip=$ip --port=$port --log-level='ERROR'
