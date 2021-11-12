$Python='python.exe'
$Script = Read-Host -Prompt "Inserte del archivo de python"
#$Path = Read-Host -Prompt "Inserte la ruta en donde se encuentra el archivo txt"
$url = Read-Host -Prompt "Inserte url"
$usuario = Read-Host -Prompt "Inserte su correo"
$receptor = Read-Host -Prompt "Inserte el correo receptor"
$mensaje = Read-Host -Prompt "Inserte el mensaje del correo"
$asunto = Read-Host -Prompt "Inserte el asunto del correo"
$contraseña = Read-Host -Prompt "Contraseña"


try {
     & $Python $Script -url $url -usuario $usuario -receptor $receptor -mensaje $mensaje -asunto $asunto -contraseña $contraseña
} catch {
    Write-Host "No existe el archivo o escribió mal un path"
}