<?php

include("clasaShukara.php");
$login=new login;

// $_SESSION["newsession"]=$value;
    $q = $_REQUEST["x"];
//dl('php_sockets.dll');
//192.168.0.145 mihai
//192.168.0.103 gabi

//web instagram login qxZap Archerpoi!one  INSTAGRAM COMMAND
// $socket = $_REQUEST["sock"];
// connect to server
session_name ("costica");
session_start();

$login->makeConnection();


$login->sendData($q);
echo $login->receiveData();
$login->closeSocket();

// $host='192.168.0.145';
// $port='6636';
// create socket
	
// get server response

?>