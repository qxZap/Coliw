<?php
session_start();
$_SESSION["newsession"]=$value;

    $q = $_REQUEST["x"];
//dl('php_sockets.dll');
//192.168.0.145 mihai
//192.168.0.103 gabi

//web instagram login qxZap Archerpoi!one  INSTAGRAM COMMAND

$host='localhost';
$port='6636';
// create socket	
$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP) or die("Could not create socket\n");
//echo "[i] Socket created<br>";
// connect to server
$result = socket_connect($socket, $host, $port) or die ("Could not connect to server\n");
//echo "[i] Socket connected<br>";
	//echo $divs;
	
	socket_write($socket, $q, strlen($q)) or die("Could not send data to server\n");
	
	
	
	// get server response
	$result = socket_read ($socket, 1024000) or die("Could not read server response\n");
	echo $result;	

    ?>