<?php

$val_status = "-1";
$val_ch = "-1";

$val_status = $_POST["status"];
$val_ch = $_POST["canal"];
echo $val_ch . " " . hexdec(strrev($val_status));
?>
