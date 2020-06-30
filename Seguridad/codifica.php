<!DOCTYPE html> 
<html lang="es"> 
<head> 
    <meta charset="UTF-8">
    <title>Codificado</title> 

<style type="text/css">  
<!--   
.texto {       
    font-family: verdana,arial; 
    font-size: 1.0em; 
    color:#FF0000;  
}  
-->  
</style>  
</head> 

<body> 
<?php 


$cadena = $_POST["cadena"]; 

	if (empty($cadena))   
	{   
		echo "<p align=\"left\">Introduzca lo que desea codificar.</p>";   
	}   
		else   
	{  

		$codifica1 = base64_encode($cadena); 
		$decodifica2 = base64_decode($codifica1); 

		echo " 
		<p> 
		<b>Codificado en base 64: </b> 
		<div class=\"texto\">$codifica1</div> 
		Descodificado en base 64: $decodifica2  
		</p> 
	"; 

} 

?> 
</body> 

</html>