$ipPublica = Invoke-RestMethod ifconfig.me
$ipLocal = Get-NetIPAddress -AddressFamily IPV4
$nmapPriv = nmap 192.168.0.15
$nmapPublica = nmap 187.161.95.205
$nmapLocal = nmap --script=http-auth-finder 192.168.0.15
$contenido = """LA IP PUBLICA ES:`n$ipPublica`nLAS IP PRIVADAS SON:`n$ipLocal
              `nLa IP local que usaré para el nmap será: 192.168.100.15, el resultado fue:`n$nmapPriv
              `nEl siguiente nmap es a la IP publica es:`n$nmapPublica
              `nY por ultimo la IP privada que usaré para este nmap es: 192.168.100.15 y el resultado fue:`n$nampLocal """


$codificado = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($contenido))
Set-Content -Value "$codificado" -Path C:\Users\Enriq\Desktop\LPC\LPC\Practica6\resultados.txt