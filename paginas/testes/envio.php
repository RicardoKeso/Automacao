<?php

$numero = rand(100000000, 999999999);

$val_status = strrev(dechex($numero));
$val_ch = $numero;

echo "
<form action=\"http://192.168.20.3/automacao/paginas/recebimento.php\" method=\"post\" name=\"teste01\">
	<input type=\"hidden\" name=\"status\" value=\"$val_status\"><br>
	<input type=\"hidden\" name=\"canal\" value=\"$val_ch\"><br>
</form> 
<script language=\"JavaScript\">document.teste01.submit();</script>
";
