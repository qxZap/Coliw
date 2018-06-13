<!DOCTYPE html>

<script src= "https://code.jquery.com/jquery-3.1.1.min.js"></script>

<html>
<head>

    <link rel="icon" href="https://cdn4.iconfinder.com/data/icons/astronomy-and-science/91/Astronomy_-_Science_07-512.png">
	<title>COLIW</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link href="https://fonts.googleapis.com/css?family=Poppins:300,400,700" rel="stylesheet">
	<link rel="stylesheet" type="text/css" href="colivaStyle.css">
</head>
<body>
	<content>
            <div id="mySidenav" class="sidenav">
                    <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
                    <a href="AboutColiva.html">About</a>
                    <a href="#">Console</a>
                    <a href="index.html">Support</a>
                  </div>
                  <span style="font-size:50px;cursor:pointer; float: left; color:#EDEDED" onclick="openNav()">&#9776;</span>
                  
                  <script>
                  function openNav() {
                      document.getElementById("mySidenav").style.width = "250px";
                  }
                  
                  function closeNav() {
                      document.getElementById("mySidenav").style.width = "0";
                  }
                  </script>            
            <section class="gabi">

                    <h2 id="logo">COLIW</h2>
                    <div class="info text-center">
                            Ready to roll
                        </div>
                        <br>
                        <br>

            <label for="textarea">Message</label>
            <form name="testform" id="dataSended">
            <textarea name="descript" rows="15" id="textarea" placeholder="      Welcome to Coliw

            Write  --help  for info." readonly></textarea>
            <label for="command">Command</label>
			
			
			
			
			<script>
			function getTextBoxValue()
			{
				return document.getElementById("input_area").value;
			}
			</script>
			
			
            <input type="text" id="input_area" name="command" placeholder="your command here"></input>
            <button hidden id="send_command" >Say Hello</button>
        </form>
			
			<script>
			var elem = document.getElementById("input_area");
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

var History=document.getElementById('input_area').value;

	$.ajax({
		data: {'x':History},
		url:"dataSender.php",
		type:'Get',
		success: function(data) {
			document.getElementById("textarea").value += History + '\n';
			document.getElementById("textarea").value += data + '\n';
			}

	});
});
</script>
</html>