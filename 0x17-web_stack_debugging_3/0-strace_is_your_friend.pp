# automated puppet fix (to find out why Apache is returning a 500 error)

exec { 'Fix WordPress site':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  path     => '/bin:/usr/bin',  # Specify the path explicitly
  unless   => 'grep -q ".php" /var/www/html/wp-settings.php',  # Check if the fix is already applied
  provider => shell,
}
