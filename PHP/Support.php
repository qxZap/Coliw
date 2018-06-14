<?php 
$host='192.168.0.145';
$port='6636';
$socket=socket_create(AF_INET, SOCK_STREAM, SOL_TCP) or die("Could not create socket\n");
socket_connect($this->socket, $this->host, $this->port) or die ("Could not connect to server\n");
?>

<!DOCTYPE html>
<script src= "https://code.jquery.com/jquery-3.1.1.min.js"></script>

<html>
<head>
	<link rel="icon" href="https://cdn4.iconfinder.com/data/icons/astronomy-and-science/91/Astronomy_-_Science_07-512.png">
	<title>ColiW</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link href="https://fonts.googleapis.com/css?family=Poppins:300,400,700" rel="stylesheet">
	<link rel="stylesheet" type="text/css" href="supportStyle.css">
</head>
<body>

	<content>
			<div id="mySidenav" class="sidenav">
					<a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
					<a href="AboutColiva.html">About</a>
					<a href="Coliw.html">Console</a>
					<a href="#">Support</a>
				  </div>
				  <span style="font-size:30px;cursor:pointer; color:#3a5575" onclick="openNav()">&#9776;</span>
				  
				  <script>
				  function openNav() {
					  document.getElementById("mySidenav").style.width = "250px";
				  }
				  
				  function closeNav() {
					  document.getElementById("mySidenav").style.width = "0";
				  }
				  </script>	

		<section class="right">
			<div class="content">
				<img src="img/operator.png">
				<h1>Let's get you set up</h1>
				<p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. </p>
			</div>
		</section>

		<section class="left">
			<form id="dataSended">
				<label for="full_name">Full Name</label>
	            <input type="text" id="input_name" name="full_name" placeholder="Insert your full name to know who we`re going to talk to">

	            <label for="email">E-mail</label>
	            <input type="email" id="input_email" name="email" placeholder="Insert your email to know where to send a reply to your issue">

	            <label for="textarea">Message</label>
	            <textarea id="textarea" id="input_message" placeholder="Insert a description of the issue"></textarea>

	            <button type="submit" id="send_command">Send Message</button>

			</form>
			<script>
					var elem = [document.getElementById("input_name"),document.getElementById("input_email"),document.getElementById("input_message")];
					elem.onkeyup = function(e){
						if(e.keyCode == 13){
							document.getElementById("send_command").click();
						}
					}
					</script>
		</section>
	</content>

</body>
<script>

		$('#dataSended').submit(function(event) {
			event.preventDefault();
		
		var History=[document.getElementById("input_name").value,document.getElementById("input_email").value,document.getElementById("input_message").value];
			$.ajax({
				data: {'x':History},
				type:'POST',
				success: function(data) {
					document.getElementById("textarea").value += History + '\n';
					document.getElementById("textarea").value += data + '\n';
					}
		
			});
		});
		
		</script>
</html>