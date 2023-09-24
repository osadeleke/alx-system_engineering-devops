# execute a command to kill a process
exec { 'kill_a_process':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
}
