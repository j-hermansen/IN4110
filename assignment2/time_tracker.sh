
# USAGE

# 1. 'LOGFILE' environment variable must be set. Add 'export LOGFILE="<logfile name>"' to end of ~/.bashrc
# 2. Source the script when terminal start: Add 'source <absolute-path-to-script>' to end of ~/.bashrc
# 3. Start using the script functions in terminal with 'track' and 'log' commands

# Example:
# track start read_about_python
# log
  # Output: read_about_python: 00:00:03
# track status
  # Output: On task: read_about_python
# track stop

# To view task in logs:
# cat ~/.local/share/$LOGFILE

state=0

track() {

  if [ $# -eq 0 ]; then
    echo -e "No arguments provided. Please provide arguments.\nUsage: track [start|stop] [name] (name only required on start command)"
    return
  fi

  case "$1" in
    "start")
      if [ $state -eq 2 ]; then
        echo -e "A Task is active.\nRun 'log' to see information about the active task."
        return
      fi

      if [ $# -eq 1 ]; then
        echo -e "Please provide a name for the task.\nUsage: 'track start [name]'"
        return
      fi

      task=$2

      start=$SECONDS
      echo -e "START\t $(date)" >> $HOME/.local/share/$LOGFILE
      echo -e "LABEL\t $2" >> $HOME/.local/share/$LOGFILE
      state=2
      ;;
    "stop")
      if [ $state -eq 1 -o $state -eq 0 ]; then
        echo "No active task to stop."
        return
      fi
      SECONDS=0
      echo -e "STOP\t $(date)" >> $HOME/.local/share/$LOGFILE
      echo "" >> $HOME/.local/share/$LOGFILE
      state=1
      ;;
    "status")
      if [ -f "$HOME/.local/share/$LOGFILE" ]; then
        cat "$HOME/.local/share/$LOGFILE"
            | tail -n1
            | grep -q LABEL && tail -n1 $HOME/.local/share/$LOGFILE
            | echo "On task: $(cut -d " " -f2)" || echo "No active task."
      else
        echo "No tasks."
      fi
      ;;
    *)
      echo "Unknown option.\nAvailable options are [start|stop|status]"
      return
      ;;
  esac

}

log() {

  if [ $state -eq 0 -o $state -eq 1 ]; then
    echo "No active task, run new task with 'track start [task-name]'"
    return
  elif [ $state -eq 2 ]; then
    duration=$((SECONDS - start))
    h=$(($duration / 3600))
    m=$(($duration / 60))
    s=$(($duration % 60))

    printf "%s: %02d:%02d:%02d\n" $task $h $m $s
  fi
}


