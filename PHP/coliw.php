
<?php 

//dl('php_sockets.dll');
$message='curwa?';
$host='localhost';
$port='6636';
// create socket	
$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP) or die("Could not create socket\n");
echo "[i] Socket created<br>";
// connect to server
$result = socket_connect($socket, $host, $port) or die ("Could not connect to server\n");
echo "[i] Socket connected<br>";
// send string to server
socket_write($socket, $message, strlen($message)) or die("Could not send data to server\n");
// get server response
$result = socket_read ($socket, 1024000) or die("Could not read server response\n");
echo "Server  says :".$result."<br>";
// close socket
while(True)
{
	echo "fac parte din while<br>";
	break;
}
socket_close($socket);


?>



