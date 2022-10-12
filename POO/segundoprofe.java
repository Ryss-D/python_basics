import java.util.Scanner;
public class segundoprofe {
    

    public static void main(String[] args) {
        Scanner lea=new Scanner(System.in);
        char respuesta;
        int cant;
        double promedio,suma,numero;
        suma=0;
        cant=0;
        System.out.print("Desea Ingresar valor (S/N): ");
        respuesta= lea.next().charAt(0); 
        while (respuesta == 'S' || respuesta == 's' ){ 
            System.out.println("Ingrese valor de número: ");
            numero=lea.nextFloat();
            suma=suma+numero;
            cant=cant+1;
            System.out.println("Desea Ingresar valor (S/N): ");
            respuesta= lea.next().charAt(0);    
        }
        promedio=suma/cant;
        System.out.println("La cantidad de números ingresos es: "+cant);
        System.out.println("La suma de los números ingresos es: "+suma);
        System.out.println("El promedio de los números ingresados es:"+promedio);
    }
    
}