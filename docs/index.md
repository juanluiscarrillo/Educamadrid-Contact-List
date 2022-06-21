## Script Python para crear listas de contactos para el correo de Educamadrid

Este script de Python transforma un documento de tipo *Csv* con los datos de un grupo de alumnos (que se puede obtener de la aplicación [Raíces]([https://github.com/juanluiscarrillo/Educamadrid-Contact-List/edit/main/docs/index.md](https://raices.madrid.org/raiz_app/jsp/portal/portalraices.html)) en un archivo de tipo *Vcf* que se puede utilizar para crear o añadir una lista de contactos al correo de Educamadrid.

You can use the [editor on GitHub](https://github.com/juanluiscarrillo/Educamadrid-Contact-List/edit/main/docs/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Utilización del *script*

Una vez descargado el script, **fromCsvToVcf.py**, ejecutarlo con el comando:

    python fromCsvToVcf.py -i *input_file* -o *output_file* - g *group1 group2 group3*
  
  
Donde:
- *input_file* contiene la ruta del fichero *csv* . Nota: es necesario incluir la extensión del archivo
- *output_file* es el nombre del fichero de salida. No es necesario incluir la extensión
- *group1 group2 group3* son los nombres de los grupos a los que queremos se añadan nuestros contactos. Debe haber al menos un grupo. No hay límite de grupos. *Importante:* Los nombres de los grupos no pueden contener espacios en blanco.  

Por ejemplo:

    python fromCsvToVcf.py -i alumnos.csv -o alumnos - g Alumnos Eso1c

Crearía el fichero *alumnos.vcf*, con dos grupos, Alumnos y Eso1c, a partir del fichero *alumnos.csv*, que se proporciona en el repositorio a modo de ejemplo con datos fictícios.


En el siguiente [vídeo](https://mediateca.educa.madrid.org/video/u9emeakcfy4m93mc) se muestra de cómo proceder en el sistema operativo **Max**.
Si se utiliza Windows, el siguiente [vídeo](https://mediateca.educa.madrid.org/video/v44hdsrnrv5rr3ar) explica el proceso para este entorno.
Por último, el siguiente [vídeo](https://mediateca.educa.madrid.org/video/sq2uexb32cw2ir49) explica cómo importar el fichero creado con la lista de contactos al correo de Educamadrid.
