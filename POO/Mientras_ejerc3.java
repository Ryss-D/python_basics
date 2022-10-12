import java.util.Scanner;


public class Mientras_ejerc3 {

    public static void main(String[] args) {
        Scanner lea= new Scanner(System.in);
        int i, contFem, contMas;
        char sexo;
        double promFemenino, promMasculino, promGeneral, sumanotaFem, sumanotaMas, sumaNotas, nota;
        i=1;
        sumanotaFem=0;
        sumanotaMas=0;
        contFem=0;
        contMas=0;
        sumaNotas=0;
        while (i<=3){
            System.out.print("Ingrese la nota del estudiante: ");
            nota=lea.nextDouble();
            System.out.print("Digite sexo del estudiante(1: Masculino -- 2:Femenino)");
            sexo=lea.next().charAt(0);
            switch (sexo){
                case '1':
                    sumanotaMas=sumanotaMas + nota;
                    contMas=contMas+1;
                    break;
                case '2':
                    sumanotaFem=sumanotaFem + nota;
                    contFem=contFem+1;
                    break;
                default:
                    System.out.println("OPCIÓN NO VALIDA");
                    break;
            }
            sumaNotas=sumaNotas+nota;
            i=i+1;   
        }
        promFemenino=sumanotaFem/contFem;
        promMasculino=sumanotaMas/contMas;
        promGeneral=sumaNotas/i;
        System.out.println("Total de estudiantes: "+(i-1));
        System.out.println("Promedio general de notas"+promGeneral);
        System.out.println("Cantidad de sexo masculino: "+contMas);
        System.out.println("Promedio de notas en los hombres: "+promMasculino);
        System.out.println("Cantidad de sexo femenino: "+contFem);
        System.out.println("Promedio de notas en los mujeres: "+promFemenino);
        
    }
    
}