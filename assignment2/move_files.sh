#!/bin/bash

# USAGE

# Run script: ./move_files.sh [-t] [filetype] [from dir] [to dir]
# Filetype are optional. All files are transferred if no filetype are specified.

# Example1 (all files):
# ./move_files images documents

# Example2 (Specified files):
# ./move_files -t png images documents

if [ $# -lt 2 ]; then
  echo -e "You should at least provide two arguments.\nUsage: ./move_files.sh -t [filetype] [from-directory] [to-directory]\nFiletype is optional."
  exit 1
elif [ $# -eq 2 ]; then
  src=$1
  dst=$2
elif [ $1 == "-t" ]; then
  t=$2
  src=$3
  dst=$4
fi

function move() {

  filetypes=${t:-*} # check if variable t is defined, or pass * (all files) to the function.

  if [ -e "$src" ]; then
    if [ ! -e "$dst" ]; then
      t_date=$(date +"%Y-%m-%d-%H-%M")
      read -p "Directory $dst does not exist. Create new directory with the name "$t_date"? (\"yes\" or \"no\"): " answer
      if [ $answer == "yes" ]; then mkdir "$t_date"; dst=$t_date; else echo "Exiting..."; exit 1; fi

    fi

    files=`ls $src/*.$filetypes` # moves all files, or specified file type, e.g. only .txt files

    for i in $files; do
      mv $i "$dst"
    done
  fi
}

move

