import os
import argparse
import pathlib


if __name__ == "__main__":
    i_help = 'Ruta del fichero CSV de entrada'
    o_help = 'Ruta del fichero VCF de salida'
    g_help = 'Lista con los grupos a los que se desee asignar separada por espacios'
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help=i_help, type=str)
    ap.add_argument("-o", "--output", required=True, help=o_help, type=str)
    ap.add_argument("-g", "--groups", required=True, nargs='+', help=g_help, type=str)
    args = ap.parse_args()

    inputPath = args.input 
    outputPath = args.output
    groups = args.groups   
    
    if not os.path.exists(inputPath):
        print('El fichero de entrada"' + inputPath + '" no existe') 
        print('El programa termina en este preciso momento')
        exit(-1)
        
    outputSuffix = pathlib.Path(outputPath).suffix.strip()
    if outputSuffix is None or len(outputSuffix)==0:
        outputPath += '.vcf'
        
    if os.path.exists(outputPath):
        print('El fichero de salida "' + outputPath + '" ya existe')
        print('El programa termina en este preciso momento')
        exit(-1)
        
    outputFolder = os.path.dirname(outputPath).strip()
    
    if outputFolder is not None and len(outputFolder) > 0:
        if not os.path.exists(outputFolder):
            os.makedirs(outputFolder)
        
    with open(inputPath, 'r') as inputFile:
        lines = inputFile.readlines()
     
    with open(outputPath, 'w') as outputFile:
        for line in lines:
            fields = line.split(',')
            if len(fields) > 1:
                outputFile.write('BEGIN:VCARD\n')
                outputFile.write('VERSION:3.0\n')
                outputFile.write('N:' + fields[2] + ';' + fields[1] + ';;;\n')
                outputFile.write('FN:' + fields[1] + ' ' + fields[2] + '\n')
                outputFile.write('EMAIL;TYPE=INTERNET;TYPE=OTHER:' + fields[3] + '@educa.madrid.org\n')
                outputFile.write('CATEGORIES:')
                for i in range(len(groups)):
                    if i>0:
                        outputFile.write(',')
                    outputFile.write(groups[i].strip())
                outputFile.write('\n')
                outputFile.write('END:VCARD\n')
        
        
