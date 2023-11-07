$file_to_edit = '/var/www/html/wp-settings.php'

# Check if the file contains "phpp" before replacing the line
exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin', '/usr/bin'],
  onlyif  => "grep -q 'phpp' ${file_to_edit}",
}
