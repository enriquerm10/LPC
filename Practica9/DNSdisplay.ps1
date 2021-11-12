$dns =  ipconfig /displaydns 
$Path = "C:\Users\Enriq\Desktop\LPC\LPC\Practica9\datosobtenidos.txt"
$codificado = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($dns))
Set-Content -Value "$codificado" -Path $Path