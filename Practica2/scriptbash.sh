#!/bin/bash


echo "Hola"
echo "este script renombrara los archivos de alguna extension en especifico"


function cambiar_nombre(){
		echo "La extension es valida para: $2"
		mv "$3" "$1$4.$2"
		
}		
		
read -p "introduce la extension de los archivos a renombrar: " EXTENSION


iter=1
for FILE in *.*; do
		ext="${FILE##*.}" #obtiene la extensio de cada archivo 
		#echo "$ext"  
		if [ $ext == $EXTENSION ];
		then
			cambiar_nombre $1 "$ext" "$FILE" "$iter" #PARAMETERO #1 es el nombre que se la dara a cada archivo seguido de un numero del 1 hasta el ultimo archivo"
			
			
			iter=$((iter+1))
		echo "ARCHIVOS $EXTENSION renombrados con exito"
		else
			echo "Extension no valida: $ext"
		fi
done